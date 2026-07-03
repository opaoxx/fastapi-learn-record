# Learning Record 0028: Provider Prediction Adapter

## Context

The project already had a provider health endpoint, but health checks only verify reachability. A real prediction call must translate local inputs into provider request JSON, then validate and translate provider response JSON back into the project's internal prediction result.

## Decision

Add `request_provider_prediction()` to `first_api/services/provider_http.py`.

This function sends a provider prediction request with `httpx.AsyncClient.post(..., json=...)`, validates the provider response with Pydantic, and returns the internal `PredictionResult`.

## Key Insight

HTTP 200 is not enough. The provider response body is external data and must be validated at the project boundary.

The adapter now separates:

- Local request meaning: `text` and `mode`
- Provider request payload: `ProviderPredictionPayload`
- Provider response body: `ProviderPredictionBody`
- Internal project result: `PredictionResult`
- Internal project failure: `AIClientError`

## Project Change

- Added `ProviderPredictionPayload`.
- Added `ProviderPredictionBody`.
- Added `request_provider_prediction()`.
- Added tests for successful request payload mapping, invalid provider response mapping, and provider HTTP 503 mapping.
- Added Lesson 0037 and Reference 0037.

## Why It Matters

Provider APIs change. Internal API contracts should not depend directly on provider JSON shapes. A provider adapter gives the project one place to translate, validate, and classify external behavior before it reaches routers, background tasks, or frontend-facing response models.

## Next Step

Connect the async provider prediction adapter into a FastAPI route while preserving the existing stable `/predict` response contract.
