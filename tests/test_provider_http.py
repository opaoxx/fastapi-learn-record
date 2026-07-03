import asyncio
import json

import httpx

from first_api.services.ai_clients import AIClientConfig, AIClientError
from first_api.services.provider_http import check_provider_health, request_provider_prediction


def run_async_health_check(client: httpx.AsyncClient) -> object:
    return asyncio.run(
        check_provider_health(
            url="https://provider.test/health",
            config=AIClientConfig(
                provider="demo",
                timeout_seconds=0.5,
                max_attempts=1,
            ),
            client=client,
        )
    )


def run_async_prediction(client: httpx.AsyncClient) -> object:
    return asyncio.run(
        request_provider_prediction(
            url="https://provider.test/predict",
            text="FastAPI is great and pleasant.",
            mode="careful",
            config=AIClientConfig(
                provider="demo",
                timeout_seconds=0.5,
                max_attempts=1,
            ),
            client=client,
        )
    )


def test_check_provider_health_returns_internal_result_for_success() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json={"status": "ok"}, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_health_check(client)
    finally:
        asyncio.run(client.aclose())

    assert result.ok is True
    assert result.provider == "demo"
    assert result.status_code == 200
    assert result.message == "The AI provider responded successfully."


def test_check_provider_health_maps_timeout_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("Read timed out.", request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_health_check(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_timeout"
    assert error.message == "The AI provider health check timed out."


def test_check_provider_health_maps_http_error_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=503, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_health_check(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."


def test_request_provider_prediction_sends_payload_and_maps_response() -> None:
    captured_request_body = {}

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal captured_request_body
        captured_request_body = json.loads(request.content)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.876},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client)
    finally:
        asyncio.run(client.aclose())

    assert captured_request_body == {
        "text": "FastAPI is great and pleasant.",
        "mode": "careful",
    }
    assert result.label == "positive"
    assert result.score == 0.88
    assert result.source == "demo-provider"


def test_request_provider_prediction_maps_invalid_json_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "confused", "score": 1.5},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_invalid_response"
    assert error.message == "The AI provider returned an invalid prediction response."


def test_request_provider_prediction_maps_provider_http_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=503, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."
