import httpx
from backend.models.paper_models import Paper
BASE_URL = "https://api.openalex.org/works"

def search_openalex(query: str,limit:int=5):
    
    params = {
       "search": query,
        "per-page":limit}
   
    try:
        response = httpx.get(BASE_URL, params=params,timeout=10)
        response.raise_for_status()
        data= response.json()
        papers=[]
        for item in data["results"]:
            authors=[]
            for author in item["authorships"]:
                authors.append(author["author"]["display_name"])
            pdf_url=item.get("primary_location", {}).get("source_url")
            paper=Paper(
                id=item["id"],
                title=item["display_name"],
                authors=authors,
                year=item.get("publication_year"),
                abstract="",
                pdf_url=pdf_url,
                source="OpenAlex",
                source_url=item["id"]
            )
            papers.append(paper)
        return  papers
    except httpx.HTTPError as e:
      print(e)
      return[]

         