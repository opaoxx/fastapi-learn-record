# Learning Record 0062 - Provider Metrics Grading Summary Validation

- Lesson: `lessons/0071-provider-metrics-grading-summary-validation.html`
- Reference: `reference/0071-provider-metrics-grading-summary-validation-cheatsheet.html`
- Core helper: `validate_provider_metrics_runbook_grading_summary()`
- Key idea: validate grading summary structure and count consistency before rendering Markdown reports.
- Validation focus:
  - required summary fields exist and are integers;
  - `grades` is a list;
  - grade detail fields have correct types;
  - aggregate counts are internally consistent.
