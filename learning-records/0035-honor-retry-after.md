# Learning Record 0035: Honor Retry-After

## Context

The provider adapter already used capped exponential backoff before retrying retryable failures. The remaining limitation was that the client estimated every retry delay locally, even when a provider response explicitly included a `Retry-After` header.

## What changed

- `parse_retry_after_delay()` parses `Retry-After` delay-seconds values.
- `parse_retry_after_delay()` parses HTTP-date values with `email.utils.parsedate_to_datetime`.
- `calculate_retry_delay()` now prefers a valid provider `Retry-After` hint over local exponential backoff.
- Provider hints are still capped by `retry_max_delay_seconds`.
- Invalid `Retry-After` values fall back to local exponential backoff.
- The HTTP status error branch passes `exc.response.headers.get("Retry-After")` into the retry wait function.
- Tests now cover delay-seconds, HTTP-date, cap behavior, invalid header fallback, and 429 retry behavior with `Retry-After`.

## Key insight

Local backoff is a client estimate. `Retry-After` is a provider hint. A robust adapter should prefer valid provider hints, but it still needs a client-side maximum wait to avoid holding synchronous API requests for too long.

## Design decision

The project honors `Retry-After` only inside retryable HTTP response failures, such as 429 and common temporary 5xx responses. Timeout and request errors still use local backoff because they do not provide a normal HTTP response header.

## Practice prompt

Explain what should happen when the provider returns `Retry-After: 5`, but the local `retry_max_delay_seconds` is `3.0`. Then explain why an invalid header such as `Retry-After: later` should fall back to local backoff rather than being treated as zero seconds.
