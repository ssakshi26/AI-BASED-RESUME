import fitz  # PyMuPDF
import docx
import os

class ResumeParser:
    def __init__(self):
        pass

    def extract_text(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            return self.extract_text_from_pdf(file_path)
        elif ext == '.docx':
            return self.extract_text_from_docx(file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    def extract_text_from_pdf(self, file_path):
        text = ""
        try:
            with fitz.open(file_path) as doc:
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            print(f"Error parsing PDF {file_path}: {e}")
            return ""

    def extract_text_from_docx(self, file_path):
        try:
            doc = docx.Document(file_path)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            return "\n".join(full_text)
        except Exception as e:
            print(f"Error parsing DOCX {file_path}: {e}")
            return ""

if __name__ == "__main__":
    # Quick test if needed
    pass
