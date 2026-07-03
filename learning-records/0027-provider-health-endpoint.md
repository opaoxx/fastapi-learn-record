# Learning Record 0027: Provider Health Endpoint

## Context

The project already had an async provider adapter, a lifespan-managed `httpx.AsyncClient`, and a dependency bridge from `app.state` to route functions. The next step was to connect these pieces into a real FastAPI endpoint without making tests depend on external network access.

## Decision

Add `GET /provider/health` to call the configured provider health URL with the dependency-injected HTTP client.

The provider URL is stored in `FIRST_API_AI_PROVIDER_HEALTH_URL` instead of being accepted as a user-controlled query parameter.

## Key Insight

An API endpoint is a translation boundary:

- Internal success result: `ProviderHealthResult`
- External success response: `ProviderHealthResponse`
- Internal provider failure: `AIClientError`
- External failure response: HTTP 503 with `ErrorResponse`

This keeps HTTPX details and provider-specific errors out of the public API contract.

## Project Change

- Added `ai_provider_health_url` to `Settings` and `.env.example`.
- Added `ProviderHealthResponse`.
- Added `GET /provider/health`.
- Mapped `AIClientError` to stable HTTP 503 JSON.
- Added tests using `httpx.MockTransport` and `app.dependency_overrides`.
- Added Lesson 0036 and Reference 0036.

## Why It Matters

Real AI services need clear failure boundaries. Provider timeouts, upstream HTTP 503 responses, and connection failures should not leak as random internal exceptions. They should become stable API responses that frontend code, tests, and future interview explanations can rely on.

## Next Step

Design a real provider prediction adapter: translate the local `PredictionRequest` into a provider request payload, then translate the provider response back into the project's stable `PredictionResponse`.
