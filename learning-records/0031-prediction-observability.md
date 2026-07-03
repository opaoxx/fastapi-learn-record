# Learning Record 0031: Prediction Observability

## Context

The project could switch `/predict` between demo and provider backends, but it did not yet expose enough runtime evidence to diagnose which backend handled a request, how long it took, or which stable error code caused a failure.

## Decision

Add low-intrusion observability to prediction endpoints:

- Success response headers: backend, source, elapsed milliseconds.
- Failure response headers: backend, elapsed milliseconds, error code.
- Success logs: `prediction_completed`.
- Failure logs: `prediction_failed`.

The JSON response body remains unchanged.

## Key Insight

Observability should help diagnose behavior without destabilizing the public API contract.

Headers give the caller and tests fast request-level visibility. Logs give the server a durable diagnostic trail. Neither requires adding debug fields to `PredictionResponse`.

## Project Change

- Added prediction observability helpers in `first_api/routers/predictions.py`.
- Added `time.perf_counter()` elapsed time measurement.
- Added module-level Python logger.
- Added headers for success and failure paths.
- Added log assertions and header assertions in prediction tests.
- Added Lesson 0040 and Reference 0040.

## Why It Matters

Real AI services need diagnosis evidence. A 503 without backend, elapsed time, or error code is hard to debug. With this lesson, the prediction endpoint now leaves enough metadata to distinguish demo failures, provider failures, invalid provider responses, and slow calls.

## Next Step

Move backend selection and observability out of the router into a deeper prediction service so the route stays thin.
