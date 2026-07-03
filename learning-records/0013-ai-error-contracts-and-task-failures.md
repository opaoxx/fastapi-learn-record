# Learning Record 0013: AI Error Contracts and Task Failures

## Date
2026-07-03

## Context
The project now has a replaceable `DemoAIClient`. The next step is to teach what happens when model-like services fail. This matters for AI service APIs because timeouts, rate limits, unavailable model servers, and malformed model outputs are normal operational cases.

## What changed
- Added `AIClientError` with stable `error_code` and `message` fields.
- Added `ErrorDetail` and `ErrorResponse` schemas.
- Updated `/predict` to convert known AI client errors into `503 Service Unavailable`.
- Updated background summary execution so known AI failures set `status="failed"` and write a stable `error`.
- Added tests for synchronous AI client failure and background task failure.
- Added lessons 0021 and 0022 plus matching quick-reference pages.

## Key insight
Synchronous endpoint failures can be represented with HTTP status codes immediately. Background task failures happen after the HTTP response has already been sent, so the final result must be represented in the task record.

## Retrieval prompts
- Why does `/predict` use 503 for a known model-client outage?
- Why does a background task failure not change the original 202 response?
- Why is `error_code` more useful to frontend code than a raw exception string?
- What fields should a client inspect when a task is `failed`?

## Next possible step
Teach pagination and filtering for task history, so a frontend can browse many task records safely.
