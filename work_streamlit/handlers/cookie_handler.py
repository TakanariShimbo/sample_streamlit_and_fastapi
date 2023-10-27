import extra_streamlit_components as stx

from handlers.jwt_handler import JwtHandler

COOKIE_KEY = "test_streamlit_cookie"


class CookieHandler:
    def __init__(self, cookie_manager: stx.CookieManager) -> None:
        self.__cookie_manager = cookie_manager
        
    def add_token(self, token: str):
        self.__cookie_manager.set(cookie=COOKIE_KEY, val=token)

    def verify_token(self) -> bool:
        token = self.__cookie_manager.get(cookie=COOKIE_KEY)
        if not token:
            return False

        if JwtHandler.verify_jws(jws_str=token):
            return True
        else:
            return False
        
    def delete_token(self):
        self.__cookie_manager.delete(cookie=COOKIE_KEY)

