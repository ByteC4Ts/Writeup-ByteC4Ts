from pwn import remote, process, context
context.log_level = 'debug'
from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import os, random


io = remote('litctf.org', 31777)

io.recvuntil(b'cipher:\n')
t1 = int(io.recvline().strip().decode())
t2 = int(io.recvline().strip().decode())

io.recvuntil(b'RSA:\n')
e, n = [int(tok) for tok in io.recvline().strip().decode().split(' ')]
c = int(io.recvline().decode())



dir = os.path.dirname(__file__)
import sys
sys.path.append(dir)

from xor_factor import factor as f
p, q = f(n, t1 ^ t2)


d = pow(e, -1, (p - 1) * (q - 1))
print(ltb(pow(c, d, n)))