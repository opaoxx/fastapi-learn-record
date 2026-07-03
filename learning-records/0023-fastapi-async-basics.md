# Learning Record 0023: FastAPI Async Basics

## Date
2026-07-03

## Context
After introducing the AI provider boundary, the next step was to understand the async model needed for external HTTP calls and other waiting-heavy operations.

## What changed
- Added `AsyncWaitResponse`.
- Added `GET /async/wait`, an async teaching endpoint that awaits `asyncio.sleep`.
- Added tests for async wait response shape and query parameter validation.
- Added lesson 0032 and reference 0032.

## Key insight
Async is about waiting efficiently, not making CPU work faster. `await` lets a coroutine pause and return control to the event loop while waiting for I/O. Synchronous blocking calls inside an async endpoint still block.

## Retrieval prompts
- Why does `await asyncio.sleep()` not block in the same way as `time.sleep()`?
- When should a FastAPI path operation be `async def`?
- Why does wrapping synchronous SQLModel code in `async def` not make the database layer asynchronous?
- What is the difference between concurrency and parallelism?

## Next possible step
Teach async external HTTP clients and connect the AI provider boundary to timeout-aware provider adapters.
