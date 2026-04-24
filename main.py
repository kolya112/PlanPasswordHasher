import hashlib
import binascii
import os

password = "12345"
iterations = 64000
salt = os.urandom(18)
hash_name = 'sha1'

dk = hashlib.pbkdf2_hmac(hash_name, password.encode(), salt, iterations)

salt_b64 = binascii.b2a_base64(salt).decode('ascii').strip()
hash_b64 = binascii.b2a_base64(dk).decode('ascii').strip()

print(f"{hash_name}:{iterations}:18:{salt_b64}:{hash_b64}")