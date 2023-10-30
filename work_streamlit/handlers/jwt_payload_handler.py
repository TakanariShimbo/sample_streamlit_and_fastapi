from uuid import uuid4
from typing import Dict, Optional, Any
from datetime import datetime, timedelta, timezone

from pydantic import BaseModel


JWT_DEFAULT_ISSUER = "localhost:8000"
JWT_DEFAULT_EXPIRE_MINUTES = 60


class JwtPayload(BaseModel):
    jti: Optional[str] = None
    iss: Optional[str] = None
    aud: Optional[str] = None
    iat: Optional[datetime] = None
    exp: Optional[datetime] = None
    ndf: Optional[datetime] = None

    @classmethod
    def init_with_defaults(
        cls,
        aud: Optional[str] = None,
    ) -> "JwtPayload":
        datetime_now = datetime.now()
        return cls(
            jti=str(uuid4()),
            iss=JWT_DEFAULT_ISSUER,
            aud=aud,
            iat=datetime_now,
            exp=datetime_now + timedelta(minutes=JWT_DEFAULT_EXPIRE_MINUTES),
            ndf=datetime_now,
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

    def to_dict(self) -> Dict[str, Any]:
        jwt_payload_dict = {
            "jti": self.jti,
            "iss": self.iss,
            "aud": self.aud,
            "iat": self.__datetime_to_timestamp(self.iat),
            "exp": self.__datetime_to_timestamp(self.exp),
            "ndf": self.__datetime_to_timestamp(self.ndf),
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
