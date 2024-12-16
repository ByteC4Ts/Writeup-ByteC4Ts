# m0leCon Beginner CTF

## Locked Door

> https://lockeddoor.challs.m0lecon.it/

## Approach

You can find `onclick="window.location.href='/xugpuhru'"` on the `#access_log_button`, removed the `disabled` attribute, and clicked the button.

In the "Previous Accesses" page, login with password `1' or 1=1 --` to download the `.pcap` files.

Then its a simple RSA decryption.

```python
# p, q = 11041929431171634223, 11919228246160504141
# cipher = 45580334060331476061869342097707478745

p, q = 9962676558042353381, 16839954032773686901
cipher = 45538264661765883251026503237437838586

e = 65537

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
msg = pow(cipher, d, n)

print(msg)  # 99004462
```

## Flag

```
ptm{iT_1s_d17fiCu1t_t0_uNl0ck_4_d00r}
```
