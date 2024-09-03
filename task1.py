import base64
import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()


IMAGE_FOLDER = "imports"
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


def process_images(image_folder):
    results = []
    print("Processing images...")
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            encoded_image = encode_image_to_base64(image_path)
            response_dict = get_response_from_api(encoded_image)
            message_content = response_dict["choices"][0]["message"]["content"]
            results.append((filename, message_content))
    return results


def save_to_csv(results, output_file):
    print("Saving generated alt text to csv")
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Alt Text"])
        writer.writerows(results)


if __name__ == "__main__":
    results = process_images(IMAGE_FOLDER)
    save_to_csv(results, "output.csv")
    print("Image alt texts saved to output.csv")
