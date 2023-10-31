import streamlit as st

from handlers.session_state_handler import SessionStateHandler
from handlers.login_handler import LoginHandler
from handlers.chatgpt_types import ChatGptType, SenderType
from handlers.chatgpt_handler import ChatGptHandler
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


# Set Titles
TitleTemplate.set_page_configs(icon="💬", title="ChatGPT")


# check login
login_handler = LoginHandler()
NotLoginTemplate.display_not_login_contents(
    check_is_login_callback=login_handler.check_is_login,
)

# display model setting
st.write("### Model Setting")
selected_model = st.selectbox(
    label="ChatGPT Model",
    options=ChatGptType.to_value_list(),
    index=SessionStateHandler.get_chat_model_index(),
    placeholder="Select model...",
)

if not selected_model:
    st.error("Please select model...")

else:
    # display chat history
    SessionStateHandler.set_chat_model_index(model_index=ChatGptType.to_index(value=selected_model))

    st.write("### Chat History")
    for chat in SessionStateHandler.get_chat_history():
        with st.chat_message(chat["role"]):
            st.write(chat["content"])

    prompt = st.chat_input(placeholder="Input prompt ...")
    if prompt:
        with st.chat_message(SenderType.USER.value):
            st.write(prompt)

        with st.chat_message(SenderType.ASSISTANT.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                answer_area=answer_area,
                original_chat_history=SessionStateHandler.get_chat_history(),
                model_type=ChatGptType.from_value(value=selected_model),
            )

        SessionStateHandler.set_chat_history(sender_type=SenderType.USER, content=prompt)
        SessionStateHandler.set_chat_history(sender_type=SenderType.ASSISTANT, content=answer)
