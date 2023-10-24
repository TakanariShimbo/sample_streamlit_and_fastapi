import streamlit as st

from handlers.session_state_handler import SessionStateHandler


class LoginCheckHandler:
    @staticmethod
    def early_return_if_not_logined():
        if not SessionStateHandler.get_logedin():
            st.error("Please login at 🏠 Home")
            st.stop()


CONTENTS_FOR_LOGEDIN = """
### :green[Logged in successfully]

Welcome to the Streamlit sample site.  
Please explore the demos available in the sidebar. 
"""


class LoginHandler:
    @classmethod
    def __display_logedin_contents(cls) -> None:
        st.markdown(CONTENTS_FOR_LOGEDIN)

    # @staticmethod
    # def __on_click_login() -> None:
    #     SessionStateHandler.set_logedin()
    
    @staticmethod
    def __send_inputs_to_backend(user_name, user_password) -> bool:
        print(f"user_name: {user_name}, password: {user_password}")
        return True
    
    @classmethod
    def __display_not_logedin_contents(cls) -> None:
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
                    return
                
                SessionStateHandler.set_logedin()
                st.rerun()

    @classmethod
    def display_contents(cls) -> None:
        if SessionStateHandler.get_logedin():
            cls.__display_logedin_contents()

        else:
            cls.__display_not_logedin_contents()