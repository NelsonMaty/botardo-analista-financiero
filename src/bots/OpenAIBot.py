from openai import OpenAI
from dotenv import load_dotenv

class OpenAIBot:
    def __init__(self):
        load_dotenv()
        self.bot = OpenAI().chat.completions

    def generate_response(self, system_message='', user_message=''):
        result = self.bot.create(
            model="gpt-3.5-turbo",
            temperature=0.1,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        return result.choices[0].message.content
