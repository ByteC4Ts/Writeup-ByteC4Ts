from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from itertools import product
import random

k1 = k3 = b"\x9dy\xb1\xa3\x7f1\x80\x1c"
choices = [209, 26, 103, 6, 214, 189]
key_space = list(product(choices[:4], repeat=8))
key_space = [bytes(k) for k in key_space]


# ================================

# 1. pt:  b"example"
# 2. ct1: enc(pt, key1)
# 3. ct2: enc(ct1, key2)
# 4. ct2: 7125383e330c692c75e0ee0886ec7779


# pt:  b"example"
# ct1: enc(pt, key1)
#        |
#   mapping1: key1 -> ct1 (65536)    enc(pt, key1) for every key1
#        |
#        ---> intersection!
#        |
#   mapping2: key2 -> ct1 (65536)    dec(ct2, key2) for every key2
#        |
# ct2: enc(ct1, key2)
# ct2: 7125383e330c692c75e0ee0886ec7779

def aes_enc(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)


def aes_dec(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)


pt = pad(b"example", 16)
ct_example = bytes.fromhex("7125383e330c692c75e0ee0886ec7779")

mapping1 = {k1 + k: aes_enc(pt, k1 + k) for k in key_space}
mapping2 = {k + k3: aes_dec(ct_example, k + k3) for k in key_space}
intersection = list(set(mapping1.values()) & set(mapping2.values()))
print(intersection)  # [b'\x9c\xc97\x93:\x95\xb1\xfb\xfb\xbdM\x0eOd\x14g']
ct1 = intersection[0]

key1 = next((k for k, v in mapping1.items() if v == ct1))
key2 = next((k for k, v in mapping2.items() if v == ct1))

ct_flag = bytes.fromhex("9ecba853742db726fb39e748a0c5cfd06b682c8f15be13bc8ba2b2304897eca2")
print(aes_dec(aes_dec(ct_flag, key2), key1))  # b'tjctf{m33t_in_th3_middl3}\x07\x07\x07\x07\x07\x07\x07'
