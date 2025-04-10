from radio_base import RadioDevice
import asyncio
import traceback
from keys import keys
import os
import crypto
import json
import monocypher

class RobotController(RadioDevice):
    def __init__(self, network):
        super().__init__("RobotController", network)
        self.address = 0x10

        self.dh_key_priv = os.urandom(32)

        # Initialize to a random key so we don't accidentally send unencrypted data
        self.dh_key_shared = os.urandom(32)

        self.send_buffer_secure = ""
        self.recv_buffer_secure = ""
        self.nonce = 0

        self.movement_counter = 0

    def reset(self):
        self.nonce = 0
        self.movement_counter = 0

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

            # To avoid the bootstrapping problem, changing the address needs to
            # be an unauthenticated operation
            if msg_type == "set_addr":
                self.address = int(msg["new_addr"]) & 0xFF
                self.send_message({
                    "msg_type": "ack_set_addr",
                    "src": self.address,
                    "dst": msg["src"]
                })

            if msg_type == "validate":
                response = crypto.compute_hmac(msg["challenge"], 0, keys["authenticity_key"])
                self.send_message({
                    "msg_type": "ack_validate",
                    "src": self.address,
                    "dst": msg["src"],
                    "response": response.hex()
                })

            if msg_type == "key_exchange":
                self.send_message({
                    "msg_type": "ack_key_exchange",
                    "src": self.address,
                    "dst": msg["src"],
                    "key": monocypher.compute_key_exchange_public_key(self.dh_key_priv).hex()
                })
                self.dh_key_shared = monocypher.key_exchange(self.dh_key_priv, bytes.fromhex(msg["key"]))

            if msg_type == "secure_data_request":
                self.process_secure_data_request(msg)

            if msg_type == "secure_data":
                self.process_secure_data(msg)

        except:
            traceback.print_exc()

    def hmac_and_encrypt(self, msg, nonce):
        msg_with_hmac = json.dumps(crypto.add_hmac(msg, nonce, keys["shared_hmac_key"]))
        msg_encrypted = crypto.encrypt(msg_with_hmac, self.dh_key_shared)
        return msg_encrypted

    def decrypt_and_check_hmac(self, msg, nonce):
        msg = crypto.decrypt(msg, self.dh_key_shared)
        if msg is None: return None
        msg_with_hmac = json.loads(msg)
        return crypto.validate_hmac(msg_with_hmac, nonce, keys["shared_hmac_key"])

    def process_secure_data_request(self, request):
        request_decrypted = self.decrypt_and_check_hmac(request["encrypted"], self.nonce)

        if request_decrypted is None:
            self.debug("message failed to validate")
            return

        # Avoid type confusion by ensuring a secure data request should always
        # be of length zero
        if len(request_decrypted) != 0:
            self.debug("message mismatch")
            return

        # If the request is valid, send our current send buffer in response
        msg = self.send_buffer_secure
        self.send_buffer_secure = ""
        msg_encrypted = self.hmac_and_encrypt(msg, self.nonce)

        self.nonce += 1

        self.send_message({
            "msg_type": "secure_data_response",
            "src": self.address,
            "dst": request["src"],
            "encrypted": msg_encrypted
        })

    def process_secure_data(self, msg):
        msg_decrypted = self.decrypt_and_check_hmac(msg["encrypted"], self.nonce)

        if msg_decrypted is None:
            self.debug("message failed to validate")
            return

        # If the request is valid, send an empty message as an acknowledgement
        msg_encrypted = self.hmac_and_encrypt("", self.nonce)
        self.nonce += 1
        self.send_message({
            "msg_type": "secure_data_ack",
            "src": self.address,
            "dst": msg["src"],
            "encrypted": msg_encrypted
        })

        self.recv_buffer_secure = msg_decrypted

    async def run(self):
        while self.running:
            await asyncio.sleep(0.05)
            # Wait for the secure messaging layer to provide a secure command
            if self.recv_buffer_secure == "get_movement":
                self.recv_buffer_secure = ""

                # Demo version sends the same four commands repeatedly
                # Full control is available in the licensed version of this system
                self.send_buffer_secure = ["east", "south", "west", "north"][self.movement_counter % 4]
                self.movement_counter += 1


