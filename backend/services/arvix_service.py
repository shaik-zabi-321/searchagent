import httpx
import xml.etree as ET
from backend.models.paper_models import Paper
BASE_URL = "https://export.arxiv.org/api/query"

def search_arvix(query: str,limit:int=5):
    
    params = {
       "search":f"all:{query}",
       "start":0,
        "max_results":limit}
   
    try:
        response = httpx.get(BASE_URL, params=params,timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.text)
        
        papers=[]
        for item in ["results"]:
            authors=[]
            for author in item["authorships"]:
                authors.append(author["author"]["display_name"])
            paper=Paper(
                title=item["display_name"],
                authors=authors,
                year=item.get("publication_year"),
                abstract="",
                pdf_url=None
            )
            papers.append(paper)
        return  papers
    except httpx.HTTPError as e:
      print(e)
      return[]

         