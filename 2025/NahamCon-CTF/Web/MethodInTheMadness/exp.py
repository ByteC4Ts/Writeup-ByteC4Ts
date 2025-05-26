import requests

url = "http://challenge.nahamcon.com:31569/"

requests.get(url + "interesting")
requests.post(url + "interesting")
requests.put(url + "interesting")
requests.options(url + "interesting")
requests.delete(url + "interesting")
requests.patch(url + "interesting")

print(requests.get(url + "poll").text)

# flag{bd399cb9c3a8b857588d8e13f490b6fd}
