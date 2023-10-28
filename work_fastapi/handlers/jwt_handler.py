# import base64
# import json
from uuid import uuid4
from typing import Dict, Optional, Any
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError, JWSError

from base import JWT_SIGNATURE_SECRET_KEY


JWT_DEFAULT_ISSUER = "localhost:8000"
JWT_DEFAULT_EXPIRE_MINUTES = 60
JWT_SIGNATURE_ALGORITHM = "HS256"


class JwtPayload:
    def __init__(
        self,
        jti: Optional[str] = None,
        iss: Optional[str] = None,
        aud: Optional[str] = None,
        iat: Optional[datetime] = None,
        exp: Optional[datetime] = None,
        ndf: Optional[datetime] = None,
    ):
        self.__jti = jti
        self.__iss = iss
        self.__aud = aud
        self.__iat = iat
        self.__exp = exp
        self.__ndf = ndf

    @classmethod
    def init_with_defaults(
        cls,
        aud: Optional[str] = None,
    ) -> "JwtPayload":
        now = datetime.now()
        return cls(
            jti=str(uuid4()),
            iss=JWT_DEFAULT_ISSUER,
            aud=aud,
            iat=now,
            exp=now + timedelta(minutes=JWT_DEFAULT_EXPIRE_MINUTES),
            ndf=now,
        )

    @classmethod
    def init_from_dict(cls, jwt_payload_dict: Dict[str, Any]) -> "JwtPayload":
        return cls(
            jti=jwt_payload_dict.get("jti", None),
            iss=jwt_payload_dict.get("iss", None),
            aud=jwt_payload_dict.get("aud", None),
            iat=cls.__timestamp_to_datetime(jwt_payload_dict.get("iat", None)),
            exp=cls.__timestamp_to_datetime(jwt_payload_dict.get("exp", None)),
            ndf=cls.__timestamp_to_datetime(jwt_payload_dict.get("ndf", None)),
        )

    @property
    def jti(self) -> Optional[str]:
        return self.__jti
    
    @property
    def iss(self) -> Optional[str]:
        return self.__iss
    
    @property
    def aud(self) -> Optional[str]:
        return self.__aud
    
    @property
    def iat(self) -> Optional[datetime]:
        return self.__iat
    
    @property
    def exp(self) -> Optional[datetime]:
        return self.__exp
    
    @property
    def ndf(self) -> Optional[datetime]:
        return self.__ndf
    
    def to_dict(self) -> Dict[str, Any]:
        jwt_payload_dict = {
            "jti": self.__jti,
            "iss": self.__iss,
            "aud": self.__aud,
            "iat": self.__datetime_to_timestamp(self.__iat),
            "exp": self.__datetime_to_timestamp(self.__exp),
            "ndf": self.__datetime_to_timestamp(self.__ndf),
        }
        jwt_payload_dict_avoid_none = {k: v for k, v in jwt_payload_dict.items() if v is not None}
        return jwt_payload_dict_avoid_none
    
    @staticmethod
    def __timestamp_to_datetime(val: Optional[int]) -> Optional[datetime]:
        if not val:
            return None

        return datetime.fromtimestamp(val, tz=timezone.utc)
        
    @staticmethod
    def __datetime_to_timestamp(val: Optional[datetime]) -> Optional[int]:
        if not val:
            return None
        
        return int(val.astimezone(timezone.utc).timestamp())
        


class JwtHandler:
    @classmethod
    def verify_jws(cls, jws_str: str) -> bool:
        # signature ng
        try:
            jws_payload = cls.decode_from_jws(jws_str=jws_str)
        except (JWSError, JWTError):
            return False
        # not has exp
        if not jws_payload.exp:
            return False
        # exp ng
        if (jws_payload.exp - datetime.now().astimezone(timezone.utc)) < timedelta(seconds=0):
            return False
        return True
    
    @classmethod
    def create_jws(cls, client_id: str) -> str:
        jwt_payload = JwtPayload.init_with_defaults(aud=client_id)
        return cls.encode_to_jws(jwt_payload=jwt_payload)

    @staticmethod
    def encode_to_jws(jwt_payload: JwtPayload) -> str:
        jwt_payload_dict = jwt_payload.to_dict()
        jwt_str = jwt.encode(
            claims=jwt_payload_dict,
            key=JWT_SIGNATURE_SECRET_KEY,
            algorithm=JWT_SIGNATURE_ALGORITHM,
        )
        return jwt_str

    @classmethod
    def decode_from_jws(cls, jws_str: str) -> JwtPayload:
        jwt_payload_dict = jwt.decode(
            token=jws_str,
            key=JWT_SIGNATURE_SECRET_KEY,
            algorithms=[JWT_SIGNATURE_ALGORITHM],
            options=cls.__get_decode_options(),
        )
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

    # @classmethod
    # def encode_to_jwt(cls, jwt_payload: JwtPayload) -> str:
    #     header = {"alg": "none", "typ": "JWT"}
    #     encoded_header = cls.__base64url_encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
    #     encoded_payload = cls.__base64url_encode(json.dumps(jwt_payload.to_dict(), separators=(',', ':')).encode('utf-8'))
    #     return f"{encoded_header}.{encoded_payload}."

    # @classmethod
    # def decode_from_jwt(cls, jwt_str: str) -> JwtPayload:
    #     _, encoded_payload, _ = jwt_str.split('.')
    #     jwt_payload_dict = json.loads(cls.__base64url_decode(encoded_payload))
    #     return JwtPayload.from_dict(jwt_payload_dict)

    # @staticmethod
    # def __base64url_encode(data: bytes) -> str:
    #     return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

    # @staticmethod
    # def __base64url_decode(data: str) -> bytes:
    #     padding = '=' * (4 - (len(data) % 4))
    #     return base64.urlsafe_b64decode(data + padding)
