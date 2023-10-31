from typing import List
from enum import Enum


class ChatGptType(Enum):
    GPT_4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"

    @classmethod
    def to_value_list(cls) -> List[str]:
        return [model.value for model in cls]

    @classmethod
    def to_index(cls, value: str) -> int:
        return cls.to_value_list().index(value)

    @classmethod
    def from_value(cls, value: str) -> "ChatGptType":
        return cls(value)
