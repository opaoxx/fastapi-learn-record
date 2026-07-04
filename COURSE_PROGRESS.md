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

## 2026-07-04 Run: Lesson 0052 Provider Metrics Endpoint

### Completed

- Continued from the Lesson 0051 checkpoint and started a new 3-lesson batch.
- Completed Lesson 0052: Provider Metrics Endpoint.
- Connected provider prediction success, retry scheduled, retry exhausted, and fail-fast outcomes to the teaching-only in-process metrics counter.
- Added `GET /provider/metrics` as a read-only snapshot endpoint with response models for metric labels and samples.
- Added tests proving provider prediction success records a metric and the endpoint returns the expected snapshot shape.
- Added Reference 0052 and updated course index/navigation from Lesson 0051 and Reference 0051.
- Updated `NOTES.md` and added `learning-records/0043-provider-metrics-endpoint.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `first_api/schemas.py`
- `first_api/routers/predictions.py`
- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0051-provider-metrics-counters.html`
- `lessons/0052-provider-metrics-endpoint.html`
- `reference/0051-provider-metrics-counters-cheatsheet.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0043-provider-metrics-endpoint.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice, including a small code path for metrics recording and snapshot exposure, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson was already a complete vertical slice from provider event to HTTP response. Extending into Lesson 0053 would risk weakening failure-outcome examples and would exceed the intended one-slice automation cadence. Continue with at most two more complete lessons before the next forced checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 37 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 64 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0053: Provider Metrics Failure Outcomes. Suggested scope:

- Add focused tests and examples for `retry_scheduled`, `retry_exhausted`, and `fail_fast` samples appearing in `GET /provider/metrics`.
- Keep the endpoint read-only and the counter explicitly teaching-only.
- Avoid introducing Prometheus/OpenTelemetry dependencies until the course is ready to discuss production exposition formats.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0053 Provider Metrics Failure Outcomes

### Completed

- Continued from the Lesson 0052 checkpoint without re-planning the whole course.
- Completed Lesson 0053: Provider Metrics Failure Outcomes.
- Added endpoint-level tests proving `GET /provider/metrics` exposes retry failure outcome samples after retryable provider HTTP 503 paths.
- Added endpoint-level tests proving non-retryable provider HTTP 400 paths produce a `fail_fast` metrics sample without scheduled retry samples.
- Added Reference 0053 and updated course index/navigation from Lesson 0052 and Reference 0052.
- Updated `NOTES.md` and added `learning-records/0044-provider-metrics-failure-outcomes.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons: 0052 and 0053.

### Files touched

- `tests/test_ai_client_dependency.py`
- `lessons/0052-provider-metrics-endpoint.html`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0044-provider-metrics-failure-outcomes.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on failure-outcome visibility through the existing metrics endpoint, with two endpoint-level tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson completes the failure-outcome testing story without introducing new metrics backend concepts. Lesson 0054 should stay separate and can focus on test isolation for process-level teaching state. One more complete lesson can be produced before the required 3-lesson checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_ai_client_dependency.py tests\test_provider_http.py -q`
- Result: 39 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 66 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0054: Provider Metrics Test Isolation. Suggested scope:

- Make the `reset_provider_metrics()` pattern explicit as a teaching topic.
- Explain why in-process global state is convenient for lessons but needs strict test boundaries.
- Consider a small pytest fixture if it improves clarity without over-refactoring.
- After Lesson 0054, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0054 Provider Metrics Test Isolation

### Completed

- Continued from the Lesson 0053 checkpoint.
- Completed Lesson 0054: Provider Metrics Test Isolation.
- Added an autouse pytest fixture in `tests/test_ai_client_dependency.py` to reset the in-process provider metrics counter before and after each test in that file.
- Removed repeated manual `reset_provider_metrics()` calls from provider metrics endpoint tests while preserving endpoint behavior coverage.
- Added Reference 0054 and updated course index/navigation from Lesson 0053 and Reference 0053.
- Updated `NOTES.md` and added `learning-records/0045-provider-metrics-test-isolation.md`.
- Completed the current 3-lesson continuation batch: Lessons 0052, 0053, and 0054.

### Files touched

- `tests/test_ai_client_dependency.py`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `lessons/0054-provider-metrics-test-isolation.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `reference/0054-provider-metrics-test-isolation-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0045-provider-metrics-test-isolation.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on test isolation for the existing in-process provider metrics counter, with a small pytest fixture refactor, one full lesson, one quick reference, navigation, and progress records.

Reason for stopping after this lesson: this run completes the 3-lesson batch that started at Lesson 0052. Per the user's checkpoint rule, the next run should start a fresh batch from Lesson 0055 after this saved checkpoint rather than continuing immediately into another lesson in the same context.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_ai_client_dependency.py tests\test_provider_http.py -q`
- Result: 39 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 66 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0055: Provider Metrics Export Shape. Suggested scope:

- Explain the difference between the current JSON teaching snapshot and production metrics exposition formats.
- Keep the first step dependency-free if possible, such as a helper that renders a simple Prometheus-like text shape from the existing snapshot.
- Preserve the warning that in-process counters are teaching-only and not multi-instance aggregation.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0055 Provider Metrics Export Shape

### Completed

- Started a fresh 3-lesson batch after the Lessons 0052-0054 checkpoint.
- Completed Lesson 0055: Provider Metrics Export Shape.
- Added a dependency-free Prometheus text-style renderer for provider metrics snapshots.
- Added `GET /provider/metrics/prometheus` using `PlainTextResponse` for a teaching text export shape.
- Added tests for stable text rendering, label value escaping, text content type, and endpoint output.
- Added Reference 0055 and updated course index/navigation from Lesson 0054 and Reference 0054.
- Updated `NOTES.md` and added `learning-records/0046-provider-metrics-export-shape.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

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
- `learning-records/0046-provider-metrics-export-shape.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on metrics export shape, including a text renderer, one read-only endpoint, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson explains the first export-shape step without mixing in deeper production concerns. Lesson 0056 should separately cover export edge-case tests and preserve depth.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 41 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 68 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0056: Provider Metrics Export Tests. Suggested scope:

- Add tests and lesson material for empty snapshots, multiple failure outcomes, label escaping edge cases, and response headers for the text export endpoint.
- Keep the implementation dependency-free and explicitly teaching-only.
- Current batch will be 2 of 3 after Lesson 0056.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lessons 0056-0057 Provider Metrics Export Tests and Snapshot Boundary

### Completed

- Continued from the Lesson 0055 checkpoint without re-planning the whole course.
- Completed Lesson 0056: Provider Metrics Export Tests.
- Added text export tests for empty snapshots, special label escaping, empty endpoint output, and retry failure outcome endpoint output.
- Completed Lesson 0057: Provider Metrics Snapshot Boundary.
- Added a counter boundary test proving mutating a returned snapshot does not change `ProviderMetricsCounter` internal state.
- Added References 0056 and 0057, updated course index/navigation from Lesson 0055 and Reference 0055.
- Updated `NOTES.md` and added learning records 0047 and 0048.
- Completed the current 3-lesson continuation batch: Lessons 0055, 0056, and 0057.

### Files touched

- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0055-provider-metrics-export-shape.html`
- `lessons/0056-provider-metrics-export-tests.html`
- `lessons/0057-provider-metrics-snapshot-boundary.html`
- `reference/0055-provider-metrics-export-shape-cheatsheet.html`
- `reference/0056-provider-metrics-export-tests-cheatsheet.html`
- `reference/0057-provider-metrics-snapshot-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0047-provider-metrics-export-tests.md`
- `learning-records/0048-provider-metrics-snapshot-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: two complete course slices to finish the active 3-lesson batch. Lesson 0056 focused on metrics text export edge-case tests. Lesson 0057 stayed intentionally smaller and focused on snapshot boundary testing to avoid starting a larger production metrics topic mid-batch.

Reason for stopping after this run: the batch that started at Lesson 0055 is now complete. Per the user's context-safety rule, save this checkpoint before continuing into the next batch.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 46 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 73 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0058: Provider Metrics Production Boundary. Suggested scope:

- Explain why the current in-process teaching counter is not a production metrics pipeline.
- Discuss multi-process, multi-instance, restart, scrape, storage, and alerting boundaries.
- Keep the next implementation slice small and verifiable, such as documentation/tests around existing endpoint descriptions or an explicit production-boundary note.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0058 Provider Metrics Production Boundary

### Completed

- Started a fresh 3-lesson batch after the Lessons 0055-0057 checkpoint.
- Completed Lesson 0058: Provider Metrics Production Boundary.
- Added an OpenAPI contract test protecting the provider metrics endpoint descriptions:
  - `GET /provider/metrics` remains documented as an in-process teaching snapshot, not production multi-instance aggregation.
  - `GET /provider/metrics/prometheus` remains documented as an educational text export shape, not a production multi-instance metrics pipeline.
- Added Reference 0058 and updated course index/navigation from Lesson 0057 and Reference 0057.
- Updated `NOTES.md` and added `learning-records/0049-provider-metrics-production-boundary.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

- `tests/test_openapi_contract.py`
- `lessons/0057-provider-metrics-snapshot-boundary.html`
- `lessons/0058-provider-metrics-production-boundary.html`
- `reference/0057-provider-metrics-snapshot-boundary-cheatsheet.html`
- `reference/0058-provider-metrics-production-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0049-provider-metrics-production-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on the production boundary of the existing teaching metrics endpoints, with one OpenAPI contract test, one full lesson, one quick reference, navigation, and progress records.

Reason for split: production metrics is broad. This lesson intentionally stopped at the documentation and contract boundary instead of adding Prometheus/OpenTelemetry dependencies or deployment instructions. Two more complete lessons can follow in this batch before the next required checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_openapi_contract.py -q`
- Result: 4 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 74 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0059: Provider Metrics Naming Contract. Suggested scope:

- Protect the metric name and label names used by the teaching metrics export.
- Explain why stable names and low-cardinality labels matter for dashboards, alerts, and long-term queries.
- Keep the implementation small and verifiable, likely with tests around metric constants and label keys.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0059 Provider Metrics Naming Contract

### Completed

- Continued from the Lesson 0058 checkpoint without re-planning the whole course.
- Completed Lesson 0059: Provider Metrics Naming Contract.
- Added tests protecting `PROVIDER_PREDICTION_METRIC_NAME`, `PROVIDER_PREDICTION_METRIC_HELP`, and the stable provider metric label keys.
- Added a representative retry-exhausted label set test to keep low-cardinality metric dimensions stable.
- Added Reference 0059 and updated course index/navigation from Lesson 0058 and Reference 0058.
- Updated `NOTES.md` and added `learning-records/0050-provider-metrics-naming-contract.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons: 0058 and 0059.

### Files touched

- `tests/test_provider_http.py`
- `lessons/0058-provider-metrics-production-boundary.html`
- `lessons/0059-provider-metrics-naming-contract.html`
- `reference/0058-provider-metrics-production-boundary-cheatsheet.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0050-provider-metrics-naming-contract.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on metrics naming stability, with two small provider HTTP tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: naming contract is a complete slice by itself. The next lesson should separately discuss rename/refactor boundaries so compatibility and migration can be taught without diluting this lesson's core idea.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 35 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 76 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0060: Provider Metrics Naming Refactor Boundary. Suggested scope:

- Explain how to handle metric or label renames safely.
- Discuss compatibility windows, duplicate export periods, documentation updates, dashboard/alert migration, and contract tests.
- After Lesson 0060, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0060 Provider Metrics Naming Refactor Boundary

### Completed

- Continued from the Lesson 0059 checkpoint.
- Completed Lesson 0060: Provider Metrics Naming Refactor Boundary.
- Added `PROVIDER_PREDICTION_METRIC_LABEL_NAMES` to make the exported provider metric label-name contract explicit.
- Added `get_provider_prediction_metric_contract()` to expose metric name, HELP text, and label names as a small rename-sensitive contract snapshot.
- Added a provider HTTP test proving the metric contract snapshot contains the fields that must be reviewed before any future metric rename.
- Added Reference 0060 and updated course index/navigation from Lesson 0059 and Reference 0059.
- Updated `NOTES.md` and added `learning-records/0051-provider-metrics-naming-refactor-boundary.md`.
- Completed the current 3-lesson continuation batch: Lessons 0058, 0059, and 0060.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0059-provider-metrics-naming-contract.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `reference/0060-provider-metrics-naming-refactor-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0051-provider-metrics-naming-refactor-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on safe metrics rename boundaries, with a small contract helper, one provider HTTP test, one full lesson, one quick reference, navigation, and progress records.

Reason for stopping after this lesson: this run completes the 3-lesson batch that started at Lesson 0058. Per the user's checkpoint rule, the next run should start a fresh batch from Lesson 0061 after this saved checkpoint rather than continuing immediately into another lesson in the same context.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 36 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 77 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0061: Provider Metrics Documentation Index. Suggested scope:

- Create or protect a single documentation entry that points to the provider metrics endpoints, naming contract, production boundary, and tests.
- Keep the implementation small and verifiable, such as a docs/reference index page or an OpenAPI/documentation consistency test.
- Start a new 3-lesson batch from Lesson 0061.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0061 Provider Metrics Documentation Index

### Completed

- Started a fresh 3-lesson batch after the Lesson 0058-0060 checkpoint.
- Completed Lesson 0061: Provider Metrics Documentation Index.
- Added `reference/provider-metrics-index.html` as a single provider metrics documentation entry for endpoints, metric contract fields, production boundary notes, related lessons, and tests.
- Added `tests/test_course_docs_contract.py` with HTML parsing tests that protect the documentation entry's required contract terms and links.
- Added Reference 0061 and updated course index/navigation from Lesson 0060 and Reference 0060.
- Updated `NOTES.md` and added `learning-records/0052-provider-metrics-documentation-index.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons: 0061.

### Files touched

- `tests/test_course_docs_contract.py`
- `reference/provider-metrics-index.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `lessons/0061-provider-metrics-documentation-index.html`
- `reference/0060-provider-metrics-naming-refactor-boundary-cheatsheet.html`
- `reference/0061-provider-metrics-documentation-index-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0052-provider-metrics-documentation-index.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on provider metrics documentation indexing, with one static documentation entry, one small HTML parser contract test file, one full lesson, one quick reference, navigation, and progress records.

Reason for split: documentation index is a complete and verifiable slice by itself. The next lesson should separately cover a runbook/checklist for investigating metric anomalies, because operational troubleshooting would add a different workflow and should not be compressed into the documentation-index lesson.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 2 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 79 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0062: Provider Metrics Runbook Checklist. Suggested scope:

- Turn the provider metrics endpoints and tests into a small troubleshooting checklist.
- Teach how to inspect success, retry scheduled, retry exhausted, and fail-fast samples.
- Keep it verifiable with a focused test or docs check if the runbook becomes a durable reference page.

### Blockers

- No project blocker found.
