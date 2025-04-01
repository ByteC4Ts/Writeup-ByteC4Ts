# Lost In Translation

## Approach

The provided script doesn’t have any obvious vulnerabilities, but the indents and spaces are quite strange!!

```python
with open("challenge.js", "r") as f:
    lines = f.readlines()

for line in lines[::2]:
    b = ""
    for ch in line:
        if ch == " ":
            b += "0"
        if ch == "\\t":
            b += "1"

    if len(b) < 4:
        continue

    i = int(b, 2)
    if i < 0x20:
        print(i & 0xf, end="")
    else:
        print(chr(i & 0xff), end="")

# swampCTF{Whit30ut_W0rk5_W0nd3r5}
```
