# Learning Record 0039: Fail-fast Observability

## Context

The provider adapter already distinguished scheduled retries from retry exhaustion. The remaining observability gap was the fail-fast path: non-retryable HTTP errors and invalid provider response bodies stopped correctly, but did not leave a dedicated structured log explaining why no retry happened.

## What changed

- Added `FailFastReason` for stable fail-fast reason values.
- Added `log_prediction_fail_fast()` in the provider HTTP adapter.
- Non-retryable provider HTTP status errors now log `provider_prediction_fail_fast`.
- Invalid provider prediction response bodies now log `provider_prediction_fail_fast`.
- Tests now verify that HTTP 400 and invalid response bodies attempt only once, emit fail-fast logs, and do not emit retry-exhausted logs.
- Added Lesson 0048 and Reference 0048, and linked them from the course index and Lesson/Reference 0047.

## Key insight

Fail fast is not the same as retry exhaustion. Retry exhaustion means the system wanted to retry but used all retry budget. Fail fast means the error classification says retrying would be misleading or wasteful.

## Design decision

Fail-fast details remain internal structured logs instead of public response fields. The public error contract still uses stable `AIClientError` codes, while logs explain why the adapter stopped after one attempt.

## Practice prompt

With `max_attempts=3` and provider response HTTP 400, explain why there is exactly one attempt, one `provider_prediction_fail_fast` log, and zero `provider_prediction_retry_exhausted` logs.
