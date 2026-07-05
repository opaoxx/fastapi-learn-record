from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


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


def iter_static_course_html_pages() -> list[Path]:
    return [
        Path("index.html"),
        *Path("lessons").glob("*.html"),
        *Path("reference").glob("*.html"),
    ]


def is_repository_local_href(href: str) -> bool:
    return not href.startswith(("http://", "https://", "mailto:", "#"))


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
        Path("lessons/0065-provider-metrics-findings-markdown-report.html"),
        Path("lessons/0066-provider-metrics-runbook-exercise-cards.html"),
        Path("lessons/0067-provider-metrics-exercise-answer-key.html"),
        Path("lessons/0068-provider-metrics-exercise-grading-anchors.html"),
        Path("lessons/0069-provider-metrics-grading-summary.html"),
        Path("lessons/0070-provider-metrics-grading-summary-markdown.html"),
        Path("lessons/0071-provider-metrics-grading-summary-validation.html"),
        Path("lessons/0072-provider-metrics-practice-session-package.html"),
        Path("lessons/0073-provider-metrics-practice-session-markdown.html"),
        Path("lessons/0074-provider-metrics-practice-release-checklist.html"),
        Path("lessons/0075-github-readme-learning-entry.html"),
        Path("lessons/0076-github-development-workflow.html"),
        Path("lessons/0077-github-actions-ci-workflow.html"),
        Path("lessons/0078-github-branch-protection-required-checks.html"),
        Path("lessons/0079-github-pull-request-template.html"),
        Path("lessons/0080-github-codeowners-review-ownership.html"),
        Path("lessons/0081-github-issue-templates.html"),
        Path("lessons/0082-github-issue-triage-labels-workflow.html"),
        Path("lessons/0083-github-projects-board-workflow.html"),
        Path("lessons/0084-github-discussions-course-qa-workflow.html"),
        Path("lessons/0085-github-release-notes-tags-workflow.html"),
        Path("lessons/0086-changelog-maintenance-workflow.html"),
        Path("lessons/0087-contributing-guide-workflow.html"),
        Path("lessons/0088-code-of-conduct-workflow.html"),
        Path("lessons/0089-security-policy-workflow.html"),
        Path("lessons/0090-license-reuse-boundary.html"),
        Path("lessons/0091-env-example-local-config-hygiene.html"),
        Path("lessons/0092-github-pages-offline-html-workflow.html"),
        Path("lessons/0093-repository-final-quality-audit-checklist.html"),
        Path("lessons/0094-static-link-navigation-contract-audit.html"),
        Path("lessons/0095-release-candidate-versioned-publishing-readiness.html"),
        Path("lessons/0096-full-course-completion-release-runbook.html"),
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
    assert "../lessons/0065-provider-metrics-findings-markdown-report.html" in parser.links
    assert "../lessons/0066-provider-metrics-runbook-exercise-cards.html" in parser.links
    assert "../lessons/0067-provider-metrics-exercise-answer-key.html" in parser.links
    assert "../lessons/0068-provider-metrics-exercise-grading-anchors.html" in parser.links
    assert "../lessons/0069-provider-metrics-grading-summary.html" in parser.links
    assert "../lessons/0070-provider-metrics-grading-summary-markdown.html" in parser.links
    assert "../lessons/0071-provider-metrics-grading-summary-validation.html" in parser.links
    assert "../lessons/0072-provider-metrics-practice-session-package.html" in parser.links
    assert "../lessons/0073-provider-metrics-practice-session-markdown.html" in parser.links
    assert "../lessons/0074-provider-metrics-practice-release-checklist.html" in parser.links
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


def test_audited_late_lessons_include_quality_audit_reinforcement() -> None:
    lesson_paths = [
        Path("lessons/0065-provider-metrics-findings-markdown-report.html"),
        Path("lessons/0066-provider-metrics-runbook-exercise-cards.html"),
        Path("lessons/0067-provider-metrics-exercise-answer-key.html"),
        Path("lessons/0068-provider-metrics-exercise-grading-anchors.html"),
        Path("lessons/0069-provider-metrics-grading-summary.html"),
        Path("lessons/0070-provider-metrics-grading-summary-markdown.html"),
        Path("lessons/0071-provider-metrics-grading-summary-validation.html"),
        Path("lessons/0072-provider-metrics-practice-session-package.html"),
        Path("lessons/0073-provider-metrics-practice-session-markdown.html"),
        Path("lessons/0074-provider-metrics-practice-release-checklist.html"),
        Path("lessons/0075-github-readme-learning-entry.html"),
        Path("lessons/0076-github-development-workflow.html"),
    ]

    for lesson_path in lesson_paths:
        parser = parse_html(lesson_path)

        assert "复核补强" in parser.text
        assert "逐行精读补充" in parser.text


def test_root_readme_guides_github_learners_to_course_and_runbook() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")

    assert "[课程总目录](index.html)" in readme
    assert "[first_api/README.md](first_api/README.md)" in readme
    assert "[开发工作流](DEVELOPMENT.md)" in readme
    assert "[Provider Metrics 文档入口](reference/provider-metrics-index.html)" in readme
    assert "[Provider Metrics 排障清单](reference/provider-metrics-runbook.html)" in readme
    assert "[Lesson 0072 - Practice Session Package](lessons/0072-provider-metrics-practice-session-package.html)" in readme
    assert "[Lesson 0073 - Practice Session Markdown](lessons/0073-provider-metrics-practice-session-markdown.html)" in readme
    assert "[Lesson 0074 - Practice Release Checklist](lessons/0074-provider-metrics-practice-release-checklist.html)" in readme
    assert "[.github/workflows/ci.yml](.github/workflows/ci.yml)" in readme
    assert "[.github/BRANCH_PROTECTION.md](.github/BRANCH_PROTECTION.md)" in readme
    assert "[.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)" in readme
    assert "[.github/CODEOWNERS](.github/CODEOWNERS)" in readme
    assert "[.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)" in readme
    assert "[.github/ISSUE_TRIAGE.md](.github/ISSUE_TRIAGE.md)" in readme
    assert "[.github/PROJECT_BOARD.md](.github/PROJECT_BOARD.md)" in readme
    assert "[.github/DISCUSSIONS.md](.github/DISCUSSIONS.md)" in readme
    assert "[.github/RELEASE_PROCESS.md](.github/RELEASE_PROCESS.md)" in readme
    assert "[CHANGELOG.md](CHANGELOG.md)" in readme
    assert "[CONTRIBUTING.md](CONTRIBUTING.md)" in readme
    assert "[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)" in readme
    assert "[SECURITY.md](SECURITY.md)" in readme
    assert "[LICENSE](LICENSE)" in readme
    assert "[.env.example](.env.example)" in readme
    assert "[.github/PAGES.md](.github/PAGES.md)" in readme
    assert "[.github/FINAL_AUDIT.md](.github/FINAL_AUDIT.md)" in readme
    assert "[.github/LINK_AUDIT.md](.github/LINK_AUDIT.md)" in readme
    assert "[.github/RELEASE_CANDIDATE.md](.github/RELEASE_CANDIDATE.md)" in readme
    assert "[.github/COURSE_COMPLETION.md](.github/COURSE_COMPLETION.md)" in readme
    assert "fastapi dev first_api/main.py" in readme
    assert "python -m pytest -q" in readme
    assert "python -m pytest tests/test_course_docs_contract.py -q" in readme


def test_development_workflow_documents_course_maintenance_contract() -> None:
    workflow = Path("DEVELOPMENT.md").read_text(encoding="utf-8")

    assert "Code Change Checklist" in workflow
    assert "Lesson Change Checklist" in workflow
    assert "Documentation Change Checklist" in workflow
    assert "GitHub Release Readiness" in workflow
    assert ".github/workflows/ci.yml" in workflow
    assert ".github/BRANCH_PROTECTION.md" in workflow
    assert ".github/PULL_REQUEST_TEMPLATE.md" in workflow
    assert ".github/CODEOWNERS" in workflow
    assert ".github/ISSUE_TEMPLATE/" in workflow
    assert ".github/ISSUE_TRIAGE.md" in workflow
    assert ".github/PROJECT_BOARD.md" in workflow
    assert ".github/DISCUSSIONS.md" in workflow
    assert ".github/RELEASE_PROCESS.md" in workflow
    assert "CHANGELOG.md" in workflow
    assert "CONTRIBUTING.md" in workflow
    assert "CODE_OF_CONDUCT.md" in workflow
    assert "SECURITY.md" in workflow
    assert "LICENSE" in workflow
    assert ".env.example" in workflow
    assert ".github/PAGES.md" in workflow
    assert ".github/FINAL_AUDIT.md" in workflow
    assert ".github/LINK_AUDIT.md" in workflow
    assert ".github/RELEASE_CANDIDATE.md" in workflow
    assert ".github/COURSE_COMPLETION.md" in workflow
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in workflow
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in workflow
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in workflow
    assert "git diff --check" in workflow
    assert "① 本节核心知识框架" in workflow
    assert "⑨ 面试高频真题+解析" in workflow


def test_github_actions_ci_runs_course_quality_gates() -> None:
    workflow = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "Course CI" in workflow
    assert "push:" in workflow
    assert "pull_request:" in workflow
    assert "actions/checkout@v4" in workflow
    assert "actions/setup-python@v5" in workflow
    assert 'python-version: "3.11"' in workflow
    assert "python -m pip install -r requirements.txt" in workflow
    assert "python -m pytest tests/test_provider_http.py -q" in workflow
    assert "python -m pytest tests/test_course_docs_contract.py -q" in workflow
    assert "python -m pytest -q" in workflow
    assert "git diff --check" in workflow


def test_branch_protection_documents_required_status_check() -> None:
    protection = Path(".github/BRANCH_PROTECTION.md").read_text(encoding="utf-8")

    assert "Branch Protection Required Checks" in protection
    assert "main" in protection
    assert "Require a pull request before merging" in protection
    assert "Require status checks to pass before merging" in protection
    assert "Require branches to be up to date before merging" in protection
    assert "Require conversation resolution before merging" in protection
    assert "Block force pushes" in protection
    assert "Block branch deletion" in protection
    assert "pytest and documentation contracts" in protection
    assert ".github/workflows/ci.yml" in protection


def test_pull_request_template_guides_course_contributors() -> None:
    template = Path(".github/PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")

    assert "Pull Request Checklist" in template
    assert "Summary" in template
    assert "What changed" in template
    assert "Why it changed" in template
    assert "Change Type" in template
    assert "Code behavior" in template
    assert "Lesson or reference page" in template
    assert "README, DEVELOPMENT, or GitHub documentation" in template
    assert "Tests or CI" in template
    assert "Verification" in template
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in template
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in template
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in template
    assert "git diff --check" in template
    assert "Course Documentation Checklist" in template
    assert "index.html" in template
    assert "NOTES.md" in template
    assert "COURSE_PROGRESS.md" in template
    assert "documentation contract tests" in template
    assert "Risk Notes" in template


def test_codeowners_maps_repository_ownership() -> None:
    owners = Path(".github/CODEOWNERS").read_text(encoding="utf-8")

    assert "CODEOWNERS teaching template" in owners
    assert "Replace these placeholder teams with real GitHub users" in owners
    assert "* @course-maintainers" in owners
    assert "/first_api/ @backend-maintainers" in owners
    assert "/tests/ @quality-maintainers" in owners
    assert "/lessons/ @course-maintainers" in owners
    assert "/reference/ @course-maintainers" in owners
    assert "/learning-records/ @course-maintainers" in owners
    assert "/README.md @repository-maintainers" in owners
    assert "/DEVELOPMENT.md @repository-maintainers" in owners
    assert "/COURSE-STANDARD.md @course-maintainers" in owners
    assert "/NOTES.md @course-maintainers" in owners
    assert "/COURSE_PROGRESS.md @course-maintainers" in owners
    assert "/.github/ @repository-maintainers" in owners


def test_issue_templates_collect_course_maintenance_requests() -> None:
    bug = Path(".github/ISSUE_TEMPLATE/bug_report.yml").read_text(encoding="utf-8")
    lesson = Path(".github/ISSUE_TEMPLATE/lesson_request.yml").read_text(encoding="utf-8")
    docs = Path(".github/ISSUE_TEMPLATE/documentation_fix.yml").read_text(encoding="utf-8")
    config = Path(".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")

    assert "name: Bug report" in bug
    assert 'labels: ["bug"]' in bug
    assert "id: steps" in bug
    assert "id: expected" in bug
    assert "id: actual" in bug
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in bug
    assert "git diff --check" in bug

    assert "name: Lesson request" in lesson
    assert 'labels: ["course", "lesson-request"]' in lesson
    assert "id: lesson-range" in lesson
    assert "id: learning-gap" in lesson
    assert "id: required-depth" in lesson
    assert "id: output-type" in lesson
    assert "New lesson HTML + quick reference" in lesson
    assert "Existing lesson audit and refactor" in lesson

    assert "name: Documentation fix" in docs
    assert 'labels: ["documentation"]' in docs
    assert "id: file" in docs
    assert "id: course-standard" in docs
    assert "The nine-section lesson structure may need to be checked." in docs
    assert "index.html, README.md, NOTES.md, or COURSE_PROGRESS.md" in docs

    assert "blank_issues_enabled: false" in config
    assert "Course reading entry" in config


def test_issue_triage_documents_label_workflow() -> None:
    triage = Path(".github/ISSUE_TRIAGE.md").read_text(encoding="utf-8")

    assert "Issue Triage Workflow" in triage
    assert "Label Taxonomy" in triage
    assert "`type:bug`" in triage
    assert "`type:lesson`" in triage
    assert "`type:docs`" in triage
    assert "`type:workflow`" in triage
    assert "`area:api`" in triage
    assert "`area:tests`" in triage
    assert "`area:lessons`" in triage
    assert "`area:reference`" in triage
    assert "`area:github`" in triage
    assert "`priority:p0`" in triage
    assert "`priority:p1`" in triage
    assert "`priority:p2`" in triage
    assert "`priority:p3`" in triage
    assert "`status:needs-repro`" in triage
    assert "`status:needs-design`" in triage
    assert "`status:ready`" in triage
    assert "`status:blocked`" in triage
    assert "`status:done`" in triage
    assert "Assign exactly one type label." in triage
    assert "Assign at least one area label." in triage
    assert "Assign one priority label." in triage
    assert "Assign one status label." in triage
    assert "Create the labels in GitHub repository settings" in triage


def test_project_board_documents_execution_workflow() -> None:
    board = Path(".github/PROJECT_BOARD.md").read_text(encoding="utf-8")

    assert "GitHub Projects Board Workflow" in board
    assert "Board Purpose" in board
    assert "Required Fields" in board
    assert "Status" in board
    assert "`Intake`" in board
    assert "`Needs Repro`" in board
    assert "`Needs Design`" in board
    assert "`Ready`" in board
    assert "`In Progress`" in board
    assert "`In Review`" in board
    assert "`Blocked`" in board
    assert "`Done`" in board
    assert "Priority" in board
    assert "`P0`" in board
    assert "`P1`" in board
    assert "`P2`" in board
    assert "`P3`" in board
    assert "Area" in board
    assert "`API`" in board
    assert "`Tests`" in board
    assert "`Lessons`" in board
    assert "`Reference`" in board
    assert "`GitHub`" in board
    assert "Type" in board
    assert "`Bug`" in board
    assert "`Lesson`" in board
    assert "`Docs`" in board
    assert "`Workflow`" in board
    assert "Triage Queue" in board
    assert "Ready Work" in board
    assert "Course Docs" in board
    assert "GitHub Workflow" in board
    assert "Done Review" in board
    assert "`status:needs-repro`" in board
    assert "`status:ready`" in board
    assert "`status:done`" in board
    assert "project item Status field must agree" in board
    assert "GitHub Projects configuration is remote state" in board


def test_discussions_document_course_qa_workflow() -> None:
    discussions = Path(".github/DISCUSSIONS.md").read_text(encoding="utf-8")

    assert "GitHub Discussions Workflow" in discussions
    assert "Recommended Categories" in discussions
    assert "Q&A" in discussions
    assert "Study Notes" in discussions
    assert "Ideas" in discussions
    assert "Show and Tell" in discussions
    assert "Announcements" in discussions
    assert "Issue vs Discussion Decision Rules" in discussions
    assert "The work is reproducible, scoped, and should change repository files." in discussions
    assert "The topic is exploratory, open-ended, or primarily educational." in discussions
    assert "Maintainers can define done." in discussions
    assert "Answer Quality Checklist" in discussions
    assert "Link the relevant lesson, reference page, source file, or test file." in discussions
    assert "Distinguish teaching demo behavior from production behavior." in discussions
    assert "If the discussion reveals repository work, open or link an issue." in discussions
    assert "Conversion Flow" in discussions
    assert "link discussion and issue both ways" in discussions
    assert "Enable GitHub Discussions in repository settings" in discussions


def test_release_process_documents_course_batch_publishing() -> None:
    release = Path(".github/RELEASE_PROCESS.md").read_text(encoding="utf-8")

    assert "GitHub Release Process" in release
    assert "GitHub Releases are remote state" in release
    assert "Release Purpose" in release
    assert "traceable learning checkpoint" in release
    assert "Tag Naming" in release
    assert "course-vYYYY.MM.DD-N" in release
    assert "Use annotated tags" in release
    assert "Never move a published tag silently" in release
    assert "Release Notes Structure" in release
    assert "Changed Lessons" in release
    assert "Changed References" in release
    assert "Code and Workflow Changes" in release
    assert "Verification" in release
    assert "Known Warnings" in release
    assert "Rollback" in release
    assert "docs contract" in release
    assert "provider HTTP" in release
    assert "full pytest" in release
    assert "git diff --check" in release
    assert "Windows LF-to-CRLF notices" in release
    assert "create annotated tag" in release
    assert "create GitHub Release from tag" in release


def test_changelog_documents_release_ledger() -> None:
    changelog = Path("CHANGELOG.md").read_text(encoding="utf-8")

    assert "Changelog" in changelog
    assert "local release ledger" in changelog
    assert "GitHub Release Notes summarize a published tag" in changelog
    assert "Unreleased" in changelog
    assert "Added" in changelog
    assert "Changed" in changelog
    assert "Fixed" in changelog
    assert "Tests" in changelog
    assert "Governance" in changelog
    assert "Entry Rules" in changelog
    assert "learner-visible changes" in changelog
    assert "test contract changes" in changelog
    assert "GitHub workflow changes" in changelog
    assert "COURSE_PROGRESS.md" in changelog
    assert "Release Heading Format" in changelog
    assert "course-vYYYY.MM.DD-N - YYYY-MM-DD" in changelog
    assert "Changelog vs Release Notes vs Course Progress" in changelog
    assert "CONTRIBUTING.md" in changelog
    assert "CODE_OF_CONDUCT.md" in changelog
    assert "SECURITY.md" in changelog
    assert "LICENSE" in changelog
    assert ".env.example" in changelog
    assert ".github/PAGES.md" in changelog
    assert ".github/FINAL_AUDIT.md" in changelog
    assert ".github/LINK_AUDIT.md" in changelog
    assert ".github/RELEASE_CANDIDATE.md" in changelog
    assert ".github/COURSE_COMPLETION.md" in changelog


def test_contributing_guide_documents_contributor_workflow() -> None:
    contributing = Path("CONTRIBUTING.md").read_text(encoding="utf-8")

    assert "Contributing Guide" in contributing
    assert "runnable FastAPI project and a structured learning archive" in contributing
    assert "Contribution Scope" in contributing
    assert "Open a discussion first" in contributing
    assert "Open an issue when the work is reproducible" in contributing
    assert "Before You Start" in contributing
    assert "README.md" in contributing
    assert "DEVELOPMENT.md" in contributing
    assert "CHANGELOG.md" in contributing
    assert "Branch and Commit Workflow" in contributing
    assert "course/add-lesson-0087-contributing" in contributing
    assert "Lesson Contribution Standard" in contributing
    assert "① 本节核心知识框架" in contributing
    assert "⑨ 面试高频真题+解析" in contributing
    assert "Final Review + CSDN Deep Dive" in contributing
    assert "Documentation Checklist" in contributing
    assert "COURSE_PROGRESS.md" in contributing
    assert "Required Verification" in contributing
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in contributing
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in contributing
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in contributing
    assert "git diff --check" in contributing
    assert "Pull Request Requirements" in contributing
    assert ".github/PULL_REQUEST_TEMPLATE.md" in contributing
    assert "Review and Ownership" in contributing
    assert ".github/CODEOWNERS" in contributing
    assert "Changelog and Release Notes" in contributing
    assert ".github/RELEASE_PROCESS.md" in contributing
    assert "Do not post secrets" in contributing


def test_code_of_conduct_documents_collaboration_safety() -> None:
    conduct = Path("CODE_OF_CONDUCT.md").read_text(encoding="utf-8")

    assert "Code of Conduct" in conduct
    assert "beginner-safe technical learning space" in conduct
    assert "Expected Behavior" in conduct
    assert "Critique code, documentation, claims, and evidence rather than attacking people." in conduct
    assert "Unacceptable Behavior" in conduct
    assert "Mocking beginner questions or using shame as a teaching method." in conduct
    assert "credentials, tokens, private logs, personal data, or proprietary source code" in conduct
    assert "Pressuring maintainers to bypass tests, review, branch protection, or documented release rules." in conduct
    assert "AI-generated or copied material" in conduct
    assert "Scope" in conduct
    assert "Reporting" in conduct
    assert "Save links, screenshots, timestamps, and the affected repository area." in conduct
    assert "Maintainer Response" in conduct
    assert "Pause review until behavior or safety concerns are resolved." in conduct
    assert "Teaching and Review Norms" in conduct
    assert "Strong review is welcome. Contempt is not." in conduct
    assert "Safety Boundary" in conduct
    assert "security issue" in conduct
    assert "Relationship to Other Documents" in conduct
    assert "CONTRIBUTING.md" in conduct
    assert "DEVELOPMENT.md" in conduct
    assert ".github/DISCUSSIONS.md" in conduct
    assert ".github/ISSUE_TRIAGE.md" in conduct
    assert ".github/RELEASE_PROCESS.md" in conduct


def test_security_policy_documents_private_disclosure_workflow() -> None:
    security = Path("SECURITY.md").read_text(encoding="utf-8")

    assert "Security Policy" in security
    assert "private and evidence-based workflow" in security
    assert "Do not publish exploit details" in security
    assert "Supported Scope" in security
    assert "Exposed credentials, API keys, tokens" in security
    assert "Authentication or authorization bypass" in security
    assert "Unsafe file upload behavior" in security
    assert "Documentation that instructs learners to use unsafe production practices" in security
    assert "does not provide a production service" in security
    assert "Not Security Reports" in security
    assert "Beginner questions about API keys, CORS, authentication, or GitHub permissions." in security
    assert "Private Reporting Workflow" in security
    assert "GitHub private vulnerability reporting" in security
    assert "Open a short public issue asking for a maintainer security contact path." in security
    assert "Affected file, route, dependency, lesson, or GitHub workflow." in security
    assert "Impact summary." in security
    assert "Minimal reproduction steps." in security
    assert "Maintainer Triage" in security
    assert "`critical`" in security
    assert "`high`" in security
    assert "`medium`" in security
    assert "`low`" in security
    assert "Fix and Disclosure Flow" in security
    assert "Public disclosure should avoid weaponized detail." in security
    assert "Required Verification" in security
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in security
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in security
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in security
    assert "git diff --check" in security
    assert "CODE_OF_CONDUCT.md" in security
    assert "CONTRIBUTING.md" in security
    assert ".github/ISSUE_TRIAGE.md" in security
    assert ".github/RELEASE_PROCESS.md" in security


def test_license_documents_reuse_boundary() -> None:
    license_text = Path("LICENSE").read_text(encoding="utf-8")

    assert "MIT License" in license_text
    assert "Copyright (c) 2026 Course Maintainers" in license_text
    assert "Permission is hereby granted, free of charge" in license_text
    assert "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell" in license_text
    assert "The above copyright notice and this permission notice shall be included" in license_text
    assert 'THE SOFTWARE IS PROVIDED "AS IS"' in license_text
    assert "WITHOUT WARRANTY OF ANY KIND" in license_text
    assert "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT" in license_text
    assert "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE" in license_text


def test_env_example_documents_local_config_hygiene() -> None:
    env_example = Path(".env.example").read_text(encoding="utf-8")
    gitignore = Path(".gitignore").read_text(encoding="utf-8")
    settings = Path("first_api/settings.py").read_text(encoding="utf-8")

    assert "Copy this file to `.env` for local learning overrides." in env_example
    assert "Keep `.env` out of Git." in env_example
    assert "Do not commit real secrets, production URLs, private tokens, or customer data." in env_example
    assert "safe teaching defaults only" in env_example
    assert 'FIRST_API_APP_NAME="First FastAPI API"' in env_example
    assert 'FIRST_API_ENVIRONMENT="development"' in env_example
    assert 'FIRST_API_API_KEY="dev-secret-key"' in env_example
    assert 'FIRST_API_AI_PROVIDER="demo"' in env_example
    assert 'FIRST_API_AI_PREDICTION_BACKEND="demo"' in env_example
    assert 'FIRST_API_AI_PROVIDER_HEALTH_URL="https://example.com"' in env_example
    assert 'FIRST_API_AI_PROVIDER_PREDICTION_URL="https://example.com/predict"' in env_example
    assert 'FIRST_API_AI_TIMEOUT_SECONDS="10"' in env_example
    assert 'FIRST_API_AI_MAX_ATTEMPTS="1"' in env_example
    assert ".env" in gitignore
    assert 'env_file=".env"' in settings
    assert 'env_prefix="FIRST_API_"' in settings


def test_pages_documentation_describes_static_course_publication() -> None:
    pages = Path(".github/PAGES.md").read_text(encoding="utf-8")

    assert "GitHub Pages and Offline HTML Workflow" in pages
    assert "static HTML files" in pages
    assert "opening `index.html` from a local clone" in pages
    assert "GitHub Pages is an optional remote publishing layer" in pages
    assert "remote state" in pages
    assert "Reading Modes" in pages
    assert "Local file" in pages
    assert "FastAPI app" in pages
    assert "GitHub file view" in pages
    assert "GitHub Pages" in pages
    assert "Recommended Pages Source" in pages
    assert "Branch: main" in pages
    assert "Folder: / (root)" in pages
    assert "Entry: index.html" in pages
    assert "Required Static Assets" in pages
    assert "assets/course.css" in pages
    assert "all files under `lessons/`" in pages
    assert "all files under `reference/`" in pages
    assert "Pre-Publish Checklist" in pages
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in pages
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in pages
    assert "git diff --check" in pages
    assert "Common Failure Modes" in pages
    assert "HTML source is shown instead of a page." in pages
    assert "Page has no styling." in pages
    assert "Lesson link returns 404." in pages


def test_final_audit_documents_release_quality_gate() -> None:
    audit = Path(".github/FINAL_AUDIT.md").read_text(encoding="utf-8")

    assert "Repository Final Quality Audit" in audit
    assert "final pre-release gate" in audit
    assert "96-lesson FastAPI course repository" in audit
    assert "lessons 0001-0096" in audit
    assert "Lesson Coverage" in audit
    assert "nine-section structure" in audit
    assert "Final Review + CSDN Deep Dive" in audit
    assert "Navigation Integrity" in audit
    assert "README.md" in audit
    assert "index.html" in audit
    assert "reference/" in audit
    assert "learning records" in audit
    assert "Governance Documents" in audit
    assert "CHANGELOG.md" in audit
    assert "CONTRIBUTING.md" in audit
    assert "CODE_OF_CONDUCT.md" in audit
    assert "SECURITY.md" in audit
    assert "LICENSE" in audit
    assert ".github/PAGES.md" in audit
    assert ".github/COURSE_COMPLETION.md" in audit
    assert ".github/LINK_AUDIT.md" in audit
    assert ".github/RELEASE_CANDIDATE.md" in audit
    assert "No Secrets" in audit
    assert "Required Verification" in audit
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in audit
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in audit
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in audit
    assert "git diff --check" in audit


def test_static_course_html_local_links_resolve_inside_repository() -> None:
    root = Path.cwd().resolve()
    broken_links: list[str] = []

    for page in iter_static_course_html_pages():
        parser = parse_html(page)

        for href in parser.links:
            if not is_repository_local_href(href):
                continue

            parsed_path = urlsplit(href).path
            if not parsed_path:
                continue

            target = (page.parent / parsed_path).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                broken_links.append(f"{page}: {href} -> outside repository")
                continue

            if not target.exists():
                broken_links.append(f"{page}: {href} -> {target}")

    assert not broken_links, "Broken local HTML links:\n" + "\n".join(broken_links)


def test_link_audit_documents_static_navigation_contract() -> None:
    audit = Path(".github/LINK_AUDIT.md").read_text(encoding="utf-8")

    assert "Static Link and Navigation Audit" in audit
    assert "plain HTML learning site" in audit
    assert "navigation quality is part of the public API" in audit
    assert "index.html" in audit
    assert "lessons/" in audit
    assert "reference/" in audit
    assert "local relative links only" in audit
    assert "External HTTP links" in audit
    assert "in-page fragments" in audit
    assert "Required Navigation Pattern" in audit
    assert "../index.html" in audit
    assert "../reference/" in audit
    assert "../lessons/" in audit
    assert "Path Rules" in audit
    assert "Do not use absolute local machine paths" in audit
    assert "Do not use GitHub blob URLs" in audit
    assert "tests/test_course_docs_contract.py" in audit
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in audit


def test_release_candidate_documents_versioned_publishing_readiness() -> None:
    rc = Path(".github/RELEASE_CANDIDATE.md").read_text(encoding="utf-8")
    release_process = Path(".github/RELEASE_PROCESS.md").read_text(encoding="utf-8")

    assert "Release Candidate Checklist" in rc
    assert "96-lesson FastAPI course" in rc
    assert "not the final GitHub Release" in rc
    assert "evidence bundle" in rc
    assert "Release Candidate Purpose" in rc
    assert "Entry Criteria" in rc
    assert "lessons 0001-0096" in rc
    assert "Freeze Rules" in rc
    assert "Do not add new lesson topics" in rc
    assert "Verification Evidence" in rc
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in rc
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in rc
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in rc
    assert "git diff --check" in rc
    assert "StarletteDeprecationWarning" in rc
    assert "Documentation Evidence" in rc
    assert ".github/COURSE_COMPLETION.md" in rc
    assert "Tag and Release Notes Readiness" in rc
    assert "course-vYYYY.MM.DD-N" in rc
    assert "annotated tag" in rc
    assert "GitHub Pages Readiness" in rc
    assert "Exit Criteria" in rc
    assert ".github/RELEASE_CANDIDATE.md" in release_process


def test_complete_course_lesson_range_has_no_numbering_gaps() -> None:
    lesson_numbers = sorted(
        int(path.name[:4])
        for path in Path("lessons").glob("*.html")
        if path.name[:4].isdigit()
    )

    assert lesson_numbers == list(range(1, 97))


def test_course_completion_runbook_documents_final_release_boundary() -> None:
    completion = Path(".github/COURSE_COMPLETION.md").read_text(encoding="utf-8")

    assert "Course Completion Release Runbook" in completion
    assert "96-lesson FastAPI course" in completion
    assert "Lesson 0096" in completion
    assert "Completion Meaning" in completion
    assert "lessons 0001-0096" in completion
    assert "no numbering gaps" in completion
    assert "nine-section review structure" in completion
    assert "matching quick reference" in completion
    assert "Final Run Order" in completion
    assert ".github/FINAL_AUDIT.md" in completion
    assert ".github/LINK_AUDIT.md" in completion
    assert ".github/RELEASE_CANDIDATE.md" in completion
    assert ".github/RELEASE_PROCESS.md" in completion
    assert ".github/PAGES.md" in completion
    assert "Required Verification" in completion
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_course_docs_contract.py -q" in completion
    assert ".\\.venv\\Scripts\\python.exe -m pytest tests\\test_provider_http.py -q" in completion
    assert ".\\.venv\\Scripts\\python.exe -m pytest -q" in completion
    assert "git diff --check" in completion
    assert "Release Announcement Draft" in completion
    assert "Do Not Announce Complete If" in completion
    assert "After Completion" in completion
