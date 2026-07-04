# Learning Record 0045 - Provider Metrics Test Isolation

## What changed

- Added an autouse pytest fixture in `tests/test_ai_client_dependency.py`.
- The fixture resets the in-process provider metrics counter before and after each test in that file.
- Removed repeated manual `reset_provider_metrics()` calls from provider metrics endpoint tests.
- Added Lesson 0054 and Reference 0054.
- Linked Lesson 0053, Reference 0053, and the course index to the new materials.
- Completed the current 3-lesson batch: Lessons 0052, 0053, and 0054.

## Key idea

In-process teaching state is convenient, but it must be isolated in tests. A yield fixture makes the setup and teardown rule explicit: start with an empty metrics counter, run the test, then clean the counter again.

## Files

- `tests/test_ai_client_dependency.py`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `lessons/0054-provider-metrics-test-isolation.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `reference/0054-provider-metrics-test-isolation-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Start a fresh batch from Lesson 0055. A good next topic is Provider Metrics Export Shape: explain the difference between the current JSON teaching snapshot and production exposition formats such as Prometheus text format or OpenTelemetry metrics.
