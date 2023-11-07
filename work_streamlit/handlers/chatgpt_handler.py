from typing import Any, Dict, List, Callable

from openai import OpenAI
from streamlit.delta_generator import DeltaGenerator

from enums.sender_type import SenderType
from enums.chatgpt_type import ChatGptType
from params import OPENAI_APIKEY


class ChatGptHandler:
    client = OpenAI(api_key=OPENAI_APIKEY)

    @classmethod
    def query_streamly(cls, prompt: str, original_chat_history: List[Dict[str, str]] = [], model_type: ChatGptType = ChatGptType.GPT_3_5_TURBO) -> Any:
        chat_history = original_chat_history.copy()
        chat_history.append({"role": SenderType.USER.value, "content": prompt})

        stream_response = cls.client.chat.completions.create(
            model=model_type.value,
            messages=chat_history,
            stream=True,
        )
        return stream_response

    @staticmethod
    def display_answer_streamly(stream_response: Any, display_func: Callable[[str], None]) -> str:
        answer = ""
        for chunk in stream_response:
            answer_peace = chunk.choices[0].delta.content or ""
            answer += answer_peace
            display_func(answer)
        return answer

    @classmethod
    def query_and_display_answer_streamly(
        cls, prompt: str, display_func: Callable[[str], None], original_chat_history: List[Dict[str, str]] = [], model_type: ChatGptType = ChatGptType.GPT_3_5_TURBO
    ) -> str:
        stream_response = cls.query_streamly(prompt=prompt, original_chat_history=original_chat_history, model_type=model_type)
        answer = cls.display_answer_streamly(stream_response=stream_response, display_func=display_func)
        return answer
