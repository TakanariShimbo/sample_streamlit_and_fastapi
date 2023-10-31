from datetime import datetime
from typing import Optional

import extra_streamlit_components as stx


COOKIE_KEY = "sample_streamlit_and_fastapi"


class CookieHandler:
    def __init__(self, cookie_manager: stx.CookieManager) -> None:
        self.__cookie_manager = cookie_manager
        
    def set_token(self, token: str, expires_at: datetime) -> None:       
        self.__cookie_manager.set(cookie=COOKIE_KEY, val=token, expires_at=expires_at)

    def get_token(self) -> Optional[str]:
        return self.__cookie_manager.get(cookie=COOKIE_KEY)
        
    def delete_token(self):
        self.__cookie_manager.delete(cookie=COOKIE_KEY)

