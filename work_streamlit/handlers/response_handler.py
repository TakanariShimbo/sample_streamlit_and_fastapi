from typing import Optional, Dict, Any

from pydantic import BaseModel


class ResponseHandler(BaseModel):
    is_success: bool
    detail: Optional[str] = None
    contents: Dict[str, Any] = {}

    @classmethod
    def init_from_response(cls, status_code: int, response_dict: Dict[str, Any]) -> "ResponseHandler":
        return cls(
            is_success=(status_code == 200),
            detail=response_dict.get("detail", None),
            contents=response_dict.get("contents", {}),
        )
