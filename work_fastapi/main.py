from fastapi import FastAPI, HTTPException, status

from handlers.jwt_rs256_signature_creater import JwtRs256SignatureCreater
from handlers.password_handler import PasswordHandler
from schemas.user_schema import User
from schemas.token_schema import TokenResponse, Token


"""
Server
"""
FAKE_REGISTERED_USERS = [
    User(user_name="admin", user_password=PasswordHandler.hash_password("admin")),
]


app = FastAPI()


@app.get("/")
async def root():
    return {"contents": "Hello world"}


@app.post("/login-user/", response_model=TokenResponse)
async def login_user(logingin_user: User):
    for registered_user in FAKE_REGISTERED_USERS:
        # search same registered_user with logingin_user
        is_username_correct = registered_user.user_name == logingin_user.user_name
        is_password_corrent = PasswordHandler.verify_password(
            raw_password=logingin_user.user_password,
            hashed_password=registered_user.user_password,
        )
        if is_username_correct and is_password_corrent:
            return {
                "contents": Token(authorized_token=JwtRs256SignatureCreater.create_jws(client_id=logingin_user.user_name)),
            }

    # if not find
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect user_name or user_password",
    )


@app.post("/register-user/", response_model=TokenResponse)
async def register_user(registering_user: User):
    for registered_user in FAKE_REGISTERED_USERS:
        # search same registered_user with register_user
        if registered_user.user_name == registering_user.user_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Same user_name is already exits.",
            )
        
    added_user = User(user_name=registering_user.user_name, user_password=PasswordHandler.hash_password(raw_password=registering_user.user_password))
    FAKE_REGISTERED_USERS.append( added_user )
    return {
        "contents": Token(authorized_token=JwtRs256SignatureCreater.create_jws(client_id=registering_user.user_name)),
    }
