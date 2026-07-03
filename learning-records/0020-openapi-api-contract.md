# Learning Record 0020: OpenAPI API Contract

## Date
2026-07-03

## Context
The project already had a browser frontend calling task-list APIs. The next learning step was to understand how FastAPI turns routes, models, parameters, and security dependencies into a visible API contract that frontend code and tests can rely on.

## What changed
- Added richer OpenAPI metadata to the FastAPI app.
- Added tag descriptions for system, items, predictions, tasks, and files.
- Named the API key security scheme `ApiKeyAuth`.
- Added summaries, descriptions, response descriptions, and parameter descriptions to task endpoints.
- Added OpenAPI contract tests for `GET /tasks` and `X-API-Key` security documentation.
- Added lesson 0029 and reference 0029.

## Key insight
FastAPI's automatic docs are generated from the same structured code that handles requests: path operations, type hints, Pydantic/SQLModel models, `Query`, `Path`, `response_model`, and security dependencies. `/openapi.json` is the machine-readable contract; `/docs` is the human-friendly rendering.

## Retrieval prompts
- Why is `/openapi.json` more fundamental than `/docs`?
- Which pieces of Python code create the `GET /tasks` query parameter contract?
- What does `response_model=SummaryTaskListResponse` contribute to OpenAPI?
- How does `APIKeyHeader` appear in the OpenAPI schema?

## Next possible step
Teach schema evolution and backward compatibility: changing JSON shape is a contract change, not just a code refactor.
