import os
from google import genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def call_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def call_gemini_stream(prompt: str):
    try:
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        for chunk in response:
            yield chunk.text
    except Exception as e:
        yield f"Error: {str(e)}"