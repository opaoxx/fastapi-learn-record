# Learning Record 0041: Provider Metrics Basics

## Context

Lesson 0049 established provider error taxonomy. The next step was to show how that taxonomy can feed metrics without immediately adding a monitoring backend or external dependency.

## What changed

- Added `ProviderMetricOutcome`, `ProviderMetricFailureCategory`, and `ProviderMetricOperation`.
- Added `ProviderMetricLabels` with an `as_dict()` method.
- Added `build_provider_metric_labels()` to produce stable provider prediction metric labels.
- Added tests for success labels and fail-fast labels.
- Tests verify metric labels do not include raw user request text.
- Added Lesson 0050 and Reference 0050.
- Updated Lesson/Reference 0049 navigation and the course index.

## Key insight

Logs explain one request. Metrics aggregate many requests over time. Metric labels must be stable and low-cardinality, so they should use taxonomy values such as `outcome`, `failure_category`, `error_code`, and `status_code` instead of raw text, response bodies, exception messages, or request IDs.

## Design decision

The course still avoids a Prometheus/OpenTelemetry dependency. It first teaches the shape of good metric labels, because that design survives whichever metrics backend is introduced later.

## Practice prompt

Explain why `status_code="400"` is acceptable as a metric label, but the original prediction text is not.
