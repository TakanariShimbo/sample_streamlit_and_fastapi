from typing import Dict, Any, Union

from pydantic import BaseModel

from schemas.response_schema import Response


class Token(BaseModel):
    authorized_token: str


class TokenResponse(Response):
    contents: Union[Token, Dict[str, Any]] = {}
