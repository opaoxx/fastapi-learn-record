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
