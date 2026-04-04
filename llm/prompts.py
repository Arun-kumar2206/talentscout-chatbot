def generate_questions_prompt(experience, tech_stack):
    return f"""
You are a senior technical interviewer.

Candidate Details:
- Experience: {experience} years
- Tech Stack: {tech_stack}

Task:
Generate 5 technical interview questions.

Rules:
- Adjust difficulty based on experience:
  0-1 yrs → basic
  2-4 yrs → intermediate
  5+ yrs → advanced
- Cover multiple technologies from the stack
- Keep questions concise
- Do NOT include answers

Output format:
1. Question
2. Question
3. Question
4. Question
5. Question
"""


def parse_tech_stack_prompt(user_input):
    return f"""
Extract all technologies from the text below.

Return ONLY a Python list.

Input:
"{user_input}"

Example Output:
["Python", "Django", "React"]
"""