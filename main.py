import hashlib
import base64
import os


def generate_plan_password(password_text):
    iterations = 64000
    salt_size = 18
    key_size = 18
    salt = os.urandom(salt_size)

    dk = hashlib.pbkdf2_hmac('sha1', password_text.encode(), salt, iterations, key_size)

    salt_b64 = base64.b64encode(salt).decode('ascii').rstrip('=')
    hash_b64 = base64.b64encode(dk).decode('ascii').rstrip('=')

    return f"sha1:{iterations}:{salt_size}:{salt_b64}:{hash_b64}"


print(generate_plan_password("12345"))