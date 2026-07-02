from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Path, status
from sqlmodel import Session, select

from ..database import get_session
from ..schemas import SummaryRequest, SummaryTask, SummaryTaskRead
from ..security import require_api_key
from ..task_worker import process_summary_task


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    dependencies=[Depends(require_api_key)],
)


@router.post("/summaries", response_model=SummaryTaskRead, status_code=status.HTTP_202_ACCEPTED)
def create_summary_task(
    payload: SummaryRequest,
    background_tasks: BackgroundTasks,
    session: Annotated[Session, Depends(get_session)],
) -> SummaryTask:
    task = SummaryTask(
        text=payload.text,
        text_length=len(payload.text),
        status="queued",
    )
    session.add(task)
    session.commit()
    session.refresh(task)

    background_tasks.add_task(process_summary_task, task.id)
    return task


@router.get("", response_model=list[SummaryTaskRead])
def list_summary_tasks(
    session: Annotated[Session, Depends(get_session)],
) -> list[SummaryTask]:
    return list(session.exec(select(SummaryTask)))


@router.get("/{task_id}", response_model=SummaryTaskRead)
def read_summary_task(
    task_id: Annotated[int, Path(ge=1)],
    session: Annotated[Session, Depends(get_session)],
) -> SummaryTask:
    task = session.get(SummaryTask, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} was not found.",
        )
    return task
