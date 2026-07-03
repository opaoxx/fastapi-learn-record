from fastapi.testclient import TestClient

from first_api.main import app


def test_cors_preflight_allows_local_frontend_origin() -> None:
    with TestClient(app) as client:
        response = client.options(
            "/files/text",
            headers={
                "Origin": "http://127.0.0.1:5500",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "X-API-Key",
            },
        )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://127.0.0.1:5500"
    assert "POST" in response.headers["access-control-allow-methods"]


def test_static_frontend_page_is_served() -> None:
    with TestClient(app) as client:
        response = client.get("/app/")

    assert response.status_code == 200
    assert "文件摘要工作台" in response.text
    assert "任务历史" in response.text
    assert "状态筛选" in response.text
    assert "history-previous" in response.text
    assert "history-next" in response.text
    assert "URLSearchParams" in response.text
