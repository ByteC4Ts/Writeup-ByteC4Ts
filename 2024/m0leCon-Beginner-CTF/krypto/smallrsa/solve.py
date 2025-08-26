from pwn import process, context
from sympy import gcd
from Crypto.Util.number import long_to_bytes, getPrime

context.log_level = 'debug'

io = process(['python3', '2024/m0leconctf/smallrsa/chall.py'])

def bin_search(p):
    l, r = 0, p
    m = (l + r) // 2

    while l < r:
        io.sendlineafter(b'> ', b'1')
        io.sendlineafter(b'hex: ', hex(m)[2:].encode())

        if b'too big' in io.recvline():
            l, r = l, m - 1
            m = (l + r) // 2
        else:
            l, r = m + 1, r
            m = (l + r) // 2
    return m



p = bin_search(getPrime(513))

d = pow(65537, -1, p - 1)



io.sendlineafter(b'> ', b'2')
ct = int(io.recvline().strip().decode(), 16)

flag = long_to_bytes(pow(ct, d, p))

print(flag)