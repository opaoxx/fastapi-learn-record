import asyncio
import logging
import random
from collections import Counter
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Literal

import httpx
from pydantic import BaseModel, Field, ValidationError

from .ai_clients import AIClientConfig, AIClientError, PredictionLabel, PredictionResult


RETRYABLE_PROVIDER_STATUS_CODES = {429, 500, 502, 503, 504}
PROVIDER_PREDICTION_METRIC_NAME = "provider_prediction_total"
PROVIDER_PREDICTION_METRIC_HELP = (
    "Provider prediction outcomes recorded by the teaching metrics counter."
)
PROVIDER_PREDICTION_METRIC_LABEL_NAMES = (
    "operation",
    "outcome",
    "failure_category",
    "error_code",
    "status_code",
)
logger = logging.getLogger(__name__)
RetrySleep = Callable[[float], Awaitable[None]]
RetryRandom = Callable[[], float]
RetryDelaySource = Literal["retry_after", "local_backoff"]
RetryFailureReason = Literal["timeout", "http_status", "request_error"]
FailFastReason = Literal["http_status", "invalid_response"]
ProviderFailureCategory = Literal[
    "timeout",
    "request_error",
    "retryable_http_status",
    "non_retryable_http_status",
    "invalid_response",
]
ProviderMetricOutcome = Literal[
    "success",
    "retry_scheduled",
    "retry_exhausted",
    "fail_fast",
]
ProviderMetricFailureCategory = ProviderFailureCategory | Literal["none"]
ProviderMetricOperation = Literal["prediction"]


@dataclass(frozen=True)
class ProviderHealthResult:
    ok: bool
    provider: str
    status_code: int
    message: str


@dataclass(frozen=True)
class RetryDelayPlan:
    delay_seconds: float
    source: RetryDelaySource


@dataclass(frozen=True)
class ProviderMetricLabels:
    operation: ProviderMetricOperation
    outcome: ProviderMetricOutcome
    failure_category: ProviderMetricFailureCategory
    error_code: str
    status_code: str

    def as_dict(self) -> dict[str, str]:
        return {
            "operation": self.operation,
            "outcome": self.outcome,
            "failure_category": self.failure_category,
            "error_code": self.error_code,
            "status_code": self.status_code,
        }


@dataclass
class ProviderMetricsCounter:
    _counts: Counter[ProviderMetricLabels] = field(default_factory=Counter)

    def increment(self, labels: ProviderMetricLabels, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError("Metric increment amount must be positive.")
        self._counts[labels] += amount

    def snapshot(self) -> list[dict[str, object]]:
        samples = sorted(
            self._counts.items(),
            key=lambda item: (
                item[0].operation,
                item[0].outcome,
                item[0].failure_category,
                item[0].error_code,
                item[0].status_code,
            ),
        )
        return [
            {
                "labels": labels.as_dict(),
                "count": count,
            }
            for labels, count in samples
        ]

    def reset(self) -> None:
        self._counts.clear()


provider_prediction_metrics = ProviderMetricsCounter()


class ProviderPredictionPayload(BaseModel):
    text: str
    mode: str


class ProviderPredictionBody(BaseModel):
    label: PredictionLabel
    score: float = Field(ge=0, le=1)


def is_retryable_provider_status(status_code: int) -> bool:
    return status_code in RETRYABLE_PROVIDER_STATUS_CODES


def classify_provider_http_status(status_code: int) -> ProviderFailureCategory:
    if is_retryable_provider_status(status_code):
        return "retryable_http_status"
    return "non_retryable_http_status"


def build_provider_metric_labels(
    outcome: ProviderMetricOutcome,
    failure_category: ProviderMetricFailureCategory = "none",
    error_code: str = "none",
    status_code: int | None = None,
) -> ProviderMetricLabels:
    return ProviderMetricLabels(
        operation="prediction",
        outcome=outcome,
        failure_category=failure_category,
        error_code=error_code,
        status_code=str(status_code) if status_code is not None else "none",
    )


def record_provider_metric(labels: ProviderMetricLabels, amount: int = 1) -> None:
    provider_prediction_metrics.increment(labels, amount=amount)


def get_provider_metrics_snapshot() -> list[dict[str, object]]:
    return provider_prediction_metrics.snapshot()


def get_provider_prediction_metric_contract() -> dict[str, object]:
    return {
        "metric_name": PROVIDER_PREDICTION_METRIC_NAME,
        "help": PROVIDER_PREDICTION_METRIC_HELP,
        "label_names": list(PROVIDER_PREDICTION_METRIC_LABEL_NAMES),
    }


def build_provider_metrics_runbook_scenario_samples() -> list[dict[str, object]]:
    return [
        {
            "labels": build_provider_metric_labels(outcome="success").as_dict(),
            "count": 3,
        },
        {
            "labels": build_provider_metric_labels(
                outcome="retry_scheduled",
                failure_category="retryable_http_status",
                error_code="ai_provider_http_error",
                status_code=503,
            ).as_dict(),
            "count": 2,
        },
        {
            "labels": build_provider_metric_labels(
                outcome="retry_exhausted",
                failure_category="retryable_http_status",
                error_code="ai_provider_http_error",
                status_code=503,
            ).as_dict(),
            "count": 1,
        },
        {
            "labels": build_provider_metric_labels(
                outcome="fail_fast",
                failure_category="non_retryable_http_status",
                error_code="ai_provider_http_error",
                status_code=400,
            ).as_dict(),
            "count": 1,
        },
    ]


def build_provider_metrics_runbook_findings(
    samples: list[dict[str, object]],
) -> list[dict[str, object]]:
    findings = []
    for sample in samples:
        labels = sample.get("labels")
        count = sample.get("count")
        if not isinstance(labels, dict):
            raise ValueError("Metric sample labels must be a dictionary.")
        if not isinstance(count, int):
            raise ValueError("Metric sample count must be an integer.")

        outcome = labels.get("outcome")
        failure_category = str(labels.get("failure_category", "none"))
        status_code = str(labels.get("status_code", "none"))

        if outcome == "success":
            finding = "Provider prediction requests are succeeding."
            next_action = (
                "Compare the success count with expected request volume before "
                "treating failure samples as system-wide."
            )
            severity = "baseline"
        elif outcome == "retry_scheduled":
            finding = "Retryable provider failures were observed and retry was scheduled."
            next_action = (
                "Check failure_category, status_code, retry delay logs, and whether "
                "retry_exhausted also appears."
            )
            severity = "investigate"
        elif outcome == "retry_exhausted":
            finding = "Retryable provider failures exhausted the configured attempts."
            next_action = (
                "Check max_attempts, provider availability, and the last retryable "
                "failure before changing retry policy."
            )
            severity = "action_required"
        elif outcome == "fail_fast":
            finding = "A non-retryable provider failure or invalid response was recorded."
            next_action = (
                "Do not increase retries first; inspect the request or response "
                "contract and the status_code."
            )
            severity = "contract_check"
        else:
            finding = "The metric sample uses an outcome without a runbook branch."
            next_action = (
                "Add an explicit runbook branch before treating this metric as "
                "operationally actionable."
            )
            severity = "unknown"

        findings.append(
            {
                "outcome": str(outcome),
                "count": count,
                "failure_category": failure_category,
                "status_code": status_code,
                "severity": severity,
                "finding": finding,
                "next_action": next_action,
            }
        )
    return findings


def render_provider_metrics_runbook_findings_markdown(
    findings: list[dict[str, object]],
) -> str:
    lines = [
        "| outcome | count | severity | finding | next_action |",
        "| --- | ---: | --- | --- | --- |",
    ]
    for finding in findings:
        lines.append(
            "| {outcome} | {count} | {severity} | {finding_text} | {next_action} |".format(
                outcome=finding["outcome"],
                count=finding["count"],
                severity=finding["severity"],
                finding_text=finding["finding"],
                next_action=finding["next_action"],
            )
        )
    return "\n".join(lines) + "\n"


def build_provider_metrics_runbook_exercise_cards(
    findings: list[dict[str, object]],
) -> list[dict[str, object]]:
    cards = []
    for index, finding in enumerate(findings, start=1):
        cards.append(
            {
                "id": f"provider-metrics-runbook-{index}",
                "prompt": (
                    "Outcome {outcome} has count {count}. What should you check next?"
                ).format(
                    outcome=finding["outcome"],
                    count=finding["count"],
                ),
                "expected_severity": finding["severity"],
                "expected_next_action": finding["next_action"],
                "answer": (
                    "{finding_text} Next action: {next_action}"
                ).format(
                    finding_text=finding["finding"],
                    next_action=finding["next_action"],
                ),
            }
        )
    return cards


def render_provider_metrics_runbook_exercise_answer_key(
    cards: list[dict[str, object]],
) -> str:
    lines = []
    for card in cards:
        lines.append(f"## {card['id']}")
        lines.append("")
        lines.append(f"Prompt: {card['prompt']}")
        lines.append(f"Expected severity: {card['expected_severity']}")
        lines.append(f"Answer: {card['answer']}")
        lines.append("")
    return "\n".join(lines)


def grade_provider_metrics_runbook_exercise_answer(
    card: dict[str, object],
    response: str,
) -> dict[str, object]:
    normalized_response = response.casefold()
    expected_severity = str(card["expected_severity"])
    expected_next_action = str(card["expected_next_action"])
    severity_matched = expected_severity.casefold() in normalized_response
    next_action_matched = expected_next_action.casefold() in normalized_response
    missing = []
    if not severity_matched:
        missing.append("expected_severity")
    if not next_action_matched:
        missing.append("expected_next_action")
    passed = not missing
    return {
        "card_id": card["id"],
        "severity_matched": severity_matched,
        "next_action_matched": next_action_matched,
        "passed": passed,
        "missing": missing,
        "feedback": (
            "Answer includes the expected severity and next action."
            if passed
            else "Missing: {items}.".format(items=", ".join(missing))
        ),
    }


def summarize_provider_metrics_runbook_exercise_grades(
    cards: list[dict[str, object]],
    responses_by_card_id: dict[str, str],
) -> dict[str, object]:
    grades = []
    answered = 0
    for card in cards:
        card_id = str(card["id"])
        if card_id in responses_by_card_id:
            answered += 1
        grade = grade_provider_metrics_runbook_exercise_answer(
            card,
            responses_by_card_id.get(card_id, ""),
        )
        grade["answered"] = card_id in responses_by_card_id
        grades.append(grade)
    passed = sum(1 for grade in grades if grade["passed"])
    total = len(cards)
    return {
        "total": total,
        "answered": answered,
        "passed": passed,
        "failed": total - passed,
        "unanswered": total - answered,
        "grades": grades,
    }


def validate_provider_metrics_runbook_grading_summary(
    summary: dict[str, object],
) -> dict[str, object]:
    errors = []
    numeric_fields = ["total", "answered", "passed", "failed", "unanswered"]
    for field in numeric_fields:
        if field not in summary:
            errors.append(f"Missing summary field: {field}.")
        elif not isinstance(summary[field], int):
            errors.append(f"Summary field must be an integer: {field}.")

    grades = summary.get("grades")
    if not isinstance(grades, list):
        errors.append("Summary field must be a list: grades.")
    else:
        for index, grade in enumerate(grades, start=1):
            if not isinstance(grade, dict):
                errors.append(f"Grade #{index} must be a dictionary.")
                continue
            for field in ["card_id", "answered", "passed", "missing", "feedback"]:
                if field not in grade:
                    errors.append(f"Grade #{index} missing field: {field}.")
            if "answered" in grade and not isinstance(grade["answered"], bool):
                errors.append(f"Grade #{index} field must be a boolean: answered.")
            if "passed" in grade and not isinstance(grade["passed"], bool):
                errors.append(f"Grade #{index} field must be a boolean: passed.")
            if "missing" in grade and not isinstance(grade["missing"], list):
                errors.append(f"Grade #{index} field must be a list: missing.")

    if all(field in summary and isinstance(summary[field], int) for field in numeric_fields):
        total = summary["total"]
        answered = summary["answered"]
        passed = summary["passed"]
        failed = summary["failed"]
        unanswered = summary["unanswered"]
        if total < 0 or answered < 0 or passed < 0 or failed < 0 or unanswered < 0:
            errors.append("Summary counts must be non-negative.")
        if answered > total:
            errors.append("Summary answered count cannot exceed total.")
        if passed > total:
            errors.append("Summary passed count cannot exceed total.")
        if failed != total - passed:
            errors.append("Summary failed count must equal total - passed.")
        if unanswered != total - answered:
            errors.append("Summary unanswered count must equal total - answered.")
        if isinstance(grades, list) and total != len(grades):
            errors.append("Summary total must equal the number of grades.")

    return {
        "valid": not errors,
        "errors": errors,
    }


def render_provider_metrics_runbook_grading_summary_markdown(
    summary: dict[str, object],
) -> str:
    lines = [
        "## Provider Metrics Runbook Grading Summary",
        "",
        "| total | answered | passed | failed | unanswered |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            "| {total} | {answered} | {passed} | {failed} | {unanswered} |"
        ).format(
            total=summary["total"],
            answered=summary["answered"],
            passed=summary["passed"],
            failed=summary["failed"],
            unanswered=summary["unanswered"],
        ),
        "",
        "## Grade Details",
        "",
        "| card_id | answered | passed | missing | feedback |",
        "| --- | --- | --- | --- | --- |",
    ]
    grades = summary["grades"]
    if not isinstance(grades, list):
        raise ValueError("Grading summary grades must be a list.")
    for grade in grades:
        missing = grade["missing"]
        if not isinstance(missing, list):
            raise ValueError("Grading detail missing field must be a list.")
        lines.append(
            "| {card_id} | {answered} | {passed} | {missing} | {feedback} |".format(
                card_id=grade["card_id"],
                answered=grade["answered"],
                passed=grade["passed"],
                missing=", ".join(str(item) for item in missing) if missing else "-",
                feedback=grade["feedback"],
            )
        )
    return "\n".join(lines) + "\n"


def build_provider_metrics_runbook_practice_session(
    responses_by_card_id: dict[str, str],
) -> dict[str, object]:
    samples = build_provider_metrics_runbook_scenario_samples()
    findings = build_provider_metrics_runbook_findings(samples)
    findings_markdown = render_provider_metrics_runbook_findings_markdown(findings)
    cards = build_provider_metrics_runbook_exercise_cards(findings)
    answer_key = render_provider_metrics_runbook_exercise_answer_key(cards)
    summary = summarize_provider_metrics_runbook_exercise_grades(
        cards,
        responses_by_card_id,
    )
    validation = validate_provider_metrics_runbook_grading_summary(summary)
    report_markdown = (
        render_provider_metrics_runbook_grading_summary_markdown(summary)
        if validation["valid"]
        else ""
    )
    return {
        "samples": samples,
        "findings": findings,
        "findings_markdown": findings_markdown,
        "cards": cards,
        "answer_key": answer_key,
        "summary": summary,
        "validation": validation,
        "report_markdown": report_markdown,
    }


def render_provider_metrics_runbook_practice_session_markdown(
    session: dict[str, object],
) -> str:
    lines = [
        "# Provider Metrics Runbook Practice Session",
        "",
        "## Findings",
        "",
        str(session["findings_markdown"]).rstrip(),
        "",
        "## Exercise Cards",
        "",
        "| card_id | prompt | expected_severity |",
        "| --- | --- | --- |",
    ]
    cards = session["cards"]
    if not isinstance(cards, list):
        raise ValueError("Practice session cards must be a list.")
    for card in cards:
        lines.append(
            "| {card_id} | {prompt} | {expected_severity} |".format(
                card_id=card["id"],
                prompt=card["prompt"],
                expected_severity=card["expected_severity"],
            )
        )
    lines.extend(
        [
            "",
            "## Answer Key",
            "",
            str(session["answer_key"]).rstrip(),
            "",
            "## Grading Report",
            "",
            str(session["report_markdown"]).rstrip(),
            "",
        ]
    )
    return "\n".join(lines)


def build_provider_metrics_runbook_practice_release_checklist(
    session: dict[str, object],
    package_markdown: str,
) -> dict[str, object]:
    checks = [
        {
            "id": "findings_markdown_present",
            "passed": bool(str(session.get("findings_markdown", "")).strip()),
            "evidence": "Findings Markdown is present.",
        },
        {
            "id": "exercise_cards_present",
            "passed": bool(session.get("cards")),
            "evidence": "Exercise cards are present.",
        },
        {
            "id": "answer_key_present",
            "passed": "## provider-metrics-runbook-" in str(session.get("answer_key", "")),
            "evidence": "Answer key contains runbook card sections.",
        },
        {
            "id": "grading_summary_valid",
            "passed": session.get("validation") == {"valid": True, "errors": []},
            "evidence": "Grading summary validation passed.",
        },
        {
            "id": "grading_report_present",
            "passed": bool(str(session.get("report_markdown", "")).strip()),
            "evidence": "Grading report Markdown is present.",
        },
        {
            "id": "package_sections_present",
            "passed": all(
                section in package_markdown
                for section in [
                    "## Findings",
                    "## Exercise Cards",
                    "## Answer Key",
                    "## Grading Report",
                ]
            ),
            "evidence": "Practice package contains all required sections.",
        },
    ]
    return {
        "ready": all(check["passed"] for check in checks),
        "checks": checks,
    }


def escape_prometheus_label_value(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


def render_provider_metrics_prometheus_text(
    samples: list[dict[str, object]],
) -> str:
    lines = [
        f"# HELP {PROVIDER_PREDICTION_METRIC_NAME} {PROVIDER_PREDICTION_METRIC_HELP}",
        f"# TYPE {PROVIDER_PREDICTION_METRIC_NAME} counter",
    ]
    for sample in samples:
        labels = sample["labels"]
        if not isinstance(labels, dict):
            raise ValueError("Metric sample labels must be a dictionary.")
        label_text = ",".join(
            f'{name}="{escape_prometheus_label_value(value)}"'
            for name, value in sorted(labels.items())
        )
        lines.append(
            f"{PROVIDER_PREDICTION_METRIC_NAME}{{{label_text}}} {sample['count']}"
        )
    return "\n".join(lines) + "\n"


def get_provider_metrics_prometheus_text() -> str:
    return render_provider_metrics_prometheus_text(get_provider_metrics_snapshot())


def reset_provider_metrics() -> None:
    provider_prediction_metrics.reset()


def classify_retry_metric_failure(
    retry_reason: RetryFailureReason,
    status_code: int | None = None,
) -> ProviderMetricFailureCategory:
    if retry_reason == "timeout":
        return "timeout"
    if retry_reason == "request_error":
        return "request_error"
    if status_code is not None:
        return classify_provider_http_status(status_code)
    return "retryable_http_status"


def retry_metric_error_code(retry_reason: RetryFailureReason) -> str:
    if retry_reason == "timeout":
        return "ai_provider_timeout"
    if retry_reason == "request_error":
        return "ai_provider_request_error"
    return "ai_provider_http_error"


def classify_fail_fast_metric_failure(
    fail_fast_reason: FailFastReason,
    status_code: int | None = None,
) -> ProviderMetricFailureCategory:
    if fail_fast_reason == "invalid_response":
        return "invalid_response"
    if status_code is not None:
        return classify_provider_http_status(status_code)
    return "non_retryable_http_status"


def parse_retry_after_delay(
    retry_after: str | None,
    now: datetime | None = None,
) -> float | None:
    if retry_after is None:
        return None

    value = retry_after.strip()
    if value.isdecimal():
        return float(value)

    try:
        retry_at = parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError, OverflowError):
        return None

    if retry_at.tzinfo is None:
        retry_at = retry_at.replace(tzinfo=timezone.utc)

    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)

    delay_seconds = (retry_at - current_time).total_seconds()
    return max(delay_seconds, 0.0)


def calculate_retry_jitter(
    config: AIClientConfig,
    random_fraction: RetryRandom = random.random,
) -> float:
    jitter_seconds = max(config.retry_jitter_seconds, 0.0)
    if jitter_seconds == 0:
        return 0.0

    fraction = min(max(random_fraction(), 0.0), 1.0)
    return jitter_seconds * fraction


def calculate_retry_delay(
    attempt: int,
    config: AIClientConfig,
    retry_after: str | None = None,
    now: datetime | None = None,
    random_fraction: RetryRandom = random.random,
) -> float:
    return build_retry_delay_plan(
        attempt,
        config,
        retry_after=retry_after,
        now=now,
        random_fraction=random_fraction,
    ).delay_seconds


def build_retry_delay_plan(
    attempt: int,
    config: AIClientConfig,
    retry_after: str | None = None,
    now: datetime | None = None,
    random_fraction: RetryRandom = random.random,
) -> RetryDelayPlan:
    base_delay = max(config.retry_base_delay_seconds, 0.0)
    max_delay = max(config.retry_max_delay_seconds, 0.0)
    provider_delay = parse_retry_after_delay(retry_after, now=now)
    if provider_delay is not None:
        return RetryDelayPlan(
            delay_seconds=min(provider_delay, max_delay),
            source="retry_after",
        )

    exponential_delay = base_delay * (2 ** (attempt - 1))
    jitter_delay = calculate_retry_jitter(config, random_fraction=random_fraction)
    return RetryDelayPlan(
        delay_seconds=min(exponential_delay + jitter_delay, max_delay),
        source="local_backoff",
    )


async def wait_before_retry(
    attempt: int,
    config: AIClientConfig,
    sleep: RetrySleep,
    retry_reason: RetryFailureReason,
    retry_after: str | None = None,
    status_code: int | None = None,
    random_fraction: RetryRandom = random.random,
) -> None:
    delay_plan = build_retry_delay_plan(
        attempt,
        config,
        retry_after=retry_after,
        random_fraction=random_fraction,
    )
    logger.info(
        "provider_prediction_retry_scheduled",
        extra={
            "attempt": attempt,
            "max_attempts": config.max_attempts,
            "retry_reason": retry_reason,
            "status_code": status_code,
            "retry_after": retry_after,
            "delay_seconds": delay_plan.delay_seconds,
            "delay_source": delay_plan.source,
        },
    )
    record_provider_metric(
        build_provider_metric_labels(
            outcome="retry_scheduled",
            failure_category=classify_retry_metric_failure(
                retry_reason,
                status_code=status_code,
            ),
            error_code=retry_metric_error_code(retry_reason),
            status_code=status_code,
        )
    )
    if delay_plan.delay_seconds > 0:
        await sleep(delay_plan.delay_seconds)


def log_retry_exhausted(
    attempt: int,
    config: AIClientConfig,
    retry_reason: RetryFailureReason,
    error_code: str,
    retry_after: str | None = None,
    status_code: int | None = None,
) -> None:
    logger.warning(
        "provider_prediction_retry_exhausted",
        extra={
            "attempt": attempt,
            "max_attempts": config.max_attempts,
            "retry_reason": retry_reason,
            "status_code": status_code,
            "retry_after": retry_after,
            "error_code": error_code,
        },
    )
    record_provider_metric(
        build_provider_metric_labels(
            outcome="retry_exhausted",
            failure_category=classify_retry_metric_failure(
                retry_reason,
                status_code=status_code,
            ),
            error_code=error_code,
            status_code=status_code,
        )
    )


def log_prediction_fail_fast(
    attempt: int,
    config: AIClientConfig,
    fail_fast_reason: FailFastReason,
    error_code: str,
    status_code: int | None = None,
) -> None:
    logger.warning(
        "provider_prediction_fail_fast",
        extra={
            "attempt": attempt,
            "max_attempts": config.max_attempts,
            "fail_fast_reason": fail_fast_reason,
            "status_code": status_code,
            "error_code": error_code,
        },
    )
    record_provider_metric(
        build_provider_metric_labels(
            outcome="fail_fast",
            failure_category=classify_fail_fast_metric_failure(
                fail_fast_reason,
                status_code=status_code,
            ),
            error_code=error_code,
            status_code=status_code,
        )
    )


async def check_provider_health(
    url: str,
    config: AIClientConfig,
    client: httpx.AsyncClient | None = None,
) -> ProviderHealthResult:
    owns_client = client is None
    active_client = client or httpx.AsyncClient(
        timeout=config.timeout_seconds,
        trust_env=False,
    )

    try:
        response = await active_client.get(url)
        response.raise_for_status()
    except httpx.TimeoutException as exc:
        raise AIClientError(
            message="The AI provider health check timed out.",
            error_code="ai_provider_timeout",
        ) from exc
    except httpx.HTTPStatusError as exc:
        raise AIClientError(
            message=f"The AI provider returned HTTP {exc.response.status_code}.",
            error_code="ai_provider_http_error",
        ) from exc
    except httpx.RequestError as exc:
        raise AIClientError(
            message="The AI provider could not be reached.",
            error_code="ai_provider_request_error",
        ) from exc
    finally:
        if owns_client:
            await active_client.aclose()

    return ProviderHealthResult(
        ok=True,
        provider=config.provider,
        status_code=response.status_code,
        message="The AI provider responded successfully.",
    )


async def request_provider_prediction(
    url: str,
    text: str,
    mode: str,
    config: AIClientConfig,
    client: httpx.AsyncClient | None = None,
    sleep: RetrySleep = asyncio.sleep,
    random_fraction: RetryRandom = random.random,
) -> PredictionResult:
    owns_client = client is None
    active_client = client or httpx.AsyncClient(
        timeout=config.timeout_seconds,
        trust_env=False,
    )

    try:
        for attempt in range(1, config.max_attempts + 1):
            try:
                response = await active_client.post(
                    url,
                    json=ProviderPredictionPayload(text=text, mode=mode).model_dump(),
                )
                response.raise_for_status()
                body = ProviderPredictionBody.model_validate(response.json())
                record_provider_metric(build_provider_metric_labels(outcome="success"))
                return PredictionResult(
                    label=body.label,
                    score=round(body.score, 2),
                    source=f"{config.provider}-provider",
                )
            except httpx.TimeoutException as exc:
                if attempt < config.max_attempts:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="timeout",
                        random_fraction=random_fraction,
                    )
                    continue
                log_retry_exhausted(
                    attempt=attempt,
                    config=config,
                    retry_reason="timeout",
                    error_code="ai_provider_timeout",
                )
                raise AIClientError(
                    message="The AI provider prediction request timed out.",
                    error_code="ai_provider_timeout",
                ) from exc
            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
                retryable_status = (
                    classify_provider_http_status(status_code)
                    == "retryable_http_status"
                )
                if attempt < config.max_attempts and retryable_status:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="http_status",
                        retry_after=exc.response.headers.get("Retry-After"),
                        status_code=status_code,
                        random_fraction=random_fraction,
                    )
                    continue
                if retryable_status:
                    log_retry_exhausted(
                        attempt=attempt,
                        config=config,
                        retry_reason="http_status",
                        error_code="ai_provider_http_error",
                        retry_after=exc.response.headers.get("Retry-After"),
                        status_code=status_code,
                    )
                else:
                    log_prediction_fail_fast(
                        attempt=attempt,
                        config=config,
                        fail_fast_reason="http_status",
                        error_code="ai_provider_http_error",
                        status_code=status_code,
                    )
                raise AIClientError(
                    message=f"The AI provider returned HTTP {status_code}.",
                    error_code="ai_provider_http_error",
                ) from exc
            except httpx.RequestError as exc:
                if attempt < config.max_attempts:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="request_error",
                        random_fraction=random_fraction,
                    )
                    continue
                log_retry_exhausted(
                    attempt=attempt,
                    config=config,
                    retry_reason="request_error",
                    error_code="ai_provider_request_error",
                )
                raise AIClientError(
                    message="The AI provider could not be reached.",
                    error_code="ai_provider_request_error",
                ) from exc
            except (ValueError, ValidationError) as exc:
                log_prediction_fail_fast(
                    attempt=attempt,
                    config=config,
                    fail_fast_reason="invalid_response",
                    error_code="ai_provider_invalid_response",
                    status_code=response.status_code,
                )
                raise AIClientError(
                    message="The AI provider returned an invalid prediction response.",
                    error_code="ai_provider_invalid_response",
                ) from exc
    finally:
        if owns_client:
            await active_client.aclose()

    raise AIClientError(
        message="The AI provider prediction request did not run.",
        error_code="ai_provider_request_error",
    )
