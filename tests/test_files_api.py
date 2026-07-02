from fastapi.testclient import TestClient

from first_api.main import app


API_KEY_HEADERS = {"X-API-Key": "dev-secret-key"}


def test_upload_text_file_and_create_summary_task() -> None:
    with TestClient(app) as client:
        uploaded = client.post(
            "/files/text",
            headers=API_KEY_HEADERS,
            files={
                "file": (
                    "notes.txt",
                    b"FastAPI UploadFile receives files as multipart form data and can feed AI processing tasks.",
                    "text/plain",
                )
            },
        )
        assert uploaded.status_code == 201
        file_id = uploaded.json()["id"]
        assert uploaded.json()["filename"] == "notes.txt"
        assert "FastAPI UploadFile" in uploaded.json()["preview"]

        created_task = client.post(
            f"/tasks/files/{file_id}/summary",
            headers=API_KEY_HEADERS,
        )
        assert created_task.status_code == 202
        assert created_task.json()["source_file_id"] == file_id

        task_id = created_task.json()["id"]
        task = client.get(f"/tasks/{task_id}", headers=API_KEY_HEADERS)
        assert task.status_code == 200
        assert task.json()["status"] == "completed"


def test_upload_requires_txt_file() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/files/text",
            headers=API_KEY_HEADERS,
            files={"file": ("notes.md", b"not accepted", "text/markdown")},
        )

    assert response.status_code == 422


def test_upload_requires_api_key() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/files/text",
            files={"file": ("notes.txt", b"missing key", "text/plain")},
        )

    assert response.status_code == 401
