# Learning Record 0022: Real AI Provider Boundary

## Date
2026-07-03

## Context
The project had a demo AI client used by `/predict` and background summary tasks. The next step was to prepare the architecture for real AI providers without coupling route handlers directly to external SDKs or network behavior.

## What changed
- Added `AIClientConfig` for provider, timeout, and max-attempt configuration.
- Added an `AIClient` Protocol to describe the project-level AI client boundary.
- Updated `DemoAIClient` to carry configuration.
- Added AI provider settings and `.env.example` entries.
- Updated prediction and summary code to depend on `AIClient` rather than `DemoAIClient`.
- Added a test that verifies provider configuration stays inside the AI client boundary.
- Added lesson 0031 and reference 0031.

## Key insight
External AI providers are unreliable dependencies. FastAPI route handlers should depend on a stable internal protocol, while provider adapters handle request translation, response parsing, timeout, retry decisions, and error mapping.

## Retrieval prompts
- Why should a router depend on `AIClient` instead of `DemoAIClient`?
- What belongs in an AI provider boundary?
- Why should automated tests use dependency overrides instead of calling the real model?
- What failure types should a real provider adapter map to stable internal errors?

## Next possible step
Teach FastAPI async basics: waiting efficiently, event loop behavior, and the difference between async I/O and blocking work.
