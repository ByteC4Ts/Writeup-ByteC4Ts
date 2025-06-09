from pwn import xor, remote


def solve():
    io = remote("challenge.nahamcon.com", 30458)

    io.recvuntil(b"The encrypted flag is: ")
    cipher = bytes.fromhex(io.recvline(keepends=False).decode())

    payload = b"a" * len(cipher)

    io.sendlineafter(b"(or 'quit' to exit):\n", payload)

    io.recvuntil(b"Encrypted: ")
    data = bytes.fromhex(io.recvline(keepends=False).decode())

    print(xor(xor(data, payload), cipher))


solve()
