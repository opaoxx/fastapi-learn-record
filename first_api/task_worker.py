from sqlmodel import Session

from .database import engine
from .services.ai_clients import get_ai_client
from .services.summary_tasks import run_summary_task


def process_summary_task(task_id: int) -> None:
    with Session(engine) as session:
        run_summary_task(
            session=session,
            task_id=task_id,
            ai_client=get_ai_client(),
        )
