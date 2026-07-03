# Learning Record 0014: Task Pagination and Status Filtering

## Date
2026-07-03

## Context
The project has database-backed summary tasks with queued, running, completed, and failed states. As task history grows, `GET /tasks` should not return every task at once, and the frontend needs a way to view only successful or failed tasks.

## What changed
- Added `offset` and `limit` query parameters to `GET /tasks`.
- Added `status` filtering with the existing `TaskStatus` Literal.
- Updated the service layer to build an ordered SQLModel query with optional `where()`, then `offset()` and `limit()`.
- Added tests for pagination, status filtering, and invalid status validation.
- Added lessons 0023 and 0024 plus matching quick-reference pages.

## Key insight
Pagination and filtering are list-view concerns. They belong in query parameters because the resource is still the task collection; the parameters only describe how to view that collection.

## Retrieval prompts
- What does `limit` control?
- What does `offset` control?
- Why should a paginated query have stable ordering?
- Why does `status=unknown` return 422?

## Next possible step
Introduce response envelopes with `items`, `limit`, `offset`, and `count` so frontends can render richer pagination controls.
