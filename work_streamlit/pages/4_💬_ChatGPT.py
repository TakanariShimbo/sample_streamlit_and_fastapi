import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from handlers.login_handler import LoginHandler
from handlers.chatgpt_handler import ChatGptHandler, USER_LABEL, ASSISTANT_LABEL
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


# Set Titles
TitleTemplate.set_page_configs(icon="💬", title="ChatGPT")


# check login
login_handler = LoginHandler()
NotLoginTemplate.display_not_login_contents(
    check_is_login_callback=login_handler.check_is_login,
)

for chat in SessionStateHandler.get_chat_history():
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

prompt = st.chat_input(placeholder="Input prompt ...")
if prompt:
    with st.chat_message(USER_LABEL):
        st.write(prompt)

    with st.chat_message(ASSISTANT_LABEL):
        answer_area = st.empty()
        answer = ChatGptHandler.query_and_display_answer_streamly(
            prompt=prompt, 
            answer_area=answer_area, 
            original_chat_history=SessionStateHandler.get_chat_history(),
        )
        
    SessionStateHandler.set_chat_history(role=USER_LABEL, content=prompt)
    SessionStateHandler.set_chat_history(role=ASSISTANT_LABEL, content=answer)