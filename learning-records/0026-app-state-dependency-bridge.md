# Learning Record 0026: App State Dependency Bridge

## Context

After learning to create a lifespan-managed `httpx.AsyncClient`, the project still exposed the client by reading `request.app.state.provider_http_client` directly inside a route. That works, but it spreads the resource storage detail into endpoint code.

## Decision

Introduce `get_provider_http_client(request: Request) -> httpx.AsyncClient` in `first_api/dependencies.py`, and inject it into the system route with `Depends`.

## Key Insight

The important design distinction is resource ownership versus resource usage:

- `lifespan` owns the long-lived resource lifecycle.
- `app.state` stores the application-level resource.
- `Depends` exposes the resource to route functions.
- Endpoint code should use the resource without owning its lifecycle or knowing too much about where it is stored.

## Project Change

- Added `get_provider_http_client()` as a dependency bridge from `Request` to `app.state`.
- Updated `GET /provider/http-client` to receive the `httpx.AsyncClient` through dependency injection.
- Added a test proving `app.dependency_overrides` can replace the provider HTTP client dependency.
- Added Lesson 0035 and Reference 0035.

## Why It Matters

This pattern prepares the project for real AI provider integration. Future provider routes can depend on an HTTP client without creating it per request, leaking it, or directly coupling every route to `app.state`.

## Next Step

Connect `check_provider_health()` to a FastAPI endpoint, using the dependency-injected HTTP client and test doubles for provider success and failure paths.
