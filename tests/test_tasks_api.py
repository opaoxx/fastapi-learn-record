from fastapi.testclient import TestClient

from first_api.main import app


API_KEY_HEADERS = {"X-API-Key": "dev-secret-key"}


def test_summary_task_requires_api_key() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/tasks/summaries",
            json={
                "text": "This request should be rejected because it does not include the API key header."
            },
        )

    assert response.status_code == 401


def test_create_and_read_summary_task() -> None:
    with TestClient(app) as client:
        created = client.post(
            "/tasks/summaries",
            headers=API_KEY_HEADERS,
            json={
                "text": "FastAPI background tasks let an API accept work quickly and continue processing after sending the initial response."
            },
        )
        assert created.status_code == 202
        task_id = created.json()["id"]

        task = client.get(f"/tasks/{task_id}", headers=API_KEY_HEADERS)
        assert task.status_code == 200
        assert task.json()["status"] == "completed"
        assert task.json()["result"].startswith("FastAPI background tasks")


def test_missing_summary_task_returns_404() -> None:
    with TestClient(app) as client:
        response = client.get("/tasks/999999", headers=API_KEY_HEADERS)

    assert response.status_code == 404
