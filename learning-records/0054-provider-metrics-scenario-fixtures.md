# Lesson 0063 - Provider Metrics Scenario Fixtures

## Completed

- Added `build_provider_metrics_runbook_scenario_samples()` to create stable provider metrics samples for runbook practice.
- Covered four core outcomes: `success`, `retry_scheduled`, `retry_exhausted`, and `fail_fast`.
- Kept the helper pure: it returns sample data and does not mutate the in-process provider metrics counter.
- Added tests for sample shape, outcome coverage, counts, labels, and Prometheus text-style rendering.
- Added Lesson 0063 and Reference 0063 pages, plus course index and provider metrics documentation navigation.

## Key Idea

Scenario fixtures are fixed observation samples. They are useful for learning how to read metrics and follow a runbook, but they are not runtime metrics and should not be exposed as production monitoring data.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- `.\.venv\Scripts\python.exe -m pytest -q`
