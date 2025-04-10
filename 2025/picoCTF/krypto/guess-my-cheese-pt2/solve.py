import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from hashlib import sha256
from pwn import *


def hexa(str):
    return sha256(str).hexdigest()


file = open("cheese_list.txt").read().strip().split("\n")

c_list = [cheese.encode() for cheese in file]
c_list += [cheese.upper().encode() for cheese in file]
c_list += [cheese.lower().encode() for cheese in file]
c_list += [cheese.replace(" ", "").encode() for cheese in file]
c_list += [cheese.replace(" ", "").upper().encode() for cheese in file]
c_list += [cheese.replace(" ", "").lower().encode() for cheese in file]


def main():
    global c_list
    io = remote("verbal-sleep.picoctf.net", 58138)
    io.recvuntil(b"you'll be able to guess it:  ")
    hash = io.recvuntil(b"\n", drop=True).decode()
    for cheese in c_list:
        for salt in range(0x100):
            if (
                hexa(salt.to_bytes() + cheese) == hash
                or hexa(cheese + salt.to_bytes()) == hash
            ):
                io.sendlineafter(b" like to do?\n", b"g")
                io.sendlineafter(b"what's my cheese?\n", cheese)
                io.sendlineafter(b"what's my salt?\n", hex(salt)[2:].encode())
                flag = io.recvline_contains(b"pico")
                print(flag)
                exit()


if __name__ == "__main__":
    main()
