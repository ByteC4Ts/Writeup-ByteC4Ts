from pwn import *
from Crypto.Util.number import long_to_bytes, isPrime
from gmpy2 import mpz


def main():
    cnn = remote("verbal-sleep.picoctf.net", 51434)

    cnn.recvuntil(b"N: ")
    n = mpz(cnn.recvuntil(b"\ne", drop=True))
    cnn.recvuntil(b"cyphertext: ")
    c = mpz(cnn.recvuntil(b"\n", drop=True))
    p = n // 2
    q = n // p
    assert isPrime(p) and n == p * q

    d = pow(0x10001, -1, (p - 1) * (q - 1))

    print(long_to_bytes(pow(c, d, n)))


if __name__ == "__main__":
    main()
