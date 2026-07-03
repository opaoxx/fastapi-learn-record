import asyncio

import httpx

from first_api.services.ai_clients import AIClientConfig, DemoAIClient
from first_api.services.predictions import PredictionServiceError, run_prediction
from first_api.settings import Settings


def test_run_prediction_uses_demo_backend() -> None:
    async def run() -> object:
        provider_client = httpx.AsyncClient(transport=httpx.MockTransport(lambda request: httpx.Response(500)))
        try:
            return await run_prediction(
                text="FastAPI is great and pleasant.",
                mode="fast",
                settings=Settings(ai_prediction_backend="demo"),
                ai_client=DemoAIClient(config=AIClientConfig(provider="demo")),
                provider_http_client=provider_client,
            )
        finally:
            await provider_client.aclose()

    result = asyncio.run(run())

    assert result.backend == "demo"
    assert result.prediction.source == "demo-ai-client"
    assert result.elapsed_ms >= 0


def test_run_prediction_wraps_provider_errors_with_backend_and_elapsed_time() -> None:
    async def run() -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(status_code=503, request=request)

        provider_client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
        try:
            await run_prediction(
                text="FastAPI is great and pleasant.",
                mode="fast",
                settings=Settings(ai_prediction_backend="provider"),
                ai_client=DemoAIClient(config=AIClientConfig(provider="demo")),
                provider_http_client=provider_client,
            )
        finally:
            await provider_client.aclose()

    try:
        asyncio.run(run())
    except PredictionServiceError as exc:
        error = exc
    else:
        raise AssertionError("Expected PredictionServiceError")

    assert error.backend == "provider"
    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."
    assert error.elapsed_ms >= 0
