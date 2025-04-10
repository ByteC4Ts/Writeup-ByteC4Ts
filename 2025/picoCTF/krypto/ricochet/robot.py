from radio_base import RadioDevice
import asyncio
from keys import keys
import traceback
import os
import crypto
import json
import robot_low_level
import monocypher

ROBOT_ADDRESS = 0x10

class Robot(RadioDevice):
    def __init__(self, network):
        super().__init__("Robot", network)
        self.start = False
        self.stop = False
        self.address = 0x20
        self.receive_buffer = []

        self.dh_key_priv = os.urandom(32)

        # Initialize to a random key so we don't accidentally send unencrypted data
        self.dh_key_shared = os.urandom(32)

        self.nonce = 0

    def debug(self, msg):
        msg = str(msg)
        self.send_message({
            "msg_type": "debug",
            "src": self.address,
            "dst": 0xFF,
            "message": msg
        })

    def message_callback(self, msg):
        try:
            msg_type = msg["msg_type"]
            msg_dst = int(msg["dst"])
            
            if msg_dst != self.address:
                return

            if msg_type == "ping":
                self.send_message({
                    "msg_type": "pong",
                    "src": self.address,
                    "dst": msg["src"]
                })

            else:
                self.receive_buffer.append(msg)

        except:
            traceback.print_exc()
        
    async def wait_message(self, msg_type):
        for _ in range(100):
            try:
                if len(self.receive_buffer):
                    msg = self.receive_buffer.pop(0)
                    if msg["msg_type"] == msg_type:
                        return msg
            except:
                traceback.print_exc()

            await asyncio.sleep(0.1)

        return {}

    def hmac_and_encrypt(self, msg, nonce):
        msg_with_hmac = json.dumps(crypto.add_hmac(msg, nonce, keys["shared_hmac_key"]))
        msg_encrypted = crypto.encrypt(msg_with_hmac, self.dh_key_shared)
        return msg_encrypted

    def decrypt_and_check_hmac(self, msg, nonce):
        msg = crypto.decrypt(msg, self.dh_key_shared)
        if msg is None: return None
        msg_with_hmac = json.loads(msg)
        return crypto.validate_hmac(msg_with_hmac, nonce, keys["shared_hmac_key"])

    async def send_secure_data(self, msg):
        msg_encrypted = self.hmac_and_encrypt(msg, self.nonce)
        self.send_message({
            "msg_type": "secure_data",
            "src": self.address,
            "dst": ROBOT_ADDRESS,
            "encrypted": msg_encrypted
        })

        response = await self.wait_message("secure_data_ack")
        ack_decrypted = self.decrypt_and_check_hmac(response["encrypted"], self.nonce)

        if ack_decrypted is None:
            self.debug("acknowledgement failed to validate")
            return

        # Ack packets are zero length
        if len(ack_decrypted) != 0:
            self.debug("acknowledgement mismatch")
            return

        self.nonce += 1

    async def recv_secure_data(self):
        # Zero length packet as a secure data request
        msg_encrypted = self.hmac_and_encrypt("", self.nonce)
        self.send_message({
            "msg_type": "secure_data_request",
            "src": self.address,
            "dst": ROBOT_ADDRESS,
            "encrypted": msg_encrypted
        })

        response = await self.wait_message("secure_data_response")
        response_decrypted = self.decrypt_and_check_hmac(response["encrypted"], self.nonce)

        if response_decrypted is None:
            self.debug("response failed to validate")
            return

        self.nonce += 1

        return response_decrypted

    async def read_command(self):
        await self.send_secure_data("get_movement")
        await asyncio.sleep(0.2)

        while True:
            resp = await self.recv_secure_data()
            if resp != "":
                return resp

    async def run(self):
        while self.running:
            while not self.start:
                await asyncio.sleep(0.1)

            self.nonce = 0

            # move the robot back to its origin/home location
            robot_low_level.reset()

            # Validate the robot's authenticity
            challenge = os.urandom(16).hex()
            self.send_message({
                "src": self.address,
                "dst": ROBOT_ADDRESS,
                "msg_type": "validate",
                "challenge": challenge
            })
            response = await self.wait_message("ack_validate")
            expected_response = crypto.compute_hmac(challenge, 0, keys["authenticity_key"])
            if response.get("response") != expected_response.hex():
                self.debug("Robot validation failed")
                self.start = False
                continue

            self.debug("Robot successfully validated")

            # Diffie-Hellman key exchange to secure future communications
            self.send_message({
                "src": self.address,
                "dst": ROBOT_ADDRESS,
                "msg_type": "key_exchange",
                "key": monocypher.compute_key_exchange_public_key(self.dh_key_priv).hex()
            })
            response = await self.wait_message("ack_key_exchange")
            self.dh_key_shared = monocypher.key_exchange(self.dh_key_priv, bytes.fromhex(response["key"]))

            # Once validated, read some commands from the controller and execute them
            for _ in range(20):
                cmd = (await self.read_command())
                if cmd is None:
                    self.debug("timed out trying to read a robot command")
                    break

                if len(cmd) != 0:
                    await robot_low_level.move(cmd)

                if self.stop:
                    break

            if self.stop:
                await robot_low_level.move("stop")
            else:
                await robot_low_level.move("done")

            self.stop = False
            self.start = False
