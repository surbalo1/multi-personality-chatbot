# utils.py
# GSI PYTHON : Python Chatbot Final Project
# Rafael Ignacio Gonzalez Chong (rig493)
# This file contains utility functions, such as querying the LLM.

from openai import OpenAI
import os

# IMPORTANT: ONLY UPDATE YOUR API KEY BELOW

#API_KEY = "gong_api_key" uncomment this line and replace with your API key
#CLIENT = OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1") uncomment this line to use the Groq API
def query_llm(message: str) -> str:
    """
    Provided function to query the LLM.
    Args:
        message: The prompt to send to the LLM
    Returns:
        The LLM's response as a string
    """
    response = CLIENT.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
    )
    return response.choices[0].message.content
    