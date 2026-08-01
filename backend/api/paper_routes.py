from fastapi import APIRouter
from backend.models.paper_models import papersearchrequest
from backend.services.arvix_service import search_papers

router= APIRouter(prefix="/papers", tags=["papers"])

@router.post("/search")
def search(request:papersearchrequest):
    return search_papers(request.query)
