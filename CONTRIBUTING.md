# Contributing Guide

Thank you for improving this course repository.

This repository is both a runnable FastAPI project and a structured learning archive. Contributions must keep code behavior, lesson content, quick references, navigation, tests, and GitHub workflow documents synchronized.

## Contribution Scope

Good first contribution types:

- Fix a broken course link, typo that changes meaning, or outdated command.
- Improve an existing lesson while keeping the fixed nine-section structure.
- Add or improve a quick reference page.
- Add focused tests for behavior, documentation contracts, or GitHub workflow documents.
- Improve README, DEVELOPMENT, CHANGELOG, release process, issue templates, or contribution workflow documentation.

Open a discussion first when the idea is exploratory, broad, or primarily educational. Open an issue when the work is reproducible, scoped, and can be reviewed against a clear definition of done.

## Before You Start

1. Read `README.md` for the learning route.
2. Read `DEVELOPMENT.md` for local commands and maintenance rules.
3. Check `CHANGELOG.md` for unreleased public changes.
4. Search existing issues and discussions before opening a new one.
5. Pick or create a scoped issue before writing a pull request.

## Branch and Commit Workflow

Use a short branch name that describes the work:

```text
docs/fix-lesson-0086-link
course/add-lesson-0087-contributing
tests/protect-contributing-guide
```

Commits should describe the user-visible or maintainer-visible change. Avoid mixing unrelated lesson rewrites, source changes, and GitHub governance changes in one pull request.

## Lesson Contribution Standard

Every full lesson must include:

1. `① 本节核心知识框架`
2. `② 核心概念底层原理`
3. `③ 全套代码逐行精读解析`
4. `④ 核心机制运行全流程拆解`
5. `⑤ 重难点、易混淆点对比辨析`
6. `⑥ 开发常见报错+坑点+解决方案`
7. `⑦ 生产环境 vs 教学环境 核心差异`
8. `⑧ 课后记忆习题+标准答案`
9. `⑨ 面试高频真题+解析`

Lessons must use the `Final Review + CSDN Deep Dive` style marker and must connect concepts to source files, tests, runtime flow, production boundaries, exercises, and interview questions.

## Documentation Checklist

When adding or changing a lesson:

- Update the lesson HTML in `lessons/`.
- Update or add the quick reference in `reference/`.
- Update `index.html` navigation.
- Update previous and next lesson navigation.
- Add a learning record under `learning-records/`.
- Update `NOTES.md`.
- Update `COURSE_PROGRESS.md`.
- Update `CHANGELOG.md` when the change is learner-visible or contributor-visible.
- Add or update documentation contract tests when a document becomes public entry point.

## Required Verification

Run these commands before opening or updating a pull request:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

If a command cannot be run, state the reason in the pull request verification section.

## Pull Request Requirements

Every pull request should include:

- Summary of what changed.
- Why the change is needed.
- Change type.
- Verification command output.
- Course documentation checklist status.
- Risk notes and known warnings.
- Linked issue or discussion when relevant.

The repository pull request template in `.github/PULL_REQUEST_TEMPLATE.md` is the source of truth for the required evidence.

## Review and Ownership

CODEOWNERS rules in `.github/CODEOWNERS` route reviews by file area. Branch protection may require CI checks, conversation resolution, and owner review before merge.

Review comments should focus on correctness, learner impact, maintainability, test coverage, and whether teaching-demo boundaries are clearly separated from production guidance.

## Changelog and Release Notes

Use `CHANGELOG.md` for curated public changes. Keep new contribution workflow changes under `Unreleased` until a course tag is published.

Use `.github/RELEASE_PROCESS.md` when maintainers publish a verified course batch with an annotated tag and GitHub Release Notes.

## Code of Conduct Boundary

This repository does not yet define a full community code of conduct. Until one exists, contributors should keep discussions technical, respectful, evidence-based, and safe for beginners.

Do not post secrets, private logs, personal data, proprietary source code, or credentials in issues, discussions, pull requests, or examples.
