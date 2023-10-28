from uuid import uuid4
from typing import Dict, Optional, Any
from datetime import datetime, timedelta, timezone


JWT_DEFAULT_ISSUER = "localhost:8000"
JWT_DEFAULT_EXPIRE_MINUTES = 60


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
