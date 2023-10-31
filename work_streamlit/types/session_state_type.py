from enum import Enum


class SessionStateType(Enum):
    LOGIN_BUTTON_STATE = "login_button_state"
    LOGIN_MESSAGE = "login_message"
    TOKEN_VERIFIED_COUNT = "token_verified_count"
    TOKEN_ACCEPTED_STATE = "token_accepted_state"
    CHAT_HISTORY = "chat_history"
    CHAT_MODEL_INDEX = "chat_model_index"