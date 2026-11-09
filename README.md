# Research Paper Search Agent — Backend Prototype

This repository contains an early FastAPI backend for a research-paper search application. The codebase includes paper request/response models and service modules intended to retrieve scholarly works from sources such as arXiv and OpenAlex.

## Current Repository Components

- FastAPI application entry point in `backend/main.py`.
- A paper-search route in `backend/api/paper_routes.py`.
- Pydantic models for paper-search requests and paper metadata in `backend/models/paper_models.py`.
- Provider service modules for arXiv and OpenAlex in `backend/services/`.

The paper model includes fields for title, authors, publication year, abstract, PDF URL and source information.

## Intended API

The route is structured around:

`POST /papers/search`

Example request body:

```json
{
  "query": "retrieval augmented generation"
}
```

The API is intended to return matching paper metadata. The current provider integration is still under development.

## Tech Stack

- Python
- FastAPI
- Pydantic
- HTTPX
- arXiv API
- OpenAlex API

## Project Status: Work in Progress

This repository is an incomplete prototype. The route currently imports a `search_papers` function from the arXiv service module, while the inspected service code defines a differently named function. Provider response mapping and route/service integration therefore need to be completed and tested before the endpoint can be considered runnable.

## Next Development Steps

- Complete and test the provider service interfaces.
- Normalize arXiv and OpenAlex results into the shared paper model.
- Connect provider results to the API route.
- Add input validation, error handling and automated tests.
- Add installation requirements and run instructions once the application dependencies are finalized.

No production readiness or complete search workflow is claimed at this stage.
