"""
TEST POST
"""
# import json
# import requests

# send_headers = {
#     "Content-Type": "application/json",
# }
# send_data = {
#     "user_name": "shinbot",
#     "user_password": "shinbot",
# }

# res = requests.post(
#     url="http://localhost:8000/login-user",
#     data=json.dumps(send_data),
#     headers=send_headers
# )

# print(res.status_code)
# print(res.json())


"""
TEST PASSWORD
"""
# from handlers.password_handler import PasswordHandler

# raw_password = "shinbot"
# hashed_password = PasswordHandler.hash_password(raw_password=raw_password)
# print(f"{raw_password}: {hashed_password}")

# print(
#     PasswordHandler.verify_password(
#         raw_password="shinbot",
#         hashed_password="$2b$12$rsf3thhIeMPCJrMdR8Os6.d4maX0QBVs3P7kH7bw9Z2pYHfX8EZdq",
#     )
# )
# "$2b$12$rsf3thhIeMPCJrMdR8Os6.d4maX0QBVs3P7kH7bw9Z2pYHfX8EZdq"


"""

"""
# from typing import Tuple
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
# import base64


# def generate_rsa_keypair() -> Tuple[str, str]:
#     # キーペアの生成
#     private_key = rsa.generate_private_key(
#         public_exponent=65537,
#         key_size=2048,
#         backend=default_backend()
#     )
    
#     # 私有鍵をPEM形式でシリアライズ
#     pem_private = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption()
#     )
    
#     # 公開鍵をPEM形式でシリアライズ
#     public_key = private_key.public_key()
#     pem_public = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )
    
#     # base64 エンコード
#     pem_private_base64 = base64.b64encode(pem_private).decode('utf-8')
#     pem_public_base64 = base64.b64encode(pem_public).decode('utf-8')
    
#     return pem_private_base64, pem_public_base64

# private_key_base64, public_key_base64 = generate_rsa_keypair()
# print("Private Key:", private_key_base64)
# print("Public Key:", public_key_base64)


# """
# Pydantic
# """
# from typing import Optional
# from pydantic import BaseModel, Field, ValidationError


# class User(BaseModel):
#     user_name: Optional[str] = Field(min_length=4, max_length=20)
#     user_password: Optional[str] = Field(min_length=8, max_length=20)

# try:
#     user = User(user_name="aa", user_password="123")
# except ValidationError as e:
#     error_message = ""
#     for error in e.errors():
#         field = error['loc'][0]
#         msg = error['msg']
#         error_message += f"{field}: {msg}\n"


import time


def sample_generator():
    cnt = 0
    while cnt < 5:
        cnt += 1
        time.sleep(1)
        yield cnt


for cnt in sample_generator():
    print(cnt)