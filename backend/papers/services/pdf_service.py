import httpx
from pathlib import Path
PAPERS_DIR=Path("backend/papers")
PAPERS_DIR.mkdir(exist_ok=True)

def download_pdf(pdf_url:str,filename:str):
    try:
        response = httpx.get(pdf_url,timeout=30)
        response.raise_for_status()
        file_path = PAPERS_DIR / f"{filename}.pdf"
        with open(file_path, "wb") as f:
            f.write(response.content)
            return file_path
    except httpx.HTTPError as e:
        print(f"error downloading pdf: {e}")
        return None