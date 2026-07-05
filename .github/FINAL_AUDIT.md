# Repository Final Quality Audit

This checklist is the final pre-release gate for the 96-lesson FastAPI course repository. It is not a substitute for tests; it defines what reviewers must verify before the course is tagged, published, or promoted through GitHub Pages.

## Audit Purpose

- Confirm that lessons 0001-0096 form one complete learning path.
- Confirm that every lesson keeps the required review structure.
- Confirm that runnable code, tests, lessons, references, learning records, and GitHub governance documents agree with each other.
- Confirm that the public repository does not expose secrets, private provider URLs, personal data, or customer data.
- Confirm that the course can be read locally, reviewed on GitHub, and optionally published through GitHub Pages.

## Lesson Coverage

Reviewers must verify:

- `lessons/` contains lessons 0001-0096 with no numbering gaps.
- `reference/` contains the matching quick reference for every protected lesson.
- `index.html` links to every lesson and quick reference.
- Each lesson contains the nine-section structure:
  - `① 本节核心知识框架`
  - `② 核心概念底层原理`
  - `③ 全套代码逐行精读解析`
  - `④ 核心机制运行全流程拆解`
  - `⑤ 重难点、易混淆点对比辨析`
  - `⑥ 开发常见报错+坑点+解决方案`
  - `⑦ 生产环境 vs 教学环境 核心差异`
  - `⑧ 课后记忆习题+标准答案`
  - `⑨ 面试高频真题+解析`
- Each lesson keeps the marker `Final Review + CSDN Deep Dive`.

## Navigation Integrity

Reviewers must verify:

- Top and bottom lesson navigation return to `index.html`.
- Previous/next lesson links are correct for adjacent lessons.
- Lesson pages link to their matching `reference/` quick reference.
- Quick reference pages link back to the matching lesson.
- `index.html` remains the public course entry.
- GitHub Pages publication uses the repository root so `assets/`, `lessons/`, and `reference/` relative links remain valid.

## Source and Test Integrity

Reviewers must verify:

- Source examples in lessons still match the real code under `first_api/`.
- API behavior described in lessons is protected by tests when it is executable behavior.
- Documentation behavior described in lessons is protected by `tests/test_course_docs_contract.py` when it is a durable repository contract.
- Provider HTTP behavior remains covered by `tests/test_provider_http.py`.
- OpenAPI and response-shape claims stay aligned with the current schemas.

## Governance Documents

Reviewers must verify that these documents exist, are linked from learner-facing documentation, and do not contradict each other:

- `README.md`
- `DEVELOPMENT.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `LICENSE`
- `.github/PAGES.md`
- `.github/COURSE_COMPLETION.md`
- `.github/LINK_AUDIT.md`
- `.github/RELEASE_CANDIDATE.md`
- `.github/RELEASE_PROCESS.md`
- `.github/DISCUSSIONS.md`
- `.github/PROJECT_BOARD.md`
- `.github/ISSUE_TRIAGE.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/CODEOWNERS`
- `.github/workflows/ci.yml`

## No Secrets

Reviewers must verify:

- `.env` is not committed.
- `.env.example` contains teaching defaults only.
- No real API key, private token, production provider URL, customer content, private log, or personal data appears in lessons, references, tests, GitHub documents, or examples.
- `SECURITY.md` remains the path for private vulnerability reporting.

## Required Verification

Run these commands before release:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Expected result:

- Documentation contract tests pass.
- Provider HTTP tests pass.
- Full pytest passes.
- `git diff --check` reports no whitespace errors. Windows LF-to-CRLF notices are acceptable when no whitespace error is reported.

## Release Decision

The repository is release-ready only when:

- all required verification commands pass;
- the newest lesson, newest reference, README, DEVELOPMENT, CHANGELOG, NOTES, COURSE_PROGRESS, and index navigation are consistent;
- no private or production secret is present;
- GitHub Pages documentation remains accurate;
- remaining known warnings are explicitly documented in release notes.
