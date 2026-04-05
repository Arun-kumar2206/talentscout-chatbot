# TalentScout Hiring Assistant

## Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot designed to streamline the candidate screening process for technical roles. Built using Streamlit and Google's Gemini AI, the application guides candidates through an interactive conversation to collect essential information such as name, contact details, experience, role, location, and tech stack. Based on the provided details, it dynamically generates tailored technical interview questions to assess the candidate's skills.

Key capabilities include:

- **Automated Information Gathering**: Step-by-step collection of candidate details with validation for email and phone numbers.
- **Dynamic Question Generation**: Uses AI to create relevant technical questions adjusted for the candidate's experience level and tech stack.
- **Real-time Chat Interface**: Provides a user-friendly chat experience with session persistence.
- **Progress Tracking**: Displays candidate information in a sidebar for easy monitoring.

## Live Demo

Try the live demo at [https://talentscout-chatbot-22.streamlit.app/](https://talentscout-chatbot-22.streamlit.app/)

## Installation Instructions

Follow these steps to set up and run the application locally:

1. **Clone the Repository**:

   ```
   git clone https://github.com/Arun-kumar2206/talentscout-chatbot.git
   cd talentscout-chatbot
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8 or higher installed. Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Obtain the API key from the [Google AI Studio](https://aistudio.google.com/) if you don't have one.

4. **Run the Application**:

   ```
   streamlit run app.py
   ```

   - Open your browser and navigate to the URL provided (usually `http://localhost:8501`).

## Usage Guide

1. **Start the Chat**: Upon launching, the chatbot greets the user and begins collecting information.
2. **Provide Details**: Respond to prompts for name, email, phone, experience, role, location, and tech stack. The system validates email and phone formats.
3. **Tech Stack Input**: List your technologies (e.g., "Python, Django, React"). The AI parses this into a structured list.
4. **Answer Questions**: After providing tech stack, the chatbot generates and asks 5 technical questions based on your experience and stack.
5. **End Conversation**: Type "exit", "quit", "bye", or "done" at any time to end the session.
6. **Monitor Progress**: View collected information in the sidebar.

The chat interface supports real-time interaction, and responses are streamed for a smooth experience.

## Technical Details

### Libraries Used

- **Streamlit (1.56.0)**: For building the web-based chat interface and managing session state.
- **Google Genai (1.70.0)**: To interact with Google's Gemini AI model for content generation.
- **Python-dotenv (1.2.2)**: For loading environment variables securely.

### Model Details

- **Gemini 2.5 Flash Lite**: A lightweight version of Google's Gemini model used for generating technical questions and parsing tech stacks. It supports streaming responses for real-time output.

### Architectural Decisions

- **Modular Structure**: The codebase is organized into folders (`core`, `llm`, `utils`) for separation of concerns:
  - `core`: Handles application logic, state management, and input processing.
  - `llm`: Manages AI interactions and prompt generation.
  - `utils`: Contains utility functions for parsing and validation.
- **Session State Management**: Uses Streamlit's session state to persist candidate data and conversation history across interactions.
- **State Machine Pattern**: The controller uses a state-based approach to guide the conversation flow, ensuring a structured user experience.
- **AI-Driven Parsing**: Relies on Gemini for tech stack extraction instead of regex, allowing flexibility with varied user inputs.
- **Streaming Responses**: Implements streaming for question generation to provide immediate feedback.
- **API Call Optimization**: To minimize costs and respect rate limits, the system uses only 2 API calls per user session: one for parsing the tech stack from user input and another for generating tailored questions. User details (name, email, phone, etc.) are collected using rule-based validation without LLM involvement, ensuring efficiency while maintaining functionality.

## Prompt Design

Prompts are carefully crafted to leverage Gemini's capabilities for information gathering and question generation:

- **Question Generation Prompt**: Takes candidate experience and tech stack as inputs. It instructs the AI to adjust question difficulty (basic for 0-1 years, intermediate for 2-4, advanced for 5+), cover multiple technologies, and output in a numbered list format. This ensures relevance and progression in questioning.
- **Tech Stack Parsing Prompt**: Provides a simple instruction to extract technologies from user input and return a Python list. This handles natural language inputs effectively, converting them into structured data.

Prompts are designed to be concise, rule-based, and output-format specific to minimize errors and ensure consistent AI responses.

## Challenges & Solutions

During development, several challenges were encountered:

- **Input Validation**: Ensuring valid email and phone formats was tricky with varied inputs. Solution: Used regex patterns for validation, with clear error messages to guide users.
- **Tech Stack Parsing**: Parsing free-form text into lists was error-prone with regex. Solution: Leveraged Gemini AI for natural language parsing, falling back to raw input if parsing fails.
- **API Rate Limits and Errors**: Potential issues with Gemini API. Solution: Added try-except blocks to handle exceptions gracefully, returning error messages to the user.
- **Excessive API Usage**: Initially, API calls were made for every question generation, quickly exceeding the free tier rate limits. Solution: Optimized to use only 2 API calls per session (one for tech stack parsing and one for question generation), without interrupting the process flow.
- **Question Presentation Flow**: At first, to reduce API calls, we made a single API call to generate all 5 questions and presented them all at once to the user, which resulted in a poor user experience. Solution: We split the questions to present one by one, allowing the user to answer each question sequentially, while still using only one API call to generate all 5 questions upfront.

These solutions enhanced reliability, user-friendliness, and maintainability of the application.
