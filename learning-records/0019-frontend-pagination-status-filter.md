# Learning Record 0019: Frontend Pagination and Status Filter

## Date
2026-07-03

## Context
The static frontend could render the first page of task history from the response envelope, but users could not change `status`, `limit`, or `offset` from the UI.

## What changed
- Added status filter buttons for all, queued, running, completed, and failed tasks.
- Added a page size selector for 3, 5, or 10 tasks per page.
- Added previous and next page buttons.
- Introduced `historyState` to keep `status`, `limit`, `offset`, `count`, and `itemsLength` together.
- Used `URLSearchParams` to build the task history query string.
- Reset `offset` to `0` when status or page size changes.
- Added lesson 0028 and reference 0028.

## Key insight
Pagination and filtering are shared state between UI controls and backend query parameters. The frontend should not hand-edit DOM rows independently of the API; it should update query state, request the backend, and render the response envelope.

## Retrieval prompts
- Why should changing `status` reset `offset`?
- Why is `URLSearchParams` safer than manual string concatenation?
- Why does the next-page button need `count`?
- Which fields belong to request state, and which fields come from the response envelope?

## Next possible step
Teach OpenAPI as the visible API contract generated from routes, query parameters, Pydantic models, and response models.

