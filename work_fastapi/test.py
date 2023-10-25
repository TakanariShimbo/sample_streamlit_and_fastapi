import json
import requests


# res = requests.get(url="http://localhost:8000")
# print(res.status_code)
# print(res.text)


send_headers = {
    "Content-Type": "application/json",
}
send_data = {
    "user_name": "shinbot",
    "user_password": "shinbot",
}

res = requests.post(
    url="http://localhost:8000/login-user",
    data=json.dumps(send_data),
    headers=send_headers
)

print(res.status_code)
print(res.json())
