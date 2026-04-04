import streamlit as st
from core.state import initialize_state
from core.controller import handle_input

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("TalentScout Hiring Assistant")

initialize_state()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your response...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = handle_input(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()