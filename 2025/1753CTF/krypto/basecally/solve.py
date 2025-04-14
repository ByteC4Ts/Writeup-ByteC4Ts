import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("out.txt", "w") as file:
    ct = open("flag.txt", "r").read().strip().split(" ")
    for i in range(2, 36):
        file.write("".join([chr(int(c, i)) for c in ct]) + "\n")

"""
flag: 1753{PUTUPUPDATEDDATEAPP}
"""
