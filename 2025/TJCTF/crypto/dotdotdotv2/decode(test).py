import numpy as np
import random

n = 64

filler = "In cybersecurity, a CTF (Capture The Flag) challenge is a competitive, gamified event where participants, either individually or in teams, are tasked with finding and exploiting vulnerabilities in systems to capture hidden information known as flags. These flags are typically used to score points. CTFs test skills in areas like cryptography, web security, reverse engineering, and forensics, offering an exciting way to learn, practice, and showcase cybersecurity expertise.  This flag is for you: "
filler += "tjct"
flag = "f{test_flag_is_here_and_it_is_very_very_loooong!}"
print(len(filler), len(flag))  # 504 49

filler = "".join([bin(ord(i))[2:].zfill(8) for i in filler])
flag = "".join([bin(ord(i))[2:].zfill(8) for i in flag])
print(len(filler), filler)  # 4032 0100100101101110...
print(len(flag), flag)  # 392 0110011001111011...

pt = filler + flag
print(len(pt))  # 4424

pt = pt + "0" * (n - len(pt) % n)
print(len(pt), pt)  # 4480 0100100101101110...

mat_pt = np.array([list(map(int, list(pt[i:i + n]))) for i in range(0, len(pt), n)])
print(mat_pt.shape)  # (m, n) -> (70, 64), bool

mat_key = np.array([[random.randint(0, 0xdeadbeef) for _ in range(n)] for _ in range(n)])
print(mat_key.shape)  # (n, n) -> (64, 64), int

mat_ct = np.dot(mat_pt, mat_key)
print(mat_ct.shape)  # (m, n) -> (70, 64), int

# ================================
# ================================

# key[8*i]'s value doesn't matter!
mat_key_test = mat_key.copy()
for row in range(n):
    if row % 8 == 0:
        mat_key_test[row] = np.zeros(n)

mat_ct_test = np.dot(mat_pt, mat_key_test)
print(np.all(mat_ct == mat_ct_test))  # True

# ================================
# ================================

from z3 import *


def solve_mat_key_col(col):
    s = Solver()
    sym_key_col = [Int(f"key_{row}") for row in range(n)]

    # for row in range(n):
    #     s.add(sym_key_col[row] >= 0)
    #     s.add(sym_key_col[row] <= 0xdeadbeef)

    k = int(len(filler) / 8) // 8  # k=63 -> known filler
    for row in range(k):
        s.add(Sum([mat_pt[row][i] * sym_key_col[i] for i in range(n)]) == int(mat_ct[row][col]))

    if s.check() == sat:
        mdl = s.model()
        col = []
        for row in range(n):
            if row % 8 == 0:
                col.append(0)
            else:
                col.append(mdl[sym_key_col[row]].as_long())
        return col
    else:
        return None


mat_key_recovered = []
for col in range(n):
    print(f"Recovering column {col}...")
    recovered_col = solve_mat_key_col(col)
    assert recovered_col is not None
    mat_key_recovered.append(recovered_col)
mat_key_recovered = np.column_stack(mat_key_recovered)

pt_recovered = np.dot(mat_ct, np.linalg.pinv(mat_key_recovered))
pt_recovered = np.rint(pt_recovered).astype(int)
pt_recovered = np.clip(pt_recovered, 0, 1)


def findchar(bitstr):
    intval = int(bitstr, 2)
    if intval < 32 or intval > 126:
        return f"({bitstr})"
    return chr(intval)


for row in range(pt_recovered.shape[0]):
    binstr = "".join(map(str, pt_recovered[row]))
    text = "".join([findchar(binstr[i:i + 8]) for i in range(0, len(binstr), 8)])
    print(f"{row}: {text}")

# 58: y experT
# 59: ise.  TH
# 60: is flag(00000000)
# 61: is for Y
# 62: ou: tjcT
# 63: f{test_F
# 64: lag_is_H
# 65: ere_and_
# 66: it_is_vE
# 67: ry_very_
# 68: loooong(00000001)
# 69: }(00000000)(00000000)(00000000)(00000000)(00000000)(00000000)(00000000)
