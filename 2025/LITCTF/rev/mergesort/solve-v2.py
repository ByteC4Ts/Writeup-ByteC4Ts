"""
recursive order (pre-order)
       0
   1       8
 2   5   9   c
3 4 6 7 a b d e
"""
ls = [0, 0, 0, 0, 2, 4, 4, 6, 8, 8, 8, 10, 12, 12, 14]
rs = [15, 7, 3, 1, 3, 7, 5, 7, 15, 11, 9, 11, 15, 13, 15]

leafs = [48, 72, 192, 288, 2430, 2430, 108, 432, 672, 1008, 224, 896, 504, 336, 180, 180]


def ratio(len_l, len_r):
    return 10 * len_l // (len_l + len_r)


pre_order = []
for i in range(15):
    l, r = ls[i], rs[i] + 1
    m = l + (r - l) // 2
    pre_order.append(ratio(sum(leafs[l:m]), sum(leafs[m:r])))
print(pre_order)

flag_base9 = "".join([str(i - 1) for i in pre_order])[::-1]
flag_base10 = int(flag_base9, 9)
print(f"LITCTF{{{flag_base10}}}")

# LITCTF{105955120379039}
