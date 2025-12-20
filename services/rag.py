import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import List, Dict

from services.embeddings import embedding_query
from services.vector_store import query_chunks

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-pro-preview")


def build_prompt(context_chunks: list[Dict], question: str) -> str:
     """
    Build prompt using retrieved context text only.
    Metadata (source/page) is NOT injected into the prompt.
    """
     
     
     context_texts = [c["text"].replace("\n", " ").strip() for c in context_chunks]
     context = "\n\n".join(context_texts)

     prompt = f"""
           You are a helpful AI assistant.

Use the context below to answer the question.
You may infer the answer by combining information from multiple parts of the context.
If the answer cannot be reasonably inferred, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
     return prompt.strip()

def extract_sources(chunks: List[Dict]) -> List[str]:
    """
    Extract unique sources in readable format.
    Example: policy.pdf (Page 3)
    """
    seen = set()
    sources = []

    for c in chunks:
        key = (c["source"], c["page"])
        if key not in seen:
            seen.add(key)
            sources.append(f'{c["source"]} (Page {c["page"]})')

    return sources



def ask_rag(question: str, session_id: str) -> Dict:
    """
    Main RAG pipeline with source citation.
    Returns:
    {
      "answer": str,
      "sources": list[str]
    }
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
        return {
            "answer": "I don't know based on the provided documents.",
            "sources": []
        }

    # 3. Build prompt
    prompt = build_prompt(chunks, question)

    # 4. Call Gemini
    response = model.generate_content(prompt)

    answer = response.text.strip()

    # 5. Extract sources
    sources = extract_sources(chunks)
    print("answer:-",answer)
    print("sources:-",sources)





    return {
        "answer": answer,
        "sources": sources
    }

