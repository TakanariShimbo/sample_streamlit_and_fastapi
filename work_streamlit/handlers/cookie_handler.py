import extra_streamlit_components as stx

from handlers.jwt_rs256_signature_verifier import JwtRs256SignatureVerifier


COOKIE_KEY = "test_streamlit_cookie"


class CookieHandler:
    def __init__(self, cookie_manager: stx.CookieManager) -> None:
        self.__cookie_manager = cookie_manager
        
    def add_token(self, token: str) -> bool:
        jwt_payload = JwtRs256SignatureVerifier.verify_jws(jws_str=token)
        if not jwt_payload:
            return False
        if not jwt_payload.exp:
            return False
        
        self.__cookie_manager.set(cookie=COOKIE_KEY, val=token, expires_at=jwt_payload.exp)
        return True

    def verify_token(self) -> bool:
        token = self.__cookie_manager.get(cookie=COOKIE_KEY)
        if not token:
            return False

        jwt_payload = JwtRs256SignatureVerifier.verify_jws(jws_str=token)
        if not jwt_payload:
            return False

        return True
        
    def delete_token(self):
        self.__cookie_manager.delete(cookie=COOKIE_KEY)

