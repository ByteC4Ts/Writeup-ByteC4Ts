from pwn import *
import tqdm


context.log_level = 'debug'


k = None

while not k:

    io = process(['python3', '2024/1337ctf/krsa/chall.py'])

    n = int(io.recvline_contains(b'n=').decode().split('=')[1])
    e = int(io.recvline_contains(b'e=').decode().split('=')[1])
    ck = int(io.recvline_contains(b'ck=').decode().split('=')[1])


    left = dict()


    for a in tqdm.trange(1, 1 << 16):
        __byte = (ck * pow(a, -e, n)) % n
        left[__byte] = a


    for b in tqdm.trange(1 << 16, 1 << 20):
        __c4ts = pow(b, e, n)
        if __c4ts in left.keys():
            k = b * left.get(pow(b, e, n))
            break
    
io.sendlineafter(b'Secret key ? ', str(k).encode())


io.interactive()