# utils.py
# This file handles the LLM connection and related helper functions.

from openai import OpenAI
import os

# ---------------------------------------------------------------
# API CONFIGURATION
# ---------------------------------------------------------------
# Set up the client to connect to Groq’s OpenAI-compatible endpoint.
# To use your own key, replace the value below with your API key.

API_KEY = "Your api goes here"
CLIENT = OpenAI(api_key=API_KEY, base_url="url base from Groq")

# ---------------------------------------------------------------
# QUERY FUNCTION
# ---------------------------------------------------------------
def query_llm(message: str) -> str:
    """
    Sends a message to the LLM and returns its response.

    Args:
        message (str): The input prompt to send.
    Returns:
        str: The models text response.
    """
    response = CLIENT.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content