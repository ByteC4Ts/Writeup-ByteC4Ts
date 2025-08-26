from pwn import *
from string import printable
import re

context.log_level = 'error'

def oracle(p):
    io = process(['python3', '2024/wannagamectf/ecb/chall.py'])
    io.sendlineafter(b'(hex): ', p.hex().encode())
    ct = bytes.fromhex(io.recvline().strip().decode())
    io.close()
    return ct

lf = len(oracle(b'a'))

flag = b''
for l in range(lf)[::-1]:
    pattern = oracle(l * b'a')[:lf]
    for char in printable:
        pay = l * b'a' + flag + char.encode()
        if oracle(pay)[:lf] == pattern:
            flag += char.encode()
            if re.match(b'W1\{.*\}', flag):
                print(flag)
                exit()
            break