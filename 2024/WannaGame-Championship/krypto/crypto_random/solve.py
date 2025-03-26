import random
import tqdm

logo = """

██████╗ ██╗   ██╗████████╗███████╗ ██████╗██╗  ██╗████████╗███████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝██║  ██║╚══██╔══╝██╔════╝
██████╔╝ ╚████╔╝    ██║   █████╗  ██║     ███████║   ██║   ███████╗
██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ██║     ╚════██║   ██║   ╚════██║
██████╔╝   ██║      ██║   ███████╗╚██████╗     ██║   ██║   ███████║
╚═════╝    ╚═╝      ╚═╝   ╚══════╝ ╚═════╝     ╚═╝   ╚═╝   ╚══════╝

"""
print(logo)


for seed in tqdm.trange(10000):
    random.seed(seed)
    c = bytes.fromhex(
        "0203e2c0dd20182bea1d00f41b25ad314740c3b239a32755bab1b3ca1a98f0127f1a1aeefa15a418e9b03ad25b3a92a46c0f5a6f41cb580f7d8a3325c76e66b937baea"
    )
    pun = []
    for _ in range(1337):
        pun += [[random.randint(0, 255) for _ in range(len(c))]]
    for p in pun[::-1]:
        c = [x ^ y for x, y in zip(c, p)]
    if b"W1{" in bytes(c):
        print(bytes(c))
        exit()
