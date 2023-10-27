from textwrap import dedent

import streamlit as st

from handlers.login_handler import LoginHandler
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


# Set Titles
TitleTemplate.set_page_configs(icon="👋", title="Logout")


# check login
login_handler = LoginHandler()
NotLoginTemplate.display_not_login_contents(
    check_is_login_callback=login_handler.check_is_login,
)


def on_click_logout() -> None:
    login_handler.logout()


contents = dedent(
    """
    ### :green[Click the button below to logout]🖱️

    Thank you for enjoying the Streamlit sample site.   
    See you again.   
    """
)
st.markdown(contents)
st.button("Logout", key="Logout Button", on_click=on_click_logout)
