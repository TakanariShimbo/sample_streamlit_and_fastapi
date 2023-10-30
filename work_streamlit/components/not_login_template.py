from typing import Callable

import streamlit as st


class NotLoginTemplate:
    @staticmethod
    def display_not_login_contents(
        check_is_login_callback: Callable[[bool], bool],
        is_verify_token: bool = True,
    ):
        if not check_is_login_callback(is_verify_token):
            st.error("Please 🏠Home as the first step.")
            st.stop()
