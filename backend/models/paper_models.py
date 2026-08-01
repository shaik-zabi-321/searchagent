from pydantic import BaseModel

class papersearchrequest(BaseModel):
    query: str

class Paper(BaseModel):
    id: str
    title: str
    authors:list[str]
    year:int | None=None
    abstract: str
    pdf_url: str | None=None
    source: str
    source_url: str

class papersearchresponse(BaseModel):
    papers: list[Paper]

