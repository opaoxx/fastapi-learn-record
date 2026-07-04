import asyncio
import json
import logging
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

import httpx

from first_api.services.ai_clients import AIClientConfig, AIClientError
from first_api.services.provider_http import (
    PROVIDER_PREDICTION_METRIC_LABEL_NAMES,
    PROVIDER_PREDICTION_METRIC_HELP,
    PROVIDER_PREDICTION_METRIC_NAME,
    ProviderMetricsCounter,
    build_provider_metrics_runbook_practice_release_checklist,
    build_provider_metrics_runbook_practice_session,
    build_provider_metrics_runbook_exercise_cards,
    build_provider_metrics_runbook_findings,
    build_provider_metrics_runbook_scenario_samples,
    build_provider_metric_labels,
    calculate_retry_jitter,
    calculate_retry_delay,
    classify_provider_http_status,
    check_provider_health,
    get_provider_prediction_metric_contract,
    get_provider_metrics_snapshot,
    grade_provider_metrics_runbook_exercise_answer,
    parse_retry_after_delay,
    render_provider_metrics_runbook_exercise_answer_key,
    render_provider_metrics_runbook_findings_markdown,
    render_provider_metrics_runbook_grading_summary_markdown,
    render_provider_metrics_runbook_practice_session_markdown,
    render_provider_metrics_prometheus_text,
    request_provider_prediction,
    reset_provider_metrics,
    summarize_provider_metrics_runbook_exercise_grades,
    validate_provider_metrics_runbook_grading_summary,
)


def run_async_health_check(client: httpx.AsyncClient) -> object:
    return asyncio.run(
        check_provider_health(
            url="https://provider.test/health",
            config=AIClientConfig(
                provider="demo",
                timeout_seconds=0.5,
                max_attempts=1,
            ),
            client=client,
        )
    )


def run_async_prediction(
    client: httpx.AsyncClient,
    max_attempts: int = 1,
    retry_base_delay_seconds: float = 0.0,
    retry_max_delay_seconds: float = 0.0,
    retry_jitter_seconds: float = 0.0,
    sleep: object | None = None,
    random_fraction: object | None = None,
) -> object:
    kwargs = {}
    if sleep is not None:
        kwargs["sleep"] = sleep
    if random_fraction is not None:
        kwargs["random_fraction"] = random_fraction

    return asyncio.run(
        request_provider_prediction(
            url="https://provider.test/predict",
            text="FastAPI is great and pleasant.",
            mode="careful",
            config=AIClientConfig(
                provider="demo",
                timeout_seconds=0.5,
                max_attempts=max_attempts,
                retry_base_delay_seconds=retry_base_delay_seconds,
                retry_max_delay_seconds=retry_max_delay_seconds,
                retry_jitter_seconds=retry_jitter_seconds,
            ),
            client=client,
            **kwargs,
        )
    )


def test_calculate_retry_delay_uses_exponential_backoff_with_cap() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=5,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
    )

    delays = [calculate_retry_delay(attempt, config) for attempt in range(1, 5)]

    assert delays == [1.0, 2.0, 3.0, 3.0]


def test_classify_provider_http_status_names_retry_taxonomy() -> None:
    retryable_statuses = [429, 500, 502, 503, 504]
    non_retryable_statuses = [400, 401, 404, 422]

    assert [
        classify_provider_http_status(status_code)
        for status_code in retryable_statuses
    ] == ["retryable_http_status"] * len(retryable_statuses)
    assert [
        classify_provider_http_status(status_code)
        for status_code in non_retryable_statuses
    ] == ["non_retryable_http_status"] * len(non_retryable_statuses)


def test_build_provider_metric_labels_uses_bounded_success_labels() -> None:
    labels = build_provider_metric_labels(outcome="success")

    assert labels.as_dict() == {
        "operation": "prediction",
        "outcome": "success",
        "failure_category": "none",
        "error_code": "none",
        "status_code": "none",
    }


def test_build_provider_metric_labels_uses_failure_taxonomy_without_request_text() -> None:
    labels = build_provider_metric_labels(
        outcome="fail_fast",
        failure_category="non_retryable_http_status",
        error_code="ai_provider_http_error",
        status_code=400,
    )

    assert labels.as_dict() == {
        "operation": "prediction",
        "outcome": "fail_fast",
        "failure_category": "non_retryable_http_status",
        "error_code": "ai_provider_http_error",
        "status_code": "400",
    }
    assert "FastAPI is great and pleasant." not in labels.as_dict().values()


def test_provider_metric_name_and_help_text_are_stable_contract() -> None:
    assert PROVIDER_PREDICTION_METRIC_NAME == "provider_prediction_total"
    assert PROVIDER_PREDICTION_METRIC_NAME.endswith("_total")
    assert (
        PROVIDER_PREDICTION_METRIC_HELP
        == "Provider prediction outcomes recorded by the teaching metrics counter."
    )


def test_provider_metric_label_names_are_stable_low_cardinality_contract() -> None:
    labels = build_provider_metric_labels(
        outcome="retry_exhausted",
        failure_category="retryable_http_status",
        error_code="ai_provider_http_error",
        status_code=503,
    )

    assert list(labels.as_dict()) == [
        "operation",
        "outcome",
        "failure_category",
        "error_code",
        "status_code",
    ]
    assert labels.as_dict() == {
        "operation": "prediction",
        "outcome": "retry_exhausted",
        "failure_category": "retryable_http_status",
        "error_code": "ai_provider_http_error",
        "status_code": "503",
    }


def test_provider_metric_contract_collects_rename_sensitive_fields() -> None:
    contract = get_provider_prediction_metric_contract()

    assert contract == {
        "metric_name": "provider_prediction_total",
        "help": "Provider prediction outcomes recorded by the teaching metrics counter.",
        "label_names": list(PROVIDER_PREDICTION_METRIC_LABEL_NAMES),
    }
    assert contract["label_names"] == [
        "operation",
        "outcome",
        "failure_category",
        "error_code",
        "status_code",
    ]


def test_provider_metrics_runbook_scenario_samples_cover_core_outcomes() -> None:
    samples = build_provider_metrics_runbook_scenario_samples()

    assert samples == [
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
    assert {sample["labels"]["outcome"] for sample in samples} == {
        "success",
        "retry_scheduled",
        "retry_exhausted",
        "fail_fast",
    }


def test_provider_metrics_runbook_scenario_samples_render_as_text() -> None:
    text = render_provider_metrics_prometheus_text(
        build_provider_metrics_runbook_scenario_samples()
    )

    assert text == (
        "# HELP provider_prediction_total Provider prediction outcomes recorded by "
        "the teaching metrics counter.\n"
        "# TYPE provider_prediction_total counter\n"
        'provider_prediction_total{error_code="none",failure_category="none",'
        'operation="prediction",outcome="success",status_code="none"} 3\n'
        'provider_prediction_total{error_code="ai_provider_http_error",'
        'failure_category="retryable_http_status",operation="prediction",'
        'outcome="retry_scheduled",status_code="503"} 2\n'
        'provider_prediction_total{error_code="ai_provider_http_error",'
        'failure_category="retryable_http_status",operation="prediction",'
        'outcome="retry_exhausted",status_code="503"} 1\n'
        'provider_prediction_total{error_code="ai_provider_http_error",'
        'failure_category="non_retryable_http_status",operation="prediction",'
        'outcome="fail_fast",status_code="400"} 1\n'
    )


def test_provider_metrics_runbook_findings_explain_core_scenario_samples() -> None:
    findings = build_provider_metrics_runbook_findings(
        build_provider_metrics_runbook_scenario_samples()
    )

    assert findings == [
        {
            "outcome": "success",
            "count": 3,
            "failure_category": "none",
            "status_code": "none",
            "severity": "baseline",
            "finding": "Provider prediction requests are succeeding.",
            "next_action": (
                "Compare the success count with expected request volume before "
                "treating failure samples as system-wide."
            ),
        },
        {
            "outcome": "retry_scheduled",
            "count": 2,
            "failure_category": "retryable_http_status",
            "status_code": "503",
            "severity": "investigate",
            "finding": (
                "Retryable provider failures were observed and retry was scheduled."
            ),
            "next_action": (
                "Check failure_category, status_code, retry delay logs, and whether "
                "retry_exhausted also appears."
            ),
        },
        {
            "outcome": "retry_exhausted",
            "count": 1,
            "failure_category": "retryable_http_status",
            "status_code": "503",
            "severity": "action_required",
            "finding": (
                "Retryable provider failures exhausted the configured attempts."
            ),
            "next_action": (
                "Check max_attempts, provider availability, and the last retryable "
                "failure before changing retry policy."
            ),
        },
        {
            "outcome": "fail_fast",
            "count": 1,
            "failure_category": "non_retryable_http_status",
            "status_code": "400",
            "severity": "contract_check",
            "finding": (
                "A non-retryable provider failure or invalid response was recorded."
            ),
            "next_action": (
                "Do not increase retries first; inspect the request or response "
                "contract and the status_code."
            ),
        },
    ]


def test_provider_metrics_runbook_findings_explain_unknown_outcomes() -> None:
    findings = build_provider_metrics_runbook_findings(
        [
            {
                "labels": {
                    "operation": "prediction",
                    "outcome": "circuit_open",
                    "failure_category": "none",
                    "error_code": "none",
                    "status_code": "none",
                },
                "count": 1,
            }
        ]
    )

    assert findings == [
        {
            "outcome": "circuit_open",
            "count": 1,
            "failure_category": "none",
            "status_code": "none",
            "severity": "unknown",
            "finding": "The metric sample uses an outcome without a runbook branch.",
            "next_action": (
                "Add an explicit runbook branch before treating this metric as "
                "operationally actionable."
            ),
        }
    ]


def test_provider_metrics_runbook_findings_reject_malformed_samples() -> None:
    try:
        build_provider_metrics_runbook_findings([{"labels": [], "count": 1}])
    except ValueError as exc:
        label_error = exc
    else:
        raise AssertionError("Expected ValueError")

    try:
        build_provider_metrics_runbook_findings(
            [{"labels": build_provider_metric_labels(outcome="success").as_dict()}]
        )
    except ValueError as exc:
        count_error = exc
    else:
        raise AssertionError("Expected ValueError")

    assert str(label_error) == "Metric sample labels must be a dictionary."
    assert str(count_error) == "Metric sample count must be an integer."


def test_provider_metrics_runbook_findings_render_as_markdown_table() -> None:
    findings = build_provider_metrics_runbook_findings(
        build_provider_metrics_runbook_scenario_samples()
    )

    markdown = render_provider_metrics_runbook_findings_markdown(findings)

    assert markdown == (
        "| outcome | count | severity | finding | next_action |\n"
        "| --- | ---: | --- | --- | --- |\n"
        "| success | 3 | baseline | Provider prediction requests are succeeding. | "
        "Compare the success count with expected request volume before treating "
        "failure samples as system-wide. |\n"
        "| retry_scheduled | 2 | investigate | Retryable provider failures were "
        "observed and retry was scheduled. | Check failure_category, status_code, "
        "retry delay logs, and whether retry_exhausted also appears. |\n"
        "| retry_exhausted | 1 | action_required | Retryable provider failures "
        "exhausted the configured attempts. | Check max_attempts, provider "
        "availability, and the last retryable failure before changing retry policy. |\n"
        "| fail_fast | 1 | contract_check | A non-retryable provider failure or "
        "invalid response was recorded. | Do not increase retries first; inspect "
        "the request or response contract and the status_code. |\n"
    )


def test_provider_metrics_runbook_exercise_cards_preserve_expected_actions() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )

    assert cards[0] == {
        "id": "provider-metrics-runbook-1",
        "prompt": "Outcome success has count 3. What should you check next?",
        "expected_severity": "baseline",
        "expected_next_action": (
            "Compare the success count with expected request volume before "
            "treating failure samples as system-wide."
        ),
        "answer": (
            "Provider prediction requests are succeeding. Next action: Compare "
            "the success count with expected request volume before treating "
            "failure samples as system-wide."
        ),
    }
    assert [card["expected_severity"] for card in cards] == [
        "baseline",
        "investigate",
        "action_required",
        "contract_check",
    ]


def test_provider_metrics_runbook_exercise_answer_key_renders_cards() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )

    answer_key = render_provider_metrics_runbook_exercise_answer_key(cards)

    assert answer_key.startswith("## provider-metrics-runbook-1\n")
    assert "Expected severity: investigate" in answer_key
    assert (
        "Answer: Retryable provider failures exhausted the configured attempts. "
        "Next action: Check max_attempts, provider availability, and the last "
        "retryable failure before changing retry policy."
    ) in answer_key
    assert answer_key.endswith("\n")


def test_provider_metrics_runbook_exercise_answer_grade_passes_exact_anchors() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )

    grade = grade_provider_metrics_runbook_exercise_answer(
        cards[2],
        (
            "Severity should be ACTION_REQUIRED. Next action: Check max_attempts, "
            "provider availability, and the last retryable failure before changing "
            "retry policy."
        ),
    )

    assert grade == {
        "card_id": "provider-metrics-runbook-3",
        "severity_matched": True,
        "next_action_matched": True,
        "passed": True,
        "missing": [],
        "feedback": "Answer includes the expected severity and next action.",
    }


def test_provider_metrics_runbook_exercise_answer_grade_reports_missing_anchors() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )

    grade = grade_provider_metrics_runbook_exercise_answer(
        cards[3],
        "Increase retries and try again.",
    )

    assert grade == {
        "card_id": "provider-metrics-runbook-4",
        "severity_matched": False,
        "next_action_matched": False,
        "passed": False,
        "missing": ["expected_severity", "expected_next_action"],
        "feedback": "Missing: expected_severity, expected_next_action.",
    }


def test_provider_metrics_runbook_exercise_grades_summary_counts_results() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )

    summary = summarize_provider_metrics_runbook_exercise_grades(
        cards[:3],
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
            "provider-metrics-runbook-2": "investigate retry failures.",
        },
    )

    assert summary["total"] == 3
    assert summary["answered"] == 2
    assert summary["passed"] == 1
    assert summary["failed"] == 2
    assert summary["unanswered"] == 1
    assert summary["grades"][0]["answered"] is True
    assert summary["grades"][0]["passed"] is True
    assert summary["grades"][1]["answered"] is True
    assert summary["grades"][1]["missing"] == ["expected_next_action"]
    assert summary["grades"][2]["answered"] is False
    assert summary["grades"][2]["missing"] == [
        "expected_severity",
        "expected_next_action",
    ]


def test_provider_metrics_runbook_grading_summary_renders_markdown() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )
    summary = summarize_provider_metrics_runbook_exercise_grades(
        cards[:2],
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
            "provider-metrics-runbook-2": "investigate retry failures.",
        },
    )

    markdown = render_provider_metrics_runbook_grading_summary_markdown(summary)

    assert markdown == (
        "## Provider Metrics Runbook Grading Summary\n"
        "\n"
        "| total | answered | passed | failed | unanswered |\n"
        "| ---: | ---: | ---: | ---: | ---: |\n"
        "| 2 | 2 | 1 | 1 | 0 |\n"
        "\n"
        "## Grade Details\n"
        "\n"
        "| card_id | answered | passed | missing | feedback |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| provider-metrics-runbook-1 | True | True | - | "
        "Answer includes the expected severity and next action. |\n"
        "| provider-metrics-runbook-2 | True | False | expected_next_action | "
        "Missing: expected_next_action. |\n"
    )


def test_provider_metrics_runbook_grading_summary_validation_accepts_valid_summary() -> None:
    cards = build_provider_metrics_runbook_exercise_cards(
        build_provider_metrics_runbook_findings(
            build_provider_metrics_runbook_scenario_samples()
        )
    )
    summary = summarize_provider_metrics_runbook_exercise_grades(
        cards[:1],
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
        },
    )

    assert validate_provider_metrics_runbook_grading_summary(summary) == {
        "valid": True,
        "errors": [],
    }


def test_provider_metrics_runbook_grading_summary_validation_reports_contract_errors() -> None:
    validation = validate_provider_metrics_runbook_grading_summary(
        {
            "total": 2,
            "answered": 3,
            "passed": 1,
            "failed": 0,
            "unanswered": 0,
            "grades": [
                {
                    "card_id": "provider-metrics-runbook-1",
                    "answered": "yes",
                    "passed": False,
                    "missing": "expected_next_action",
                }
            ],
        }
    )

    assert validation == {
        "valid": False,
        "errors": [
            "Grade #1 missing field: feedback.",
            "Grade #1 field must be a boolean: answered.",
            "Grade #1 field must be a list: missing.",
            "Summary answered count cannot exceed total.",
            "Summary failed count must equal total - passed.",
            "Summary unanswered count must equal total - answered.",
            "Summary total must equal the number of grades.",
        ],
    }


def test_provider_metrics_runbook_practice_session_builds_end_to_end_artifacts() -> None:
    session = build_provider_metrics_runbook_practice_session(
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
            "provider-metrics-runbook-3": (
                "action_required. Check max_attempts, provider availability, and "
                "the last retryable failure before changing retry policy."
            ),
        }
    )

    assert len(session["samples"]) == 4
    assert len(session["findings"]) == 4
    assert len(session["cards"]) == 4
    assert session["summary"]["total"] == 4
    assert session["summary"]["answered"] == 2
    assert session["summary"]["passed"] == 2
    assert session["summary"]["failed"] == 2
    assert session["summary"]["unanswered"] == 2
    assert session["validation"] == {"valid": True, "errors": []}
    assert session["findings_markdown"].startswith(
        "| outcome | count | severity | finding | next_action |\n"
    )
    assert "## provider-metrics-runbook-1\n" in session["answer_key"]
    assert session["report_markdown"].startswith(
        "## Provider Metrics Runbook Grading Summary\n"
    )


def test_provider_metrics_runbook_practice_session_renders_markdown_package() -> None:
    session = build_provider_metrics_runbook_practice_session(
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
        }
    )

    markdown = render_provider_metrics_runbook_practice_session_markdown(session)

    assert markdown.startswith("# Provider Metrics Runbook Practice Session\n")
    assert "## Findings\n\n| outcome | count | severity | finding | next_action |\n" in markdown
    assert (
        "## Exercise Cards\n\n"
        "| card_id | prompt | expected_severity |\n"
        "| --- | --- | --- |\n"
        "| provider-metrics-runbook-1 | Outcome success has count 3. "
        "What should you check next? | baseline |\n"
    ) in markdown
    assert "## Answer Key\n\n## provider-metrics-runbook-1\n" in markdown
    assert "## Grading Report\n\n## Provider Metrics Runbook Grading Summary\n" in markdown
    assert markdown.endswith("\n")


def test_provider_metrics_runbook_practice_release_checklist_accepts_complete_package() -> None:
    session = build_provider_metrics_runbook_practice_session(
        {
            "provider-metrics-runbook-1": (
                "baseline. Compare the success count with expected request volume "
                "before treating failure samples as system-wide."
            ),
        }
    )
    package_markdown = render_provider_metrics_runbook_practice_session_markdown(session)

    checklist = build_provider_metrics_runbook_practice_release_checklist(
        session,
        package_markdown,
    )

    assert checklist["ready"] is True
    assert [check["id"] for check in checklist["checks"]] == [
        "findings_markdown_present",
        "exercise_cards_present",
        "answer_key_present",
        "grading_summary_valid",
        "grading_report_present",
        "package_sections_present",
    ]
    assert all(check["passed"] for check in checklist["checks"])


def test_provider_metrics_runbook_practice_release_checklist_reports_missing_package_sections() -> None:
    session = build_provider_metrics_runbook_practice_session({})

    checklist = build_provider_metrics_runbook_practice_release_checklist(
        {**session, "report_markdown": ""},
        "# Provider Metrics Runbook Practice Session\n\n## Findings\n",
    )

    assert checklist["ready"] is False
    failed_checks = [
        check["id"] for check in checklist["checks"] if not check["passed"]
    ]
    assert failed_checks == [
        "grading_report_present",
        "package_sections_present",
    ]


def test_provider_metrics_counter_accumulates_samples_by_label_set() -> None:
    counter = ProviderMetricsCounter()
    success_labels = build_provider_metric_labels(outcome="success")
    fail_fast_labels = build_provider_metric_labels(
        outcome="fail_fast",
        failure_category="non_retryable_http_status",
        error_code="ai_provider_http_error",
        status_code=400,
    )

    counter.increment(success_labels)
    counter.increment(success_labels)
    counter.increment(fail_fast_labels)

    assert counter.snapshot() == [
        {
            "labels": fail_fast_labels.as_dict(),
            "count": 1,
        },
        {
            "labels": success_labels.as_dict(),
            "count": 2,
        },
    ]


def test_provider_metrics_counter_snapshot_is_detached_from_counter_state() -> None:
    counter = ProviderMetricsCounter()
    labels = build_provider_metric_labels(outcome="success")

    counter.increment(labels)
    snapshot = counter.snapshot()
    snapshot[0]["count"] = 999
    snapshot[0]["labels"]["outcome"] = "fail_fast"

    assert counter.snapshot() == [
        {
            "labels": labels.as_dict(),
            "count": 1,
        }
    ]


def test_provider_metrics_counter_rejects_non_positive_increment() -> None:
    counter = ProviderMetricsCounter()
    labels = build_provider_metric_labels(outcome="success")

    try:
        counter.increment(labels, amount=0)
    except ValueError as exc:
        error = exc
    else:
        raise AssertionError("Expected ValueError")

    assert str(error) == "Metric increment amount must be positive."


def test_request_provider_prediction_records_success_metric() -> None:
    reset_provider_metrics()

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.876},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        run_async_prediction(client)
        snapshot = get_provider_metrics_snapshot()
    finally:
        asyncio.run(client.aclose())
        reset_provider_metrics()

    assert snapshot == [
        {
            "labels": build_provider_metric_labels(outcome="success").as_dict(),
            "count": 1,
        }
    ]


def test_render_provider_metrics_prometheus_text_uses_stable_text_shape() -> None:
    samples = [
        {
            "labels": build_provider_metric_labels(outcome="success").as_dict(),
            "count": 2,
        },
        {
            "labels": build_provider_metric_labels(
                outcome="fail_fast",
                failure_category="non_retryable_http_status",
                error_code='provider_"quoted"_error',
                status_code=400,
            ).as_dict(),
            "count": 1,
        },
    ]

    text = render_provider_metrics_prometheus_text(samples)

    assert text == (
        "# HELP provider_prediction_total Provider prediction outcomes recorded by "
        "the teaching metrics counter.\n"
        "# TYPE provider_prediction_total counter\n"
        'provider_prediction_total{error_code="none",failure_category="none",'
        'operation="prediction",outcome="success",status_code="none"} 2\n'
        'provider_prediction_total{error_code="provider_\\"quoted\\"_error",'
        'failure_category="non_retryable_http_status",operation="prediction",'
        'outcome="fail_fast",status_code="400"} 1\n'
    )


def test_render_provider_metrics_prometheus_text_handles_empty_snapshot() -> None:
    text = render_provider_metrics_prometheus_text([])

    assert text == (
        "# HELP provider_prediction_total Provider prediction outcomes recorded by "
        "the teaching metrics counter.\n"
        "# TYPE provider_prediction_total counter\n"
    )


def test_render_provider_metrics_prometheus_text_escapes_special_label_values() -> None:
    samples = [
        {
            "labels": build_provider_metric_labels(
                outcome="fail_fast",
                failure_category="invalid_response",
                error_code='line\\one\n"two"',
                status_code=200,
            ).as_dict(),
            "count": 1,
        }
    ]

    text = render_provider_metrics_prometheus_text(samples)

    assert (
        'error_code="line\\\\one\\n\\"two\\""'
        in text
    )


def test_calculate_retry_jitter_uses_bounded_random_fraction() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    jitter = calculate_retry_jitter(config, random_fraction=lambda: 0.4)

    assert jitter == 0.2


def test_calculate_retry_delay_adds_jitter_to_local_backoff() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(attempt=2, config=config, random_fraction=lambda: 0.4)

    assert delay == 2.2


def test_calculate_retry_delay_caps_backoff_after_jitter() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=2.9,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(attempt=1, config=config, random_fraction=lambda: 1.0)

    assert delay == 3.0


def test_parse_retry_after_delay_accepts_delay_seconds() -> None:
    assert parse_retry_after_delay("5") == 5.0


def test_parse_retry_after_delay_accepts_http_date() -> None:
    now = datetime(2026, 7, 4, 12, 0, tzinfo=timezone.utc)
    retry_at = now + timedelta(seconds=7)
    retry_after = format_datetime(retry_at, usegmt=True)

    assert parse_retry_after_delay(retry_after, now=now) == 7.0


def test_calculate_retry_delay_prefers_retry_after_with_cap() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(
        attempt=1,
        config=config,
        retry_after="5",
        random_fraction=lambda: 1.0,
    )

    assert delay == 3.0


def test_calculate_retry_delay_ignores_invalid_retry_after() -> None:
    config = AIClientConfig(
        provider="demo",
        timeout_seconds=0.5,
        max_attempts=3,
        retry_base_delay_seconds=1.0,
        retry_max_delay_seconds=3.0,
        retry_jitter_seconds=0.5,
    )

    delay = calculate_retry_delay(
        attempt=2,
        config=config,
        retry_after="later",
        random_fraction=lambda: 0.4,
    )

    assert delay == 2.2


def test_check_provider_health_returns_internal_result_for_success() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=200, json={"status": "ok"}, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_health_check(client)
    finally:
        asyncio.run(client.aclose())

    assert result.ok is True
    assert result.provider == "demo"
    assert result.status_code == 200
    assert result.message == "The AI provider responded successfully."


def test_check_provider_health_maps_timeout_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("Read timed out.", request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_health_check(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_timeout"
    assert error.message == "The AI provider health check timed out."


def test_check_provider_health_maps_http_error_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=503, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_health_check(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."


def test_request_provider_prediction_sends_payload_and_maps_response() -> None:
    captured_request_body = {}

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal captured_request_body
        captured_request_body = json.loads(request.content)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.876},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client)
    finally:
        asyncio.run(client.aclose())

    assert captured_request_body == {
        "text": "FastAPI is great and pleasant.",
        "mode": "careful",
    }
    assert result.label == "positive"
    assert result.score == 0.88
    assert result.source == "demo-provider"


def test_request_provider_prediction_maps_invalid_json_to_ai_client_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json={"label": "confused", "score": 1.5},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_invalid_response"
    assert error.message == "The AI provider returned an invalid prediction response."


def test_request_provider_prediction_maps_provider_http_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code=503, request=request)

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."


def test_request_provider_prediction_retries_retryable_http_error_then_succeeds() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.93},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client, max_attempts=2)
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert result.label == "positive"
    assert result.score == 0.93


def test_request_provider_prediction_retries_timeout_then_succeeds() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ReadTimeout("Read timed out.", request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.91},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(client, max_attempts=2)
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert result.label == "positive"
    assert result.score == 0.91


def test_request_provider_prediction_waits_between_retryable_failures() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.95},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=3,
            retry_base_delay_seconds=1.0,
            retry_max_delay_seconds=3.0,
            retry_jitter_seconds=0.0,
            sleep=fake_sleep,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 3
    assert sleep_calls == [1.0, 2.0]
    assert result.label == "positive"
    assert result.score == 0.95


def test_request_provider_prediction_uses_retry_after_header() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                status_code=429,
                headers={"Retry-After": "2"},
                request=request,
            )
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.94},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=0.1,
            retry_max_delay_seconds=5.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 1.0,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert sleep_calls == [2.0]
    assert result.label == "positive"
    assert result.score == 0.94


def test_request_provider_prediction_adds_jitter_to_local_retry_delay() -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(status_code=503, request=request)
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.92},
            request=request,
        )

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=1.0,
            retry_max_delay_seconds=3.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 0.4,
        )
    finally:
        asyncio.run(client.aclose())

    assert attempts == 2
    assert sleep_calls == [1.2]
    assert result.label == "positive"
    assert result.score == 0.92


def test_request_provider_prediction_logs_retry_schedule_for_http_error(caplog) -> None:
    attempts = 0
    sleep_calls = []

    async def fake_sleep(delay_seconds: float) -> None:
        sleep_calls.append(delay_seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                status_code=429,
                headers={"Retry-After": "2"},
                request=request,
            )
        return httpx.Response(
            status_code=200,
            json={"label": "positive", "score": 0.96},
            request=request,
        )

    caplog.set_level(logging.INFO, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        result = run_async_prediction(
            client,
            max_attempts=2,
            retry_base_delay_seconds=0.1,
            retry_max_delay_seconds=5.0,
            retry_jitter_seconds=0.5,
            sleep=fake_sleep,
            random_fraction=lambda: 1.0,
        )
    finally:
        asyncio.run(client.aclose())

    retry_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_scheduled"
    ]

    assert attempts == 2
    assert sleep_calls == [2.0]
    assert result.label == "positive"
    assert len(retry_records) == 1
    assert retry_records[0].attempt == 1
    assert retry_records[0].max_attempts == 2
    assert retry_records[0].retry_reason == "http_status"
    assert retry_records[0].status_code == 429
    assert retry_records[0].retry_after == "2"
    assert retry_records[0].delay_seconds == 2.0
    assert retry_records[0].delay_source == "retry_after"


def test_request_provider_prediction_stops_after_max_attempts(caplog) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(status_code=503, request=request)

    caplog.set_level(logging.WARNING, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    exhausted_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_exhausted"
    ]

    assert attempts == 3
    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 503."
    assert len(exhausted_records) == 1
    assert exhausted_records[0].attempt == 3
    assert exhausted_records[0].max_attempts == 3
    assert exhausted_records[0].retry_reason == "http_status"
    assert exhausted_records[0].status_code == 503
    assert exhausted_records[0].retry_after is None
    assert exhausted_records[0].error_code == "ai_provider_http_error"


def test_request_provider_prediction_does_not_retry_non_retryable_http_error(caplog) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(status_code=400, request=request)

    caplog.set_level(logging.WARNING, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    fail_fast_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_fail_fast"
    ]
    exhausted_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_exhausted"
    ]

    assert attempts == 1
    assert error.error_code == "ai_provider_http_error"
    assert error.message == "The AI provider returned HTTP 400."
    assert len(fail_fast_records) == 1
    assert fail_fast_records[0].attempt == 1
    assert fail_fast_records[0].max_attempts == 3
    assert fail_fast_records[0].fail_fast_reason == "http_status"
    assert fail_fast_records[0].status_code == 400
    assert fail_fast_records[0].error_code == "ai_provider_http_error"
    assert exhausted_records == []


def test_request_provider_prediction_does_not_retry_invalid_response(caplog) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(
            status_code=200,
            json={"label": "confused", "score": 1.5},
            request=request,
        )

    caplog.set_level(logging.WARNING, logger="first_api.services.provider_http")

    transport = httpx.MockTransport(handler)
    client = httpx.AsyncClient(transport=transport)
    try:
        try:
            run_async_prediction(client, max_attempts=3)
        except AIClientError as exc:
            error = exc
        else:
            raise AssertionError("Expected AIClientError")
    finally:
        asyncio.run(client.aclose())

    fail_fast_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_fail_fast"
    ]
    exhausted_records = [
        record
        for record in caplog.records
        if record.getMessage() == "provider_prediction_retry_exhausted"
    ]

    assert attempts == 1
    assert error.error_code == "ai_provider_invalid_response"
    assert len(fail_fast_records) == 1
    assert fail_fast_records[0].attempt == 1
    assert fail_fast_records[0].max_attempts == 3
    assert fail_fast_records[0].fail_fast_reason == "invalid_response"
    assert fail_fast_records[0].status_code == 200
    assert fail_fast_records[0].error_code == "ai_provider_invalid_response"
    assert exhausted_records == []
