# Learning Record 0017: Frontend Task History

## Date
2026-07-03

## Context
The task list API now returns a response envelope with `items`, `count`, `limit`, and `offset`. The static frontend still only displayed the immediate upload/task response and did not show a durable task history.

## What changed
- Added a task history section to the static frontend at `/app/`.
- Added a refresh button that calls `GET /tasks?limit=5&offset=0` with `X-API-Key`.
- Rendered `page.items` into task rows and rendered `count`, `limit`, and `offset` as page metadata.
- Reused `parseJsonResponse()` as the frontend error boundary for non-2xx responses.
- Refreshed task history after uploading a file and creating a summary task.
- Added lesson 0027 and reference 0027 under the new course quality standard.

## Key insight
An API response shape is a contract between backend and frontend. Once `GET /tasks` returns an envelope, the frontend must treat `items` as the task array and the other fields as UI metadata.

## Retrieval prompts
- Why does the frontend read `page.items` instead of iterating over `page`?
- Why does `fetch` code still need to check `response.ok`?
- What UI information can be built from `count`, `limit`, and `offset`?
- Why should a refresh clear old DOM nodes before appending new task rows?

## Next possible step
Turn `limit`, `offset`, and `status` into visible frontend controls for pagination and status filtering.

