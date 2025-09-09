# chatbot_logic.py
# GSI PYTHON : Python Chatbot Final Project
# Rafael Ignacio Gonzalez Chong (rig493)
# This file contains the chatbot logic, including different bot personalities and their behaviors.

from typing import List, Dict
from utils import query_llm

################################################################

class Memory:
    """store last 3 messages"""

    def __init__(self):
        # Store last 3 messages
        self.messages = []

    def add_message(self, role: str, content: str) -> None:
        # Add a new message as a dictionary
        self.messages.append({'role': role, 'content': content})
        # Keep only last 3 messages
        self.messages = self.messages[-3:]

    def get_recent_messages(self) -> str:
        # Build a string from the last 3 messages
        output = ""
        for m in self.messages:
            output += f"{m['role'].capitalize()}: {m['content']}\n"
        return output.strip()
   
################################################################

class Chatbot:
    """base chatbot"""

    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()

    def _create_prompt(self, user_input: str) -> str:
        # combine memory and user input into a prompt
        history = self.memory.get_recent_messages()
        prompt = f"{history}\nUser: {user_input}\n{self.name}:"
        return prompt

    def generate_response(self, user_input: str) -> str:
        # store input
        self.memory.add_message("user", user_input)
        # create prompt
        prompt = self._create_prompt(user_input)
        # query the LLM
        response = query_llm(prompt)
        # store response
        self.memory.add_message("bot", response)
        return response

################################################################

class FriendlyBot(Chatbot):
    """friendly bot"""

    def _create_prompt(self, user_input: str) -> str:

        history = self.memory.get_recent_messages()
        prompt = (
            "You are Chavoso AI, a super friendly and casual AI chatbot!"
            f"{history}\nUser: {user_input}\nJoy:"
        )
        return prompt
    
################################################################

class TeacherBot(Chatbot):
    """teacher bot"""

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
    
################################################################

class GrumpyBot(Chatbot):
    """the grumpy bot"""

    def _create_prompt(self, user_input: str) -> str:
        # Personality: blunt, a little rude, with dry humor—but still gives answers!
        history = self.memory.get_recent_messages()
        prompt = (
            "You are Grumpy, a chatbot who is always a bit annoyed and sarcastic. "
            f"{history}\nUser: {user_input}\nGrumpy:"
        )
        return prompt

################################################################

def main():
    """Main interaction loop"""
    # Let user choose personality
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
    
    print(f"\n{bot.name}: Hello! How can I help you today? ")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break
        
        response = bot.generate_response(user_input)
        print(f"{bot.name}: {response}")

if __name__ == "__main__":
    main()