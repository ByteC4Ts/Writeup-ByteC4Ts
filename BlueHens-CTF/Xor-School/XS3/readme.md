# BlueHens CTF

## XS1

> XS3: Roman Xor

> https://gist.github.com/AndyNovo/309325b566b2df42b984e2401fedbaab

## Approach

### Step 1: leak the possible position

Firstly, this challenge encrypting multiple plaintexts with the same key. Noticed the XOR between ASCII characters is less than `64`, while the XOR between an ASCII character and a space is greater than `64`. In the first phase, we identify the possible leaked chars.




## Flag

```
udctf{crypto_web_misc_4ll_0f_th3_ab0ve}
```
