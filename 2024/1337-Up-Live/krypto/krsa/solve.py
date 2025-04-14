from pwn import process
import os
from tqdm import trange

os.chdir(os.path.dirname(os.path.abspath(__file__)))


io = process(["python3", "chall.py"])

n = int(io.recvline_contains(b"n=").decode().split("=")[1])
e = int(io.recvline_contains(b"e=").decode().split("=")[1])
ck = int(io.recvline_contains(b"ck=").decode().split("=")[1])


res = {}
for a in trange(1, 0x10000):
    tmp = (pow(a, -e, n) * ck) % n
    res[tmp] = a


for b in trange(0x10000, 0xFFFFF):
    tmp = pow(b, e, n)
    if res.get(tmp):
        print("oke")
        k = res[tmp] * b
        break

io.sendlineafter(b"Secret key ? ", str(k).encode())

print(io.recvline())
