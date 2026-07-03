# Learning Record 0037: Retry Observability

## Context

The provider adapter already supported retry policy, capped exponential backoff, `Retry-After`, and jitter. The remaining issue was explainability: when a retry happened, the code waited correctly, but the retry plan was not visible in structured logs.

## What changed

- Added a `RetryDelayPlan` dataclass with `delay_seconds` and `source`.
- Added `build_retry_delay_plan()` so retry delay calculation can expose whether the delay came from `Retry-After` or local backoff.
- Kept `calculate_retry_delay()` returning a float for existing callers and tests.
- Added a module logger to `first_api.services.provider_http`.
- `wait_before_retry()` now logs `provider_prediction_retry_scheduled` before sleeping.
- Retry logs include `attempt`, `max_attempts`, `retry_reason`, `status_code`, `retry_after`, `delay_seconds`, and `delay_source`.
- Added a pytest `caplog` test that verifies the structured retry log fields for a 429 response with `Retry-After`.

## Key insight

Retry behavior is part of production behavior. If the system retries silently, slow requests and temporary provider failures become hard to explain. A stable log event with structured fields makes retry behavior searchable, testable, and diagnosable without changing the public API response shape.

## Design decision

Retry details remain internal observability data instead of being added to `PredictionResponse`. This keeps the public JSON contract stable while still giving developers enough information to debug provider instability.

## Practice prompt

Explain why `delay_source="retry_after"` and `delay_source="local_backoff"` are more useful than only logging `delay_seconds=2.0`.
