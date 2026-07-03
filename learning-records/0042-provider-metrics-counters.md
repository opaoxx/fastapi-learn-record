# Learning Record 0042: Provider Metrics Counters

## Context

Lesson 0050 defined stable provider metric labels. The next step was to demonstrate the simplest metric aggregation idea: a counter increments counts for repeated label sets.

## What changed

- Added `ProviderMetricsCounter`, a teaching-only in-process counter.
- The counter stores `ProviderMetricLabels` as keys and accumulates counts.
- Added `snapshot()` to expose samples as `{"labels": ..., "count": ...}` dictionaries.
- Added validation that increment amounts must be positive.
- Added tests for repeated label accumulation and invalid increment amounts.
- Added Lesson 0051 and Reference 0051.
- Updated Lesson/Reference 0050 navigation and the course index.

## Key insight

Counter metrics aggregate many events over time. They are not a replacement for structured logs: logs explain one request, while counters show how often each stable label set occurred.

## Design decision

The counter is explicitly presented as an educational in-process model, not a production monitoring backend. It teaches counter semantics before introducing endpoint exposure or external metrics systems.

## Practice prompt

Explain why two success events with identical labels produce one sample with `count=2`, while a fail-fast event produces a separate sample.
