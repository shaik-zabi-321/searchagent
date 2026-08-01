import fitz
from path import Path
def extract_text(pdf_path):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    pages = []
    with fitz.open(pdf_path) as doc:
        for page_number,page in enumerate(doc,start=1):
            text = page.get_text()
            pages.append(
                fitz.Page(page_number=page_number, text=text))
    
    return pages
