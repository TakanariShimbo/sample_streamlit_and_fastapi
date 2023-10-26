import json
from typing import Dict, Any

import requests
import extra_streamlit_components as stx

from handlers.session_state_handler import SessionStateHandler
from handlers.cookie_handler import CookieHandler
from base import BACKEND_URL


class LoginHandler:
    def __init__(self):
        self.cookie_manager = stx.CookieManager()
        self.cookie_handler = CookieHandler(self.cookie_manager)

    def check_is_loggedin(self) -> bool:
        if SessionStateHandler.get_loggedin():
            return True
        elif self.cookie_handler.verify_token():
            return True
        else:
            return False

    def logout(self):
        SessionStateHandler.set_loggedin(is_loggedin=False)
        self.cookie_handler.delete_token()
    
    def on_click_login_start(self) -> None:
        SessionStateHandler.set_login_button_submitting(is_submitting=True)
        SessionStateHandler.set_login_message(None)
        

    def on_click_login_process(self, inputs_dict: Dict[str, Any]) -> bool:
        # Frontend Eealy Return
        missing_labels = [label for label, value in inputs_dict.items() if not value]
        if missing_labels:
            SessionStateHandler.set_login_message(message=f"Please input {missing_labels[0]}")
            return False

        # Backend Eealy Return
        if not self.__send_inputs_to_backend(**inputs_dict):
            SessionStateHandler.set_login_message(message=f"Incorrect 'User Name' or 'Password'")
            return False

        self.cookie_handler.add_token()
        SessionStateHandler.set_loggedin(is_loggedin=True)
        return True
    
    def on_click_login_finish(self) -> None:
        SessionStateHandler.set_login_button_submitting(is_submitting=False)

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