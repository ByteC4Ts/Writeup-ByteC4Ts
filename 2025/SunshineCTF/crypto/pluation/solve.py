from Crypto.Util import Counter
from Crypto.Cipher import AES
from pwn import xor, remote, context
import re
context.log_level = 'debug'


conn = remote('chal.sunshinectf.games', 25403)


known = b'Greetings, Earthlings.'[:16]
c = 0


conn.recvuntil('== BEGINNING TRANSMISSION ==\n\n')

cts = []
for _ in range(64):
    cts.append(bytes.fromhex(conn.recvline().strip().decode()))


ks = [xor(known, c[:16]) for c in cts]


keystream = b''.join(ks)


message = xor(keystream, cts[0])


print(re.findall(b'sun{.*}', message))