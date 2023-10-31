from enum import Enum


class SessionStateType(Enum):
    REGISTER_BUTTON_STATE = "register_button_state"
    REGISTER_MESSAGE = "register_message"

    LOGIN_BUTTON_STATE = "login_button_state"
    LOGIN_MESSAGE = "login_message"
    
    TOKEN_VALUE = "token_value"
    TOKEN_VERIFIED_COUNT = "token_verified_count"
    TOKEN_ACCEPTED_STATE = "token_accepted_state"
    
    CHAT_HISTORY = "chat_history"
    CHAT_MODEL_INDEX = "chat_model_index"