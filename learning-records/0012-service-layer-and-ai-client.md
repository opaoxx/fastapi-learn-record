# Learning Record 0012: Service Layer and AI Client

## Date
2026-07-03

## Context
The project now has routers, database-backed CRUD, protected task endpoints, upload APIs, and a static frontend. Route handlers were beginning to hold too much business logic. The learner's long-term goal includes AI service APIs, so the project needs a shape where model calls can be replaced without rewriting HTTP routes.

## What changed
- Added `first_api/services/summary_tasks.py` for task creation, reading, listing, and execution.
- Added `first_api/services/ai_clients.py` with `DemoAIClient` and `PredictionResult`.
- Refactored `/predict` to receive an AI client with `Depends(get_ai_client)`.
- Refactored background summary execution to call the AI client through the service layer.
- Added a dependency-override test for the AI client.
- Added lessons 0019 and 0020 plus matching quick-reference pages.

## Key insight
Router functions should mainly handle HTTP concerns. Business actions belong in services. Model-like behavior belongs behind a client object so the demo implementation can later be replaced by a real LLM/VLM client while keeping API contracts stable.

## Retrieval prompts
- What should stay in a router function?
- What belongs in a service function?
- Why is `PredictionResult` not the same as `PredictionResponse`?
- How does `app.dependency_overrides` help test model-backed endpoints?

## Next possible step
Introduce richer error handling for model-client failures, including timeout-style errors and a stable error response contract.
