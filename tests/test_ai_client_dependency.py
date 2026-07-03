import asyncio
import logging

import httpx
from fastapi.testclient import TestClient

from first_api.dependencies import get_provider_http_client
from first_api.main import app
from first_api.services.ai_clients import AIClientConfig, AIClientError, DemoAIClient, PredictionResult, get_ai_client
from first_api.settings import Settings, get_settings


PREDICTIONS_LOGGER = "first_api.routers.predictions"


class FixedAIClient:
    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
        return PredictionResult(
            label="positive",
            score=0.99,
            source="fixed-test-client",
        )

    def summarize(self, text: str) -> str:
        return "fixed summary"


def override_ai_client() -> FixedAIClient:
    return FixedAIClient()


class FailingAIClient:
    def predict_sentiment(self, text: str, mode: str) -> PredictionResult:
        raise AIClientError(
            message="The test AI client is unavailable.",
            error_code="test_ai_unavailable",
        )

    def summarize(self, text: str) -> str:
        return "unreachable"


def override_failing_ai_client() -> FailingAIClient:
    return FailingAIClient()


def test_predict_uses_overridable_ai_client_dependency(caplog) -> None:
    caplog.set_level(logging.INFO, logger=PREDICTIONS_LOGGER)
    app.dependency_overrides[get_ai_client] = override_ai_client
    try:
        with TestClient(app) as client:
            response = client.post(
                "/predict",
                json={
                    "text": "This sentence is intentionally controlled by a test client.",
                    "mode": "fast",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json()["label"] == "positive"
    assert response.json()["score"] == 0.99
    assert response.json()["source"] == "fixed-test-client"
    assert response.headers["x-prediction-backend"] == "demo"
    assert response.headers["x-prediction-source"] == "fixed-test-client"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0

    log_record = next(record for record in caplog.records if record.message == "prediction_completed")
    assert log_record.prediction_backend == "demo"
    assert log_record.prediction_source == "fixed-test-client"


def test_demo_ai_client_keeps_provider_configuration_at_boundary() -> None:
    ai_client = DemoAIClient(
        config=AIClientConfig(
            provider="demo",
            timeout_seconds=2.5,
            max_attempts=2,
        )
    )

    prediction = ai_client.predict_sentiment("FastAPI is pleasant and nice.", mode="fast")

    assert prediction.source == "demo-ai-client"
    assert ai_client.config.timeout_seconds == 2.5
    assert ai_client.config.max_attempts == 2


def test_predict_returns_stable_error_when_ai_client_fails() -> None:
    app.dependency_overrides[get_ai_client] = override_failing_ai_client
    try:
        with TestClient(app) as client:
            response = client.post(
                "/predict",
                json={
                    "text": "This sentence triggers a controlled AI client failure.",
                    "mode": "fast",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 503
    assert response.headers["x-prediction-backend"] == "demo"
    assert response.headers["x-prediction-error-code"] == "test_ai_unavailable"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0
    assert response.json() == {
        "detail": {
            "error_code": "test_ai_unavailable",
            "message": "The test AI client is unavailable.",
        }
    }


def test_provider_predict_endpoint_uses_provider_adapter() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.873},
            request=request,
        )

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.post(
                "/provider/predict",
                json={
                    "text": "FastAPI is great and pleasant.",
                    "mode": "careful",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 200
    assert response.headers["x-prediction-backend"] == "provider"
    assert response.headers["x-prediction-source"] == "demo-provider"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0
    assert response.json() == {
        "label": "positive",
        "score": 0.87,
        "source": "demo-provider",
        "text_length": 30,
    }


def test_provider_predict_endpoint_maps_provider_errors_to_503() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "confused", "score": 1.5},
            request=request,
        )

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.post(
                "/provider/predict",
                json={
                    "text": "FastAPI is great and pleasant.",
                    "mode": "careful",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 503
    assert response.headers["x-prediction-backend"] == "provider"
    assert response.headers["x-prediction-error-code"] == "ai_provider_invalid_response"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0
    assert response.json() == {
        "detail": {
            "error_code": "ai_provider_invalid_response",
            "message": "The AI provider returned an invalid prediction response.",
        }
    }


def test_predict_can_switch_to_provider_backend() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.914},
            request=request,
        )

    def override_provider_settings() -> Settings:
        return Settings(ai_prediction_backend="provider")

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_settings] = override_provider_settings
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.post(
                "/predict",
                json={
                    "text": "FastAPI is great and pleasant.",
                    "mode": "careful",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 200
    assert response.headers["x-prediction-backend"] == "provider"
    assert response.headers["x-prediction-source"] == "demo-provider"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0
    assert response.json() == {
        "label": "positive",
        "score": 0.91,
        "source": "demo-provider",
        "text_length": 30,
    }


def test_predict_provider_backend_maps_provider_errors_to_503() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=503, request=request)

    def override_provider_settings() -> Settings:
        return Settings(ai_prediction_backend="provider")

    replacement_client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        trust_env=False,
    )
    app.dependency_overrides[get_settings] = override_provider_settings
    app.dependency_overrides[get_provider_http_client] = lambda: replacement_client

    try:
        with TestClient(app) as client:
            response = client.post(
                "/predict",
                json={
                    "text": "FastAPI is great and pleasant.",
                    "mode": "careful",
                    "temperature": 0.2,
                },
            )
    finally:
        app.dependency_overrides.clear()
        asyncio.run(replacement_client.aclose())

    assert response.status_code == 503
    assert response.headers["x-prediction-backend"] == "provider"
    assert response.headers["x-prediction-error-code"] == "ai_provider_http_error"
    assert float(response.headers["x-prediction-elapsed-ms"]) >= 0
    assert response.json() == {
        "detail": {
            "error_code": "ai_provider_http_error",
            "message": "The AI provider returned HTTP 503.",
        }
    }
