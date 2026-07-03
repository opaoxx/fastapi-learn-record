from sqlalchemy import func
from sqlmodel import Session, select

from ..schemas import SummaryTask, SummaryTaskListResponse, TaskStatus, UploadedTextFile
from .ai_clients import AIClient, AIClientError


def create_summary_task(
    session: Session,
    text: str,
    source_file_id: int | None = None,
) -> SummaryTask:
    task = SummaryTask(
        text=text,
        text_length=len(text),
        source_file_id=source_file_id,
        status="queued",
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def create_summary_task_from_file(
    session: Session,
    uploaded_file: UploadedTextFile,
) -> SummaryTask:
    return create_summary_task(
        session=session,
        text=uploaded_file.content,
        source_file_id=uploaded_file.id,
    )


def list_summary_tasks(
    session: Session,
    task_status: TaskStatus | None = None,
    offset: int = 0,
    limit: int = 20,
) -> SummaryTaskListResponse:
    statement = select(SummaryTask).order_by(SummaryTask.id.desc())
    count_statement = select(func.count()).select_from(SummaryTask)
    if task_status is not None:
        statement = statement.where(SummaryTask.status == task_status)
        count_statement = count_statement.where(SummaryTask.status == task_status)
    statement = statement.offset(offset).limit(limit)
    items = list(session.exec(statement))
    count = session.exec(count_statement).one()
    return SummaryTaskListResponse(
        items=items,
        count=count,
        limit=limit,
        offset=offset,
    )


def read_summary_task(session: Session, task_id: int) -> SummaryTask | None:
    return session.get(SummaryTask, task_id)


def run_summary_task(session: Session, task_id: int, ai_client: AIClient) -> None:
    task = session.get(SummaryTask, task_id)
    if task is None:
        return

    try:
        task.status = "running"
        session.add(task)
        session.commit()
        session.refresh(task)

        task.result = ai_client.summarize(task.text)
        task.status = "completed"
        task.error = None
    except AIClientError as exc:
        task.status = "failed"
        task.error = f"{exc.error_code}: {exc.message}"
    except Exception:
        task.status = "failed"
        task.error = "unexpected_task_error: The summary task failed unexpectedly."
    finally:
        session.add(task)
        session.commit()
