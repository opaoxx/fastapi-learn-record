from fastapi.testclient import TestClient

from first_api.main import app
from first_api.services.ai_clients import PredictionResult, get_ai_client


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


def test_predict_uses_overridable_ai_client_dependency() -> None:
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
