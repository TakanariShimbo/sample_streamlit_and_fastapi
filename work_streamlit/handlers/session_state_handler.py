from typing import Optional

import streamlit as st


class SessionStateHandler:
    @staticmethod
    def get_login_state() -> bool:
        return st.session_state.get("login_state", False)
    
    @staticmethod
    def set_login_state(is_login: bool) -> None:
        setattr(st.session_state, "login_state", is_login)

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