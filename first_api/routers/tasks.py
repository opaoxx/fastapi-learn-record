from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Path, Query, status
from sqlmodel import Session

from ..database import get_session
from ..schemas import (
    SummaryRequest,
    SummaryTask,
    SummaryTaskListResponse,
    SummaryTaskRead,
    TaskStatus,
    UploadedTextFile,
)
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


@router.post(
    "/summaries",
    response_model=SummaryTaskRead,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Create a summary task from raw text",
    description=(
        "Accepts text, stores a queued summary task, schedules background processing, "
        "and returns the task record immediately."
    ),
    response_description="The accepted summary task.",
)
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


@router.post(
    "/files/{file_id}/summary",
    response_model=SummaryTaskRead,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Create a summary task from an uploaded text file",
    description=(
        "Reads an existing uploaded text file, creates a queued summary task from its content, "
        "and schedules background processing."
    ),
    response_description="The accepted file-backed summary task.",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "The uploaded text file does not exist."},
    },
)
def create_file_summary_task(
    file_id: Annotated[int, Path(ge=1, description="The uploaded text file ID.")],
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


@router.get(
    "",
    response_model=SummaryTaskListResponse,
    summary="List summary tasks",
    description=(
        "Returns a newest-first page of summary tasks. Clients can filter by task status "
        "and use limit/offset pagination."
    ),
    response_description="A paginated task-list response envelope.",
)
def list_summary_tasks(
    session: Annotated[Session, Depends(get_session)],
    task_status: Annotated[
        TaskStatus | None,
        Query(alias="status", description="Optional status filter for the task list."),
    ] = None,
    offset: Annotated[int, Query(ge=0, description="Zero-based number of matching tasks to skip.")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="Maximum number of tasks to return.")] = 20,
) -> SummaryTaskListResponse:
    return list_summary_task_records(
        session=session,
        task_status=task_status,
        offset=offset,
        limit=limit,
    )


@router.get(
    "/{task_id}",
    response_model=SummaryTaskRead,
    summary="Read one summary task",
    description="Returns the current status, result, or stored error for a single summary task.",
    response_description="The requested summary task.",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "The summary task does not exist."},
    },
)
def read_summary_task(
    task_id: Annotated[int, Path(ge=1, description="The summary task ID.")],
    session: Annotated[Session, Depends(get_session)],
) -> SummaryTask:
    task = read_summary_task_record(session, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} was not found.",
        )
    return task
