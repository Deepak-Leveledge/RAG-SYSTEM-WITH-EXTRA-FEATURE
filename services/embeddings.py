# from sentence_transformers import SentenceTransformer

# # Load a pre-trained model
# model = SentenceTransformer('all-mpnet-base-v2')

# def embedding_text(texts:list[str]) -> list[list[float]]:
#     """Generate embeddings for the given text."""

#     if texts is None or len(texts) == 0:
#         return []
    

#     embeddings = model.encode(
#         texts,
#         convert_to_numpy=True,
#         normalize_embeddings=True)
    

#     return embeddings.tolist()


# def embedding_query(query: str) -> list[float]:
#     """Generate embedding for the given query."""

#     if query is None or len(query) == 0:
#         return []
    

#     embedding = model.encode(
#         query,
#         convert_to_numpy=True,
#         normalize_embeddings=True)
    

#     return embedding.tolist()



import os
from typing import List
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini embedding model
EMBEDDING_MODEL = "models/text-embedding-004"


def embedding_text(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using Google Gemini.
    """

    if not texts:
        return []

    embeddings = []

    for text in texts:
        response = genai.embed_content(
            model=EMBEDDING_MODEL,
            content=text,
            task_type="retrieval_document"
        )
        embeddings.append(response["embedding"])

    return embeddings


def embedding_query(query: str) -> List[float]:
    """
    Generate embedding for a single query using Google Gemini.
    """

    if not query:
        return []

    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=query,
        task_type="retrieval_query"
    )

    return response["embedding"]
