# app.py
# Streamlit interface that connects the multi-personality chatbot logic.

import streamlit as st
from chatbot_logic import FriendlyBot, TeacherBot, GrumpyBot

# --- Page setup ---
st.set_page_config(
    page_title="AI BOTS",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Your AI Chat Companion")
st.write("Pick a bot from the sidebar and start chatting.")

# --- Sidebar config ---
with st.sidebar:
    st.header("Configuration")

    # Keep the bot instance across reruns
    if "bot" not in st.session_state:
        st.session_state.bot = None

    # Bot selector
    bot_choice = st.radio(
        "Choose personality:",
        ("Friendly", "Teacher", "Grumpy"),
        key="bot_choice_radio",
        disabled=st.session_state.bot is not None
    )

    subject = ""
    if bot_choice == "Teacher":
        # Subject and name only matter for TeacherBot
        subject = st.text_input(
            "Subject:",
            "Quantum Mechanics",
            key="subject_input",
            disabled=st.session_state.bot is not None
        )
        bot_name = st.text_input(
            "Teacher name:",
            "Albert",
            key="name_input",
            disabled=st.session_state.bot is not None
        )

    # Start chat button
    if st.button("Start Chat", key="start_button", disabled=st.session_state.bot is not None):
        if bot_choice == "Friendly":
            st.session_state.bot = FriendlyBot(name="Joy")
        elif bot_choice == "Teacher":
            if subject and bot_name:
                st.session_state.bot = TeacherBot(name=f"Professor {bot_name}", subject=subject)
            else:
                st.warning("Please fill in both fields for the Teacher Bot.")
                st.stop()
        else:
            st.session_state.bot = GrumpyBot(name="Grumpy")

        # Initialize history
        st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]
        st.rerun()

    # Reset chat
    if st.session_state.bot is not None:
        if st.button("Reset Conversation", key="reset_button"):
            st.session_state.bot = None
            st.session_state.messages = []
            st.rerun()

# --- Main chat area ---
if st.session_state.get("bot"):
    for msg in st.session_state.get("messages", []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Type something..."):
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate bot reply
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.bot.generate_response(prompt)
                st.markdown(response)

        # Save reply to history
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.info("Set up your chatbot in the sidebar and click 'Start Chat'.")