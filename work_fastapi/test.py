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
TEST JwtHandler
"""
# from handlers.jwt_handler import JwtHandler, JwtPayload

# original_jwt_payload = JwtPayload.init_with_defaults(aud="AudienceName")
# print(original_jwt_payload.to_dict())

# true_jws_str = JwtHandler.encode_to_jws(jwt_payload=original_jwt_payload)
# print(true_jws_str)

# decoded_jwt_payload = JwtHandler.decode_from_jws(jws_str=true_jws_str)
# print(decoded_jwt_payload.to_dict())


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
