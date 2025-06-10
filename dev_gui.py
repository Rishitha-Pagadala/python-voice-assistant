import streamlit as st
from dev_logic import listen, speak, generate_response, get_time, play_music, play_youtube_video, \
    google_search, get_weather, tell_joke, calculate, close_browser, open_website

# App config
st.set_page_config(page_title="Voice Chatbot", page_icon="", layout="centered")

st.title("Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Voice toggle
speak_toggle = st.sidebar.checkbox("🔊 Enable Voice Response", value=True)

# Display chat history using chat bubbles
for chat in st.session_state.chat_history:
    with st.chat_message("user" if chat["sender"] == "user" else "assistant"):
        st.markdown(chat["text"])

# Input section using Streamlit's new chat input box
user_query = st.chat_input("Say something or type your request...")

# Option to speak instead of typing
if st.button("🎤 Speak Instead"):
    user_query = listen()
    st.success(f"You said: {user_query}")

# Process user query
if user_query:
    st.session_state.chat_history.append({"sender": "user", "text": user_query})

    user_query = user_query.lower()
    # Determine response
    if any(kw in user_query.lower() for kw in ["exit", "bye", "quit"]):
        response = "Goodbye!"
    elif "open" in user_query:
        response = open_website(user_query)
    elif "close browser" in user_query:
        response = close_browser()
    elif "time" in user_query:
        response = get_time()
    elif "play music" in user_query:
        response = play_music()
    elif "play" in user_query and "youtube" in user_query:
        response = play_youtube_video(user_query)
    elif "search" in user_query:
        response = google_search(user_query)
    elif "weather" in user_query:
        response = get_weather()
    elif "joke" in user_query:
        response = tell_joke()
    elif "calculate" in user_query:
        response = calculate(user_query)
    else:
        response = generate_response(user_query)

    st.session_state.chat_history.append({"sender": "dev", "text": response})

    # Show response in chat
    with st.chat_message("assistant"):
        if "Opening" in response and "http" in response:
            st.markdown(response, unsafe_allow_html=True)
        else:
            st.markdown(response)

    # Speak it out
    speak(response, speak_out_loud=speak_toggle)

# Chat reset button
st.sidebar.markdown("---")
if st.sidebar.button("🔁 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()
