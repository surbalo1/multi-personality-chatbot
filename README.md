🤖 AI Bot: Multi-Personality AI Chat Companion

A flexible, interactive AI chatbot built with Python and Streamlit, designed for multiple personalities, real-time conversations, and an intuitive web interface. Perfect for demonstrating software architecture, prompt engineering, and full-stack integration with LLMs.

✨ Features
	•	Multiple Bot Personalities
	•	Friendly Bot (Joy): Cheerful, casual, and approachable
	•	Teacher Bot: Expert instructor customizable by subject and name
	•	Grumpy Bot: Sarcastic and witty, still helpful
	•	Interactive Web Interface: Streamlit-based chat interface with sidebar controls
	•	Memory System: Maintains last 3 messages for contextual conversations
	•	Customizable Teacher Bot: Define subject and instructor name for personalized learning
	•	Real-Time Conversation: Smooth chat flow with “thinking” indicators

💻 Skills Demonstrated

This project highlights technical skills applied to embedded systems and full-stack development:
	•	Python & Streamlit: Building interactive web interfaces
	•	Prompt Engineering: Modular design for multiple chatbot personalities
	•	LLM Integration: Groq API and Llama 3.3 70B model
	•	Software Architecture: Base class + subclasses for scalable and maintainable code
	•	Memory Handling: Contextual message storage and retrieval
	•	IoT & Embedded Knowledge (portfolio highlight): While not hardware, demonstrates systematic thinking similar to embedded development workflows

🚀 Getting Started

Prerequisites
	•	Python 3.7+
	•	Groq API key (for Llama-3.3-70b-versatile model)

Installation
	1.	Clone the repository:

git clone https://github.com/surbalo1/multi-personality-chatbot.git
cd multi-personality-chatbot


	2.	Install dependencies:

pip install streamlit openai


	3.	Add your API key in utils.py:

API_KEY = "your_groq_api_key_here"



Running the App

Web Interface (Recommended)

streamlit run app.py

Command-Line Interface

python chatbot_logic.py

📁 Project Structure

multi-personality-chatbot/
├── app.py             # Streamlit web interface
├── chatbot_logic.py   # Core chatbot logic and personalities
├── utils.py           # LLM integration and helper functions
└── README.md          # Project documentation

🔧 How It Works
	1.	Memory System: Stores last 3 messages to maintain conversation context
	2.	Base Chatbot Class: Shared functionality for all bot types
	3.	Specialized Bots: FriendlyBot, TeacherBot, GrumpyBot with custom behaviors
	4.	LLM Integration: Uses Groq API to query Llama-3.3-70b model

Bot Personalities
	•	FriendlyBot: Casual, engaging, and approachable responses
	•	TeacherBot: Subject-matter expert, customizable by name and topic
	•	GrumpyBot: Sarcastic, witty, and concise

🎯 Usage Examples

Web Interface
	1.	Open the app in a browser
	2.	Select a bot personality in the sidebar
	3.	For Teacher Bot, set subject and instructor name
	4.	Click Start Chat to begin
	5.	Use Reset Conversation to switch personalities

Command-Line

$ python chatbot_logic.py
Choose your chatbot:
1. Friendly Bot
2. Teacher Bot
3. Grumpy Bot
Enter 1, 2, or 3: 2
What subject should I teach? Embedded Systems

🔐 Security Notes
	•	Keep your API key private
	•	Use environment variables in production
	•	API key in code is for learning purposes only

👨‍💻 Author

surbalo1
Python Chatbot & Embedded Systems Enthusiast

📄 License

Educational project for learning and portfolio demonstration.

⸻

Built with ❤️ using Python, Streamlit, and Groq API