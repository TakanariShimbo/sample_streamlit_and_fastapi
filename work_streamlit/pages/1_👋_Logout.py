from textwrap import dedent

import streamlit as st

from handlers.title_handler import TitleHandler
from handlers.login_handler import LoginHandler


# Set Titles
TitleHandler.set_title(icon="👋", title="Logout")


# check login
login_handler = LoginHandler()
if not login_handler.check_is_login(is_verify_token=False):
    st.error("Please login at 🏠 Home")
    st.stop()


def on_click_logout() -> None:
    login_handler.logout()


contents = dedent(
    """
    ### :green[Able to logout below button]🐌

    Thank you for enjoying the Streamlit sample site.   
    See you again.   
    """
)
st.markdown(contents)
st.button("Logout", key="Logout Button", on_click=on_click_logout)
