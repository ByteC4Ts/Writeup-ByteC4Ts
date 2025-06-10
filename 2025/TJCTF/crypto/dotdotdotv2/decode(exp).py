import numpy as np
from z3 import *

n = 64

filler = "In cybersecurity, a CTF (Capture The Flag) challenge is a competitive, gamified event where participants, either individually or in teams, are tasked with finding and exploiting vulnerabilities in systems to capture hidden information known as flags. These flags are typically used to score points. CTFs test skills in areas like cryptography, web security, reverse engineering, and forensics, offering an exciting way to learn, practice, and showcase cybersecurity expertise.  This flag is for you: "
filler += "tjct"
filler = "".join([bin(ord(i))[2:].zfill(8) for i in filler])
pt = filler
pt = pt + "0" * (n - len(pt) % n)
print(len(pt), pt)  # 4096 0100100101101110...

mat_pt = np.array([list(map(int, list(pt[i:i + n]))) for i in range(0, len(pt), n)])

mat_ct = []
with open("encoded.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
for line in lines:
    mat_ct.append(list(map(int, line.split())))
mat_ct = np.array(mat_ct)


def solve_mat_key_col(col):
    s = Solver()
    sym_key_col = [Int(f"key_{row}") for row in range(n)]

    for row in range(n):
        s.add(sym_key_col[row] >= 0)
        s.add(sym_key_col[row] <= 0xdeadbeef)

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

# 58: y expert
# 59: ise.  Th
# 60: is flag
# 61: is for y
# 62: ou: tjct
# 63: f{us3fu2
# 64: 89312953
# 65: }(00000000)(00000000)(00000000)(00000000)(00000000)(00000000)(00000000)

# tjctf{us3fu289312953}
