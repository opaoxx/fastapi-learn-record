from sqlmodel import Session

from first_api.database import engine
from first_api.services.ai_clients import AIClientError
from first_api.services.summary_tasks import create_summary_task, run_summary_task


class FailingSummaryClient:
    def summarize(self, text: str) -> str:
        raise AIClientError(
            message="The summary model timed out.",
            error_code="summary_model_timeout",
        )


def test_summary_task_records_failed_status_when_ai_client_fails() -> None:
    with Session(engine) as session:
        task = create_summary_task(
            session=session,
            text="This text is long enough to create a task that will fail in a controlled way.",
        )

        run_summary_task(
            session=session,
            task_id=task.id,
            ai_client=FailingSummaryClient(),
        )

        failed_task = session.get(type(task), task.id)

    assert failed_task is not None
    assert failed_task.status == "failed"
    assert failed_task.result is None
    assert failed_task.error == "summary_model_timeout: The summary model timed out."
