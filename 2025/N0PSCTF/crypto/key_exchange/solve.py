from pwn import process
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES
from hashlib import sha256


io = process(["python3", "2025/N0PSCTF/crypto/key_exchange/chall.py"])

p = int.from_bytes(io.recv(1024))
g = int.from_bytes(io.recv(1024))
k_a = int.from_bytes(io.recv(1024))


k_b = 1
io.sendline(k_b.to_bytes(1024))


data = io.recvall()

iv, ct = data[:16], data[16:]

k = 1
k = k.to_bytes((k.bit_length() + 7) // 8)

key = sha256(k).digest()

cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)

print(cipher.decrypt(ct))
