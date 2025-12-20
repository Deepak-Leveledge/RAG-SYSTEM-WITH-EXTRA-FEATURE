import os
from pypdf import PdfReader
from docx import Document
from typing import List,Dict

# For pdf Files 
def extract_text_from_pdf(file_path:str)->List[Dict]:
    " Extract text from a PDF file. "
    reader = PdfReader(file_path)
    source = os.path.basename(file_path)

    blocks: List[Dict] = []
    # text=[]
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text and page_text.strip():
            blocks.append(
                {
                    "text": page_text.strip(),
                    "source": source,
                    "page": page_number,
                }
            )

    return blocks



# For docx Files
def extract_text_from_docx(file_path:str)->str:
    "Extract text from a DOCX file."
    doc= Document(file_path)
    source = os.path.basename(file_path)

    blocks: List[Dict] = []

    for idx, para in enumerate(doc.paragraphs, start=1):
        if para.text and para.text.strip():
            blocks.append(
                {
                    "text": para.text.strip(),
                    "source": source,
                    "page": idx,  # paragraph index as page surrogate
                }
            )

    return blocks


def load_document(file_path:str)->List[Dict]:
    """load the document based on file extension and extract text."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    

    ext = os.path.splitext(file_path)[1].lower()

    if ext ==".pdf":
        return extract_text_from_pdf(file_path)
    
    elif ext ==".docx":
        return extract_text_from_docx(file_path)
    
    else:
        raise ValueError(f"Unsupported file format Only PDF and DOCX are allowed: {ext}")