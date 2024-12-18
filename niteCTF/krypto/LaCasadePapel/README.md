# niteCTF
<br>

## LaCasadePapel
<br>

## Approach
Take a quick look at source code, realise that `md5()` function return a `base64` encoded string. We can recover original `hash` ezly using `base64.b64decode()` function.
```python
def md5(secret, msg):
    hash = hashlib.md5(secret + msg).hexdigest().encode()
    return base64.b64encode(hash).decode()
cp = md5(secret, msg)
hash = base64.b64decode(cp)
```
In `fool_alice()` function, `user_hmac = base64.b64decode(md5(secret, user_name))`, correct `user_hmac` can be recovered like follow:
```python
cp = md5(secret, b'Bob33') #give it to server
hmac = base64.b64decode(cp)
#now receive password
```
`password` is obtained from step 2 - `fool_alice()`, give it to server and recover `flag`.

# Flag
```
nite{El_Prof3_0f_Prec1s10n_Pl4ns}
```