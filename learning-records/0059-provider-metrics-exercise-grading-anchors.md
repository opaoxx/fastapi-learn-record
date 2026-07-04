# Learning Record 0059 - Provider Metrics Exercise Grading Anchors

- Lesson: `lessons/0068-provider-metrics-exercise-grading-anchors.html`
- Reference: `reference/0068-provider-metrics-exercise-grading-anchors-cheatsheet.html`
- Core helper: `grade_provider_metrics_runbook_exercise_answer()`
- Key idea: teaching-grade scoring should start with deterministic anchors before introducing fuzzy semantic evaluation.
- Validation focus:
  - pass when response contains expected severity and expected next action;
  - report both missing anchors when response omits them;
  - keep grading pure and separate from provider calls, metrics counters, and answer-key rendering.
