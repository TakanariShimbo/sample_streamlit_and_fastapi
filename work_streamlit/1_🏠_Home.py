from textwrap import dedent

import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from components.title_template import TitleTemplate
from handlers.login_handler import LoginHandler


# Set Titles
TitleTemplate.set_page_configs(icon="🏠", title="Home")


# Contents
login_handler = LoginHandler()


def display_login_success_content():
    def on_click_logout() -> None:
        login_handler.logout()


    contents = dedent(
        """
        ### :green[Click the button below to logout]👋

        Thank you for enjoying the Streamlit sample site.   
        See you again.   
        """
    )
    st.markdown(contents)
    st.button("Logout", key="Logout Button", on_click=on_click_logout)


def display_login_form():
    with st.form("login_form", clear_on_submit=False):
        inputs_dict = {
            "user_name": st.text_input("User Name", type="default", key="User Name Input in Login Form", disabled=SessionStateHandler.get_login_button_state()),
            "user_password": st.text_input("Password", type="password", key="Password Input in Login Form", disabled=SessionStateHandler.get_login_button_state()),
        }
    
        login_message = SessionStateHandler.get_login_message()
        if login_message:
            st.error(login_message)

        if st.form_submit_button("Login", on_click=login_handler.on_click_login_start, disabled=SessionStateHandler.get_login_button_state()):
            with st.spinner():
                is_login_success = login_handler.on_click_login_process(inputs_dict)
            login_handler.on_click_login_finish()    
            if is_login_success:
                # go to display login success content        
                pass
            else:    
                st.rerun()
    if SessionStateHandler.get_token_accepted():
        st.balloons()
        display_login_success_content()


if not login_handler.check_is_login():
    display_login_form()

else:
    display_login_success_content()
