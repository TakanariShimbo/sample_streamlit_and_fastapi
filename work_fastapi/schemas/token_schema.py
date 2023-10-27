from pydantic import BaseModel


class Token(BaseModel):
    authorized_token: str
