# Import the "genai" module from the Google package.
# This module allows you to interact with Google's Generative AI models.
from google import genai


from dotenv import load_dotenv

import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# Create a client object.
# The client is used to connect your Python code with Google's AI service.
# It handles authentication and API communication behind the scenes.
client = genai.Client(api_key=api_key)


# Send a request to the AI model and store the result in "response".

response = client.models.generate_content(
# Specify which AI model you want to use.
# "gemini-3.5-flash" is a fast and lightweight Gemini model.
    model="gemini-3.5-flash",
# The input/prompt given to the AI model.
# The AI will generate an answer based on this text.
    contents="Explain how AI works in a few words"
)

# Print the generated text response from the AI model.
# response.text contains the AI's final answer as plain text.


print(response.text)
