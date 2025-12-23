import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import List, Dict

from services.embeddings import embedding_query
from services.vector_store import query_chunks,get_all_chunk_for_summary
from services.chat_memory import get_history, add_user_and_assistant_message

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-pro-preview")


def build_prompt(context_chunks: list[Dict], question: str,history: list[dict]) -> str:
     """
    Build prompt using:
    - previous conversation (light memory)
    - retrieved context
    - current question
    """
     

     # ---- format history ----
     history_text = ""
     for h in history:
        role = "User" if h["role"] == "user" else "AI"
        history_text += f"{role}: {h['content']}\n"
     
     
     context_texts = [c["text"].replace("\n", " ").strip() for c in context_chunks]
     context = "\n\n".join(context_texts)

     prompt = f"""
           You are a helpful AI assistant.


Previous conversation:
{history_text if history_text else "None"}

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
      # 0 Get chat history
    history = get_history(session_id)

    # 1. Embed the question
    query_vector = embedding_query(question)

    # 2. Retrieve relevant chunks
    chunks = query_chunks(
        session_id=session_id,
        query_vector=query_vector,
        top_k=5
    )

    

    if not chunks:
        answer = "I don't know based on the provided documents."
        add_user_and_assistant_message(session_id, question, answer)
        return {"answer": answer, "sources": []}

    # 3. Build prompt
    prompt = build_prompt(chunks, question, history)

    # 4. Call Gemini
    response = model.generate_content(prompt)

    answer = response.text.strip()
    add_user_and_assistant_message(session_id, question, answer)

    # 5. Extract sources
    sources = extract_sources(chunks)
    print("answer:-",answer)
    # print("sources:-",sources)
    # print("prompt:-",prompt)
    print("history:-",history)
    print("session_id:-",session_id)





    return {
        "answer": answer,
        "sources": sources
    }



def build_summary_prompt(chunks:list[Dict])-> str:
    """
    Build prompt for document summary.
    """

    texts = [
        c["text"].replace("\n", " ").strip()
        for c in chunks
        if c.get("text")
    ]


    # limit context size (VERY IMPORTANT)
    texts = texts[:20]

    content = "\n\n".join(texts)

    prompt = f"""
You are an AI assistant.

Summarize the following documents in a clear and structured way.
Focus on:
- Purpose
- Key features
- Processes
- Policies
- Important points

Content:
{content}

Summary:
"""
    return prompt.strip()



def summarize_documents(session_id: str) -> dict:
    """
    Generate a high-level summary of all uploaded documents.
    """

    # 1️⃣ Fetch all chunks
    chunks = get_all_chunk_for_summary(session_id=session_id, limit=50)

    if not chunks:
        return {
            "summary": "No documents found to summarize."
        }

    # 2️⃣ Build summary prompt
    prompt = build_summary_prompt(chunks)

    # 3️⃣ Call Gemini
    response = model.generate_content(prompt)
    summary = response.text.strip()

    return {
        "summary": summary
    }
