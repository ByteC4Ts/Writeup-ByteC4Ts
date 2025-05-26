with open("flag.sh", "rb") as f:
    content = f.read()

simplified = b""

for ch in content:
    if 32 <= ch <= 126:
        simplified += bytes([ch])

with open("flag_simplified.sh", "wb") as f:
    f.write(simplified)
