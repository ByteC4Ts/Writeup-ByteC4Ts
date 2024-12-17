# 1337Up Live CTF
<br>

## Schodinger Pad
_An easy XOR challenge_
<br>

## Approach
Let's take a quick look at the `otp()` function:
```python
MAX_LENGTH = 160
KEY = ''.join(random.choices(
            string.ascii_letters + string.digits, k=160)).encode()
def otp(p, k):
    k_r = (k * ((len(p) // len(k)) + 1))[:len(p)]
    return bytes([p ^ k for p, k in zip(p, k_r)])
```

Notice that if `len(p) == len(k)`, then `k_r = k * 2[:len(p)]`, or basically `k_r = k`.    
So I will send the payload of _160-byte_ length:
```python
payload = b'3rg0u' * 32
key = otp(payload, KEY)
key = xor(key, payload)
```
Now, we successfully recovered the original `KEY`. The next step is to find original `ciphertext`. Glance at the `check_cat_box()` function:
```python
def check_cat_box(ciphertext, cat_state):
    c = bytearray(ciphertext)
    if cat_state == 1:
        for i in range(len(c)):
            c[i] = ((c[i] << 1) & 0xFF) ^ 0xAC
    else:
        for i in range(len(c)):
            c[i] = ((c[i] >> 1) | (c[i] << 7)) & 0xFF
            c[i] ^= 0xCA
    return bytes(c)
```
Get back to the `KEY`, if we print all the values in `string.ascii_letters + string.digits` in binary, all of them have the form `0b0xxxxxxx`. So, we shift them to the left 1-bit, them will become `0bxxxxxxx0`, ez to recover.
```python
def ret(cs):
    res = bytearray()
    for c in cs:
        res.append(c ^ 0xAC >> 1)
    return res
```
Finally, we have to gacha until ''_the cat still alive_'', get the `ciphertext` and decipher.

```python
key = xor(ret(c_cipher), PAYLOAD)
flag = xor(flag_encrypted, key)
```

## Flag
```
INTIGRITI{d34d_0r_4l1v3}
```