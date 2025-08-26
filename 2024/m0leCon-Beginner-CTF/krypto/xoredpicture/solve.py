from pwn import xor

pic = open('2024/m0leconctf/xoredpicture/flag_enc.png', 'rb').read()

header = bytes.fromhex('89504E470D0A1A0A0000000D49484452')

key = xor(pic[:16], header)

open('2024/m0leconctf/xoredpicture/flag.png', 'wb').write(xor(key, pic))