# Learning Record 0018: Retrofit Lessons 0022-0026

## Date
2026-07-03

## Context
The learner reported that lessons 22 through 26 were useful but too thin compared with earlier lessons. They wanted deeper principle-first explanations suitable for sharing publicly on GitHub, including for readers with weaker foundations.

## What changed
- Rewrote lessons 0022 through 0026 with stronger background, mental models, mechanism explanations, code reading, common mistakes, experiments, and retrieval practice.
- Updated references 0022 through 0026 from short code reminders into more complete quick-review sheets.
- Corrected lesson 0023 and 0024 examples to match the current response envelope shape.
- Preserved existing navigation while improving conceptual continuity from async task failure to pagination, status filtering, response envelopes, and count queries.

## Key insight
The 22-26 lesson group is one conceptual arc: asynchronous task results become queryable task records; task records need pagination and filtering; frontend pagination needs a response envelope; the envelope needs a correct count query.

## Retrieval prompts
- Why does 202 Accepted not prove a background task succeeded?
- Why should list pagination use stable ordering?
- Why should invalid status values return 422 instead of an empty list?
- Why is changing a response from a bare array to an envelope a breaking API change?
- Why does count share filters but not offset and limit?

## Next possible step
Continue with lesson 0028: frontend pagination and status filtering, now using the deeper conceptual base from lessons 0023 through 0027.

