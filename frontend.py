
# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="SafeSpace – AI Mental Health Therapist", layout="wide", page_icon="🧠")

# Custom CSS for healthcare look
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #e0f7fa 0%, #f8bbd0 100%);
    }
    .stApp {
        background: linear-gradient(120deg, #e0f7fa 0%, #f8bbd0 100%);
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1976d2;
        text-align: center;
        margin-bottom: 0.5rem;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #388e3c;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    .stChatMessage, .stTextInput, .stButton, .stMarkdown, .stTextArea {
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    .stChatMessage.user {
        background: #fffde7;
        border-radius: 12px;
        margin-bottom: 0.5rem;
        border: 1px solid #ffe082;
    }
    .stChatMessage.assistant {
        background: #e3f2fd;
        border-radius: 12px;
        margin-bottom: 0.5rem;
        border: 1px solid #90caf9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Branding and subtitle for Abhishek AI Mental Health Assistant
st.markdown('<div class="main-header">🧠 Abhishek AI Mental Health Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your confidential AI mental health companion. Feel free to share your thoughts and feelings in a safe, supportive space.</div>', unsafe_allow_html=True)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input area
with st.container():
    user_input = st.chat_input("How are you feeling today? Type your thoughts...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        try:
            response = requests.post(BACKEND_URL, json={"message": user_input})
            data = response.json()
            assistant_msg = f'{data["response"]} <span style="font-size:0.8em;color:#90caf9;">[TOOL: {data["tool_called"]}]</span>'
        except Exception as e:
            assistant_msg = f"<span style='color:red;'>Error: {e}</span>"
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_msg})

# Chat history display
st.markdown("<hr style='margin:1.5rem 0;'>", unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align:center; margin-top:2rem; color:#888;'>
  <span style='font-size:1.1em;'>💙 Powered by AI | For informational purposes only. Not a substitute for professional help.</span>
</div>
""", unsafe_allow_html=True)