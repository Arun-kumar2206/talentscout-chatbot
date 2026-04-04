import streamlit as st

EXIT_KEYWORDS = ["exit", "quit", "bye", "done"]

def handle_input(user_input):
    user_input = user_input.strip()

    if user_input.lower() in EXIT_KEYWORDS:
        st.session_state.state = "end"
        return "Thank you for your time and effort! Our team will reach out to you soon."

    state = st.session_state.state

    if state == "greeting":
        st.session_state.state = "ask_name"
        return "Welcome to TalentScout! Let's get started.\n\n What is your full name?"
    
    elif state == "ask_name":
        st.session_state.candidate["name"] = user_input
        st.session_state.state = "ask_email"
        return "Please enter your email address."
    
    elif state == "ask_email":
        st.session_state.candidate["email"] = user_input
        st.session_state.state = "ask_phone"
        return "Please enter your phone number."
    
    elif state == "ask_phone":
        st.session_state.candidate["phone"] = user_input
        st.session_state.state = "ask_experience"
        return "How many years of experience do you have?"
    
    elif state == "ask_experience":
        st.session_state.candidate["experience"] = user_input
        st.session_state.state = "ask_role"
        return "What role are you applying for?"
    
    elif state == "ask_role":
        st.session_state.candidate["role"] = user_input
        st.session_state.state = "ask_location"
        return "What is your current location?"
    
    elif state == "ask_location":
        st.session_state.candidate["location"] = user_input
        st.session_state.state = "ask_tech_stack"
        return "List your tech stack (languages, frameworks, tools)."
    
    elif state == "ask_tech_stack":
        st.session_state.candidate["tech_stack"] = user_input
        st.session_state.state = "generate_questions"
        return "Thanks! Generating technical questions for you..."
    
    elif state == "generate_questions":
        return "Questions will be generated in next step..."
    
    elif state == "end":
        return "Conversation already ended."

    return "Sorry, I didn't understand that. can you please repeat it again."