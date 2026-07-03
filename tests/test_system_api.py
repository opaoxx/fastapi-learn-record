import asyncio

import httpx
from fastapi.testclient import TestClient

from first_api.dependencies import get_provider_http_client
from first_api.main import app


def test_async_wait_endpoint_returns_wait_metadata() -> None:
    with TestClient(app) as client:
        response = client.get("/async/wait?delay=0")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "delay_seconds": 0.0,
        "message": "The endpoint awaited without doing CPU work.",
    }


def test_async_wait_endpoint_validates_delay_bounds() -> None:
    with TestClient(app) as client:
        response = client.get("/async/wait?delay=2")

    assert response.status_code == 422


def test_provider_http_client_is_created_by_lifespan() -> None:
    with TestClient(app) as client:
        response = client.get("/provider/http-client")

    assert response.status_code == 200
    assert response.json() == {
        "provider": "demo",
        "timeout_seconds": 10.0,
        "client_ready": True,
    }


def test_provider_http_client_dependency_can_be_overridden() -> None:
    replacement_client = httpx.AsyncClient(timeout=0.1, trust_env=False)
    asyncio.run(replacement_client.aclose())
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.get("/provider/http-client")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["client_ready"] is False


def test_provider_health_endpoint_uses_dependency_injected_client() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200)

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.get("/provider/health")
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 200
    assert response.json() == {
        "ok": True,
        "provider": "demo",
        "status_code": 200,
        "message": "The AI provider responded successfully.",
    }


def test_provider_health_endpoint_maps_provider_errors_to_503() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(503)

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.get("/provider/health")
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 503
    assert response.json() == {
        "detail": {
            "error_code": "ai_provider_http_error",
            "message": "The AI provider returned HTTP 503.",
        }
    }
