from llm.geminiAPI import call_gemini
from llm.prompts import parse_tech_stack_prompt
import ast

def parse_tech_stack(user_input):
    prompt = parse_tech_stack_prompt(user_input)
    response = call_gemini(prompt)

    try:
        tech_list = ast.literal_eval(response)
        return tech_list
    except:
        return [user_input]
