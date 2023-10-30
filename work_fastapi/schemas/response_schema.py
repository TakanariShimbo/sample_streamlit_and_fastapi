from typing import Optional

from pydantic import BaseModel


class Response(BaseModel):
    detail: Optional[str] = None

