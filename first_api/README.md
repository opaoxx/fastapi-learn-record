# First FastAPI API

This is the starter project for lesson 0001.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
fastapi dev first_api/main.py
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## Why this exists

The ordinary backend endpoints build the foundation. The `/predict` endpoint hints at the later AI-service shape: request in, model-like function runs, typed response out.

## Structure

```text
first_api/
  main.py
  schemas.py
  database.py
  dependencies.py
  routers/
    system.py
    items.py
    predictions.py
```

`main.py` creates the FastAPI app and includes routers. Models live in `schemas.py`, SQLite setup and database sessions live in `database.py`, shared request setup lives in `dependencies.py`, and route handlers live in `routers/`.

The app creates a local SQLite file at `first_api/first_api.db` when it starts. That file is ignored by Git because it is local runtime data.

## Configuration

Copy `.env.example` to `.env` for local overrides:

```powershell
Copy-Item .env.example .env
```

The protected write endpoints use `FIRST_API_API_KEY`, which defaults to `dev-secret-key` for local learning. Include it as an `X-API-Key` header when calling `POST`, `PATCH`, or `DELETE` item endpoints.
