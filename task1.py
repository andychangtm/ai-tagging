from openai import OpenAI
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

API_KEY = os.getenv('api_key')

client = OpenAI(
    api_key= API_KEY
)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://ihe-delft-ihe-website-production.s3.eu-central-1.amazonaws.com/s3fs-public/styles/530x530/public/2022-11/Sea%20level%20rise%20Vietnam.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
print(response.usage)