from pwn import remote, process, context
context.log_level = 'debug'
from sage.all import *
from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
import os, random, math

# dir = os.path.dirname(__file__)
# io = process(['python3', dir + '/chall.py'])
io = remote('litctf.org', 31789)


bound = 996491788296388609
l = int(math.sqrt(bound))

pos_exp = [l + e for e in (1, 3, 5, 7)]
neg_exp = [-l - e for e in (0, 2, 4, 6)]
pos_rs = []
neg_rs = []


for i in range(4):
    io.sendlineafter(b'guess): ', str(pos_exp[i]).encode())
    pos_rs.append(int(io.recvline().strip().decode()))
    io.sendlineafter(b'guess): ', str(neg_exp[i]).encode())
    neg_rs.append(int(io.recvline().strip().decode()))

x1 = pos_rs[0] * neg_rs[0] - pos_rs[1] * neg_rs[1]
x2 = pos_rs[2] * neg_rs[2] - pos_rs[3] * neg_rs[3]


n = list(factor(gcd(x1, x2)))[-1][0]

io.sendlineafter(b'guess): ', b'guess')
io.sendlineafter(b'n? ', str(n).encode())

io.interactive()

