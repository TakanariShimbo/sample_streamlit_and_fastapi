from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


"""
Base
"""
class LoginUser(BaseModel):
    user_name: str
    user_password: str

class CreateUser(BaseModel):
    user_name: str
    user_password: str

class User(CreateUser):
    user_id: int


"""
Server
"""
app = FastAPI()


@app.get("/")
async def root():
    return {"contents" : "Hello world"}


@app.post("/login-user/")
async def login_user(login_user: LoginUser):
    registered_users = [
        LoginUser(user_name="ikezus", user_password="ikezus"),
        LoginUser(user_name="shinbot", user_password="shinbot"),
    ]

    for registered_user in registered_users:
        if registered_user.user_name == login_user.user_name and registered_user.user_password == login_user.user_password:
            return {
                "user_name": registered_user.user_name,
                "user_password": registered_user.user_password,
            }

    raise HTTPException(status_code=400, detail="Incorrect user_name or user_password")