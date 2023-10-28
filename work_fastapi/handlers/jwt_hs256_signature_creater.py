from jose import jwt

from base import JWT_SIGNATURE_SECRET_KEY
from handlers.jwt_payload_handler import JwtPayload


JWT_SIGNATURE_ALGORITHM = "HS256"


class JwtHs256SignatureCreater:
    @classmethod
    def create_jws(cls, client_id: str) -> str:
        jwt_payload = JwtPayload.init_with_defaults(aud=client_id)
        return cls.__create_jws_from_payload(jwt_payload=jwt_payload)

    @staticmethod
    def __create_jws_from_payload(jwt_payload: JwtPayload) -> str:
        jwt_payload_dict = jwt_payload.to_dict()
        jwt_str = jwt.encode(
            claims=jwt_payload_dict,
            key=JWT_SIGNATURE_SECRET_KEY,
            algorithm=JWT_SIGNATURE_ALGORITHM,
        )
        return jwt_str
