from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-mpnet-base-v2')

def embedding_text(texts:list[str]) -> list[list[float]]:
    """Generate embeddings for the given text."""

    if texts is None or len(texts) == 0:
        return []
    

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True)
    

    return embeddings.tolist()


def embedding_query(query: str) -> list[float]:
    """Generate embedding for the given query."""

    if query is None or len(query) == 0:
        return []
    

    embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True)
    

    return embedding.tolist()