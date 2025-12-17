import os
import uuid
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

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
    chunks: list[str],
    embeddings: list[list[float]],
):
    """
    Store chunk embeddings in Pinecone.
    """
    vectors = []

    for text, vector in zip(chunks, embeddings):
        vectors.append(
            {
                "id": str(uuid.uuid4()),
                "values": vector,
                "metadata": {
                    "session_id": session_id,
                    "text": text,
                },
            }
        )

    index.upsert(vectors=vectors)


def query_chunks(
    session_id: str,
    query_vector: list[float],
    top_k: int = 5,
) -> list[str]:
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

    return [m["metadata"]["text"] for m in matches]
