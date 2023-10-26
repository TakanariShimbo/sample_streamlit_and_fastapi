from typing import Optional


class BackendResponseHandler:
    def __init__(self, is_success: bool, message: Optional[str] = None) -> None:
        self.__is_success = is_success
        self.__message = message

    @property
    def is_success(self) -> bool:
        return self.__is_success
    
    @property
    def message(self) -> Optional[str]:
        return self.__message