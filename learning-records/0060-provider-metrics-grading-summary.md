# Learning Record 0060 - Provider Metrics Grading Summary

- Lesson: `lessons/0069-provider-metrics-grading-summary.html`
- Reference: `reference/0069-provider-metrics-grading-summary-cheatsheet.html`
- Core helper: `summarize_provider_metrics_runbook_exercise_grades()`
- Key idea: batch grading should reuse single-answer grading, then add completion and pass/fail statistics without storing raw response text.
- Validation focus:
  - count total, answered, passed, failed, and unanswered correctly;
  - preserve per-card grade details;
  - distinguish unanswered cards from answered-but-wrong cards.
