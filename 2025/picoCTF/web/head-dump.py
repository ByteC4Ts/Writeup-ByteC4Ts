import requests
import re

url = "http://verbal-sleep.picoctf.net:64996/heapdump"
resp = requests.get(url)
matches = re.findall(r"picoCTF\{.*?}", resp.text)
print(matches)

# picoCTF{Pat!3nt_15_Th3_K3y_439bb394}
