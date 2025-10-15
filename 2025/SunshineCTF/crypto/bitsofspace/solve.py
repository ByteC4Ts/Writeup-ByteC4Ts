import os, struct
from pwn import xor, remote, context
context.log_level = 'debug'




dir = os.path.dirname(__file__)
data = open(dir + '/voyager.bin', 'rb').read()
iv = data[:16]
VALID_DEVICES = {
    0x13371337: b"Status Relay\n",
    0x1337babe: b"Ground Station Alpha\n",
    0xdeadbeef: b"Lunar Relay\n",
    0xdeadbabe: b"Restricted Relay\n"
}

known = [struct.pack('<I', k) for k in VALID_DEVICES.keys()]
fake = struct.pack('<I', 0xdeadbabe)

fs = [xor(xor(iv[:4], k), fake) + iv[4:] for k in known]



for f in fs:
    conn = remote('sunshinectf.games', 25401)
    conn.sendlineafter(b'Send your subscription packet:\n', f + data[len(f):])
    conn.recvall()
    conn.close()


