# Learning Record 0011: CORS and Static Frontend

## Date
2026-07-03

## Context
The learner has completed API basics, database-backed CRUD, protected endpoints, background summary tasks, and text-file upload. The next useful step is to connect the backend to a browser frontend, because the long-term mission includes AI-service endpoints that can be called by a UI.

## What changed
- Added local CORS configuration with FastAPI `CORSMiddleware`.
- Added a static frontend served from `/app/`.
- Added browser-style tests for CORS preflight and static page serving.
- Added lessons 0017 and 0018 plus matching quick-reference pages.

## Key insight
CORS is not normal backend business logic. It is a browser-enforced access-control layer based on `origin`. API tools may call an endpoint successfully while browser JavaScript is blocked unless the backend returns the required CORS headers.

## Retrieval prompts
- What three parts make up an origin?
- Why does `X-API-Key` usually trigger a CORS preflight request?
- Why should a frontend file upload use `FormData` instead of raw JSON?
- What is the difference between `StaticFiles` and `APIRouter`?

## Next possible step
Introduce service-layer functions so route handlers stay thin before replacing the demo summary function with a real model client.
