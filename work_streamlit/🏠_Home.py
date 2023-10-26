from textwrap import dedent

import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from handlers.title_handler import TitleHandler
from handlers.login_handler import LoginHandler


# Set Titles
TitleHandler.set_title(icon="🏠", title="Home")


# Contents
def display_login_success_content():
    def on_click_logout() -> None:
        login_handler.logout()

    contents = dedent(
        """
        ### :green[Logged in successfully]🎉

        Welcome to the Streamlit sample site.  
        Please explore the demos available in the sidebar. 
        """
    )
    st.markdown(contents)
    st.button("Logout", key="Logout Button", on_click=on_click_logout)


def display_login_form():
    login_form =  st.form("login_form", clear_on_submit=False)
    inputs_dict = {
        "user_name": login_form.text_input("User Name", type="default", key="User Name Input in Login Form"),
        "user_password": login_form.text_input("Password", type="password", key="Password Input in Login Form"),
    }
    
    login_message = SessionStateHandler.get_login_message()
    if login_message:
        login_form.error(login_message)

    if login_form.form_submit_button("Login", on_click=login_handler.on_click_login_start, disabled=SessionStateHandler.get_login_button_submitting()):
        with st.spinner():
            is_success = login_handler.on_click_login_process(inputs_dict)
        login_handler.on_click_login_finish()    
        if is_success:
            display_login_success_content()
        else:
            st.rerun()


login_handler = LoginHandler()
if not login_handler.check_is_loggedin():
    display_login_form()

else:
    display_login_success_content()
