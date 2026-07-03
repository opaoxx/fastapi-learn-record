from fastapi.testclient import TestClient

from first_api.main import app


def test_openapi_documents_task_list_contract() -> None:
    with TestClient(app) as client:
        response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()

    operation = schema["paths"]["/tasks"]["get"]
    assert operation["tags"] == ["tasks"]
    assert operation["summary"] == "List summary tasks"
    assert operation["responses"]["200"]["description"] == "A paginated task-list response envelope."
    assert operation["responses"]["200"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/SummaryTaskListResponse"
    }
    assert operation["security"] == [{"ApiKeyAuth": []}]

    parameters = {parameter["name"]: parameter for parameter in operation["parameters"]}
    assert parameters["status"]["in"] == "query"
    assert parameters["status"]["schema"]["anyOf"][0]["enum"] == [
        "queued",
        "running",
        "completed",
        "failed",
    ]
    assert parameters["limit"]["schema"]["maximum"] == 100
    assert parameters["limit"]["schema"]["minimum"] == 1
    assert parameters["offset"]["schema"]["minimum"] == 0


def test_openapi_documents_api_key_security_scheme() -> None:
    with TestClient(app) as client:
        response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()

    security_scheme = schema["components"]["securitySchemes"]["ApiKeyAuth"]
    assert security_scheme["type"] == "apiKey"
    assert security_scheme["in"] == "header"
    assert security_scheme["name"] == "X-API-Key"
