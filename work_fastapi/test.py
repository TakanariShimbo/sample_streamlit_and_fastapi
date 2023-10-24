import json
import requests


# res = requests.get(url="http://localhost:8000")
# print(res.status_code)
# print(res.text)


send_headers = {
    "Content-Type": "application/json",
}
send_data = {
    "user_name": "takanari shimbo",
    "user_password": "!qaz2wsx",
}

res = requests.post(
    url="http://localhost:8000/create-user",
    data=json.dumps(send_data),
    headers=send_headers
)

print(res.status_code)
print(res.json())
