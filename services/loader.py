import os
from pypdf import PdfReader
from docx import Document

# For pdf Files 
def extract_text_from_pdf(file_path:str)->str:
    " Extract text from a PDF file. "
    reader = PdfReader(file_path)
    text=[]
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)



# For docx Files
def extract_text_from_docx(file_path:str)->str:
    "Extract text from a DOCX file."
    doc= Document(file_path)
    text=[]
    for para in doc.paragraphs:
        if para.text:
            text.append(para.text)
    return "\n".join(text)


def load_document(file_path:str)->str:
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