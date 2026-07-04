# Learning Record 0050 - Provider Metrics Naming Contract

## What changed

- Added tests protecting the provider prediction metric name and HELP text.
- Added tests protecting the provider prediction metric label keys and a representative retry-exhausted label set.
- Added Lesson 0059 and Reference 0059.
- Linked Lesson 0058, Reference 0058, and the course index to the new materials.
- Current 3-lesson batch is now 2 of 3 complete: Lessons 0058 and 0059.

## Key idea

Metric names and label names are monitoring API. Once exported, dashboards, alerts, docs, and debugging queries can depend on them. They should be stable, low-cardinality, and protected by tests.

## Files

- `tests/test_provider_http.py`
- `lessons/0058-provider-metrics-production-boundary.html`
- `lessons/0059-provider-metrics-naming-contract.html`
- `reference/0058-provider-metrics-production-boundary-cheatsheet.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Lesson 0060 can continue with Provider Metrics Naming Refactor Boundary: how to handle metric or label renames safely with compatibility, migration notes, tests, and documentation updates.
