from jose import jwt
from jose.constants import ALGORITHMS
from jose.backends.rsa_backend import RSAKey

from params import JWT_RS256_SIGNATURE_PRIVATE_KEY
from handlers.jwt_payload_handler import JwtPayload


class JwtRs256SignatureCreater:
    @classmethod
    def create_jws(cls, client_id: str) -> str:
        jwt_payload = JwtPayload.init_with_defaults(aud=client_id)
        return cls.__create_jws_from_payload(jwt_payload=jwt_payload)

    @staticmethod
    def __create_jws_from_payload(jwt_payload: JwtPayload) -> str:
        jwt_payload_dict = jwt_payload.to_dict()
        jwt_str = jwt.encode(
            claims=jwt_payload_dict,
            key=RSAKey(key=JWT_RS256_SIGNATURE_PRIVATE_KEY, algorithm=ALGORITHMS.RS256),
            algorithm=ALGORITHMS.RS256,
        )
        return jwt_str
