from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.Padding import pad


p = 15471456606036645889
s1 = 3681934504574973317
s2 = 4155039551524372589
s3 = 9036939555423197298
iv = bytes.fromhex('6c9315b13f092fbc49adffbf1c770b54')
ct = bytes.fromhex('af9dc7dfd04bdf4b61a1cf5ec6f9537819592e44b4a20c87455d01f67d738c035837915903330b67168ca91147299c422616390dae7be68212e37801b76a74d4')



a = ((s3- s2) * pow(s2 - s1, -1, p)) % p
b = (s2 - a * s1) % p

s0 = ((s1 - b) * pow(a, -1, p)) % p


s1, s2, s3 = a, b, s0


for i in range(100):
    a = ((s3- s2) * pow(s2 - s1, -1, p)) % p
    b = (s2 - a * s1) % p

    s0 = ((s1 - b) * pow(a, -1, p)) % p
    s1, s2, s3 = a, b, s0



for _ in range(4):
    r = (a * s0 + b) % p
    s0 = r

key = pad(l2b(r**2), 16)

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
print(cipher.decrypt(ct))