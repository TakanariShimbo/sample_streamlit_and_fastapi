import json
from textwrap import dedent
from typing import Dict, Any

import requests
import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from base import BACKEND_URL


class LoginCheckHandler:
    @staticmethod
    def early_return_if_not_logined():
        if not SessionStateHandler.get_loggedin():
            st.error("Please login at 🏠 Home")
            st.stop()


class LoginHandler:
    @staticmethod
    def __display_loggedin_contents() -> None:
        contents = dedent(
            """
            ### :green[Logged in successfully]🎉

            Welcome to the Streamlit sample site.  
            Please explore the demos available in the sidebar. 
            """
        )
        st.markdown(contents)

    @staticmethod
    def __on_click_login_start() -> None:
        SessionStateHandler.set_login_button_submitting(is_submitting=True)
        SessionStateHandler.set_login_message(None)

    @classmethod
    def __on_click_login_process(cls, inputs_dict: Dict[str, Any]) -> None:
        # Frontend Eealy Return
        missing_labels = [label for label, value in inputs_dict.items() if not value]
        if missing_labels:
            SessionStateHandler.set_login_message(f"Please input {missing_labels[0]}")
            return

        # Backend Eealy Return
        if not cls.__send_inputs_to_backend(
            user_name=inputs_dict["User Name"],
            user_password=inputs_dict["Password"],
        ):
            SessionStateHandler.set_login_message(f"Incorrect 'User Name' or 'Password'")
            return

        SessionStateHandler.set_loggedin()

    @staticmethod
    def __on_click_login_finish() -> None:
        SessionStateHandler.set_login_button_submitting(is_submitting=False)
        st.rerun()  

    @staticmethod
    def __send_inputs_to_backend(user_name: str, user_password: str) -> bool:
        login_backend_url = f"{BACKEND_URL}/login-user/"
        send_data = {
            "user_name": user_name,
            "user_password": user_password,
        }
        send_headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(
            url=login_backend_url,
            data=json.dumps(send_data),
            headers=send_headers,
        )
        if response.status_code == 200:
            return True
        else:
            return False

    @classmethod
    def __display_not_loggedin_contents(cls) -> None:
        with st.form("login_form"):
            inputs_dict = {
                "User Name": st.text_input("User Name", type="default"),
                "Password": st.text_input("Password", type="password"),
            }
            login_message = SessionStateHandler.get_login_message()
            if login_message:
                st.error(login_message)

            if st.form_submit_button("Login", on_click=cls.__on_click_login_start ,disabled=SessionStateHandler.get_login_button_submitting()):
                with st.spinner():
                    cls.__on_click_login_process(inputs_dict)
                cls.__on_click_login_finish()           

    @classmethod
    def display_contents(cls) -> None:
        if SessionStateHandler.get_loggedin():
            cls.__display_loggedin_contents()

        else:
            cls.__display_not_loggedin_contents()
