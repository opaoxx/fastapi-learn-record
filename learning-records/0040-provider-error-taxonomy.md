# Learning Record 0040: Provider Error Taxonomy

## Context

The course had already implemented retry scheduling, retry exhaustion, and fail-fast observability. The next need was to make the language around provider failures explicit so future lessons can discuss errors without mixing failure type, retry decision, log event, and public error code.

## What changed

- Added `ProviderFailureCategory` to name provider failure categories.
- Added `classify_provider_http_status()` to classify HTTP status failures as `retryable_http_status` or `non_retryable_http_status`.
- Updated the HTTP status error branch to use the classification helper while preserving behavior.
- Added a test that protects retryable and non-retryable HTTP taxonomy names.
- Added Lesson 0049 and Reference 0049.
- Updated Lesson/Reference 0048 navigation and the course index.

## Key insight

Failure category and log event are different dimensions. HTTP 503 has the category `retryable_http_status`; depending on attempt budget, it may create a scheduled retry log or an exhausted retry log. HTTP 400 has the category `non_retryable_http_status` and should create a fail-fast log.

## Design decision

The taxonomy starts as a small `Literal` alias and helper instead of a heavier enum or class hierarchy. That keeps the beginner course readable while still giving tests and lessons stable names to depend on.

## Practice prompt

Explain why `retryable_http_status` is not the same kind of concept as `provider_prediction_retry_scheduled`.
