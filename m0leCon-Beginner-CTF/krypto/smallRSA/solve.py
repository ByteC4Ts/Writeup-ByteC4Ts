from Crypto.Util.number import *
from pwn import *
from sage.all import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    ms = []
    io = process(["python3", "chall.py"])
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"hex: ", b"2")
    c1 = int(io.recvlinesS(3)[0].strip(), 16)
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"hex: ", b"3")
    c2 = int(io.recvlinesS(3)[0].strip(), 16)
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"hex: ", b"5")
    c3 = int(io.recvlinesS(3)[0].strip(), 16)

    m1 = pow(2, 0x10001)
    m2 = pow(3, 0x10001)
    m3 = pow(5, 0x10001)

    n = gcd([m1 - c1, m2 - c2, m3 - c3])

    l, r = 0, int(sqrt(n))
    p = (l + r) // 2
    while l < r:
        io.sendlineafter(b"> ", b"1")
        io.sendlineafter(b"hex: ", long_to_bytes(p).hex().encode())
        recv = io.recvlinesS(3)
        if "b'Error: message to encrypt is too big'" in recv:
            l, r = l, p - 1
            p = (l + r) // 2
        else:
            l, r = p + 1, r
            p = (l + r) // 2

    io.sendlineafter(b"> ", b"2")
    ct = int(io.recvlinesS(3)[0], 16)
    q = n // p
    d = pow(0x10001, -1, (p - 1) * (q - 1))
    flag = long_to_bytes(pow(ct, d, n))
    io.close()
    if b"ptm{" in flag:
        print(flag)
        exit(0)
