import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("api_key")
MODEL = "gpt-4o-mini"
ARTICLE_FILEPATH = "csv/article_content.csv"
TAG_OPTIONS_FILEPATH = "csv/tag_options.csv"


client = OpenAI(api_key=API_KEY)


def generate_tags(article, available_tags):
    prompt = f"Determine the relevant tags for the following article:\n\n {article}\n\n Using the following tags only:\n\n {available_tags}."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}], model=MODEL
    )
    result = chat_completion.choices[0].message.content
    return result


def process_article(article_filepath, tag_options_filepath):
    with open(article_filepath, mode="r", encoding="utf-8") as file:
        article_content = file.read()
    with open(tag_options_filepath, mode="r", encoding="utf-8") as file:
        available_tags = file.read()
    article_tags = generate_tags(article_content, available_tags)
    print("Generated tags for article:\n\n", article_tags)


if __name__ == "__main__":
    process_article(ARTICLE_FILEPATH, TAG_OPTIONS_FILEPATH)
