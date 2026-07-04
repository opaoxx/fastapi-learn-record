# Learning Record 0046 - Provider Metrics Export Shape

## What changed

- Added a dependency-free renderer for provider metrics snapshots in a Prometheus text-style teaching format.
- Added `GET /provider/metrics/prometheus` with `PlainTextResponse`.
- Added tests for stable text rendering, label escaping, text content type, and endpoint output.
- Added Lesson 0055 and Reference 0055.
- Linked Lesson 0054, Reference 0054, and the course index to the new materials.
- Started a fresh 3-lesson batch after the 0052-0054 checkpoint.

## Key idea

Metrics facts and export shape are separate. The in-process counter stores facts, JSON snapshot is useful for teaching and debugging, and text export shows the shape monitoring systems commonly scrape. This is still a teaching export, not a production multi-instance metrics pipeline.

## Files

- `first_api/services/provider_http.py`
- `first_api/routers/predictions.py`
- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0054-provider-metrics-test-isolation.html`
- `lessons/0055-provider-metrics-export-shape.html`
- `reference/0054-provider-metrics-test-isolation-cheatsheet.html`
- `reference/0055-provider-metrics-export-shape-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Lesson 0056 can deepen Provider Metrics Export Tests by covering empty snapshots, multiple failure outcomes, escaping edge cases, and endpoint response headers.
