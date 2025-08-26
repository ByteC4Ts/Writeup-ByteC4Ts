## Solution

This challenge is quite straightforward when `otp()` is just a repeated-key XOR operation, and server' `KEY` is 160-byte length. Cuz server accept our 160-byte plaintext, the `KEY` is ezly recovered.     


Take a glance on `string.ascii_letters + string.digits`, all of them are 0-leading, meaning that they are in form `0b0xxxxxxx`, there is no information lost when rotating 1 bit to the left (in case of `alive` cat). Script to recover:

```python
def ret(cs):
    res = bytearray()
    for c in cs:
        res.append(c ^ 0xAC >> 1)
    return res
```

Just gacha till the cat is "_alive_", and capture flag.


## Flag
```
INTIGRITI{d34d_0r_4l1v3}
```