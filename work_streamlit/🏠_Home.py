import streamlit as st

from handlers.title_handler import TitleHandler
from handlers.login_handler import LoginHandler


# Set Titles
TitleHandler.set_title(icon="🏠", title="Home")


# Contents
LoginHandler.display_contents()