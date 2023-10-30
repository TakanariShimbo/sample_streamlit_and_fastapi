import json
from typing import Dict, Any, Optional

import requests
import extra_streamlit_components as stx
from pydantic import ValidationError

from handlers.session_state_handler import SessionStateHandler
from handlers.cookie_handler import CookieHandler
from handlers.response_handler import ResponseHandler
from schemas.user_schema import LoginUser
from base import BACKEND_URL


MAX_VERIFY_COUNT = 2


# st.cashe_resource or st.cashe_data is require ?
def get_manager() -> stx.CookieManager:
    return stx.CookieManager()


class LoginHandler:
    def __init__(self):
        self.__cookie_manager = get_manager()
        self.__cookie_handler = CookieHandler(self.__cookie_manager)

    def check_is_login(self, is_verify_token_required=True) -> bool:
        if SessionStateHandler.get_token_accepted():
            return True
        elif SessionStateHandler.get_token_varified_count() >= MAX_VERIFY_COUNT:
            return SessionStateHandler.get_token_accepted()
        elif not is_verify_token_required:
            return False

        # run only 2 times in session
        return self.__verify_token()

    def logout(self):
        SessionStateHandler.set_token_accepted(is_token_accepted=False)
        self.__cookie_handler.delete_token()

    def on_click_login_start(self) -> None:
        SessionStateHandler.set_login_button_state(is_active=True)
        SessionStateHandler.set_login_message(None)

    def on_click_login_process(self, inputs_dict: Dict[str, Any]) -> bool:
        # Frontend Eealy Return
        login_user = self.__inputs_check(inputs_dict=inputs_dict)
        if not login_user:
            return False

        # Backend Eealy Return
        backend_response = self.__send_inputs_to_backend(**inputs_dict)
        if not backend_response.is_success:
            SessionStateHandler.set_login_message(message=backend_response.detail)
            return False

        # Add Token
        is_success = self.__cookie_handler.add_token(token=backend_response.contents["authorized_token"])
        if not is_success:
            return False

        SessionStateHandler.set_token_accepted(is_token_accepted=True)
        return True

    @staticmethod
    def __inputs_check(inputs_dict: Dict[str, Any]) -> Optional[LoginUser]:
        try:
            login_user = LoginUser(**inputs_dict)
            return login_user
        except ValidationError as e:
            error_message = ""
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                error_message += f"{field}: {msg}"
                SessionStateHandler.set_login_message(message=error_message)
                return None

    def on_click_login_finish(self) -> None:
        SessionStateHandler.set_login_button_state(is_active=False)

    def __verify_token(self) -> bool:
        is_accepted = self.__cookie_handler.verify_token()
        SessionStateHandler.add_token_varified_count()
        if is_accepted:
            SessionStateHandler.set_token_accepted(is_token_accepted=True)
        return is_accepted

    @staticmethod
    def __send_inputs_to_backend(user_name: str, user_password: str, timeout_seconds: int = 10) -> ResponseHandler:
        login_backend_url = f"{BACKEND_URL}/login-user/"
        send_data = {
            "user_name": user_name,
            "user_password": user_password,
        }
        send_headers = {
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                url=login_backend_url,
                data=json.dumps(send_data),
                headers=send_headers,
                timeout=timeout_seconds,
            )
        except requests.Timeout:
            return ResponseHandler(is_success=False, detail="TimeoutError: request to backend server.")
        except requests.RequestException as e:
            return ResponseHandler(is_success=False, detail=f"RequestError: request to backend server. {str(e)}")

        try:
            response_dict = response.json()
        except json.JSONDecodeError:
            return ResponseHandler(is_success=False, detail="JSONDecodeError: Failed to parse json of response from backend server.")

        return ResponseHandler.init_from_response(status_code=response.status_code, response_dict=response_dict)
