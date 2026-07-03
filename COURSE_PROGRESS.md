# Course Progress

## 2026-07-04 Run: Lesson 0048 Fail-fast Observability

### Completed

- Located current course progress from `NOTES.md`, `learning-records/0038-retry-exhaustion.md`, and the latest Lesson/Reference 0047 files.
- Completed Lesson 0048: Fail-fast Observability.
- Added fail-fast structured logging for provider prediction non-retryable HTTP errors and invalid provider response bodies.
- Added tests proving HTTP 400 and invalid response body paths do not retry and do not emit retry-exhausted logs.
- Added Reference 0048 and updated course index/navigation from Lesson 0047 and Reference 0047.
- Updated `NOTES.md` and added `learning-records/0039-fail-fast-observability.md`.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0047-retry-exhaustion.html`
- `lessons/0048-fail-fast-observability.html`
- `reference/0047-retry-exhaustion-cheatsheet.html`
- `reference/0048-fail-fast-observability-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0039-fail-fast-observability.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice, including one code behavior improvement, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: extending into Lesson 0049 in the same run would risk compressing the explanation quality and weakening verification. The next run should continue with exactly one new lesson slice.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 23 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 57 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0049: Provider Error Taxonomy. Suggested scope:

- Organize provider failure classes into a clear taxonomy: timeout, request error, retryable HTTP status, non-retryable HTTP status, invalid response, scheduled retry, retry exhaustion, and fail fast.
- Prefer a small, verifiable slice. A good candidate is a lesson/reference pair plus tests or documentation that ensure the taxonomy names stay stable.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0049 Provider Error Taxonomy

### Completed

- Continued from the Lesson 0048 checkpoint without re-planning the whole course.
- Completed Lesson 0049: Provider Error Taxonomy.
- Added `ProviderFailureCategory` and `classify_provider_http_status()` to make HTTP status retry taxonomy explicit.
- Added a provider HTTP test that protects taxonomy names for retryable and non-retryable status codes.
- Added Reference 0049 and updated course index/navigation from Lesson 0048 and Reference 0048.
- Updated `NOTES.md` and added `learning-records/0040-provider-error-taxonomy.md`.
- Updated automation rule: after every 3 completed lessons, stop and save a checkpoint; this continuation batch has completed 1 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0048-fail-fast-observability.html`
- `lessons/0049-provider-error-taxonomy.html`
- `reference/0048-fail-fast-observability-cheatsheet.html`
- `reference/0049-provider-error-taxonomy-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0040-provider-error-taxonomy.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one compact but complete course slice, including a small taxonomy helper, focused test coverage, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this is lesson 1 of the new 3-lesson continuation batch. Continue with at most two more complete lessons before forcing a checkpoint/compaction stop. If quota becomes risky earlier, stop with a checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 24 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 58 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0050: Provider Metrics Basics. Suggested scope:

- Explain the difference between logs and metrics for provider failures.
- Prefer a small, verifiable implementation such as in-process counters or a metrics-shape helper if it fits the project without adding dependencies.
- Keep the lesson tied to the provider error taxonomy from Lesson 0049.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0050 Provider Metrics Basics

### Completed

- Continued from the Lesson 0049 checkpoint.
- Completed Lesson 0050: Provider Metrics Basics.
- Added `ProviderMetricLabels` and `build_provider_metric_labels()` to define stable low-cardinality provider prediction metric labels.
- Added tests for success labels and fail-fast failure labels, including a guard that raw request text is not used as a metric label value.
- Added Reference 0050 and updated course index/navigation from Lesson 0049 and Reference 0049.
- Updated `NOTES.md` and added `learning-records/0041-provider-metrics-basics.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0049-provider-error-taxonomy.html`
- `lessons/0050-provider-metrics-basics.html`
- `reference/0049-provider-error-taxonomy-cheatsheet.html`
- `reference/0050-provider-metrics-basics-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0041-provider-metrics-basics.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one focused lesson slice covering metric label shape rather than a full metrics backend. This keeps the lesson complete without adding deployment or monitoring-platform complexity.

Reason for split: this is lesson 2 of the current 3-lesson continuation batch. One more complete lesson can be produced before the required checkpoint/compaction stop, unless quota becomes risky earlier.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 26 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 60 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0051: Provider Metrics Counters. Suggested scope:

- Add a small dependency-free in-process counter or counter-shape helper for provider prediction outcomes.
- Keep it explicitly educational and avoid presenting in-memory counters as a production multi-process metrics solution.
- After Lesson 0051, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0051 Provider Metrics Counters

### Completed

- Continued from the Lesson 0050 checkpoint.
- Completed Lesson 0051: Provider Metrics Counters.
- Added teaching-only `ProviderMetricsCounter` to demonstrate count accumulation by stable provider metric label sets.
- Added tests for repeated label accumulation and rejecting non-positive increments.
- Added Reference 0051 and updated course index/navigation from Lesson 0050 and Reference 0050.
- Updated `NOTES.md` and added `learning-records/0042-provider-metrics-counters.md`.
- Completed the current 3-lesson continuation batch: Lessons 0049, 0050, and 0051.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0050-provider-metrics-basics.html`
- `lessons/0051-provider-metrics-counters.html`
- `reference/0050-provider-metrics-basics-cheatsheet.html`
- `reference/0051-provider-metrics-counters-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0042-provider-metrics-counters.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one focused counter-semantics lesson using a dependency-free teaching helper, plus tests, lesson, reference, navigation, and progress records.

Reason for stopping after this lesson: user requested automatic context checkpointing after every 3 completed lessons. This run completed the 3-lesson batch after Lesson 0048: Lessons 0049, 0050, and 0051.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 28 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 62 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0052: Provider Metrics Endpoint. Suggested scope:

- Expose a read-only teaching endpoint or service-level snapshot for provider metrics.
- Keep clear that in-process metrics are educational and not production multi-instance aggregation.
- Start a new 3-lesson batch from Lesson 0052.

### Blockers

- No project blocker found.
