# Learning Record 0029: Provider Predict Endpoint

## Context

The project had a provider prediction adapter, but it was not yet exposed through a FastAPI route. The existing `/predict` endpoint still used the synchronous demo AI client.

## Decision

Add a new `POST /provider/predict` endpoint instead of replacing `/predict` immediately.

The new endpoint:

- Uses the existing `PredictionRequest`.
- Returns the existing `PredictionResponse`.
- Reads `FIRST_API_AI_PROVIDER_PREDICTION_URL` from settings.
- Uses the lifespan-managed provider HTTP client through `Depends`.
- Calls `request_provider_prediction()`.
- Maps `AIClientError` to HTTP 503.

## Key Insight

Provider integration should be gradual. A new provider-specific endpoint lets the project validate the async provider path while keeping the old demo endpoint stable for earlier lessons, local experimentation, and tests.

## Project Change

- Added `ai_provider_prediction_url` to settings and `.env.example`.
- Added `POST /provider/predict`.
- Added tests for successful provider prediction mapping and invalid provider response mapping.
- Added Lesson 0038 and Reference 0038.

## Why It Matters

Real API evolution must protect existing callers. Even when the internal implementation changes from a demo client to a real provider, the public response contract should remain stable. The route should coordinate dependencies and response mapping, while the provider adapter handles external HTTP details.

## Next Step

Introduce a backend-selection setting so `/predict` can choose between demo mode and provider mode without duplicating endpoint behavior forever.
