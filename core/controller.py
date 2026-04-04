import streamlit as st
from utils.parser import parse_tech_stack
from llm.geminiAPI import call_gemini
from llm.prompts import generate_questions_prompt
from utils.parser import is_valid_email, is_valid_phone

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
        if not is_valid_email(user_input):
            return "Invalid email format. Please enter a valid email."
        st.session_state.candidate["email"] = user_input
        st.session_state.state = "ask_phone"
        return "Please enter your phone number."
    
    elif state == "ask_phone":
        if not is_valid_phone(user_input):
            return "Invalid phone number. Enter 10 digits (with optional +)."

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
        tech_list = parse_tech_stack(user_input)
        st.session_state.candidate["tech_stack"] = tech_list
        st.session_state.state = "generate_questions"
        return f"Got it! Tech stack identified: {', '.join(tech_list)}.\n\nGenerating questions..."
    
    elif state == "generate_questions":
        candidate = st.session_state.candidate

        prompt = generate_questions_prompt(
            candidate["experience"],
            candidate["tech_stack"]
        )

        questions = call_gemini(prompt)

        st.session_state.questions = questions
        st.session_state.state = "end"

        summary = f"""
Candidate Summary
- Name: {candidate['name']}
- Role: {candidate['role']}
- Experience: {candidate['experience']} years
- Tech Stack: {', '.join(candidate['tech_stack'])}

---

Technical Questions
{questions}

---

Thank you for applying to TalentScout!
Our team will review your responses and contact you soon.
"""
        return summary
    
    elif state == "end":
        return "Conversation already ended."

    return "I didn't quite understant that. Please respond according to the question or type 'exit' to quit."