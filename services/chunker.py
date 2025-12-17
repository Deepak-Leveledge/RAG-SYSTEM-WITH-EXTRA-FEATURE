def chunk_text(text:str, chunk_size:int=800, overlap:int=200)->list:
    """Chunk text into smaller segments with overlap."""

    if not text:
        return []
    

    chunks=[]
    start=0
    text_length=len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

        if start <0:
            start=0

    return chunks