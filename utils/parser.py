from llm.geminiAPI import call_gemini
from llm.prompts import parse_tech_stack_prompt
import ast
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone)

def parse_tech_stack(user_input):
    prompt = parse_tech_stack_prompt(user_input)
    response = call_gemini(prompt)

    try:
        tech_list = ast.literal_eval(response)
        return tech_list
    except:
        return [user_input]
