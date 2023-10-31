import cv2
import streamlit as st

from enums.sender_type import SenderType
from enums.chatgpt_type import ChatGptType
from handlers.session_state_handler import SessionStateHandler
from handlers.login_handler import LoginHandler
from handlers.chatgpt_handler import ChatGptHandler
from components.title_template import TitleTemplate
from components.not_login_template import NotLoginTemplate


st.cache_data
def get_avator_logo_dict():
    return {
        ChatGptType.GPT_3_5_TURBO: cv2.imread("images/gpt_3_5_logo.png"),
        ChatGptType.GPT_3_5_TURBO_16K: cv2.imread("images/gpt_3_5_logo.png"),
        ChatGptType.GPT_4: cv2.imread("images/gpt_4_logo.png"),
    }


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
    model_type = ChatGptType.from_value(value=selected_model)

    # delete chat history if model changed
    if SessionStateHandler.get_chat_model_index() != ChatGptType.to_index(value=selected_model):
        SessionStateHandler.reset_chat_history()

    # display chat history
    SessionStateHandler.set_chat_model_index(model_index=ChatGptType.to_index(value=selected_model))

    st.write("### Chat History")
    for chat in SessionStateHandler.get_chat_history():
        if chat["role"] == SenderType.USER.value:
            with st.chat_message(name=SenderType.USER.value):
                st.write(chat["content"])
        else:
            with st.chat_message(name=model_type.value, avatar=get_avator_logo_dict()[model_type]):
                st.write(chat["content"])

    prompt = st.chat_input(placeholder="Input prompt ...")
    if prompt:
        with st.chat_message(name=SenderType.USER.value):
            st.write(prompt)

        with st.chat_message(name=model_type.value, avatar=get_avator_logo_dict()[model_type]):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                answer_area=answer_area,
                original_chat_history=SessionStateHandler.get_chat_history(),
                model_type=model_type,
            )

        SessionStateHandler.set_chat_history(sender_type=SenderType.USER, content=prompt)
        SessionStateHandler.set_chat_history(sender_type=SenderType.ASSISTANT, content=answer)
