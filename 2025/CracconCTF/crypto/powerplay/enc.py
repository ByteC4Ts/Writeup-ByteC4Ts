from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import flag,key
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(flag, AES.block_size))
print(ciphertext.hex())
#f0f931dd9fe3b1568a8fac88f61d55c76d356778ba7a6e0b08d0fbee83a9314b68f8a4c92c534d71daf22b88de551a11