# Learning Record 0030: Prediction Backend Switch

## Context

The project had two prediction endpoints:

- `POST /predict` for the demo AI client.
- `POST /provider/predict` for the external provider adapter.

This was useful for learning, but a real public API should avoid keeping multiple similar prediction endpoints forever.

## Decision

Add `FIRST_API_AI_PREDICTION_BACKEND` with allowed values `demo` and `provider`.

The main `POST /predict` endpoint now chooses its internal backend based on this setting:

- `demo`: use the existing `AIClient` dependency.
- `provider`: use the async provider prediction adapter with the lifespan-managed HTTP client.

## Key Insight

Public API contracts should remain stable while internal implementations can change by environment.

The caller still sends `PredictionRequest` and receives `PredictionResponse`. The service decides whether the implementation is demo or provider.

## Project Change

- Added `ai_prediction_backend` to settings and `.env.example`.
- Upgraded `POST /predict` to `async def`.
- Added `build_prediction_response()` to keep response construction shared.
- Added tests that override settings to switch `/predict` into provider mode without editing `.env`.
- Added Lesson 0039 and Reference 0039.

## Why It Matters

This is a realistic API evolution pattern. Local development can keep a deterministic demo backend, while deployed environments can switch to a provider backend. Tests can verify both paths using dependency overrides and `MockTransport`.

## Next Step

Add observability around prediction calls: backend, provider, elapsed time, and stable error codes.
