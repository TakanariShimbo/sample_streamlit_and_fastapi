from pydantic import BaseModel


class LoginUser(BaseModel):
    user_name: str
    user_password: str

class CreateUser(BaseModel):
    user_name: str
    user_password: str