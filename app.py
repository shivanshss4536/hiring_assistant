import streamlit as st
from chatbot import HiringAssistant

st.set_page_config(page_title="Hiring Assistant", layout="centered")

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .chat-container {
        background: #f8f9fa;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
        max-height: 400px;
        overflow-y: auto;
    }
    
    .user-message {
        background: #007bff;
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 15px 15px 0 15px;
        margin: 0.5rem 0;
        display: inline-block;
        max-width: 80%;
        word-wrap: break-word;
    }
    
    .bot-message {
        background: #28a745;
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 15px 15px 15px 0;
        margin: 0.5rem 0;
        display: inline-block;
        max-width: 80%;
        word-wrap: break-word;
    }
    
    .info-message {
        background: #17a2b8;
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 15px 15px 15px 0;
        margin: 0.5rem 0;
        display: inline-block;
        max-width: 80%;
        word-wrap: break-word;
        font-style: italic;
    }
    
    .input-section {
        background: #291818;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e9ecef;
        padding: 0.75rem 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    
    .status-indicator {
        background: #6c757d;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 5px;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'assistant' not in st.session_state:
    st.session_state.assistant = HiringAssistant()
if 'active' not in st.session_state:
    st.session_state.active = True

st.markdown('<div class="main-header"><h1>🤖 TalentScout Hiring Assistant</h1><p>Your AI-powered recruitment companion with intelligent fallback questions</p></div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔧 Question Generation System")
    st.markdown("""
    The chatbot uses a **3-level fallback system**:
    
    1. **🤖 AI Generated** - Uses OpenAI to create custom questions
    2. **📚 Predefined Tech** - Uses curated questions for specific technologies
    3. **🎯 General Questions** - Uses broad technical questions as backup
    
    This ensures you always get relevant questions, even if the AI service is unavailable.
    """)
    
    if st.session_state.chat_history:
        current_source = st.session_state.assistant.get_question_source()
        st.markdown(f"**Current Question Source:** {current_source}")

if not st.session_state.chat_history:
    greeting = st.session_state.assistant.get_greeting()
    st.session_state.chat_history.append(("bot", greeting))

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == 'user':
        st.markdown(f'<div class="user-message"><strong>You:</strong> {message}</div>', unsafe_allow_html=True)
    elif sender == 'info':
        st.markdown(f'<div class="info-message"><strong>Info:</strong> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message"><strong>Bot:</strong> {message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)

def submit_message():
    if st.session_state.user_input.strip():
        st.session_state.chat_history.append(("user", st.session_state.user_input))
        bot_response, ended = st.session_state.assistant.process_message(st.session_state.user_input)
        st.session_state.chat_history.append(("bot", bot_response))
        if ended:
            st.session_state.active = False
        st.session_state.user_input = ""

user_input = st.text_input(
    "💬 Type your message here...", 
    key="user_input", 
    disabled=not st.session_state.active,
    on_change=submit_message
)

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🚀 Send", disabled=not st.session_state.active or not st.session_state.user_input.strip()):
        submit_message()
with col2:
    if st.button("🔄 Reset Chat", disabled=not st.session_state.chat_history):
        st.session_state.chat_history = []
        st.session_state.assistant = HiringAssistant()
        st.session_state.active = True
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
