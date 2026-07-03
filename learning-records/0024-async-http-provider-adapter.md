# Learning Record 0024: Async HTTP Provider Adapter

## Date
2026-07-03

## Context
After learning the AI provider boundary and FastAPI async basics, the next step was to connect them with a timeout-aware async HTTP adapter shape that can be tested without calling a real external provider.

## What changed
- Added `httpx` as a direct project dependency.
- Added `services/provider_http.py`.
- Added `ProviderHealthResult`.
- Added `check_provider_health()` using `httpx.AsyncClient`.
- Mapped timeout, HTTP status, and request errors to stable `AIClientError` codes.
- Added `tests/test_provider_http.py` with `httpx.MockTransport`.
- Added lesson 0033 and reference 0033.

## Key insight
An external AI provider adapter should translate external HTTP responses and exceptions into stable internal results and errors. Automated tests should simulate provider behavior with a mock transport instead of calling the real network.

## Retrieval prompts
- Why should provider HTTP exceptions be mapped inside the adapter?
- What does `response.raise_for_status()` do for 4xx and 5xx responses?
- Why is `MockTransport` useful for provider tests?
- Who should close an `AsyncClient` when it is passed into a function?

## Next possible step
Teach FastAPI lifespan and long-lived `AsyncClient` management, or connect an async provider adapter to a new async prediction endpoint.
