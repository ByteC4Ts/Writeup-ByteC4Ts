"""
recursive order (pre-order)
       0
   1       8
 2   5   9   c
3 4 6 7 a b d e
...

output order (post-order)
       e
   6       d
 2   5   9   c
0 1 3 4 7 8 a b
...
"""

leafs = [48, 72, 192, 288, 2430, 2430, 108, 432, 672, 1008, 224, 896, 504, 336, 180, 180]


def ratio(len_l, len_r):
    return 10 * len_l // (len_l + len_r)


# post-order
stack, post_order = [], []
for leaf in leafs:
    stack.append((leaf, 0))
    while len(stack) > 1 and stack[-1][1] == stack[-2][1]:
        node_r, node_l = stack.pop(), stack.pop()
        depth, len_l, len_r = node_l[1], node_l[0], node_r[0]
        post_order.append(ratio(len_l, len_r))
        stack.append((len_l + len_r, depth + 1))
print(post_order)

# pre-order
mapping = "e6201534d978cab"
pre_order = [post_order[int(i, 16)] for i in mapping]
print(pre_order)

flag_base9 = "".join([str(i - 1) for i in pre_order])[::-1]
flag_base10 = int(flag_base9, 9)
print(f"LITCTF{{{flag_base10}}}")

# LITCTF{105955120379039}
