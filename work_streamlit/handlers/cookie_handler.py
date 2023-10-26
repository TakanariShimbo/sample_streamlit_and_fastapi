import extra_streamlit_components as stx


COOKIE_KEY = "test_streamlit_cookie"
COOKIE_VAL = "xxxxxxxxxxxxxxxxxxxxx"


class CookieHandler:
    def __init__(self, cookie_manager: stx.CookieManager) -> None:
        self.cookie_manager = cookie_manager
        
    def add_token(self):
        self.cookie_manager.set(cookie=COOKIE_KEY, val=COOKIE_VAL)
        print("add_token")

    def verify_token(self) -> bool:
        if self.cookie_manager.get(cookie=COOKIE_KEY):
            return True
        else:
            return False
        
    def delete_token(self):
        self.cookie_manager.delete(cookie=COOKIE_KEY)

