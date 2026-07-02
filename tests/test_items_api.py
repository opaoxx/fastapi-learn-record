from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from first_api.database import get_session
from first_api.main import app
from first_api.schemas import Item


API_KEY_HEADERS = {"X-API-Key": "dev-secret-key"}


def create_test_session() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all(
            [
                Item(name="FastAPI Beginner Course", category="course", price=0, in_stock=True),
                Item(name="Python Backend Handbook", category="book", price=39.9, in_stock=True),
            ]
        )
        session.commit()
        yield session


def test_create_update_and_delete_item() -> None:
    session_generator = create_test_session()
    session = next(session_generator)

    def override_get_session() -> Generator[Session, None, None]:
        yield session

    app.dependency_overrides[get_session] = override_get_session

    try:
        with TestClient(app) as client:
            created = client.post(
                "/items",
                headers=API_KEY_HEADERS,
                json={
                    "name": "Test API Notebook",
                    "category": "book",
                    "price": 15.5,
                    "in_stock": True,
                },
            )
            assert created.status_code == 201
            item_id = created.json()["id"]

            updated = client.patch(
                f"/items/{item_id}",
                headers=API_KEY_HEADERS,
                json={
                    "price": 18.0,
                    "in_stock": False,
                },
            )
            assert updated.status_code == 200
            assert updated.json()["name"] == "Test API Notebook"
            assert updated.json()["price"] == 18.0
            assert updated.json()["in_stock"] is False

            deleted = client.delete(f"/items/{item_id}", headers=API_KEY_HEADERS)
            assert deleted.status_code == 204

            missing = client.get(f"/items/{item_id}")
            assert missing.status_code == 404
    finally:
        app.dependency_overrides.clear()
        session.close()
        try:
            next(session_generator)
        except StopIteration:
            pass


def test_invalid_update_returns_422() -> None:
    session_generator = create_test_session()
    session = next(session_generator)

    def override_get_session() -> Generator[Session, None, None]:
        yield session

    app.dependency_overrides[get_session] = override_get_session

    try:
        with TestClient(app) as client:
            response = client.patch("/items/1", headers=API_KEY_HEADERS, json={"price": -1})
            assert response.status_code == 422
    finally:
        app.dependency_overrides.clear()
        session.close()
        try:
            next(session_generator)
        except StopIteration:
            pass


def test_create_item_requires_api_key() -> None:
    session_generator = create_test_session()
    session = next(session_generator)

    def override_get_session() -> Generator[Session, None, None]:
        yield session

    app.dependency_overrides[get_session] = override_get_session

    try:
        with TestClient(app) as client:
            response = client.post(
                "/items",
                json={
                    "name": "No Key Item",
                    "category": "book",
                    "price": 5,
                    "in_stock": True,
                },
            )
            assert response.status_code == 401
    finally:
        app.dependency_overrides.clear()
        session.close()
        try:
            next(session_generator)
        except StopIteration:
            pass
