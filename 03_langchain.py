# langchain + google gemini
# LangChain wrapper for Google Gemini models
# This allows us to use Gemini in a standardized "LLM format"
# which works with chains, agents, memory, and tools
from langchain_google_genai import ChatGoogleGenerativeAI


# Loads environment variables from .env file
# Used to securely store API keys instead of writing them in code
from dotenv import load_dotenv
import os

load_dotenv()


# Create an LLM object (this is our AI model interface)
# Select Gemini model
# Select Gemini model

# llm is your object of ChatGoogleGenerativeAI class.

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


prompt = input("Enter your Prompt here: ")
# Send prompt to AI model
# invoke() is LangChain's standard method for calling LLMs
# response = llm.invoke("Explain AI in simple words")

# response.content contains the actual AI-generated text
# 

for chunk in llm.stream(prompt):
        print(chunk.content, end="", flush=True)