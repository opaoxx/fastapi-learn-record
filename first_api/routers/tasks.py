from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Path, status
from sqlmodel import Session

from ..database import get_session
from ..schemas import SummaryRequest, SummaryTask, SummaryTaskRead, UploadedTextFile
from ..security import require_api_key
from ..services.summary_tasks import (
    create_summary_task_from_file,
    create_summary_task as create_summary_task_record,
    list_summary_tasks as list_summary_task_records,
    read_summary_task as read_summary_task_record,
)
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
    task = create_summary_task_record(
        session=session,
        text=payload.text,
    )

    background_tasks.add_task(process_summary_task, task.id)
    return task


@router.post("/files/{file_id}/summary", response_model=SummaryTaskRead, status_code=status.HTTP_202_ACCEPTED)
def create_file_summary_task(
    file_id: Annotated[int, Path(ge=1)],
    background_tasks: BackgroundTasks,
    session: Annotated[Session, Depends(get_session)],
) -> SummaryTask:
    uploaded_file = session.get(UploadedTextFile, file_id)
    if uploaded_file is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} was not found.",
        )

    task = create_summary_task_from_file(
        session=session,
        uploaded_file=uploaded_file,
    )

    background_tasks.add_task(process_summary_task, task.id)
    return task


@router.get("", response_model=list[SummaryTaskRead])
def list_summary_tasks(
    session: Annotated[Session, Depends(get_session)],
) -> list[SummaryTask]:
    return list_summary_task_records(session)


@router.get("/{task_id}", response_model=SummaryTaskRead)
def read_summary_task(
    task_id: Annotated[int, Path(ge=1)],
    session: Annotated[Session, Depends(get_session)],
) -> SummaryTask:
    task = read_summary_task_record(session, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} was not found.",
        )
    return task
