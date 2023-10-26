from typing import Optional

import streamlit as st


class SessionStateHandler:
    @staticmethod
    def get_loggedin() -> bool:
        return st.session_state.get("loggedin", False)
    
    @staticmethod
    def set_loggedin(is_loggedin: bool) -> None:
        setattr(st.session_state, "loggedin", is_loggedin)

    @staticmethod
    def get_login_button_submitting() -> bool:
        return st.session_state.get("login_button", False)

    @staticmethod
    def set_login_button_submitting(is_submitting: bool) -> None:
        setattr(st.session_state, "login_button", is_submitting)

    @staticmethod
    def get_login_message() -> str:
        return st.session_state.get("login_message", None)

    @staticmethod
    def set_login_message(message: Optional[str]) -> None:
        setattr(st.session_state, "login_message", message)