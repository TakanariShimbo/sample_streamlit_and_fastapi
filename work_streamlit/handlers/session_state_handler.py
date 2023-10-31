from typing import Optional, List, Dict

import streamlit as st

from enums.sender_type import SenderType
from enums.session_state_type import SessionStateType


class SessionStateHandler:
    """
    REGISTER_BUTTON_STATE
    """
    @staticmethod
    def get_register_button_state() -> bool:
        return st.session_state.get(SessionStateType.REGISTER_BUTTON_STATE.value, False)

    @staticmethod
    def set_register_button_state(is_active: bool) -> None:
        setattr(st.session_state, SessionStateType.REGISTER_BUTTON_STATE.value, is_active)

    """
    REGISTER_MESSAGE
    """
    @staticmethod
    def get_register_message() -> str:
        return st.session_state.get(SessionStateType.REGISTER_MESSAGE.value, None)

    @staticmethod
    def set_register_message(message: Optional[str]) -> None:
        setattr(st.session_state, SessionStateType.REGISTER_MESSAGE.value, message)

    """
    LOGIN_BUTTON_STATE
    """
    @staticmethod
    def get_login_button_state() -> bool:
        return st.session_state.get(SessionStateType.LOGIN_BUTTON_STATE.value, False)

    @staticmethod
    def set_login_button_state(is_active: bool) -> None:
        setattr(st.session_state, SessionStateType.LOGIN_BUTTON_STATE.value, is_active)

    """
    LOGIN_MESSAGE
    """
    @staticmethod
    def get_login_message() -> str:
        return st.session_state.get(SessionStateType.LOGIN_MESSAGE.value, None)

    @staticmethod
    def set_login_message(message: Optional[str]) -> None:
        setattr(st.session_state, SessionStateType.LOGIN_MESSAGE.value, message)

    """
    TOKEN_VERIFIED_COUNT
    """
    @staticmethod
    def get_token_verified_count() -> int:
        return st.session_state.get(SessionStateType.TOKEN_VERIFIED_COUNT.value, 0)

    @staticmethod
    def add_token_verified_count() -> None:
        try:
            st.session_state[SessionStateType.TOKEN_VERIFIED_COUNT.value] += 1
        except (AttributeError, KeyError):
            setattr(st.session_state, SessionStateType.TOKEN_VERIFIED_COUNT.value, 1)

    """
    TOKEN_ACCEPTED_STATE
    """
    @staticmethod
    def get_token_accepted() -> bool:
        return st.session_state.get(SessionStateType.TOKEN_ACCEPTED_STATE.value, False)

    @staticmethod
    def set_token_accepted(is_token_accepted: bool) -> None:
        setattr(st.session_state, SessionStateType.TOKEN_ACCEPTED_STATE.value, is_token_accepted)

    """
    CHAT_HISTORY
    """
    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get(SessionStateType.CHAT_HISTORY.value, [])

    @staticmethod
    def set_chat_history(sender_type: SenderType, content: str) -> None:
        chat_dict = {"role": sender_type.value, "content": content}
        try:
            st.session_state[SessionStateType.CHAT_HISTORY.value].append(chat_dict)
        except (AttributeError, KeyError):
            setattr(st.session_state, SessionStateType.CHAT_HISTORY.value, [chat_dict])

    """
    CHAT_MODEL_INDEX
    """
    @staticmethod
    def get_chat_model_index() -> int:
        return st.session_state.get(SessionStateType.CHAT_MODEL_INDEX.value, 0)

    @staticmethod
    def set_chat_model_index(model_index: int) -> None:
        setattr(st.session_state, SessionStateType.CHAT_MODEL_INDEX.value, model_index)
