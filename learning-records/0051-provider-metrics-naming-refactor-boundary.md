# Learning Record 0051 - Provider Metrics Naming Refactor Boundary

## What changed

- Added `PROVIDER_PREDICTION_METRIC_LABEL_NAMES` to make exported provider metric label names explicit.
- Added `get_provider_prediction_metric_contract()` to expose metric name, HELP text, and label names as a small contract snapshot.
- Added a provider HTTP test proving the metric contract snapshot collects rename-sensitive fields.
- Added Lesson 0060 and Reference 0060.
- Linked Lesson 0059, Reference 0059, and the course index to the new materials.
- Completed the current 3-lesson batch: Lessons 0058, 0059, and 0060.

## Key idea

Metrics rename is a compatibility migration, not ordinary refactoring. Before changing a metric name or label name, collect the contract surface, plan a compatibility window, migrate dashboards and alerts, verify consumers, and only then remove old names.

## Files

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0059-provider-metrics-naming-contract.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `reference/0060-provider-metrics-naming-refactor-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Start a fresh batch with Lesson 0061: Provider Metrics Documentation Index. Suggested scope: create or protect a single documentation entry that points to the provider metrics endpoints, naming contract, production boundary, and tests.
