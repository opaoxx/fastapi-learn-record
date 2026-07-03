# Learning Record 0015: List Response Envelope and Count

## Date
2026-07-03

## Context
The task list already supported pagination and status filtering, but it returned a bare list. That was enough to display rows, but not enough for a frontend to know total result count or build pagination controls.

## What changed
- Added `SummaryTaskListResponse` with `items`, `count`, `limit`, and `offset`.
- Changed `GET /tasks` from `list[SummaryTaskRead]` to `SummaryTaskListResponse`.
- Added a count query using `select(func.count()).select_from(SummaryTask)`.
- Kept status filtering consistent between the items query and the count query.
- Updated tests to assert the response envelope and filtered counts.
- Added lessons 0025 and 0026 plus matching quick-reference pages.

## Key insight
`items` is the current page. `count` is the total number of records matching the current filter. They are intentionally different when pagination is active.

## Retrieval prompts
- Why is a response envelope better than a bare list for paginated endpoints?
- Why should count use the same filter conditions as the items query?
- Why should count not receive `offset()` and `limit()`?
- What frontend UI can be built from `count`, `limit`, and `offset`?

## Next possible step
Update the static frontend to show task history with pagination controls and status filters.
