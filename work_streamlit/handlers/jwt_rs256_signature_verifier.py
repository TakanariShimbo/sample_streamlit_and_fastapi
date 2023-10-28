from typing import Optional
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError, JWSError
from jose.constants import ALGORITHMS
from jose.backends.rsa_backend import RSAKey

from handlers.jwt_payload_handler import JwtPayload    
from base import JWT_RS256_SIGNATURE_PUBLIC_KEY


class JwtRs256SignatureVerifier:
    @classmethod
    def verify_jws(cls, jws_str: str) -> Optional[JwtPayload]:
        jwt_payload = cls.__parse_payload_from_jws(jws_str=jws_str)
        # signature ng
        if not jwt_payload:
            return None
        # not has exp
        if not jwt_payload.exp:
            return None
        # exp ng
        if (jwt_payload.exp - datetime.now().astimezone(timezone.utc)) < timedelta(seconds=0):
            return None
        return jwt_payload

    @classmethod
    def __parse_payload_from_jws(cls, jws_str: str) -> Optional[JwtPayload]:
        try:
            jwt_payload_dict = jwt.decode(
                token=jws_str,
                key=RSAKey(key=JWT_RS256_SIGNATURE_PUBLIC_KEY, algorithm=ALGORITHMS.RS256),
                algorithms=[ALGORITHMS.RS256],
                options=cls.__get_decode_options(),
            )
        except (JWSError, JWTError):
            return None
        
        jwt_payload = JwtPayload.init_from_dict(jwt_payload_dict=jwt_payload_dict)
        return jwt_payload
    
    @staticmethod
    def __get_decode_options():
        decode_options = {
            "verify_signature": True,
            "verify_aud": False,
            "verify_iat": False,
            "verify_exp": False,
            "verify_nbf": False,
            "verify_iss": False,
            "verify_sub": False,
            "verify_jti": False,
            "verify_at_hash": False,
            "require_aud": False,
            "require_iat": False,
            "require_exp": False,
            "require_nbf": False,
            "require_iss": False,
            "require_sub": False,
            "require_jti": False,
            "require_at_hash": False,
            "leeway": 0,
        }
        return decode_options
