from dotenv import load_dotenv
from openai import OpenAI
import os


class OpenaiConnection():
    def __init__(self, openai_key) -> None:
        self.client = OpenAI(api_key=openai_key)
    
    def request_prompt(self, prompt: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        message = response.choices[0].message.content
        return message


load_dotenv(f"{os.path.dirname(os.path.abspath(__file__))}/../../.env")
openai_connection = OpenaiConnection(os.getenv('API_KEY_GPT'))