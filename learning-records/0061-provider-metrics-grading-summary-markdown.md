# Learning Record 0061 - Provider Metrics Grading Summary Markdown

- Lesson: `lessons/0070-provider-metrics-grading-summary-markdown.html`
- Reference: `reference/0070-provider-metrics-grading-summary-markdown-cheatsheet.html`
- Core helper: `render_provider_metrics_runbook_grading_summary_markdown()`
- Key idea: report rendering should consume structured summary data without recalculating grading results or exposing raw response text.
- Validation focus:
  - render a stable summary table;
  - render stable per-card grade details;
  - display empty missing lists as `-`;
  - reject malformed summary detail shapes early.
