from services.chat_memory import get_history, add_user_and_assistant_message
import os 
from dotenv import load_dotenv
import google.generativeai as genai
from typing import List, Dict

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-pro-preview")


def ask_general_llm(question: str, session_id: str):
    """
    Streaming general-purpose LLM chat (no RAG, no tools)
    """

    try:

        history = get_history(session_id)

        history_text = ""
        for h in history:
            role = "User" if h["role"] == "user" else "AI"
            history_text += f"{role}: {h['content']}\n"

        prompt = f"""
You are a helpful AI assistant.
Answer the user's question clearly and accurately.

Previous conversation:
{history_text if history_text else "None"}

User question:
{question}

Answer:
""".strip()
        
        response = model.generate_content(prompt)

        answer = response.text.strip()
        add_user_and_assistant_message(session_id, question, answer)
        print("General LLM answer:", answer)


        return {
        "answer": answer
        
    }

        
    except Exception as e:
        raise e