from typing import Optional, Dict, Any


class BackendResponseHandler:
    def __init__(
        self,
        is_success: bool,
        message: Optional[str] = None,
        contents: Dict[str, Any] = {},
    ) -> None:
        self.__is_success = is_success
        self.__message = message
        self.__contents = contents

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def message(self) -> Optional[str]:
        return self.__message

    @property
    def contents(self) -> Dict[str, Any]:
        return self.__contents
