import jwt

SECRET_KEY = "super_safe_key"

token = jwt.encode(
    {
        "username": "jack",
        "is_admin": 1,
    },
    SECRET_KEY,
    algorithm="HS256",
)
print(token)

data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(data)

for ch in range(256):
    try:
        modified_token = token + chr(ch)
        data = jwt.decode(modified_token, SECRET_KEY, algorithms=["HS256"])
        print(ch, chr(ch), modified_token)
    except Exception as e:
        pass
