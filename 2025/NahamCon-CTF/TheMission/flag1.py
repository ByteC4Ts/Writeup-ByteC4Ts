import requests

url = "http://challenge.nahamcon.com:31992"

resp = requests.get(url + "/robots.txt")

print(resp.text)
# User-agent: *
# Disallow: /internal-dash
#
# #flag_1{858c82dc956f35dd1a30c4d47bcb57fb}
