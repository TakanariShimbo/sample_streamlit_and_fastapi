from typing import Any, Dict, List

import openai
from streamlit.delta_generator import DeltaGenerator

from params import OPENAI_APIKEY


openai.api_key = OPENAI_APIKEY


USER_LABEL = "user"
ASSISTANT_LABEL = "assistant"


class ChatGptHandler:
    @staticmethod
    def query_streamly(prompt: str, original_chat_history: List[Dict[str, str]] = [], model: str = "gpt-3.5-turbo") -> Any:
        chat_history = original_chat_history.copy()
        chat_history.append({"role": "user", "content": prompt})
        
        stream_response = openai.ChatCompletion.create(
            model=model,
            messages=chat_history,
            stream=True,
        )
        return stream_response
    
    @staticmethod
    def display_answer_streamly(stream_response: Any, answer_area: DeltaGenerator) -> str:
        answer = ""
        for chunk in stream_response:
            answer_peace = chunk["choices"][0]["delta"].get("content", "")
            answer += answer_peace
            answer_area.write(answer)
        return answer

    @classmethod
    def query_and_display_answer_streamly(cls, prompt: str, answer_area: DeltaGenerator, original_chat_history: List[Dict[str, str]] = [], model: str = "gpt-3.5-turbo") -> str:
        stream_response = cls.query_streamly(prompt=prompt, original_chat_history=original_chat_history, model=model)
        answer = cls.display_answer_streamly(stream_response=stream_response, answer_area=answer_area)
        return answer