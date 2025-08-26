from pwn import *
context.log_level = 'debug'

PAYLOAD = b"c4ts" * 40

def check():
    io = remote("pad.ctf.intigriti.io", 1348)
    # io = remote("localhost", 1337)


    enc_flag = bytes.fromhex(io.recvline_contains(b'cat not in box').decode().strip().split(': ')[1])
    io.sendafter(b'you try it for yourself?', PAYLOAD)
    respone = io.recvline_contains(b'cat state')
    print(respone)

    state = b'alive' in respone
    c_cipher = bytes.fromhex(respone.decode().split(': ')[1])
    io.close()
    return state, enc_flag, c_cipher


def ret(cs):
    res = bytearray()
    for c in cs:
        res.append((c ^ 0xAC) >> 1)
    return res


def main():
    state, enc_flag, c_cipher = check()
    while not state:
        state, enc_flag, c_cipher = check()
    c_cipher = ret(c_cipher)
    key = xor(PAYLOAD, c_cipher)
    flag = xor(enc_flag, key)
    print(flag)


if __name__ == "__main__":
    main()
