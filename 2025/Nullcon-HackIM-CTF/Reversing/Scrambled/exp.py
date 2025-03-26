def hex_string_to_byte_list(hexstr):
    assert len(hexstr) % 2 == 0
    return [int(hexstr[i:i + 2], 16) for i in range(0, len(hexstr), 2)]


result = hex_string_to_byte_list("1e78197567121966196e757e1f69781e1e1f7e736d6d1f75196e75191b646e196f6465510b0b0b57")

prefix = "ENO{"
for i in range(len(result)):
    print(result[i] ^ ord(prefix[i % len(prefix)]), end=" ")
    if i % 4 == 3:
        print()

# 91 54 86 14
# 34 92 86 29
# 92 32 58 5
# 90 39 55 101
# 91 81 49 8
# 40 35 80 14
# 92 32 58 98
# 94 42 33 98
# 42 42 42 42    <- leak key!!
# 78 69 68 44


key = 42

for i in range(len(result)):
    print(chr(result[i] ^ key), end="")
    if i % 4 == 3:
        print()

# 4R3_
# M83L
# 3D_T
# 5CR4
# 45TY
# GG5_
# 3D_3
# 1ND3
# ENO{
# !!!}

# ENO{5CR4M83L3D_3GG5_4R3_1ND33D_T45TY!!!}
