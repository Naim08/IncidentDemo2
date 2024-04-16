import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import time

def generate_jwt(private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": "your_issuer_id"
    }

    token = jwt.encode(payload, private_key, algorithm="RS256")
    return token

if __name__ == "__main__":
    private_key_path = "./resolvdapp.2024-04-15.private-key.pem"
    jwt_token = generate_jwt(private_key_path)
    print("JWT Token:", jwt_token)