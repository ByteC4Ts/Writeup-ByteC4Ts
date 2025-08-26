import random, tqdm, re





for seed in tqdm.trange(10000):
    random.seed(seed)
    ct = bytes.fromhex('0203e2c0dd20182bea1d00f41b25ad314740c3b239a32755bab1b3ca1a98f0127f1a1aeefa15a418e9b03ad25b3a92a46c0f5a6f41cb580f7d8a3325c76e66b937baea')

    tokens = [[random.randint(0, 255) for x in range(len(ct))] for y in range(1337)][::-1]

    for tok in tokens:
        ct = [x ^ y for x, y in zip(ct, tok)]

    if re.match(b'W1\{.*\}', bytes(ct)):
        print(bytes(ct))
        exit()
