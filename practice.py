from langchain_google_genai import chatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = input("Enter your Prompt here: ")

for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)


