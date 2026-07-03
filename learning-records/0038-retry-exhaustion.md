# Learning Record 0038: Retry Exhaustion

## Context

The provider adapter already logged `provider_prediction_retry_scheduled` before sleeping between retry attempts. That explained intermediate retry behavior, but it did not explicitly mark the final moment when all attempts were exhausted.

## What changed

- Added `RetryFailureReason` to make retry reason values explicit.
- Added `log_retry_exhausted()` in the provider HTTP adapter.
- The adapter now logs `provider_prediction_retry_exhausted` at warning level when timeout, request error, or retryable HTTP status failures reach the final allowed attempt.
- HTTP 400-style non-retryable status failures are not logged as retry exhaustion.
- Invalid provider response bodies are not logged as retry exhaustion.
- The max-attempts test now uses `caplog` to verify exhausted log fields.

## Key insight

Scheduled retry and retry exhaustion are different events. A scheduled retry means the request failed but still has retry budget. Retry exhaustion means the error was retryable, but the retry budget has been fully spent and the adapter must stop.

## Design decision

Retry exhaustion remains an internal warning log instead of a public response-body field. The public error response still comes from the existing `AIClientError` mapping, while logs preserve internal diagnostic details.

## Practice prompt

With `max_attempts=3` and provider responses `503, 503, 503`, explain why the first two failures create scheduled retry logs but the third creates an exhausted log.
