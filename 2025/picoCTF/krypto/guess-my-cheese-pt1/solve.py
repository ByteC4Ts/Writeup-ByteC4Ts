import string

omega = string.ascii_uppercase


def affine_en(str, a, b):
    res = ""
    for char in str:
        res += omega[(a * omega.index(char) + b) % len(omega)]
    return res


def affine_de(str, a, b):
    res = ""
    for char in str:
        res += omega[(a * omega.index(char) - b) % len(omega)]
    return res


print(affine_de("XATIIBG".upper(), pow(11, -1, 26), 1))
