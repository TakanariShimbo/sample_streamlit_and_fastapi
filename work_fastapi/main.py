from fastapi import FastAPI, HTTPException, status

from handlers.jwt_rs256_signature_creater import JwtRs256SignatureCreater
from handlers.password_handler import PasswordHandler
from schemas.user_schema import LoginUser
from schemas.token_schema import Token


"""
Server
"""
FAKE_REGISTERED_USERS = [
    LoginUser(user_name="shinbot", user_password=PasswordHandler.hash_password("shinbot")),
]

app = FastAPI()


@app.get("/")
async def root():
    return {"contents": "Hello world"}


@app.post("/login-user/", response_model=Token)
async def login_user(login_user: LoginUser):
    for registered_user in FAKE_REGISTERED_USERS:
        # search same registered_user with login_user
        is_username_correct = registered_user.user_name == login_user.user_name
        is_password_corrent = PasswordHandler.verify_password(
            raw_password=login_user.user_password,
            hashed_password=registered_user.user_password,
        )
        if is_username_correct and is_password_corrent:
            return {
                "detail": "Login success!",
                "contents": {
                    "authorized_token": JwtRs256SignatureCreater.create_jws(client_id=login_user.user_name),
                },
            }

    # if not find
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect user_name or user_password",
    )
