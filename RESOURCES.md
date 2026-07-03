# FastAPI Resources

## Knowledge

- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
  Official tutorial. Use for installation, first app setup, request models, response models, and the main learning path.
- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
  Official first endpoint explanation. Use for the mental model of app instance, path operation decorator, and path operation function.
- [FastAPI Concurrency and async / await](https://fastapi.tiangolo.com/async/)
  Official explanation of async path operation functions, concurrency, parallelism, and when to use `async def`.
- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
  Official guide to dynamic URL segments. Use when moving from fixed routes to item-specific routes.
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
  Official guide to query parameters and defaults. Use when teaching list filtering and search-like endpoints.
- [FastAPI Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
  Official guide to `Query` validation, aliases, deprecation, and schema inclusion. Use when teaching bounds such as `limit >= 1`, optional query parameters, and compatibility-aware parameter changes.
- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
  Official guide to receiving JSON request bodies with Pydantic models. Use for POST endpoints and AI-service inputs.
- [FastAPI Body - Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
  Official guide to field-level validation and JSON Schema metadata. Use for request validation rules.
- [Pydantic Models](https://pydantic.dev/docs/validation/latest/concepts/models/)
  Official Pydantic model concept guide. Use for explaining BaseModel, validation, model methods, and data conversion.
- [Pydantic Fields](https://pydantic.dev/docs/validation/latest/concepts/fields/)
  Official Pydantic field concept guide. Use for explaining Field, defaults, constraints, and schema metadata.
- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
  Official guide to response validation and filtering. Use when designing API contracts for frontend and AI-service consumers.
- [FastAPI Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)
  Official guide to API metadata, tag metadata, OpenAPI URL, and docs URLs. Use when teaching OpenAPI as an API contract.
- [FastAPI Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)
  Official guide to path operation summaries, descriptions, response descriptions, and deprecation metadata. Use when improving generated API documentation.
- [FastAPI Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/)
  Official guide to adding extra response metadata to OpenAPI. Use when documenting non-200 responses and model-backed error shapes.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
  Official OpenAPI specification. Use when explaining OpenAPI as a machine-readable API description format.
- [Google AIP-180: Backwards Compatibility](https://google.aip.dev/180)
  Google API design guidance for compatible and incompatible API changes. Use when teaching API schema evolution.
- [Google AIP-185: API Versioning](https://google.aip.dev/185)
  Google API design guidance for versioning. Use when teaching when compatibility breaks require a new version.
- [Semantic Versioning 2.0.0](https://semver.org/)
  Official SemVer specification. Use as a simple vocabulary for patch, minor, and major compatibility thinking.
- [FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
  Official guide to HTTPException and error responses. Use when teaching 404 and business-level API errors.
- [FastAPI Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
  Official guide to APIRouter and multi-file project structure. Use when teaching project organization.
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
  Official guide to dependency injection. Use when teaching Depends, shared logic, database sessions, auth, and reusable request setup.
- [FastAPI Classes as Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/)
  Official guide to class-based dependencies. Use when teaching grouped query parameters and reusable dependency objects.
- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
  Official guide to SQL databases with SQLModel. Use when teaching SQLite, SQLModel, sessions, and CRUD.
- [FastAPI Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)
  Official guide to dependencies that clean up resources. Use when teaching database session dependencies.
- [SQLModel Simple Hero API](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/)
  Official SQLModel FastAPI tutorial. Use when reinforcing table models and database-backed API endpoints.
- [SQLModel Limit and Offset](https://sqlmodel.tiangolo.com/tutorial/fastapi/limit-and-offset/)
  Official SQLModel pagination tutorial. Use when teaching `offset()` and `limit()` on database-backed list endpoints.
- [SQLAlchemy SQL Functions](https://docs.sqlalchemy.org/en/latest/core/functions.html)
  Official SQLAlchemy reference for `func`. Use when teaching count queries such as `select(func.count())`.
- [SQLModel Update Data with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/update/)
  Official SQLModel update tutorial. Use when teaching PATCH-style partial updates and update models.
- [SQLModel Delete Data with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/delete/)
  Official SQLModel delete tutorial. Use when teaching DELETE endpoints and 204 responses.
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
  Official guide to TestClient and pytest. Use when teaching automated API tests.
- [FastAPI Testing Dependencies with Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
  Official guide to app.dependency_overrides. Use when teaching test databases, mocked services, and replacing dependencies.
- [FastAPI Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)
  Official guide to application startup and shutdown with async context managers. Use when teaching long-lived resource lifecycle.
- [Python typing.Protocol specification](https://typing.python.org/en/latest/spec/protocol.html)
  Official typing specification for protocols and structural subtyping. Use when teaching replaceable service interfaces.
- [FastAPI Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)
  Official guide to Pydantic Settings in FastAPI. Use when teaching application configuration and environment variables.
- [Pydantic Settings](https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/)
  Official pydantic-settings concept guide. Use when teaching BaseSettings, env_prefix, and .env loading.
- [FastAPI Security Tools](https://fastapi.tiangolo.com/reference/security/)
  Official reference for API key security helpers. Use when teaching APIKeyHeader and OpenAPI integration.
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
  Official overview of FastAPI security schemes. Use when comparing API keys, bearer tokens, and OAuth2.
- [FastAPI Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/)
  Official guide to reading request headers. Use when teaching X-API-Key and other header-based metadata.
- [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  Official guide to BackgroundTasks. Use when teaching post-response work and lightweight asynchronous patterns.
- [FastAPI BackgroundTasks Reference](https://fastapi.tiangolo.com/reference/background/)
  Official API reference for BackgroundTasks. Use for exact class behavior and method names.
- [MDN 202 Accepted](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/202)
  HTTP reference for 202 semantics. Use when explaining task submission responses.
- [MDN 503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/503)
  HTTP reference for temporary service unavailability. Use when explaining model-client outages, timeouts, and retryable AI-service failures.
- [FastAPI Request Files](https://fastapi.tiangolo.com/tutorial/request-files/)
  Official guide to File, bytes, and UploadFile. Use when teaching file upload endpoints.
- [FastAPI Request Forms and Files](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/)
  Official guide to receiving files and form data together. Use when teaching multipart/form-data.
- [FastAPI UploadFile Reference](https://fastapi.tiangolo.com/reference/uploadfile/)
  Official UploadFile class reference. Use when explaining filename, content_type, and async read.
- [FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/)
  Official guide to Cross-Origin Resource Sharing. Use when teaching browser frontends, origins, preflight requests, and CORSMiddleware.
- [FastAPI Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
  Official guide to middleware. Use when explaining application-wide request/response processing such as CORS.
- [FastAPI Static Files](https://fastapi.tiangolo.com/tutorial/static-files/)
  Official guide to StaticFiles and mounted static applications. Use when teaching simple frontend pages served by FastAPI.
- [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
  Official browser API documentation for `fetch`, `Request`, and `Response`. Use when teaching browser-to-API calls.
- [MDN Response.json()](https://developer.mozilla.org/en-US/docs/Web/API/Response/json)
  Official documentation for parsing response bodies into JavaScript objects. Use when teaching JSON response handling.
- [MDN Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
  Official DOM documentation for creating elements. Use when teaching dynamic UI rendering without a framework.
- [MDN Element.append()](https://developer.mozilla.org/en-US/docs/Web/API/Element/append)
  Official DOM documentation for appending nodes and strings. Use when teaching small vanilla-JavaScript render functions.
- [MDN URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
  Official Web API documentation for building and manipulating query strings. Use when teaching frontend controls that call query-parameter APIs.
- [MDN HTMLElement.dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
  Official DOM documentation for reading `data-*` attributes from elements. Use when teaching filter buttons backed by data attributes.
- [MDN Button Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
  Official HTML reference for buttons. Use when teaching clickable controls and explicit `type="button"` behavior.
- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)
  Official Python standard-library documentation. Use when teaching small internal data result objects such as `PredictionResult`.
- [Python typing](https://docs.python.org/3/library/typing.html)
  Official Python typing documentation. Use when teaching `Literal`, type aliases, and typed service boundaries.
- [Python asyncio Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
  Official asyncio documentation for coroutines, tasks, cooperative scheduling, and `asyncio.sleep`.
- [Python asyncio Conceptual Overview](https://docs.python.org/3/howto/a-conceptual-overview-of-asyncio.html)
  Official conceptual guide to asyncio. Use when teaching event loops and non-blocking waiting.
- [Python logging](https://docs.python.org/3/library/logging.html)
  Official Python logging module documentation. Use when teaching application logs, structured context with `extra`, and failure diagnostics.
- [Python time](https://docs.python.org/3/library/time.html)
  Official Python time module documentation. Use when teaching elapsed-time measurement with monotonic performance timers.
- [HTTPX Timeouts](https://www.python-httpx.org/advanced/timeouts/)
  Official HTTPX guide to timeout behavior. Use when teaching external provider calls and failure boundaries.
- [HTTPX Async Support](https://www.python-httpx.org/async/)
  Official HTTPX guide to AsyncClient usage. Use when teaching async external HTTP provider adapters.
- [HTTPX QuickStart](https://www.python-httpx.org/quickstart/)
  Official HTTPX quickstart for common request methods and sending POST data. Use when teaching provider adapter request payloads.
- [HTTPX Clients](https://www.python-httpx.org/advanced/clients/)
  Official HTTPX guide to client instances and connection pooling. Use when teaching long-lived HTTP clients.
- [HTTPX Exceptions](https://www.python-httpx.org/exceptions/)
  Official HTTPX exception hierarchy. Use when teaching provider error mapping.
- [HTTPX Transports](https://www.python-httpx.org/advanced/transports/)
  Official HTTPX guide to transports and connection retries. Use when introducing cautious retry behavior for external dependencies.
- [Uvicorn Documentation](https://uvicorn.dev/)
  ASGI server documentation. Use when learning what actually runs the FastAPI app locally or in production.
- [FastAPI Response Headers](https://fastapi.tiangolo.com/advanced/response-headers/)
  Official FastAPI guide to setting response headers while still using response models. Use when teaching lightweight request observability.
- [pytest Logging](https://docs.pytest.org/en/stable/how-to/logging.html)
  Official pytest guide to capturing and asserting logs with `caplog`.
- [Starlette Applications](https://starlette.dev/applications/)
  Starlette documentation for application state. Use when teaching `app.state` in FastAPI.

## Wisdom (Communities)

- [FastAPI GitHub Discussions](https://github.com/fastapi/fastapi/discussions)
  Maintainer-adjacent community for real-world questions and design tradeoffs.
- [FastAPI GitHub Issues](https://github.com/fastapi/fastapi/issues)
  Use carefully for bug reports and edge cases after checking the official docs first.
- [Stack Overflow: fastapi](https://stackoverflow.com/questions/tagged/fastapi)
  Useful for practical debugging, but answers should be checked against current official docs.
