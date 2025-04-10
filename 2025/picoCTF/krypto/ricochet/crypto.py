import hashlib
import monocypher
import os

def compute_hmac(message, nonce, key):
    hmac = (message + str(nonce) + key.hex()).encode()
    for _ in range(32):
        hmac = monocypher.blake2b(hmac + key)
    return monocypher.blake2b(hmac)

def add_hmac(message, nonce, key):
    hmac = compute_hmac(message, nonce, key)
    return {"message": message, "nonce": nonce, "hmac": hmac.hex()}

def validate_hmac(message, nonce, key):
    hmac = compute_hmac(message["message"], nonce, key)
    if message["hmac"] == hmac.hex() and message["nonce"] == nonce:
        return message["message"]

    return None

def encrypt(message, key):
    key = monocypher.blake2b(key)[:32]
    nonce = os.urandom(24)
    tag, ciphertext = monocypher.lock(key, nonce, message.encode())
    return ciphertext.hex() + ";" + tag.hex() + ";" + nonce.hex()

def decrypt(message, key):
    key = monocypher.blake2b(key)[:32]
    ciphertext, tag, nonce = message.split(";")
    plaintext = monocypher.unlock(key, bytes.fromhex(nonce), bytes.fromhex(tag), bytes.fromhex(ciphertext))
    return plaintext
