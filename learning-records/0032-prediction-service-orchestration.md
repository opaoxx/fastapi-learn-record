# Learning Record 0032: Prediction Service Orchestration

## Context

Prediction routes had grown beyond simple HTTP translation. They selected the backend, called demo or provider implementations, measured elapsed time, wrapped failures, set headers, wrote logs, and returned response models.

## Decision

Move prediction orchestration into `first_api/services/predictions.py`.

The new service layer exposes:

- `PredictionServiceResult`
- `PredictionServiceError`
- `run_prediction()`

Routers now call the service and translate service results into HTTP responses, headers, logs, or HTTP exceptions.

## Key Insight

Routers should handle protocol concerns. Services should handle use-case orchestration.

The service layer can stay independent of FastAPI-specific `HTTPException`, while still returning enough context for the router to build observability headers and stable error responses.

## Project Change

- Added `first_api/services/predictions.py`.
- Moved backend selection and elapsed-time measurement into `run_prediction()`.
- Wrapped lower-level `AIClientError` as `PredictionServiceError`.
- Refactored prediction routes to use the service.
- Added `tests/test_prediction_service.py`.
- Added Lesson 0041 and Reference 0041.

## Why It Matters

This makes the prediction path easier to test and extend. Future features such as retry, caching, rate limiting, or provider fallback can be added to the service layer without making the FastAPI router harder to read.

## Next Step

Add a cautious retry policy for provider calls and explain which failures are retryable.
