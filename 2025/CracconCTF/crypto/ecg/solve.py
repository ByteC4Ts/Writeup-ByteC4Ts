from math import gcd
from sage.all import factor
from Crypto.Util.number import long_to_bytes as ltb
from tqdm import trange


xs = [1471188920,8580498,528503476,577384753,534687615,631132756,1181691587,494356384,450508778,224733577,240456085]

s0, s1, s2, s3, s4 = xs[:5]

t1 = (s2-s1)**2 - (s3-s2)*(s1-s0)
t2 = (s3-s2)**2 - (s4-s3)*(s2-s1)

n = list(factor(gcd(t1, t2)))[-1][0]

e = (1 <<65537) % (n - 1)

cm = (pow(s1-s0, -1, n) * ((s2-s1) % n)) % n

c = (s2 - ((cm * s1) % n)) % n

S = (((s0 - c) % n) * pow(cm, -1, n)) % n


def roots_of_unity(e, phi, n, rounds=500):
    phi_coprime = phi
    while gcd(phi_coprime, e) != 1:
        phi_coprime //= gcd(phi_coprime, e)

    roots = set(pow(i, phi_coprime, n) for i in trange(1, rounds))

    assert all(pow(root, e, n) == 1 for root in roots)
    return roots, phi_coprime


roots, phi = roots_of_unity(e, n - 1, n)


d = pow(e, -1, phi)
m = pow(cm, d, n)

assert(pow(m, e, n)) == cm


segs = b''.join([ltb(x) for x in [n, S, c]])

for m in [ltb((m * root) % n) for root in roots]:
    print(b'possible flag: craccon{%b}' % (segs + m))
