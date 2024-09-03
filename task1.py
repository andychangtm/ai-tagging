from openai import OpenAI
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

API_KEY = os.getenv('api_key')

client = OpenAI(
    api_key= API_KEY
)
prompt = "Give me a most popular hotel in Brisbane"
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user","content": prompt}
    ],
    model="gpt-4o-mini",
)
print("".join([choice.message.content for choice in chat_completion.choices]))