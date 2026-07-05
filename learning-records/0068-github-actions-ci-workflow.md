# Learning Record 0068 - GitHub Actions CI Workflow

## What changed

- Added `.github/workflows/ci.yml` as the repository-level CI workflow.
- The workflow runs provider HTTP tests, documentation contract tests, the full pytest suite, and committed diff whitespace checks.
- Added Lesson 0077 and Reference 0077 to explain CI triggers, runner setup, dependency installation, test layering, and production boundaries.

## Why it matters

The course repository is now protected by the same quality gates documented in `DEVELOPMENT.md`. New contributors can open a pull request and receive automatic feedback before their changes are merged.

## Verification focus

- `.github/workflows/ci.yml`
- `tests/test_course_docs_contract.py`
- `lessons/0077-github-actions-ci-workflow.html`
- `reference/0077-github-actions-ci-workflow-cheatsheet.html`
