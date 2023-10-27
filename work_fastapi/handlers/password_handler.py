from passlib.context import CryptContext


PASSWORD_HASH_METHOD = "bcrypt"


class PasswordHandler:
    password_context = CryptContext(schemes=[PASSWORD_HASH_METHOD], deprecated="auto")

    @classmethod
    def verify_password(cls, raw_password: str, hashed_password: str) -> bool:
        is_accepted = cls.password_context.verify(secret=raw_password, hash=hashed_password)
        return is_accepted

    @classmethod
    def hash_password(cls, raw_password: str) -> str:
        hashed_password = cls.password_context.hash(secret=raw_password)
        return hashed_password

