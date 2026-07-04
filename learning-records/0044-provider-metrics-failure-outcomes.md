# Learning Record 0044 - Provider Metrics Failure Outcomes

## What changed

- Added endpoint-level tests for provider metrics failure outcomes.
- Verified that repeated provider HTTP 503 responses produce both `retry_scheduled` and `retry_exhausted` samples in `GET /provider/metrics`.
- Verified that provider HTTP 400 produces a single `fail_fast` sample with `non_retryable_http_status`.
- Added Lesson 0053 and Reference 0053.
- Linked Lesson 0052, Reference 0052, and the course index to the new materials.

## Key idea

Provider failure metrics should describe system action, not only error existence. `retry_scheduled` means the system is still trying to recover, `retry_exhausted` means retryable failure became final, and `fail_fast` means retry would be wasteful or misleading.

## Files

- `tests/test_ai_client_dependency.py`
- `lessons/0052-provider-metrics-endpoint.html`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Lesson 0054 can focus on Provider Metrics Test Isolation by making the reset pattern explicit and explaining why process-level teaching state needs careful test boundaries.
