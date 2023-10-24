from fastapi import FastAPI
from pydantic import BaseModel


"""
Base
"""
class CreateUserInfo(BaseModel):
    user_name: str
    user_password: str

class UserInfo(CreateUserInfo):
    user_id: int


"""
Server
"""
app = FastAPI()


@app.get("/")
async def root():
    return {"contents":"Hello world"}


@app.post("/create-user/")
async def create_user_info(create_user_info: CreateUserInfo):
    return {
        "user_id": 1,
        "user_name": create_user_info.user_name, 
        "user_password": create_user_info.user_password,
    }