from typing import Optional, List, Dict

import streamlit as st


class SessionStateHandler:
    @staticmethod
    def get_login_button_state() -> bool:
        return st.session_state.get("login_button", False)

    @staticmethod
    def set_login_button_state(is_active: bool) -> None:
        setattr(st.session_state, "login_button", is_active)

    @staticmethod
    def get_login_message() -> str:
        return st.session_state.get("login_message", None)

    @staticmethod
    def set_login_message(message: Optional[str]) -> None:
        setattr(st.session_state, "login_message", message)

    @staticmethod
    def get_token_varified_count() -> int:
        return st.session_state.get("token_varified", 0)

    @staticmethod
    def add_token_varified_count() -> None:
        try:
            st.session_state["token_varified"] += 1
        except (AttributeError, KeyError):
            setattr(st.session_state, "token_varified", 1)

    @staticmethod
    def get_token_accepted() -> bool:
        return st.session_state.get("token_accepted", False)

    @staticmethod
    def set_token_accepted(is_token_accepted: bool) -> None:
        setattr(st.session_state, "token_accepted", is_token_accepted)

    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get("chat_history", [])

    @staticmethod
    def set_chat_history(role: str, content: str) -> None:
        chat_dict = {"role": role, "content": content}
        try:
            st.session_state["chat_history"].append(chat_dict)
        except (AttributeError, KeyError):
            setattr(st.session_state, "chat_history", [chat_dict])
