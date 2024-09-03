import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()

IMAGE_PATH = "beach.jpg"
API_KEY = os.getenv('api_key')
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"
PROMPT = "What's in this image?"


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_response_from_api(encoded_image):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": PROMPT
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        },
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == "__main__":
    encoded_image = encode_image_to_base64(IMAGE_PATH)
    response_dict = get_response_from_api(encoded_image)
    message_content = response_dict["choices"][0]["message"]["content"]
    print("Response Message:")
    print(message_content)
