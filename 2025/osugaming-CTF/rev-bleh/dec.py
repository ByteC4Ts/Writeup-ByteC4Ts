import json


def dec(target_hex):
    key = "PL4YING_CTFS_ISNTBETTER_THAN_OSU"
    target = bytes.fromhex(target_hex)
    state = 4919
    decrypted = []

    for i in range(32):
        y = (target[i] - (state + 128)) % 256
        z = (y ^ (ord(key[i]) + 128)) % 256
        x = (z - 6) % 256
        decrypted.append(chr(x))
        state = target[i]

    return "".join(decrypted)


extracted = json.load(open("extracted.json"))
extracted = sorted(extracted.items(), key=lambda x: int(x[0][4:]))
inp = ""
for file, h in extracted:
    print(f"{file}: {dec(h)}")
    inp += dec(h)

with open("inp.jpg", "wb") as f:
    f.write(bytes.fromhex(inp))

# osu{bl3h_bleh_b13h_m4n_1_l0v3_aut0_r3vs_e4fb25f｝
