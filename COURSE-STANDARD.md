# FastAPI Course Standard

## Purpose

This course is not only a sequence of code changes. It should help the learner understand why a backend API is designed this way, how FastAPI implements the idea, and how to verify the behavior in a real project.

From lesson 0027 onward, every lesson should be written as a small but serious technical article: concept first, mechanism second, code third, experiment last.

## Lesson Depth Contract

Each new lesson should include these parts unless the lesson is intentionally tiny:

1. Learning goals
   - State the concrete skill the learner will gain.
   - State the conceptual question the lesson answers.

2. Background and motivation
   - Explain what problem appears in real backend or AI-service projects.
   - Explain why the previous project state is not enough.
   - Connect the topic to the long-term mission: backend API, AI service endpoint, interview-ready project.

3. Core concepts
   - Define new terms before using them heavily.
   - Explain the mental model, not only the syntax.
   - Use analogies only when they reduce confusion; always return to the technical definition.

4. Mechanism
   - Describe the runtime flow step by step.
   - For FastAPI topics, explain how request parsing, dependency injection, validation, response serialization, routing, middleware, or background work participates.
   - For database topics, explain query shape, transaction/session behavior, persistence, and result shape.
   - For frontend/API integration topics, explain browser behavior, HTTP request shape, JSON contract, and UI state.

5. Code reading
   - Show the important code in context.
   - Read the code line by line or block by block.
   - Explain why this design was chosen and what would break if it were changed carelessly.

6. Hands-on implementation
   - Make a small, runnable project change.
   - Keep the implementation tied to the existing project.
   - Avoid unrelated refactors.

7. Experiments and observations
   - Provide at least one concrete request, browser action, or test command.
   - Ask the learner to observe status code, JSON shape, database effect, or UI behavior.
   - Include expected output or expected behavior.

8. Common mistakes
   - List beginner-level traps and how to diagnose them.
   - Include common FastAPI/Pydantic/SQLModel/frontend errors when relevant.

9. Retrieval practice
   - Add a short quiz.
   - Questions should test understanding, not only memory.
   - Answers can be hidden with `<details>` in lesson HTML.

10. Summary and next step
    - End with what changed in the learner's mental model.
    - Link to previous lesson, next lesson, course index, and quick reference.
    - Recommend primary sources from official documentation where possible.

## Two-Lesson Batch Rule

Two-lesson batches are allowed, but the batch must still preserve depth.

Preferred pattern:

- Lesson A: principle and backend/API contract.
- Lesson B: application, UI/test integration, or production-style hardening.

Avoid making two shallow lessons just to move faster. If the topic is dense, one deep lesson is better than two thin ones.

## Reference Page Contract

Each reference page should be a compressed tool, not a second long article.

It should include:

- Key mental model.
- Minimal syntax.
- Parameter or field table.
- Common mistakes.
- One or two canonical examples.
- Links back to the lesson and course index.

## Quality Checklist Before Finishing a Lesson

- Does the lesson explain why the topic matters?
- Are new terms defined before they are used?
- Is the runtime or data flow visible?
- Is there enough principle to answer interview-style "why" questions?
- Is the code connected to the principle?
- Is there at least one runnable experiment?
- Are beginner mistakes included?
- Are navigation links complete?
- Are official or primary resources linked?
- Did tests or link checks run when code or pages changed?

## Immediate Course Plan

The next stage should slow down slightly and deepen the browser/API integration track:

1. Lesson 0027: Frontend Task History
   - Principle: UI state is a projection of an API contract.
   - Mechanism: `fetch`, headers, response envelope, DOM rendering, and failure display.
   - Code: render `/tasks` history from `items`, `count`, `limit`, and `offset`.

2. Lesson 0028: Frontend Pagination and Status Filtering
   - Principle: pagination and filtering are shared state between URL query parameters and UI controls.
   - Mechanism: `status`, `limit`, `offset`, disabled buttons, reset-on-filter-change.
   - Code: add status controls and previous/next page controls.

3. Lesson 0029: OpenAPI as API Contract
   - Principle: FastAPI's automatic docs are generated from type hints, Pydantic models, routes, and response models.
   - Mechanism: how `/docs` and `/openapi.json` reflect the backend contract.
   - Code: inspect and improve summaries, tags, descriptions, and error responses.

4. Lesson 0030: Schema Evolution and Backward Compatibility
   - Principle: changing JSON shape is a contract change, not only a code change.
   - Mechanism: compatibility, versioning, migration, tests as contract guards.
   - Code: compare old bare-list response and new envelope response.

5. Lesson 0031: Real AI Provider Boundary
   - Principle: external AI calls are unreliable dependencies and should live behind a stable interface.
   - Mechanism: timeout, retry boundary, error mapping, fake client for tests.
   - Code: prepare the demo AI client interface for a future real provider.

6. Lesson 0032: Async Basics for FastAPI
   - Principle: async is about waiting efficiently, not making CPU work faster.
   - Mechanism: event loop, `async def`, blocking calls, sync database caveat.
   - Code: compare a small async route with existing sync routes.

