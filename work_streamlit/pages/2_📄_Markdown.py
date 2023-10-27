from textwrap import dedent

import streamlit as st

from handlers.login_handler import LoginHandler
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


# Set Titles
TitleTemplate.set_page_configs(icon="📄", title="Markdown")


# check login
login_handler = LoginHandler()
NotLoginTemplate.display_not_login_contents(
    check_is_login_callback=login_handler.check_is_login,
)


# Contents
markdown_contents = dedent(
    """
    ### List
    - content1
    - content2
    - content3

    ### Code
    - python
    ```python
    print("hello world")
    ```

    - html
    ```html
    <h1>Title</h1>
    <p>this is sample.</p>
    ```

    ### LaTex
    The below equation represents the motion equation.

    $$
    F = ma
    $$

    here, $F$ is force, $m$ is mass, $a$ is accelaration.
    """
)
st.markdown(markdown_contents)
