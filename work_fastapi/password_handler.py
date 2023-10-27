from passlib.context import CryptContext


PASSWORD_HASH_METHOD = "bcrypt"


class PasswordHandler:
    password_context = CryptContext(schemes=[PASSWORD_HASH_METHOD], deprecated="auto")

    @classmethod
    def verify_password(cls, raw_password: str, hashed_password: str) -> bool:
        is_accepted = cls.password_context.verify(raw_password, hashed_password)
        return is_accepted

    @classmethod
    def get_password_hash(cls, raw_password) -> str:
        hashed_password = cls.password_context.hash(raw_password)
        return hashed_password


if __name__ == "__main__":
    raw_password = "shinbot"
    hashed_password = PasswordHandler.get_password_hash(raw_password=raw_password)
    print(f"{raw_password}: {hashed_password}")
