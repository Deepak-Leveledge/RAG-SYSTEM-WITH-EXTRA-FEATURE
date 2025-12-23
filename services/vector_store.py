import os
import uuid
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from typing import List, Dict



load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX")
INDEX_HOST = os.getenv("INDEX_HOST")

DIMENSION = 768


pc = Pinecone(api_key=PINECONE_API_KEY)

# connect to existing index
index = pc.Index(PINECONE_INDEX_NAME)

# def get_index():
#     """Create or return Pinecone index."""
#     if PINECONE_INDEX_NAME not in pc.list_indexes().names():
#         pc.create_index(
#             name=PINECONE_INDEX_NAME,
#             dimension=DIMENSION,
#             metric="cosine",
#             spec=ServerlessSpec(
#                 cloud="aws",
#                 # region=PINECONE_ENV,
#             ),
#         )

#     return pc.Index(PINECONE_INDEX_NAME)

def upsert_chunks(
    session_id: str,
    chunks: list[Dict],
    embeddings: list[list[float]],
):
    """
    Store chunk embeddings in Pinecone.
    """

    if not chunks:
        return

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings length mismatch")
    

    vectors = []

    for chunk, vector in zip(chunks, embeddings):
        vectors.append(
            {
                "id": str(uuid.uuid4()),
                "values": vector,
                "metadata": {
                    "session_id": session_id,
                    "text": chunk["text"],
                    "source": chunk["source"],
                    "page": chunk["page"],
                },
            }
        )

    index.upsert(vectors=vectors)



def query_chunks(
    session_id: str,
    query_vector: list[float],
    top_k: int = 8,
) -> list[Dict]:
    """
    Query relevant chunks from Pinecone.
    """
    result = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        filter={"session_id": session_id},
    )

    matches = result.get("matches", [])

    chunks = []

    for m in matches:
        metadata = m.get("metadata", {})
        chunks.append(
            {
                "text": metadata.get("text", ""),
                "source": metadata.get("source", ""),
                "page": metadata.get("page", None),
            }
        )

    return chunks



def get_all_chunk_for_summary(session_id: str,  limit :int =100 ) -> list[Dict]:
    """
    Fetch all chunks for a session (used for document summary).
    """

    result = index.query(
        vector=[0.0] * DIMENSION,  # dummy vector
        top_k=limit,
        include_metadata=True,
        filter={"session_id": session_id},
    )

    matches = result.get("matches", [])

    chunks= []
    for m in matches:
        meta = m.get("metadata", {})
        chunks.append(
            {
                "text": meta.get("text", ""),
                "source": meta.get("source", ""),
                "page": meta.get("page", None),
            }
        )

    return chunks