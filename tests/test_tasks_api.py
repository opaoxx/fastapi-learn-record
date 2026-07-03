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


def test_list_summary_tasks_supports_limit_and_offset() -> None:
    with TestClient(app) as client:
        for index in range(3):
            created = client.post(
                "/tasks/summaries",
                headers=API_KEY_HEADERS,
                json={
                    "text": f"Pagination example task number {index} has enough text to be accepted."
                },
            )
            assert created.status_code == 202

        first_page = client.get("/tasks?limit=1&offset=0", headers=API_KEY_HEADERS)
        second_page = client.get("/tasks?limit=1&offset=1", headers=API_KEY_HEADERS)

    assert first_page.status_code == 200
    assert second_page.status_code == 200
    assert first_page.json()["limit"] == 1
    assert first_page.json()["offset"] == 0
    assert first_page.json()["count"] >= 3
    assert len(first_page.json()["items"]) == 1
    assert len(second_page.json()["items"]) == 1
    assert first_page.json()["items"][0]["id"] != second_page.json()["items"][0]["id"]


def test_list_summary_tasks_returns_response_envelope_contract() -> None:
    with TestClient(app) as client:
        response = client.get("/tasks?limit=5&offset=0", headers=API_KEY_HEADERS)

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert set(payload) == {"items", "count", "limit", "offset"}
    assert isinstance(payload["items"], list)
    assert isinstance(payload["count"], int)
    assert isinstance(payload["limit"], int)
    assert isinstance(payload["offset"], int)


def test_list_summary_tasks_supports_status_filter() -> None:
    with TestClient(app) as client:
        created = client.post(
            "/tasks/summaries",
            headers=API_KEY_HEADERS,
            json={
                "text": "This task should complete so the status filter can find completed records."
            },
        )
        assert created.status_code == 202

        completed = client.get("/tasks?status=completed&limit=10", headers=API_KEY_HEADERS)
        invalid = client.get("/tasks?status=unknown", headers=API_KEY_HEADERS)

    assert completed.status_code == 200
    assert completed.json()["count"] >= 1
    assert completed.json()["limit"] == 10
    assert completed.json()["offset"] == 0
    assert any(task["id"] == created.json()["id"] for task in completed.json()["items"])
    assert all(task["status"] == "completed" for task in completed.json()["items"])
    assert invalid.status_code == 422


def test_list_summary_tasks_count_respects_status_filter() -> None:
    with TestClient(app) as client:
        completed_task = client.post(
            "/tasks/summaries",
            headers=API_KEY_HEADERS,
            json={
                "text": "This task should be completed and counted by the completed task filter."
            },
        )
        failed_task = client.post(
            "/tasks/summaries",
            headers=API_KEY_HEADERS,
            json={
                "text": "This task should simulate-ai-failure and be counted by the failed filter."
            },
        )
        assert completed_task.status_code == 202
        assert failed_task.status_code == 202

        completed = client.get("/tasks?status=completed&limit=100", headers=API_KEY_HEADERS)
        failed = client.get("/tasks?status=failed&limit=100", headers=API_KEY_HEADERS)

    assert completed.status_code == 200
    assert failed.status_code == 200
    assert completed.json()["count"] >= len(completed.json()["items"])
    assert failed.json()["count"] >= len(failed.json()["items"])
    assert all(task["status"] == "completed" for task in completed.json()["items"])
    assert all(task["status"] == "failed" for task in failed.json()["items"])
    assert any(task["id"] == completed_task.json()["id"] for task in completed.json()["items"])
    assert any(task["id"] == failed_task.json()["id"] for task in failed.json()["items"])
