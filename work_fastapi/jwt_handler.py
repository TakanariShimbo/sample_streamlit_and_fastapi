import base64
import json
from typing import Dict, Optional, Any, Union
from datetime import datetime, timedelta, timezone

from jose import jwt


ACCESS_TOKEN_EXPIRE_MINUTES = 60
JWT_SIGNATURE_ALGORITHM = "HS256"
JWT_SIGNATURE_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" #THIS IS SAMPLE
JWT_DECODE_OPTIONS = {
    'verify_signature': True,
    'verify_aud': False,
    'verify_iat': False,
    'verify_exp': False,
    'verify_nbf': False,
    'verify_iss': False,
    'verify_sub': False,
    'verify_jti': False,
    'verify_at_hash': False,
    'require_aud': False,
    'require_iat': False,
    'require_exp': False,
    'require_nbf': False,
    'require_iss': False,
    'require_sub': False,
    'require_jti': False,
    'require_at_hash': False,
    'leeway': 0,
}


class JwtPayload:
    def __init__(
        self,
        jti: Optional[str] = None,
        iss: Optional[str] = None,
        aud: Optional[str] = None,
        iat: Optional[datetime] = datetime.utcnow(),
        exp: Optional[datetime] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        ndf: Optional[datetime] = None,
    ):
        self.__jti = jti
        self.__iss = iss
        self.__aud = aud
        self.__iat = iat
        self.__exp = exp
        self.__ndf = ndf

    @classmethod
    def from_dict(cls, jwt_payload_dict: Dict[str, Any]) -> "JwtPayload":
        return cls(
            jti=jwt_payload_dict.get("jti", None),
            iss=jwt_payload_dict.get("iss", None),
            aud=jwt_payload_dict.get("aud", None),
            iat=cls.timestamp_to_datetime(jwt_payload_dict.get("iat", None)),
            exp=cls.timestamp_to_datetime(jwt_payload_dict.get("exp", None)),
            ndf=cls.timestamp_to_datetime(jwt_payload_dict.get("ndf", None)),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "jti": self.__jti,
            "iss": self.__iss,
            "aud": self.__aud,
            "iat": self.datetime_to_timestamp(self.__iat),
            "exp": self.datetime_to_timestamp(self.__exp),
            "ndf": self.datetime_to_timestamp(self.__ndf),
        }
    
    @staticmethod
    def timestamp_to_datetime(val: Optional[int]) -> Optional[datetime]:
        if val:
            return datetime.fromtimestamp(val, tz=timezone.utc)
        return None
    
    @staticmethod
    def datetime_to_timestamp(val: Optional[datetime]) -> Optional[int]:
        if val:
            return int(val.timestamp())
        return None

class JwtHandler:
    @staticmethod
    def encode_to_jws(jwt_payload: JwtPayload) -> str:
        jwt_payload_dict = jwt_payload.to_dict()
        jwt_str = jwt.encode(jwt_payload_dict, JWT_SIGNATURE_SECRET_KEY, algorithm=JWT_SIGNATURE_ALGORITHM)
        return jwt_str

    @staticmethod
    def decode_from_jws(jws_str: str) -> JwtPayload:
        jwt_payload_dict = jwt.decode(jws_str, JWT_SIGNATURE_SECRET_KEY, algorithms=[JWT_SIGNATURE_ALGORITHM], options=JWT_DECODE_OPTIONS)
        jwt_payload = JwtPayload.from_dict(jwt_payload_dict=jwt_payload_dict)
        return jwt_payload

    @classmethod
    def encode_to_jwt(cls, jwt_payload: JwtPayload) -> str:
        header = {"alg": "none", "typ": "JWT"}
        encoded_header = cls.__base64url_encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
        encoded_payload = cls.__base64url_encode(json.dumps(jwt_payload.to_dict(), separators=(',', ':')).encode('utf-8'))
        return f"{encoded_header}.{encoded_payload}."

    @classmethod
    def decode_from_jwt(cls, jwt_str: str) -> JwtPayload:
        _, encoded_payload, _ = jwt_str.split('.')
        jwt_payload_dict = json.loads(cls.__base64url_decode(encoded_payload))
        return JwtPayload.from_dict(jwt_payload_dict)

    @staticmethod
    def __base64url_encode(data: bytes) -> str:
        return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

    @staticmethod
    def __base64url_decode(data: str) -> bytes:
        padding = '=' * (4 - (len(data) % 4))
        return base64.urlsafe_b64decode(data + padding)
    
    
if __name__ == "__main__":
    original_jwt_payload = JwtPayload(iss="IssuerName", aud="AudienceName")
    print(original_jwt_payload.to_dict())

    true_jws_str = JwtHandler.encode_to_jws(jwt_payload=original_jwt_payload)
    print(true_jws_str)

    decoded_jwt_payload = JwtHandler.decode_from_jws(jws_str=true_jws_str)
    print(decoded_jwt_payload.to_dict())



