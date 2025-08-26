import gostcrypto, os
# from secret import key
from Crypto.Util.Padding import pad


# with open("flag.txt", "rb") as f:
#     flag = bytearray(f.read())
key = bytes(range(36, 36 + 32))
flag = b'W1{4a9f2b823dc8d09fd732d741954ccce2}'
try:
    plaintext = bytearray.fromhex(input("Plaintext (hex): "))
    plaintext = pad(plaintext + flag, 16)

    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    print(ciphertext.hex())
except Exception as e:
    print(e)
    exit(0)
