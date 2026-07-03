# Learning Record 0036: Retry Jitter

## Context

The provider adapter already supported retry policy, capped exponential backoff, and `Retry-After`. The remaining issue was synchronization: many clients using the same backoff formula can still retry at the same time and create request spikes.

## What changed

- `Settings` now includes `ai_retry_jitter_seconds`.
- `.env.example` documents `FIRST_API_AI_RETRY_JITTER_SECONDS`.
- `AIClientConfig` carries `retry_jitter_seconds`.
- `calculate_retry_jitter()` computes a bounded random delay.
- `calculate_retry_delay()` adds jitter to local exponential backoff.
- Valid `Retry-After` hints are not jittered.
- `request_provider_prediction()` accepts an injectable `random_fraction` function for deterministic tests.
- Provider HTTP tests now verify jitter math, max-delay capping after jitter, invalid `Retry-After` fallback with jitter, and real retry wait behavior with fixed random input.

## Key insight

Backoff slows retries down. Jitter spreads retries out. Without jitter, clients that fail at the same time and use the same backoff formula can still retry in synchronized clusters.

## Design decision

The project uses simple additive jitter:

```text
delay = min(exponential_delay + random_fraction * retry_jitter_seconds, max_delay)
```

This is not the most advanced production strategy, but it is easy to reason about and test. More advanced strategies such as full jitter can be introduced later.

## Practice prompt

With `base_delay=1.0`, `attempt=2`, `retry_jitter_seconds=0.5`, and `random_fraction=0.4`, explain why the final local retry delay is `2.2` seconds before max-delay capping.
