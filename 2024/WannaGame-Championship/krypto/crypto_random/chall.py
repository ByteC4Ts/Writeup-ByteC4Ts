import random

random.seed(random.randint(0, 10000))
flag = [c for c in open("flag.txt", "rb").read()]
for _ in range(1337):
  flag = [x ^ y for x, y in zip(flag, [random.randint(0, 255) for _ in range(len(flag))])]
print(bytes(flag).hex())

# 0203e2c0dd20182bea1d00f41b25ad314740c3b239a32755bab1b3ca1a98f0127f1a1aeefa15a418e9b03ad25b3a92a46c0f5a6f41cb580f7d8a3325c76e66b937baea