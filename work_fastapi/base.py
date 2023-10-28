# from jose.backends.rsa_backend import RSAKey
# from jose.constants import ALGORITHMS
# RSAKey(key=public_key, algorithm=ALGORITHMS.RS256)
# JWT_SIGNATURE_ALGORITHM = "RS256"
# with open("private_key.pem", "r") as f:
#     JWT_SIGNATURE_PRIVATE_KEY = f.read()
# with open("public_key.pem", "r") as f:
#     JWT_SIGNATURE_PUBLIC_KEY = f.read()

JWT_SIGNATURE_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" #THIS IS SAMPLE
