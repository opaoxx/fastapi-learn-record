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
  settings.py
  security.py
  task_worker.py
  frontend/
    index.html
  services/
    ai_clients.py
    summary_tasks.py
  routers/
    system.py
    items.py
    predictions.py
    tasks.py
    files.py
```

`main.py` creates the FastAPI app, configures CORS, includes routers, and mounts the static frontend. Models live in `schemas.py`, SQLite setup and database sessions live in `database.py`, shared request setup lives in `dependencies.py`, route handlers live in `routers/`, and reusable business logic lives in `services/`.

The app creates a local SQLite file at `first_api/first_api.db` when it starts. That file is ignored by Git because it is local runtime data.

## Configuration

Copy `.env.example` to `.env` for local overrides:

```powershell
Copy-Item .env.example .env
```

The protected write endpoints use `FIRST_API_API_KEY`, which defaults to `dev-secret-key` for local learning. Include it as an `X-API-Key` header when calling `POST`, `PATCH`, or `DELETE` item endpoints.

The task endpoints under `/tasks` are also protected with `X-API-Key`. They demonstrate the AI-service pattern of accepting work with `202 Accepted`, processing it in the background, and letting clients query task status later.

The file endpoints under `/files` are protected with `X-API-Key`. They currently accept small UTF-8 `.txt` uploads and store metadata plus text content in SQLite for learning purposes.

## Browser frontend

The app serves a tiny static frontend at:

- http://127.0.0.1:8000/app/

It uploads a `.txt` file, creates a summary task, and shows the JSON result. CORS is configured for common local frontend origins such as `http://127.0.0.1:5500` and `http://localhost:5500`.

## Service layer

The `services/` package keeps business logic out of route handlers:

- `services/summary_tasks.py` creates, reads, lists, and runs summary task records.
- `services/ai_clients.py` contains `DemoAIClient`, a replaceable model-like client used by `/predict` and background summary tasks.

The `/predict` endpoint receives its AI client with `Depends(get_ai_client)`, so tests can replace it through `app.dependency_overrides`.
