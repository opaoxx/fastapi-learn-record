from sqlmodel import Session

from .database import engine
from .schemas import SummaryTask


def build_demo_summary(text: str) -> str:
    words = text.split()
    if len(words) <= 12:
        return text
    return " ".join(words[:12]) + " ..."


def process_summary_task(task_id: int) -> None:
    with Session(engine) as session:
        task = session.get(SummaryTask, task_id)
        if task is None:
            return

        try:
            task.status = "running"
            session.add(task)
            session.commit()
            session.refresh(task)

            task.result = build_demo_summary(task.text)
            task.status = "completed"
            task.error = None
        except Exception as exc:
            task.status = "failed"
            task.error = str(exc)
        finally:
            session.add(task)
            session.commit()
