from pwn import *
import os.path as path
import base64

os.chdir(path.dirname(path.abspath(__file__)))
# io = process(["python3", "chall.py"])
host = 'serverhost'
port = 0000
io = remote(host, port)


io.sendlineafter(b"option: ", b"1")
io.sendlineafter(b"message: ", b"Bob33")
hash = io.recvline().decode().strip().split(": ")[1]
hash = base64.b64decode(hash)

io.sendlineafter(b"option: ", b"2")
io.sendlineafter(b"name: ", b"Bob33")
io.sendlineafter(b"HMAC: ", hash)
password = io.recvlinesS(3)[-1]

io.sendlineafter(b"option: ", b"3")
io.sendlineafter(b"Password: ", password.encode())

print(io.recvlinesS(2)[1])
