import os
from dotenv import load_dotenv
import google.generativeai as genai

from services.embeddings import embedding_query
from services.vector_store import query_chunks

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-pro-preview")


def build_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful AI assistant.
Answer the question strictly using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt.strip()


def ask_rag(question: str, session_id: str) -> str:
    """
    Main RAG pipeline function.
    """
    # 1. Embed the question
    query_vector = embedding_query(question)

    # 2. Retrieve relevant chunks
    chunks = query_chunks(
        session_id=session_id,
        query_vector=query_vector,
        top_k=5
    )

    if not chunks:
        return "I don't know based on the provided documents."

    # 3. Build prompt
    prompt = build_prompt(chunks, question)

    # 4. Call Gemini
    response = model.generate_content(prompt)

    return response.text.strip()
