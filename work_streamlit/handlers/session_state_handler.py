import streamlit as st


class SessionStateHandler:
    @staticmethod
    def get_loggedin() -> bool:
        return st.session_state.get("loggedin", False)
    
    @staticmethod
    def set_loggedin() -> None:
        setattr(st.session_state, "loggedin", True)