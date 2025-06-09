from pwn import *

exe = './gradeViewer'
#p = process(exe)
p = remote("tjc.tf",31624)
context.log_level = 'debug'

secret = b'f1shc0de'
teacher_id = b'-62482'

p.sendline(teacher_id)
p.recvuntil(b'Enter your password [a-z, 0-9]:')
p.sendline(secret)
p.interactive()
