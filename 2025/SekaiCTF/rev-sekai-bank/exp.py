import requests
import hashlib
import hmac

# ~/Library/Android/sdk/build-tools/34.0.0/apksigner verify --print-certs SekaiBank.apk
# Signer #1 certificate DN: C=ID, ST=Bali, L=Indonesia, O=HYPERHUG, OU=Development, CN=Aimar S. Adhitya
# Signer #1 certificate SHA-256 digest: 3f3cf8830acc96530d5564317fe480ab581dfc55ec8fe55e67dddbe1fdb605be
# Signer #1 certificate SHA-1 digest: 2c9760ee9615adabdee0e228aed91e3d4ebdebdf
# Signer #1 certificate MD5 digest: fcab4af1f7411b4ba70ec2fa915dee8e
cert_sha256_hex = "3f3cf8830acc96530d5564317fe480ab581dfc55ec8fe55e67dddbe1fdb605be"
key = bytes.fromhex(cert_sha256_hex)

string_to_sign = 'POST/api/flag{"unmask_flag":true}'
signature_bytes = hmac.new(key, string_to_sign.encode(), hashlib.sha256).hexdigest()
print(signature_bytes)

resp = requests.post(
    "https://sekaibank-api.chals.sekai.team/api/flag",
    json={"unmask_flag": True},
    headers={"X-Signature": signature_bytes},
)
print(resp.text)

# SEKAI{are-you-ready-for-the-real-challenge?}
