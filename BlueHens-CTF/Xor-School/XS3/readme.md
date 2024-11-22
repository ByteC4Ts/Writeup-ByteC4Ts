# BlueHens CTF

## XS1

> XS3: Roman Xor

> https://gist.github.com/AndyNovo/309325b566b2df42b984e2401fedbaab

## Approach

### Step 1: leak the possible position

Firstly, this challenge encrypting multiple plaintexts with the same key. Noticed the XOR between ASCII characters is less than `64`, while the XOR between an ASCII character and a space is greater than `64`. In the first phase, we identify the possible leaked chars.

```python
ciphers = [
    '43794c9c8faa2cff24edc8afe507a13f62837c7e166f428cab5aff893225ff19104bc8754c1c09',
    '5d315e8786e62cf763e9d4afe80ca13b649a717e11615986b642f3952f76b71b0342c4',
    '46785a8bcae62aeb60a5deeef107a1256ed7792752695886ff50f5886171ff1717',
    '5d315e819fe621b966e08dfae906e43a78837b31162e5e8cff46e8953275f20a0d5ad23d4712144c',
    '557f4dce9ee220b967e4dfffe616e9216a9934291b7d5690bb45ba922e6afc',
    '55315a868fef35f16beac6afe810a1206a81717e1e6b5690b152ba953462ff0c424acd6e0307055a81b93590c1fe',
    '557d489dcafd2df870a5cfe0e816f268628334291b7a5fc2aa58f99f3276f616160fc27c5116',
    '557f4dce8bee21fc24f1c5eaa712ee3f6e853431142e448db216fb9e2b70e5110c48816b46011e5a',
    '407e099783ef29fd24edc4fca704f33d6283343f1c6a178ab645ba962464f1581147c0714f530350d5f53690dee6',
    '40785ace93e530b970edccfba711e0312b9e607e1c6143c2b616e3953425f317425bc9780317085ac5a6',
]

# target:
target = "41754a9a8cf13da976dac4e1d810b1253f994b6f47514387b106e8a57175a40a0370d22c4d14084d9ea8"


def cipher_to_byte_list(cipher):
    return [int(cipher[i:i + 2], 16) for i in range(0, len(cipher), 2)]


ciphers = [cipher_to_byte_list(c) for c in ciphers]
target = cipher_to_byte_list(target)

stats = [[] for _ in range(len(target))]


def leak(cipher):
    for i in range(min(len(target), len(cipher))):
        if target[i] ^ cipher[i] >= 64:
            stats[i].append(cipher[i] ^ target[i] ^ ord(' '))


for cipher in ciphers:
    leak(cipher)


def mode(ls):
    if ls:
        return max(set(ls), key=ls.count)
    else:
        return 0


message = ""
for stats_ch in stats:
    if len(stats_ch) > 4:
        message += "."
    else:
        m = mode(stats_ch)
        if len(stats_ch) == 1 or stats_ch.count(m) > 1:
            message += chr(m)
        else:
            ch = "."
            for c in stats_ch:
                if 65 <= c <= 90 or 97 <= c <= 122:
                    ch = chr(c)
            message += ch

print(message)
```

```
.dctf{..r_in_..m.n_.._ten.r..p.ra_s.ng..k}
```

### Step 2: guess char by char from the start

There are some cases that `.` appears: maybe at this position none of the ciphertext is a space, or the character's ASCII value is less than `64` (such as a digit), etc. However, with prior knowledge, we can immediately see that the first few letters of the flag are `"udctf"`, which allows us to enter the second phase of guessing.

Because this challenge states that the ciphertext is a sentence from a poem, we can always guess the next character of an incomplete word based on the semantics of a sentence. As long as the next position of any ciphertext is restored, we can restore that digit of the key.

In theory, this can be repeated indefinitely, but actually after guessing a certain number of characters, we can search them on Google, and find the original text: https://milton.host.dartmouth.edu/reading_room/comus/text.shtml

### Step 3: restore the entire key

In the third phase, finding a sentence (if it is long enough) can restore the entire key. The final code is as follows, it was not written all at once, but was supplemented while guessing.

```python
# ----- guess the rest -----

ciphers.append(cipher_to_byte_list(
    "41754a9a8cf13da976dac4e1d810b1253f994b6f47514387b106e8a57175a40a0370d22c4d14084d9ea8"  # target
    # "d c t f { x 0 r _ i n _ r 0 m 4 n _ 1 5 _ t e n 0 r _ 0 p 3 r a _ s 1 n g e r ? } "
))
key = [
    52, 17, 41, 238, 234, 138, 69, 153, 4, 133, 173, 143, 135, 98, 129, 72, 11, 247, 20, 94, 114, 14, 55,
    226, 223
]  # try byte by byte

# enough info to find the poem:
# https://milton.host.dartmouth.edu/reading_room/comus/text.shtml

c7 = "and adde the power of som adjuring verse"
for i in range(len(key), len(c7)):
    key.append(ord(c7[i]) ^ ciphers[7][i])

key.append(161)
key.append(213)

for cipher in ciphers:
    for i in range(min(len(key), len(cipher))):
        print(chr(cipher[i] ^ key[i]), end="")
    print()
```

## Flag

```
udctf{x0r_in_r0m4n_15_ten0r_0p3ra_s1nger?}
```
