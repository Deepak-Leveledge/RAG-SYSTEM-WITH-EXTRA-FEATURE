import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3-pro-preview")



def detect_intent(question: str) -> str:
    """
    Detect intent: rag | general | tool
    """

    prompt = f"""
Classify the user's intent into ONE category:

- rag: the question requires information from uploaded documents or PDFs
- tool: the question requires web search, latest information, current events, news, or real-time data
- general: general knowledge, explanations, or conversational questions that do NOT require latest information

If the question asks for latest, current, today, news, or recent events,
you MUST choose "tool"

Examples:
Q: What is machine learning?
A: general

Q: What does page 14 say?
A: rag

Q: Latest news about OpenAI
A: tool

Q: Who is the current CEO of Google?
A: tool

Q: Explain transformers
A: general

Reply with ONLY one word: rag, tool, or general.

Question:
{question}

Answer:
""".strip()

    try:
        response = model.generate_content(prompt)
        intent = response.text.strip().lower()
        print("Detected intent:", intent)

        return intent if intent in ["rag", "general", "tool"] else "general"
    except Exception:
        return "general"