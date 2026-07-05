# Development Workflow

This repository is both a runnable FastAPI project and a course archive. Treat code, tests, lessons, references, and README links as one learning product.

## Before You Change Code

1. Read the related lesson and quick reference in `lessons/` and `reference/`.
2. Check the matching tests under `tests/`.
3. Keep the change small enough to verify with targeted tests.

## Code Change Checklist

- Update the implementation in `first_api/`.
- Add or update tests in `tests/`.
- Run the targeted test file first.
- Run the full test suite before considering the change complete.

Common commands:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

The same quality gates are also encoded in `.github/workflows/ci.yml` so pull requests can be checked by GitHub Actions before merge.

Main branch protection and the required status check name are documented in `.github/BRANCH_PROTECTION.md`.

Pull request evidence requirements are documented in `.github/PULL_REQUEST_TEMPLATE.md`.

Repository review ownership is documented in `.github/CODEOWNERS`; replace placeholder owner teams with real GitHub users or organization teams before enforcing code owner reviews.

Issue intake forms are documented in `.github/ISSUE_TEMPLATE/`; keep bug reports, lesson requests, and documentation fixes separated so triage stays actionable.

Issue label triage is documented in `.github/ISSUE_TRIAGE.md`; use type, area, priority, and status labels before turning feedback into implementation work.

GitHub Projects board workflow is documented in `.github/PROJECT_BOARD.md`; keep project Status, Priority, Area, Type, and Lesson fields aligned with issue labels and course maintenance records.

GitHub Discussions workflow is documented in `.github/DISCUSSIONS.md`; route exploratory learner questions to Discussions and convert concrete repository work back into templated issues.

GitHub release publishing is documented in `.github/RELEASE_PROCESS.md`; use annotated tags and release notes to publish verified course batches.

Changelog maintenance is documented in `CHANGELOG.md`; keep notable learner-visible, test-contract, and GitHub governance changes in `Unreleased` until a course tag is published.

Contributor workflow is documented in `CONTRIBUTING.md`; use it as the contributor-facing path from discussion or issue to branch, verification, pull request, review, changelog, and release readiness.

Public collaboration safety is documented in `CODE_OF_CONDUCT.md`; keep beginner-safe discussions, evidence-based review, reporting, maintainer response, and public data-safety boundaries aligned with contribution workflow.

Security reporting is documented in `SECURITY.md`; keep vulnerability details, secrets, private logs, personal data, and working attack steps out of public issues, discussions, pull requests, and comments.

Repository reuse rights are documented in `LICENSE`; keep the copyright notice, permission notice, and license link discoverable when publishing course batches or reuse guidance.

Local configuration shape is documented in `.env.example`; keep committed values safe for teaching, keep real `.env` files ignored, and never commit production secrets, private provider URLs, tokens, or customer data.

Static course publication is documented in `.github/PAGES.md`; keep `index.html`, `assets/course.css`, `lessons/`, and `reference/` aligned for both offline reading and optional GitHub Pages publishing.

Repository final quality audit is documented in `.github/FINAL_AUDIT.md`; use it before tagging, publishing, or promoting the completed 96-lesson course through GitHub Pages.

Static link and navigation audit is documented in `.github/LINK_AUDIT.md`; keep local HTML links in `index.html`, `lessons/`, and `reference/` resolvable before publishing new course pages.

Release-candidate readiness is documented in `.github/RELEASE_CANDIDATE.md`; enter it before creating annotated tags, GitHub Release Notes, or Pages promotion for a course batch.

Full course completion is documented in `.github/COURSE_COMPLETION.md`; use it after Lesson 0096 exists and before announcing the 96-lesson baseline as complete.

## Lesson Change Checklist

Every new lesson should include:

- a complete HTML lesson in `lessons/`;
- a quick reference page in `reference/`;
- an entry in `index.html`;
- a learning record in `learning-records/`;
- an update to `NOTES.md`;
- an update to `COURSE_PROGRESS.md`;
- documentation contract coverage when the lesson becomes part of the protected course path.

Lessons must keep the fixed review structure:

1. `① 本节核心知识框架`
2. `② 核心概念底层原理`
3. `③ 全套代码逐行精读解析`
4. `④ 核心机制运行全流程拆解`
5. `⑤ 重难点、易混淆点对比辨析`
6. `⑥ 开发常见报错+坑点+解决方案`
7. `⑦ 生产环境 vs 教学环境 核心差异`
8. `⑧ 课后记忆习题+标准答案`
9. `⑨ 面试高频真题+解析`

## Documentation Change Checklist

When changing README or course navigation:

- keep `README.md` linked to `index.html`;
- keep `README.md` linked to `first_api/README.md`;
- keep provider metrics links discoverable from `README.md`;
- update `tests/test_course_docs_contract.py` when a new document becomes a public entry point;
- run the documentation contract tests.

## GitHub Release Readiness

Before publishing course updates:

1. Confirm `README.md` gives a clear learning route.
2. Confirm `index.html` lists the new lesson and quick reference.
3. Confirm provider metrics docs link to the latest runbook training package when relevant.
4. Run targeted tests, documentation contract tests, full tests, and `git diff --check`.

This project currently treats Windows LF-to-CRLF notices from Git as non-blocking warnings. Whitespace errors from `git diff --check` are blocking.
