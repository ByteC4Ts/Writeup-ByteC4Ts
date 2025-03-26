# WannaGame Championship
<br>

## Crypto Random
<br>

A XOR challenge<br>
## Approach
Cuz the `seed` is in `range(10000)`, it's feasible to brute force.    
With each seed, create a list of length `1337`, which each element is a list of `len(c)` numbers in `range(0, 255)`.
```python
for seed in trange(10000):
    c = bytes.fromhex('0203e2c0dd20182bea1d00f41b25ad314740c3b239a32755bab1b3ca1a98f0127f1a1aeefa15a418e9b03ad25b3a92a46c0f5a6f41cb580f7d8a3325c76e66b937baea')
    random.seed(seed)
    pun = []
    for _ in range(1337):
        pun += [[random.randint(0, 255) for _ in len(c)]]
```
Now reverse `pun` and `xor` `c` with all elements in `pun`. Check if `b'W1{'` in result, print it and exit.
```python
for p in pun[::-1]:
        c = [x ^ y for x, y in zip(c, p)]
    if b"W1{" in bytes(c):
        print(bytes(c))
        exit()
```
## Flag
```
W1{maybe_the_seed_is_too_small..._b32fe938a402c22144b9d6497fd5a709}
```