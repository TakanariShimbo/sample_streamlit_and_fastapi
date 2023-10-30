from typing import Optional, Dict, Any


class BackendResponseHandler:
    def __init__(
        self,
        is_success: bool,
        detail: Optional[str] = None,
        contents: Dict[str, Any] = {},
    ) -> None:
        self.__is_success = is_success
        self.__detail = detail
        self.__contents = contents

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def detail(self) -> Optional[str]:
        return self.__detail

    @property
    def contents(self) -> Dict[str, Any]:
        return self.__contents

    @classmethod
    def init_from_response(cls, status_code: int, response_dict: Dict[str, Any]) -> "BackendResponseHandler":
        return cls(
            is_success=(status_code == 200),
            detail=response_dict.get("detail", None),
            contents=response_dict.get("contents", {}),
        )
