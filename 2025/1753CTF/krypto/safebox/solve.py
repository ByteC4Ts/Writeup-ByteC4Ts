import os
from pwn import xor

os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open("flag.bin", "rb") as file:
    ct = file.read()

with open("zero220.bin", "rb") as file:
    ctx = file.read()


print(xor(ct, ctx))


"""
flag: 1753c{encrypt3d_but_n0t_s0000_s4fe_b0x}
"""
