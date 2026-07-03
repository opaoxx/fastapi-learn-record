# Learning Record 0021: Schema Evolution and Backward Compatibility

## Date
2026-07-03

## Context
After learning OpenAPI as an API contract, the next step was to understand how API schemas can change over time without unexpectedly breaking frontend clients or future AI-service consumers.

## What changed
- Added field descriptions and numeric constraints to `SummaryTaskListResponse`.
- Added a runtime response-envelope contract test for `GET /tasks`.
- Added an OpenAPI schema test for the required task-list envelope fields and numeric bounds.
- Added lesson 0030 and reference 0030.

## Key insight
Changing JSON shape is a public contract change. Adding optional capabilities can often be backward compatible, but deleting fields, renaming fields, changing field types, adding required request fields, or changing default semantics can break existing clients.

## Retrieval prompts
- Why is changing a field name equivalent to removing one field and adding another?
- Why is changing `GET /tasks` from a bare array to an envelope a breaking change for old clients?
- What is the difference between runtime response tests and OpenAPI schema tests?
- When should an API use deprecation or a new version?

## Next possible step
Teach the real AI provider boundary: external AI calls need timeouts, explicit failure mapping, retry decisions, and test doubles.
