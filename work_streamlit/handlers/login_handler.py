import json

import requests
import streamlit as st

from handlers.session_state_handler import SessionStateHandler


class LoginCheckHandler:
    @staticmethod
    def early_return_if_not_logined():
        if not SessionStateHandler.get_loggedin():
            st.error("Please login at 🏠 Home")
            st.stop()


LOGGEDIN_CONTENTS = """
### :green[Logged in successfully]🎉

Welcome to the Streamlit sample site.  
Please explore the demos available in the sidebar. 
"""


BACKEND_URL = "http://localhost:8000"


class LoginHandler:
    @classmethod
    def __display_loggedin_contents(cls) -> None:
        st.markdown(LOGGEDIN_CONTENTS)

    # @staticmethod
    # def __on_click_login() -> None:
    #     SessionStateHandler.set_loggedin()
    
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
            headers=send_headers
        )
        if response.status_code == 200:
            return True
        else:
            return False
    
    @classmethod
    def __display_not_loggedin_contents(cls) -> None:
        # st.button("Login", on_click=cls.__on_click_login, args=())

        with st.form("login_form"):
            user_name_label = "User Name"
            password_label = "Password"
            inputs_dict = {
                user_name_label: st.text_input(user_name_label, type="default"),
                password_label: st.text_input(password_label, type="password")
            }
            
            if st.form_submit_button("Login"):
                missing_labels = [label for label, value in inputs_dict.items() if not value]
                
                if missing_labels:
                    st.error(f"Please input {missing_labels[0]}")
                    return

                if not cls.__send_inputs_to_backend(
                    user_name=inputs_dict["User Name"], 
                    user_password=inputs_dict["Password"],
                ):
                    st.error(f"Incorrect {user_name_label} or {password_label}")
                    return
                
                SessionStateHandler.set_loggedin()
                st.rerun()

    @classmethod
    def display_contents(cls) -> None:
        if SessionStateHandler.get_loggedin():
            cls.__display_loggedin_contents()

        else:
            cls.__display_not_loggedin_contents()