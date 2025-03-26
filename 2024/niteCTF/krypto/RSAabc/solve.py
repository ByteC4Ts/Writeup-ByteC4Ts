import os.path as path
from sage.all import *
import ast

ABSPATH = path.abspath(path.dirname(__file__))


def mod_inv(inp):
    res = []
    for n in inp:
        fs = list(factor(n))
        fs = [(p ** (e - 1) * (p - 1)) for p, e in fs]
        res += [prod(fs)]
    return [pow(0x10001, -1, phi) for phi in res]


def reverse_char(char):
    if char == "e":
        return "_"
    if char.isupper():
        return chr(155 - ord(char))
    elif char.islower():
        return chr(219 - ord(char))


def googly(number, position):
    mask = 1 << position
    return number ^ mask


file = open(path.join(ABSPATH, "out.txt"))

cipher, cs, ns = file.read().strip().split("\n")

cs = ast.literal_eval(cs)
ns = ast.literal_eval(ns)


language = {
    "Α": "A",
    "α": "a",
    "Β": "B",
    "β": "b",
    "Σ": "S",
    "σ": "c",
    "Δ": "D",
    "δ": "d",
    "Ε": "E",
    "ε": "e",
    "Φ": "F",
    "φ": "f",
    "Γ": "G",
    "γ": "g",
    "Η": "H",
    "η": "h",
    "Ι": "I",
    "ι": "i",
    "Ξ": "J",
    "ξ": "j",
    "Κ": "K",
    "κ": "k",
    "Λ": "L",
    "λ": "l",
    "Μ": "M",
    "μ": "m",
    "Ν": "N",
    "ν": "n",
    "Ο": "O",
    "ο": "o",
    "Π": "P",
    "π": "p",
    "Θ": "Q",
    "θ": "q",
    "Ρ": "R",
    "ρ": "r",
    "ς": "s",
    "Τ": "T",
    "τ": "t",
    "Υ": "Y",
    "υ": "y",
    "Ω": "V",
    "ω": "v",
    "Ψ": "W",
    "ψ": "w",
    "Χ": "X",
    "χ": "x",
    "Ζ": "Z",
    "ζ": "z",
}


pt = []

ds = mod_inv(ns)

for i, ch in enumerate(cipher):
    if ch.isascii():
        pt += [reverse_char(ch)]
        continue
    eng = language.get(ch)
    c = googly(cs[i], cs[i].bit_length() - ord(eng))
    pt += [chr(pow(c, ds[i], ns[i]))]


print("".join(pt))
