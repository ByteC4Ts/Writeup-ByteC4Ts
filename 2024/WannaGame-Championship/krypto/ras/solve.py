from Crypto.Util.number import *
from sage.all import *
from pwn import *
from ast import literal_eval
import sympy

io = process(['python3', '2024/wannagamectf/ras/chall.py'])

def recv_data():
    return literal_eval(io.recvline().decode())


cs, es, ps = [], [], []
for _ in range(100):
    p, q = getPrime(256), getPrime(256)
    
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b'comma: ', f'{p},{q}'.encode())
    
    io.sendlineafter(b'> ', b'2')

    valid = True
    tmp_es, tmp_cs = [], []
    for _ in range(3):
        e, c = recv_data()
        tmp_es.append(e)
        tmp_cs.append(c)
        if gcd(e, p - 1) != 1:
            valid = False
            break
    
    if valid:
        ps.append(p)
        es.append(tmp_es)
        cs.append(tmp_cs)


# calc actual remainders
rs1, rs2, rs3 = [], [], []
for p, el, cl in zip(ps, es, cs):
    e1, e2, e3 = el
    c1, c2, c3 = cl
    d1, d2, d3 = inverse(e1, p-1), inverse(e2, p-1), inverse(e3, p-1)

    rs1.append(pow(c1, d1, p))
    rs2.append(pow(c2, d2, p))
    rs3.append(pow(c3, d3, p))



m1, m2, m3 = crt(rs1, ps), crt(rs2, ps), crt(rs3, ps)


x = sympy.symbols('x')
f1, f2, f3 = sympy.solve(x**3 - m2*x**2 + m3*x -m1, x)

print(long_to_bytes(f1) + long_to_bytes(f2) + long_to_bytes(f3))