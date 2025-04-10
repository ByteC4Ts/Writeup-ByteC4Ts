from sage.all import *
from pwn import xor, remote, process
import os
from Crypto.Util.number import long_to_bytes

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# io = process(["python3", "challenge.py"])
io = remote("activist-birds.picoctf.net", 64125)


def parse_data(value):
    value = bytes.fromhex(value)
    return value[:-28], value[-28:-12], value[-12:]


def poly(msg):
    q = (len(msg) + 15) // 16
    poly = 0
    for i in range(q):
        sub = msg1[i * 16 : i * 16 + 16] + b"\x01"
        sub += (17 - len(sub)) * b"\0"
        num = int.from_bytes(sub, "little")
        poly = (poly + num) * r_sym
    return poly


def forge(msg, r, s):
    q = (len(msg) + 15) // 16
    tot = 0

    for i in range(q):
        sub = msg[i * 16 : i * 16 + 16] + b"\x01"
        sub += (17 - len(sub)) * b"\0"
        num = int.from_bytes(sub, "little")
        tot = (tot + num) * r

    tot = tot % p
    result = (tot + s) % (1 << 128)
    return long_to_bytes(result)[::-1]


def format(msg):
    return (
        msg
        + b"\0" * (16 - (len(msg) & 0x0F))
        + long_to_bytes(0, 8)[::-1]
        + long_to_bytes(len(msg), 8)[::-1]
    )


p1 = io.recvline_startswith(b"Plaintext (hex): ").decode().split(": ")[1]
data1 = io.recvline_startswith(b"Ciphertext (hex): ").decode().split(": ")[1]
p2 = io.recvline_startswith(b"Plaintext (hex): ").decode().split(": ")[1]
data2 = io.recvline_startswith(b"Ciphertext (hex): ").decode().split(": ")[1]


ct1, tag1, nonce1 = parse_data(data1)
ct2, tag2, nonce2 = parse_data(data2)

assert nonce1 == nonce2

goal = "But it's only secure if used correctly!"

key_stream = xor(ct1, bytes.fromhex(p1))[: len(goal)]
goal = xor(key_stream, goal.encode())


t1 = int.from_bytes(tag1, "little")
t2 = int.from_bytes(tag2, "little")

p = (1 << 130) - 5
r_sym = PolynomialRing(GF(p), "r").gens()[0]


msg1 = format(ct1)
msg2 = format(ct2)

poly1 = poly(msg1)
poly2 = poly(msg2)


possible_r = []

for k in range(-5, 5 + 1):
    roots = (poly1 - poly2 - (t1 - t2) + k * 2**128).roots()
    for root, mult in roots:
        possible_r.append(int(root))

for r in possible_r:
    if int(r).bit_length() <= 124:
        break

s = (t1 - int(poly1.subs({r_sym: r}))) % (2**128)


print(forge(format(goal), r, s))

io.sendlineafter(
    b"What is your message? ",
    (goal + forge(format(goal), r, s) + nonce1).hex().encode(),
)


print(io.recvline_contains(b"pico"))
