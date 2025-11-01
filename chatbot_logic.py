# chatbot_logic.py
# This file handles chatbot logic, memory management, and bot personalities.

from typing import List, Dict
from utils import query_llm

# -------------------------------------------------------------------

class Memory:
    # Stores the last 3 messages between user and bot

    def __init__(self):
        self.messages = []  # list to keep conversation history

    def add_message(self, role: str, content: str) -> None:
        # adds a new message and keeps only the last 3
        self.messages.append({'role': role, 'content': content})
        self.messages = self.messages[-3:]

    def get_recent_messages(self) -> str:
        # builds a short history string from recent messages
        output = ""
        for m in self.messages:
            output += f"{m['role'].capitalize()}: {m['content']}\n"
        return output.strip()

# -------------------------------------------------------------------

class Chatbot:
    # base chatbot class used by all bot types

    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()

    def _create_prompt(self, user_input: str) -> str:
        # combines memory and user input into a prompt for the model
        history = self.memory.get_recent_messages()
        prompt = f"{history}\nUser: {user_input}\n{self.name}:"
        return prompt

    def generate_response(self, user_input: str) -> str:
        # saves user input, builds prompt, and queries the LLM
        self.memory.add_message("user", user_input)
        prompt = self._create_prompt(user_input)
        response = query_llm(prompt)
        self.memory.add_message("bot", response)
        return response

# -------------------------------------------------------------------

class FriendlyBot(Chatbot):
    # cheerful and casual personality

    def _create_prompt(self, user_input: str) -> str:
        history = self.memory.get_recent_messages()
        prompt = (
            "You are Chavoso AI, a super friendly and casual chatbot!"
            f"{history}\nUser: {user_input}\nJoy:"
        )
        return prompt

# -------------------------------------------------------------------

class TeacherBot(Chatbot):
    # teacher personality, specialized in a given subject

    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

    def _create_prompt(self, user_input: str) -> str:
        history = self.memory.get_recent_messages()
        prompt = (
            f"You are {self.name}, an expert teacher in {self.subject}. "
            f"{history}\nStudent: {user_input}\n{self.name}:"
        )
        return prompt

# -------------------------------------------------------------------

class GrumpyBot(Chatbot):
    # sarcastic bot, always a bit annoyed but still helpful

    def _create_prompt(self, user_input: str) -> str:
        history = self.memory.get_recent_messages()
        prompt = (
            "You are Grumpy, a chatbot who is always a bit annoyed and sarcastic. "
            f"{history}\nUser: {user_input}\nGrumpy:"
        )
        return prompt

# -------------------------------------------------------------------

def main():
    # allows testing the bot directly from the terminal
    print("Choose your chatbot:")
    print("1. Friendly Bot")
    print("2. Teacher Bot")
    print("3. Grumpy Bot")

    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        bot = FriendlyBot("Joy")
    elif choice == "2":
        subject = input("What subject should I teach? ")
        bot = TeacherBot("Mr. Incredible", subject)
    else:
        bot = GrumpyBot("Grumpy")

    print(f"\n{bot.name}: Hello! How can I help you today?")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break

        response = bot.generate_response(user_input)
        print(f"{bot.name}: {response}")

# -------------------------------------------------------------------

if __name__ == "__main__":
    main()