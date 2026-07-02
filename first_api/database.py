from collections.abc import Generator
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine, select

from .schemas import Item


DATABASE_URL = f"sqlite:///{Path(__file__).with_name('first_api.db')}"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed_items(session)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def seed_items(session: Session) -> None:
    existing_item = session.exec(select(Item)).first()
    if existing_item is not None:
        return

    session.add_all(
        [
            Item(name="FastAPI Beginner Course", category="course", price=0, in_stock=True),
            Item(name="Python Backend Handbook", category="book", price=39.9, in_stock=True),
            Item(name="API Debug Toolkit", category="tool", price=19.9, in_stock=False),
        ]
    )
    session.commit()
