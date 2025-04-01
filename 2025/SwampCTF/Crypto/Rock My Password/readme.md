# Rock My Password

## Approach

Generate a dictionary containing all 10-digit passwords in `rockyou.txt`:

```python
with open("rockyou.txt", "r", encoding="iso-8859-1") as f:
    lines = f.readlines()

print(len(lines))  # 14344392
lines = [line.strip() for line in lines]
lines = list(filter(lambda x: len(x) == 10, lines))
lines = [f"""swampCTF{{{line}}}""" for line in lines]  # swampCTF{rockyoupassword}
print(len(lines))  # 2013689

with open("dict.txt", "w") as f:
    f.write("\n".join(lines))
```

`dict.txt` should be like:

```
swampCTF{1234567890}
swampCTF{basketball}
swampCTF{tinkerbell}
swampCTF{hellokitty}
...
```

Then crack the password:

```python
from hashlib import md5, sha256, sha512
import tqdm


def myhash(password):
    data = password.encode()
    for _ in range(100):
        data = md5(data).digest()
    for _ in range(100):
        data = sha256(data).digest()
    for _ in range(100):
        data = sha512(data).digest()
    return data.hex()


with open("dict.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
target = "f600d59a5cdd245a45297079299f2fcd811a8c5461d979f09b73d21b11fbb4f899389e588745c6a9af13749eebbdc2e72336cc57ccf90953e6f9096996a58dcc"
for line in tqdm.tqdm(lines):
    if myhash(line) == target:
        print(line)
        break

# swampCTF{secretcode}
```
