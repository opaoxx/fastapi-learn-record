# Learning Record 0034: Backoff Before Retry

## Context

The project already had a provider retry policy for timeout, request errors, 429, and common temporary 5xx responses. The remaining reliability issue was that immediate retries can amplify provider overload by sending many repeated requests in a short time.

## What changed

- `Settings` now includes `ai_retry_base_delay_seconds` and `ai_retry_max_delay_seconds`.
- `.env.example` documents `FIRST_API_AI_RETRY_BASE_DELAY_SECONDS` and `FIRST_API_AI_RETRY_MAX_DELAY_SECONDS`.
- `AIClientConfig` carries retry delay settings alongside timeout and max attempts.
- `request_provider_prediction()` now waits before retrying retryable failures.
- `calculate_retry_delay()` implements capped exponential backoff.
- Tests use a fake async sleep function to assert delay values without actually waiting.

## Key insight

Retry policy answers whether a failure should be retried. Backoff answers how long the client should wait before retrying. Without backoff, retries can turn a temporary provider outage into a larger request storm.

## Design decision

The backoff logic lives in the provider adapter because it depends on provider retry behavior. The sleep function is injectable so tests can verify delay decisions without slowing down the suite.

## Practice prompt

With `retry_base_delay_seconds=1.0` and `retry_max_delay_seconds=3.0`, explain why the first four failed attempts produce delays of `1.0`, `2.0`, `3.0`, and `3.0` seconds.
