# Learning Record 0072 - GitHub Issue Templates

## What changed

- Added `.github/ISSUE_TEMPLATE/` with structured GitHub Issue Forms.
- Added separate templates for bug reports, lesson requests, and documentation fixes.
- Disabled blank issues so new feedback enters through a structured, triage-ready form.
- Added Lesson 0081 and Reference 0081 to explain issue intake, YAML fields, required validations, labels, and production differences.

## Why it matters

Issue templates are the repository's input contract. They turn vague learner feedback into reproducible bugs, actionable course requests, or scoped documentation fixes before maintainers start triage.

## Verification focus

- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/lesson_request.yml`
- `.github/ISSUE_TEMPLATE/documentation_fix.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `tests/test_course_docs_contract.py`
- `lessons/0081-github-issue-templates.html`
- `reference/0081-github-issue-templates-cheatsheet.html`
