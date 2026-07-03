import asyncio
import json
import logging
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

import httpx

from first_api.services.ai_clients import AIClientConfig, AIClientError
from first_api.services.provider_http import (
    calculate_retry_jitter,
    calculate_retry_delay,
    check_provider_health,
    parse_retry_after_delay,
    request_provider_prediction,
)


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


def run_async_prediction(
    client: httpx.AsyncClient,
    max_attempts: int = 1,
    retry_base_delay_seconds: float = 0.0,
    retry_max_delay_seconds: float = 0.0,
    retry_jitter_seconds: float = 0.0,
    sleep: object | None = None,
    random_fraction: object | None = None,
) -> object:
    kwargs = {}
    if sleep is not None:
        kwargs["sleep"] = sleep
    if random_fraction is not None:
        kwargs["random_fraction"] = random_fraction

    return asyncio.run(
        request_provider_prediction(
            url="https://provider.test/predict",
            text="FastAPI is great and pleasant.",
            mode="careful",
            config=AIClientConfig(
                provider="demo",
                timeout_seconds=0.5,
                max_attempts=max_attempts,
                retry_base_delay_seconds=retry_base_delay_seconds,
                retry_max_delay_seconds=retry_max_delay_seconds,
                retry_jitter_seconds=retry_jitter_seconds,
            ),
            client=client,
            **kwargs,
        )
    )


def test_calculate_retry_delay_uses_exponential_backoff_with_cap() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=5,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
    )

    delays = [calculate_retry_delay(attempt, config) for attempt in range(1, 5)]

    assert delays == [1.0, 2.0, 3.0, 3.0]


def test_calculate_retry_jitter_uses_bounded_random_fraction() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    jitter = calculate_retry_jitter(config, random_fraction=lambda: 0.4)

    assert jitter == 0.2


def test_calculate_retry_delay_adds_jitter_to_local_backoff() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(attempt=2, config=config, random_fraction=lambda: 0.4)

    assert delay == 2.2


def test_calculate_retry_delay_caps_backoff_after_jitter() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=2.9,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(attempt=1, config=config, random_fraction=lambda: 1.0)

    assert delay == 3.0


def test_parse_retry_after_delay_accepts_delay_seconds() -> None:
    assert parse_retry_after_delay("5") == 5.0


def test_parse_retry_after_delay_accepts_http_date() -> None:
    now = datetime(2026, 7, 4, 12, 0, tzinfo=timezone.utc)
    retry_at = now + timedelta(seconds=7)
    retry_after = format_datetime(retry_at, usegmt=True)

    assert parse_retry_after_delay(retry_after, now=now) == 7.0


def test_calculate_retry_delay_prefers_retry_after_with_cap() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(
        attempt=1,
        config=config,
        retry_after="5",
        random_fraction=lambda: 1.0,
    )

    assert delay == 3.0


def test_calculate_retry_delay_ignores_invalid_retry_after() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(
        attempt=2,
        config=config,
        retry_after="later",
        random_fraction=lambda: 0.4,
    )

    assert delay == 2.2


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


def test_request_provider_prediction_retries_retryable_http_error_then_succeeds() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.93},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client, max_attempts=2)
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert result.label == "positive"
    assert result.score == 0.93


def test_request_provider_prediction_retries_timeout_then_succeeds() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ReadTimeout("Read timed out.", request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.91},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client, max_attempts=2)
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert result.label == "positive"
    assert result.score == 0.91


def test_request_provider_prediction_waits_between_retryable_failures() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.95},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=3,
            retry_base_delay_seconds=1.0,
            retry_max_delay_seconds=3.0,
            retry_jitter_seconds=0.0,
            sleep=fake_sleep,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 3
    assert sleep_calls == [1.0, 2.0]
    assert result.label == "positive"
    assert result.score == 0.95


def test_request_provider_prediction_uses_retry_after_header() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                status_code=429,
                headers={"Retry-After": "2"},
                request=request,
            )
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.94},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=0.1,
            retry_max_delay_seconds=5.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 1.0,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert sleep_calls == [2.0]
    assert result.label == "positive"
    assert result.score == 0.94


def test_request_provider_prediction_adds_jitter_to_local_retry_delay() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.92},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=1.0,
            retry_max_delay_seconds=3.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 0.4,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert sleep_calls == [1.2]
    assert result.label == "positive"
    assert result.score == 0.92


def test_request_provider_prediction_logs_retry_schedule_for_http_error(caplog) -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                status_code=429,
                headers={"Retry-After": "2"},
                request=request,
            )
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.96},
            request=request,
        )

    caplog.set_level(logging.INFO, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=0.1,
            retry_max_delay_seconds=5.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 1.0,
        )
    finally:
        asyncio.run(client.aclose())

    retry_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_scheduled"
    ]

    assert attempts == 2
    assert sleep_calls == [2.0]
    assert result.label == "positive"
    assert len(retry_records) == 1
    assert retry_records[0].attempt == 1
    assert retry_records[0].max_attempts == 2
    assert retry_records[0].retry_reason == "http_status"
    assert retry_records[0].status_code == 429
    assert retry_records[0].retry_after == "2"
    assert retry_records[0].delay_seconds == 2.0
    assert retry_records[0].delay_source == "retry_after"


def test_request_provider_prediction_stops_after_max_attempts(caplog) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(status_code=503, request=request)

    caplog.set_level(logging.WARNING, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    exhausted_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_exhausted"
    ]

    assert attempts == 3
    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."
    assert len(exhausted_records) == 1
    assert exhausted_records[0].attempt == 3
    assert exhausted_records[0].max_attempts == 3
    assert exhausted_records[0].retry_reason == "http_status"
    assert exhausted_records[0].status_code == 503
    assert exhausted_records[0].retry_after is None
    assert exhausted_records[0].error_code == "ai_provider_http_error"


def test_request_provider_prediction_does_not_retry_non_retryable_http_error() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(status_code=400, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert attempts == 1
    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 400."


def test_request_provider_prediction_does_not_retry_invalid_response() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(
            status_code=200,
            json={"label": "confused", "score": 1.5},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert attempts == 1
    assert error.error_code == "ai_provider_invalid_response"
