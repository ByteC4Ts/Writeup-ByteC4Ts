from pwn import *

PAYLOAD = b"3rg0u" * 32


def check():
    io = remote("pad.ctf.intigriti.io", 1348)
    io.recvuntil(b"Encrypted (cat state=ERROR! 'cat not in box'): ")
    flag_encrypted = bytes.fromhex(io.recvline().decode().strip())
    io.recvuntil(b"\nAnyway, why don't you try it for yourself?\n")
    io.sendline(PAYLOAD)
    s = io.recvline().decode().strip().split(": ")
    state = "alive" in s[0]
    c_cipher = bytes.fromhex(s[1])
    io.close()
    return state, flag_encrypted, c_cipher


def ret(cs):
    res = bytearray()
    for c in cs:
        res.append((c ^ 0xAC) >> 1)
    return res


def main():
    state, flag_encrypted, c_cipher = check()
    while not state:
        state, flag_encrypted, c_cipher = check()
    key = xor(ret(c_cipher), PAYLOAD)
    flag = xor(flag_encrypted, key)
    print(flag)


if __name__ == "__main__":
    main()

"""
b"Schrodinger's cat in a quantum bind, INTIGRITI{d34d_0r_4l1v3} hidden, hard to find. Is it alive, or has fate been spun? In superposition, the game's never done."
"""
