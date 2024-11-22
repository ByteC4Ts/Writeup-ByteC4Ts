# BlueHens CTF

## XS1

> XS1: XOR without XOR

```python
# In [15]: (flag*32)[::17][:32]
# Out[15]: 'u_cnfrj_sr_b_34}yd1tt{0upt04lbmb'
```

## Approach

```python
out = "u_cnfrj_sr_b_34}yd1tt{0upt04lbmb"
flag = [" "] * 100

for i in range(len(out)):
    flag[i] = out[(i * 17) % 32]

print("".join(flag))
```

## Flag

```
udctf{just_4_b4by_1ntr0_pr0bl3m}
```
