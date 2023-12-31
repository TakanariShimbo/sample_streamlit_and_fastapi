from pydantic import BaseModel, Field


class User(BaseModel):
    user_name: str = Field(min_length=4, max_length=20)
    user_password: str = Field(min_length=4, max_length=20)
