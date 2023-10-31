from textwrap import dedent

import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from components.title_template import TitleTemplate
from handlers.login_handler import LoginHandler


# Set Titles
TitleTemplate.set_page_configs(icon="🆕", title="Register")


# Contents
login_handler = LoginHandler()


def display_already_registered_content():
    st.info("You are already registered👍")


def display_register_success_content():
    contents = dedent(
        """
        ### :green[Success to register your account]🎉

        Thank you for registering.   
        Let's enjoy the Streamlit sample site
        """
    )
    st.markdown(contents)


def display_register_form():
    with st.form("register_form", clear_on_submit=False):
        inputs_dict = {
            "user_name": st.text_input("User Name", type="default", key="User Name Input in Register Form", disabled=SessionStateHandler.get_register_button_state()),
            "user_password": st.text_input("Password", type="password", key="Password Input in Register Form", disabled=SessionStateHandler.get_register_button_state()),
        }
    
        register_message = SessionStateHandler.get_register_message()
        if register_message:
            st.error(register_message)

        if st.form_submit_button("Register", on_click=login_handler.on_click_register_start, disabled=SessionStateHandler.get_register_button_state()):
            with st.spinner():
                is_register_success = login_handler.on_click_register_process(inputs_dict)
            login_handler.on_click_register_finish()    
            if is_register_success:
                # go to display register success content        
                pass
            else:    
                st.rerun()
    if SessionStateHandler.get_token_accepted():
        st.balloons()
        display_register_success_content()


if not login_handler.check_is_login():
    display_register_form()

else:
    display_already_registered_content()
