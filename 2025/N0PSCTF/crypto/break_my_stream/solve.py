from pwn import process, xor

io = process(["python3", "2025/N0PSCTF/crypto/break_my_stream/chall.py"])


ct = io.recvline_contains(b"one last thing: ", keepends=False).split(b": ")[1]
ct = bytes.fromhex(ct.decode())

payload = 256 * b"a"

io.sendlineafter(b"message: ", payload)

data = bytes.fromhex(io.recvline(keepends=False).decode())


key = xor(data, payload)
print(xor(key, ct))
