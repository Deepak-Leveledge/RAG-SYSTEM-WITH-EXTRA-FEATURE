from services.vector_store import upsert_chunks, query_chunks
from services.embeddings import embedding_text, embedding_query


def test_vector_store():
    session_id = "test-session-123"

    texts = [
        "Employees can arrive late twice a month.",
        "Salary is credited on the 1st of every month."
    ]

    vectors = embedding_text(texts)
    upsert_chunks(session_id, texts, vectors)

    query = "What is the late arrival policy?"
    query_vector = embedding_query(query)

    results = query_chunks(session_id, query_vector)

    assert len(results) > 0
    print("✅ Pinecone existing index query working")
    print("Result:", results[0])


if __name__ == "__main__":
    test_vector_store()
