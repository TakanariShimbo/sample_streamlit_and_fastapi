
# """
# Image Generation
# """
# from openai import OpenAI
# from params import OPENAI_APIKEY
# client = OpenAI(api_key=OPENAI_APIKEY)

# response = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat",
#     size="1024x1024",
#     quality="standard",
#     n=1,
# )
# image_b64 = response.data[0].b64_json
# image_url = response.data[0].url
# print(image_b64, image_url)


"""
Image Generation
"""
from enums.chatgpt_type import ChatGptType
from handlers.chatgpt_handler import ChatGptHandler


ChatGptHandler.query_and_display_answer_streamly(
    prompt="hello",
    display_func=print,
    model_type=ChatGptType.GPT_4_1106_PREVIEW,
)
