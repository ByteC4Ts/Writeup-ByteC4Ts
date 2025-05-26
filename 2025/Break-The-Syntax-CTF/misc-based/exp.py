import base64

with open("top_secret", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    # IA==
    # SA==
    # aQ==
    # ...

base64_charmap = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def decode(line):
    i = base64_charmap.index(line[0])
    i <<= 6
    i |= base64_charmap.index(line[1])
    return i


flag = ""

for i in range(0, len(lines), 2):
    print(lines[i], lines[i + 1], end=" ")
    i1, i2 = decode(lines[i]), decode(lines[i + 1])
    print(hex(i1), hex(i2), end=" ")
    b64dec1, b64dec2 = base64.b64decode(lines[i]), base64.b64decode(lines[i + 1])
    print(b64dec1.decode("utf-8") + b64dec2.decode("utf-8"), end=" ")
    lsb1, lsb2 = i1 & 0xF, i2 & 0xF
    if lsb1 + lsb2 != 0:
        ch = chr(lsb1 << 4 | lsb2)
        flag += ch
        print("  |  " + ch, end="")
    print()

print(flag)

# BtSCTF{You_really_are_an_expert_in_bases}
