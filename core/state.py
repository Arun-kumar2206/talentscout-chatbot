import streamlit as st

def initialize_state():
    if "state" not in st.session_state:
        st.session_state.state = "greeting"
    
    if "candidate" not in st.session_state:
        st.session_state.candidate = {
            "name": "",
            "email": "",
            "phone": "",
            "experience": "",
            "role": "",
            "location": "",
            "tech_stack": []
        }
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "questions" not in st.session_state:
        st.session_state.questions = []