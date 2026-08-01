from fastapi import FastAPI
from backend.api.paper_routes import router as paper_router

app = FastAPI(
    title="research ai",
    version="1.0.0",

)
app.include_router(paper_router)
@app.get("/")
def home():
    return {
        "message": "research ai backend running"
    }

    
