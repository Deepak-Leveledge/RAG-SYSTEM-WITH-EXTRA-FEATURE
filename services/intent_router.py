import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3-pro-preview")



def detect_intent(question: str) -> str:
    """
    Detect intent: rag | general
    """

    prompt = f"""
Classify the user's intent into ONE category:

- rag: question requires uploaded documents or PDFs
- general: general knowledge or conversation

Reply with ONLY one word: rag or general.

Question:
{question}

Answer:
""".strip()

    try:
        response = model.generate_content(prompt)
        intent = response.text.strip().lower()
        print("Detected intent:", intent)

        return intent if intent in ["rag", "general"] else "general"
    except Exception:
        return "general"