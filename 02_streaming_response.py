from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content_stream(
    model = "gemini-3.5-flash",
    contents = "what langchain do?"
)

for chunk in response:
    print(chunk.text, end="", flush= True) 