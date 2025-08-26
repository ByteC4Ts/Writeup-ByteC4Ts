from Crypto.Util.number import *
# from secret import flag
import random

flag = b'W1{wi3rd_ch41!En9e_n33d_4_WlErD_s0O!luti0n_6f339749663eeb3508c3b00c15872e41}'

class RAS(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = (p**3 - p)*(q**3 - q)

    def generate_e(self):
        e = random.randint(self.p * self.q, (self.p * self.q)**2)
        return e

    def encrypt(self, pt):
        e = self.generate_e()
        assert pt < self.n
        c = pow(pt, e, self.n)
        return e, c

flag1, flag2, flag3 = bytes_to_long(flag[:len(flag)//3]), bytes_to_long(flag[len(flag)//3:2*len(flag)//3]), bytes_to_long(flag[2*len(flag)//3:])

# shuffle it
m1 = flag1*flag2*flag3
m2 = flag1 + flag2 + flag3
m3 = flag1 * flag2 + flag2 * flag3 + flag3 * flag1

nbit = 256
menu = '''
Welcome to my RAS
1. Send primes
2. Get encrypted flag
'''

b = False
print(m1, m2, m3)
print(menu)
while True:
    try:
        choose = input('> ')
        if choose == '1':
            primes = input(f"Send me two {nbit}-bit strong primes, separated by comma: ")
            try:
                p, q = map(int, primes.strip().split(','))
            except:
                raise Exception("Invalid input")

            if (isPrime(p) and isPrime(q) and
                p != q and
                p.bit_length() == q.bit_length() == nbit):
                b = True
                ras = RAS(p, q)
            else:
                print("Primes not strong enough!")
        elif choose == '2':
            if b:
                print(ras.encrypt(m1))
                print(ras.encrypt(m2))
                print(ras.encrypt(m3))
            else:
                raise Exception("You must send strong primes first!!!")
        else:
            raise Exception("Invalid choice!!!")

    except Exception as e:
        print(f"Error: {str(e)}")
        break
