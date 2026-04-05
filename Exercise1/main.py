import os
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(
    api_key="yourapi",
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="What is purpose of genai.",
    model="openai/gpt-oss-20b",
)
print(response.output_text)