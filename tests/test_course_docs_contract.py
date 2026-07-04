from html.parser import HTMLParser
from pathlib import Path


class LinkAndTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if href is not None:
            self.links.append(href)

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.text_parts.append(data.strip())

    @property
    def text(self) -> str:
        return " ".join(self.text_parts)


def parse_html(path: Path) -> LinkAndTextParser:
    parser = LinkAndTextParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def test_rebuilt_foundation_lessons_use_exam_review_structure() -> None:
    lesson_paths = [
        Path("lessons/0001-first-fastapi-api.html"),
        Path("lessons/0002-request-body-pydantic.html"),
        Path("lessons/0003-path-and-query-parameters.html"),
        Path("lessons/0004-response-models-and-errors.html"),
        Path("lessons/0005-project-structure-apirouter.html"),
        Path("lessons/0006-dependencies-depends.html"),
        Path("lessons/0007-sqlite-sqlmodel-basics.html"),
        Path("lessons/0008-database-session-crud.html"),
        Path("lessons/0009-update-delete-crud.html"),
        Path("lessons/0010-api-testing-testclient.html"),
        Path("lessons/0011-settings-env-vars.html"),
        Path("lessons/0012-api-key-auth.html"),
        Path("lessons/0013-background-tasks.html"),
        Path("lessons/0014-task-status-api.html"),
        Path("lessons/0015-uploadfile-text-files.html"),
        Path("lessons/0016-file-summary-tasks.html"),
        Path("lessons/0017-cors-browser-frontend.html"),
        Path("lessons/0018-static-frontend-fetch.html"),
        Path("lessons/0019-service-layer-thin-routers.html"),
        Path("lessons/0020-ai-client-dependency.html"),
        Path("lessons/0021-ai-client-errors.html"),
        Path("lessons/0022-task-failure-status.html"),
        Path("lessons/0023-task-list-pagination.html"),
        Path("lessons/0024-task-status-filter.html"),
        Path("lessons/0025-list-response-envelope.html"),
        Path("lessons/0026-count-query.html"),
        Path("lessons/0027-frontend-task-history.html"),
        Path("lessons/0028-frontend-pagination-status-filter.html"),
        Path("lessons/0029-openapi-api-contract.html"),
        Path("lessons/0030-schema-evolution-compatibility.html"),
        Path("lessons/0031-real-ai-provider-boundary.html"),
        Path("lessons/0032-fastapi-async-basics.html"),
        Path("lessons/0033-async-http-provider-adapter.html"),
        Path("lessons/0034-lifespan-http-client.html"),
        Path("lessons/0035-app-state-dependency-bridge.html"),
        Path("lessons/0036-provider-health-endpoint.html"),
        Path("lessons/0037-provider-prediction-adapter.html"),
        Path("lessons/0038-provider-predict-endpoint.html"),
        Path("lessons/0039-prediction-backend-switch.html"),
        Path("lessons/0040-prediction-observability.html"),
        Path("lessons/0041-prediction-service-orchestration.html"),
        Path("lessons/0042-provider-retry-policy.html"),
        Path("lessons/0043-backoff-before-retry.html"),
        Path("lessons/0044-honor-retry-after.html"),
        Path("lessons/0045-retry-jitter.html"),
        Path("lessons/0046-retry-observability.html"),
        Path("lessons/0047-retry-exhaustion.html"),
        Path("lessons/0048-fail-fast-observability.html"),
        Path("lessons/0049-provider-error-taxonomy.html"),
        Path("lessons/0050-provider-metrics-basics.html"),
        Path("lessons/0051-provider-metrics-counters.html"),
        Path("lessons/0052-provider-metrics-endpoint.html"),
        Path("lessons/0053-provider-metrics-failure-outcomes.html"),
        Path("lessons/0054-provider-metrics-test-isolation.html"),
        Path("lessons/0055-provider-metrics-export-shape.html"),
        Path("lessons/0056-provider-metrics-export-tests.html"),
        Path("lessons/0057-provider-metrics-snapshot-boundary.html"),
        Path("lessons/0058-provider-metrics-production-boundary.html"),
        Path("lessons/0059-provider-metrics-naming-contract.html"),
        Path("lessons/0060-provider-metrics-naming-refactor-boundary.html"),
        Path("lessons/0061-provider-metrics-documentation-index.html"),
        Path("lessons/0062-provider-metrics-runbook-checklist.html"),
        Path("lessons/0063-provider-metrics-scenario-fixtures.html"),
        Path("lessons/0064-provider-metrics-runbook-findings.html"),
    ]
    required_sections = [
        "① 本节核心知识框架",
        "② 核心概念底层原理",
        "③ 全套代码逐行精读解析",
        "④ 核心机制运行全流程拆解",
        "⑤ 重难点、易混淆点对比辨析",
        "⑥ 开发常见报错+坑点+解决方案",
        "⑦ 生产环境 vs 教学环境 核心差异",
        "⑧ 课后记忆习题+标准答案",
        "⑨ 面试高频真题+解析",
    ]

    for lesson_path in lesson_paths:
        parser = parse_html(lesson_path)

        for section in required_sections:
            assert section in parser.text
        assert "Final Review + CSDN Deep Dive" in parser.text


def test_provider_metrics_documentation_index_lists_operational_contract() -> None:
    docs_index = Path("reference/provider-metrics-index.html")

    parser = parse_html(docs_index)

    assert "/provider/metrics" in parser.text
    assert "/provider/metrics/prometheus" in parser.text
    assert "provider_prediction_total" in parser.text
    assert "get_provider_prediction_metric_contract" in parser.text
    assert "not a production multi-instance metrics pipeline" in parser.text


def test_provider_metrics_documentation_index_links_learning_and_tests() -> None:
    docs_index = Path("reference/provider-metrics-index.html")

    parser = parse_html(docs_index)

    assert "../lessons/0058-provider-metrics-production-boundary.html" in parser.links
    assert "../lessons/0059-provider-metrics-naming-contract.html" in parser.links
    assert "../lessons/0060-provider-metrics-naming-refactor-boundary.html" in parser.links
    assert "../lessons/0061-provider-metrics-documentation-index.html" in parser.links
    assert "../lessons/0062-provider-metrics-runbook-checklist.html" in parser.links
    assert "../lessons/0063-provider-metrics-scenario-fixtures.html" in parser.links
    assert "../lessons/0064-provider-metrics-runbook-findings.html" in parser.links
    assert "../tests/test_provider_http.py" in parser.links
    assert "../tests/test_openapi_contract.py" in parser.links


def test_provider_metrics_runbook_lists_investigation_contract() -> None:
    runbook = Path("reference/provider-metrics-runbook.html")

    parser = parse_html(runbook)

    assert "/provider/metrics" in parser.text
    assert "/provider/metrics/prometheus" in parser.text
    assert "provider_prediction_total" in parser.text
    assert "success" in parser.text
    assert "retry_scheduled" in parser.text
    assert "retry_exhausted" in parser.text
    assert "fail_fast" in parser.text
    assert "teaching signal, not a paging alert" in parser.text


def test_provider_metrics_runbook_links_docs_lessons_and_tests() -> None:
    runbook = Path("reference/provider-metrics-runbook.html")

    parser = parse_html(runbook)

    assert "./provider-metrics-index.html" in parser.links
    assert "../lessons/0062-provider-metrics-runbook-checklist.html" in parser.links
    assert "../lessons/0063-provider-metrics-scenario-fixtures.html" in parser.links
    assert "../lessons/0064-provider-metrics-runbook-findings.html" in parser.links
    assert "../tests/test_provider_http.py" in parser.links
    assert "../tests/test_ai_client_dependency.py" in parser.links
    assert "../tests/test_course_docs_contract.py" in parser.links
