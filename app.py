import streamlit as st
from core.state import initialize_state
from core.controller import handle_input
import time

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
    TalentScout Hiring Assistant
    </h1>
    <p style='text-align: center;'>
    AI-powered candidate screening chatbot
    </p>
    """,
    unsafe_allow_html=True
)
st.sidebar.title("Candidate Progress")

initialize_state()

candidate = st.session_state.candidate

st.sidebar.write(f"**Name:** {candidate['name']}")
st.sidebar.write(f"**Email:** {candidate['email']}")
st.sidebar.write(f"**Phone:** {candidate['phone']}")
st.sidebar.write(f"**Experience:** {candidate['experience']}")
st.sidebar.write(f"**Role:** {candidate['role']}")
st.sidebar.write(f"**Location:** {candidate['location']}")
st.sidebar.write(f"**Tech Stack:** {candidate['tech_stack']}")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your response...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = handle_input(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    time.sleep(1)

    st.rerun()