import streamlit as st


class SessionStateHandler:
    @staticmethod
    def get_logedin() -> bool:
        return st.session_state.get("logedin", False)
    
    @staticmethod
    def set_logedin() -> None:
        setattr(st.session_state, "logedin", True)