import fitz

def extract_text_from_pdf(uploaded_file):
    """Extract text content from an uploaded PDF file using PyMuPDF."""
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"
