import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from hashlib import sha256
from pwn import xor

prefix = b"picoCTF"

c = bytes.fromhex(open("output.txt").read().strip())
key = xor(c, prefix)[: len(prefix)]
print(xor(key, c[7:14]))
for i in range(14, len(c), 32):
    key = sha256(key).digest()
    print(xor(c[i : i + 32], key))
