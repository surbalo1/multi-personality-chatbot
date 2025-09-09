# 🤖 UTBot: Your AI Chat Companion

A versatile AI chatbot application built with Python and Streamlit, featuring multiple personality types and an intuitive web interface.

## ✨ Features

- **Multiple Bot Personalities**:
  - **Friendly Bot** (Joy): A super friendly and casual AI companion
  - **Teacher Bot**: An expert educator that can teach any subject you specify
  - **Grumpy Bot**: A sarcastic bot with dry humor but still helpful

- **Interactive Web Interface**: Built with Streamlit for an easy-to-use chat experience
- **Memory System**: Remembers the last 3 messages for contextual conversations
- **Customizable Teacher Bot**: Choose the subject and name for personalized learning
- **Real-time Chat**: Seamless conversation flow with thinking indicators

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- API key for Groq (using Llama-3.3-70b-versatile model)

### Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install streamlit openai
   ```

3. Update your API key in `utils.py`:
   ```python
   API_KEY = "your_groq_api_key_here"
   ```

### Running the Application

#### Web Interface (Recommended)
```bash
streamlit run app.py
```

#### Command Line Interface
```bash
python chatbot_logic.py
```

## 📁 Project Structure

```
chatbot/
├── app.py              # Streamlit web interface
├── chatbot_logic.py    # Core chatbot logic and personalities
├── utils.py           # Utility functions and LLM integration
└── README.md          # Project documentation
```

## 🔧 How It Works

### Architecture

1. **Memory System**: The `Memory` class stores the last 3 messages to maintain conversation context
2. **Base Chatbot Class**: Provides common functionality for all bot types
3. **Specialized Bots**: Each personality inherits from the base class with unique prompt engineering
4. **LLM Integration**: Uses Groq's API with the Llama-3.3-70b-versatile model

### Bot Personalities

- **FriendlyBot**: Uses casual, enthusiastic language with a friendly tone
- **TeacherBot**: Acts as an expert educator in a specified subject with a given name
- **GrumpyBot**: Responds with sarcasm and dry humor while still being helpful

## 🎯 Usage Examples

### Web Interface
1. Open the application in your browser
2. Choose a bot personality from the sidebar
3. For Teacher Bot, specify a subject and name
4. Click "Start Chat" to begin the conversation
5. Use "Reset Conversation" to start over with a different bot

### Command Line
```bash
$ python chatbot_logic.py
Choose your chatbot:
1. Friendly Bot
2. Teacher Bot  
3. Grumpy Bot
Enter 1, 2, or 3: 2
What subject should I teach? Quantum Physics
```

## 🔐 Security Notes

- Keep your API key secure and never commit it to version control
- Consider using environment variables for production deployments
- The current implementation includes the API key directly in the code for educational purposes

## 👨‍💻 Author

**Rafael Ignacio Gonzalez Chong** (rig493)  
GSI PYTHON - Python Chatbot Final Project

## 📄 License

This project is for educational purposes as part of a Python programming course.

## 🤝 Contributing

This is a student project, but suggestions and improvements are welcome for educational purposes.

---

*Built with ❤️ using Python, Streamlit, and Groq AI*