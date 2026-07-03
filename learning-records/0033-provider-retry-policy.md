# Learning Record 0033: Provider Retry Policy

## Context

The learner is building a FastAPI project that can expose AI-style prediction endpoints. The project already has a provider prediction adapter and a prediction service orchestration layer. The next reliability concern is how to handle temporary external provider failures without making routers or services responsible for low-level HTTP transport details.

## What changed

- `request_provider_prediction()` now uses `AIClientConfig.max_attempts`.
- Provider prediction calls retry timeout and request errors until the attempt budget is exhausted.
- HTTP 429, 500, 502, 503, and 504 are treated as retryable provider statuses.
- 400-style non-retryable HTTP errors fail immediately.
- Invalid provider response JSON or Pydantic validation failures fail immediately.
- Tests now verify successful retry after 503, max-attempt exhaustion, fail-fast 400 behavior, and fail-fast invalid response behavior.

## Key insight

Retry is not a generic "try again" loop. It is a policy that classifies failures. The project should retry only failures that plausibly represent temporary provider or network conditions, and it should fail fast when the request, authentication, URL, or response contract is wrong.

## Design decision

The retry policy lives in `first_api/services/provider_http.py`, not in the FastAPI router and not in the prediction service. This keeps provider-specific HTTP knowledge inside the provider adapter:

- HTTPX exceptions belong to the adapter boundary.
- HTTP status-code retry decisions belong to the adapter boundary.
- Provider response-body validation belongs to the adapter boundary.
- The service still receives a stable `PredictionResult` or `AIClientError`.
- The router still translates service results into HTTP responses.

## Practice prompt

Explain why `max_attempts=3` means "at most three total provider requests", and why the app should retry a 503 but not retry a 400 or an invalid provider response body.
