import asyncio
import websockets


async def websocket_client():
    uri = "ws://verbal-sleep.picoctf.net:61344/ws/"
    async with websockets.connect(uri) as ws:
        await ws.send("eval -100000")
        response = await ws.recv()
        print(f"Received: {response}")
        # Received: Huh???? How can I be losing this badly... I resign... here's your flag: picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_a2a9bbe9}


asyncio.run(websocket_client())

# picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_a2a9bbe9}
