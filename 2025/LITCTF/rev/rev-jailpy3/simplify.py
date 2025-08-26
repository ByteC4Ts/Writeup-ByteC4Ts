# Python 3.13
import re

# code.py is not uploaded due to its size is too large ^v^
with open("code.py", "r") as f:
    code = f.read()


def simplify1(code):
    def replace_fn(match):
        return '"' + eval(match.group()) + '"'

    pattern = r"(?:chr\((?:\d+(?:\^\d+)+)\)\+)+(?:chr\((?:\d+(?:\^\d+)+)\))"
    return re.sub(pattern, replace_fn, code)


def simplify2(code):
    def replace_fn(match):
        return str(eval(match.group()))

    pattern = re.escape(
        r'{}.__class__.__subclasses__()[2].copy.__builtins__["__import__"]("subprocess").select.') + "[A-Z]+"
    return re.sub(pattern, replace_fn, code)


def simplify3(code):
    pattern = re.escape(r'{}.__class__.__subclasses__()[2].copy.__builtins__["chr"]')
    return re.sub(pattern, "chr", code)


code = simplify1(code)
code = simplify2(code)
code = simplify3(code)
code = simplify1(code)
code = simplify2(code)
code = simplify3(code)
code = simplify1(code)

with open("code-simplify.py", "w") as f:
    f.write(code)

# LITCTF{h0w_c0nvolu7ed_c4n_i7_g37_f0r_0n3_s1mpl3_w0rk4round??}
