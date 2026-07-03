# Learning Record 0025: Lifespan HTTP Client

## Date
2026-07-03

## Context
The project had an async HTTP provider adapter, but long-lived HTTP client lifecycle was not yet managed by the FastAPI application.

## What changed
- Created a lifespan-managed `httpx.AsyncClient` in `main.py`.
- Stored provider HTTP client configuration and readiness state on `app.state`.
- Closed the client during lifespan shutdown.
- Added `ProviderHttpClientStateResponse`.
- Added `GET /provider/http-client` as a teaching endpoint.
- Added a system test confirming the client is created during lifespan startup.
- Set provider HTTP clients to `trust_env=False` to keep local proxy settings from breaking the learning app.
- Added lesson 0034 and reference 0034.

## Key insight
Long-lived resources such as HTTP clients should have explicit application lifecycles. FastAPI lifespan is the right place to create them before requests are served and close them when the app shuts down.

## Retrieval prompts
- What runs before and after `yield` in a FastAPI lifespan context manager?
- Why is a long-lived HTTP client better than creating a new client per request?
- What belongs in `app.state`, and what does not?
- Why can `trust_env=False` make tests more stable on machines with proxy environment variables?

## Next possible step
Connect the lifespan-managed HTTP client to a provider adapter through a FastAPI dependency and a real route.
