from typing import List, Dict


def chunk_text(blocks: List[Dict], chunk_size: int = 800, overlap: int = 200) -> List[Dict]:
    """
    Chunk structured text blocks while preserving source and page metadata.

    Input block format:
    {
      "text": str,
      "source": str,
      "page": int
    }

    Output chunk format:
    {
      "text": str,
      "source": str,
      "page": int
    }
    """
    if not blocks:
        return []
    

    chunked_blocks: List[Dict] = []

    for block in blocks:
        text = block["text"]
        source = block["source"]
        page = block["page"]

        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + chunk_size
            chunk_text = text[start:end]

            if chunk_text.strip():
                chunked_blocks.append(
                    {
                        "text": chunk_text.strip(),
                        "source": source,
                        "page": page,
                    }
                )

            start += chunk_size - overlap

            if start < 0:
                start = 0

    return chunked_blocks