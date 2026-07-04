# Lesson 0064 - Provider Metrics Runbook Findings

## Completed

- Added `build_provider_metrics_runbook_findings()` to translate provider metric samples into teaching-level findings.
- The helper returns `outcome`, `count`, `failure_category`, `status_code`, `severity`, `finding`, and `next_action`.
- Covered stable runbook branches for `success`, `retry_scheduled`, `retry_exhausted`, and `fail_fast`.
- Added an `unknown` branch so new metric outcomes are not silently ignored before the runbook is updated.
- Added tests for core scenario findings, unknown outcomes, and malformed sample validation.
- Added Lesson 0064 and Reference 0064 pages, plus navigation updates.

## Key Idea

Metrics remain low-cardinality machine facts. Findings are human-facing interpretations generated above the metric layer. Keeping those layers separate prevents long explanatory text from leaking into metric labels.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- `.\.venv\Scripts\python.exe -m pytest -q`
