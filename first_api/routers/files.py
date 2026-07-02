from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, Path, UploadFile, status
from sqlmodel import Session

from ..database import get_session
from ..schemas import UploadedTextFile, UploadedTextFileRead
from ..security import require_api_key


MAX_TEXT_FILE_BYTES = 20_000


router = APIRouter(
    prefix="/files",
    tags=["files"],
    dependencies=[Depends(require_api_key)],
)


@router.post("/text", response_model=UploadedTextFileRead, status_code=status.HTTP_201_CREATED)
async def upload_text_file(
    file: Annotated[UploadFile, File(description="A UTF-8 .txt file.")],
    session: Annotated[Session, Depends(get_session)],
) -> UploadedTextFile:
    if not file.filename or not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Only .txt files are accepted in this lesson.",
        )

    raw_content = await file.read()
    if len(raw_content) > MAX_TEXT_FILE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Text file must be at most {MAX_TEXT_FILE_BYTES} bytes.",
        )

    try:
        content = raw_content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Text file must be UTF-8 encoded.",
        ) from exc

    uploaded_file = UploadedTextFile(
        filename=file.filename,
        content_type=file.content_type or "application/octet-stream",
        size_bytes=len(raw_content),
        content=content,
        preview=content[:160],
    )
    session.add(uploaded_file)
    session.commit()
    session.refresh(uploaded_file)
    return uploaded_file


@router.get("/text/{file_id}", response_model=UploadedTextFileRead)
def read_text_file(
    file_id: Annotated[int, Path(ge=1)],
    session: Annotated[Session, Depends(get_session)],
) -> UploadedTextFile:
    uploaded_file = session.get(UploadedTextFile, file_id)
    if uploaded_file is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File {file_id} was not found.",
        )
    return uploaded_file
