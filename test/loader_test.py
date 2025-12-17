from services.loader import load_document
import os 

def test_load_pdf():
    file_path = "temp\89dd5d0f-d7b8-4b9a-bac3-6455952499e1\Gupta_Deepak_CV (2).pdf"
    text = load_document(file_path)

    assert isinstance(text, str)
    assert len(text) > 0
    print("✅ PDF loader test passed")
    # print(text)



def test_load_docx():
    file_path ="temp\89dd5d0f-d7b8-4b9a-bac3-6455952499e1\Gupta_Deepak_CV (2).docx"
    text = load_document(file_path)

    assert isinstance(text, str)
    assert len(text) > 0
    print("✅ DOCX loader test passed")
    # print(text)

    

if __name__ == "__main__":
    test_load_pdf()
    test_load_docx()