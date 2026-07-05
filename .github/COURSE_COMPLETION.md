# Course Completion Release Runbook

This runbook defines the final completion procedure for the 96-lesson FastAPI course. It is used after Lesson 0096 exists and before maintainers announce the course as complete.

## Completion Meaning

The course is complete only when:

- lessons 0001-0096 exist with no numbering gaps;
- each protected lesson keeps the required nine-section review structure;
- each included lesson has a matching quick reference;
- `index.html` links the complete lesson and reference sequence;
- source code, tests, lessons, references, and workflow documents agree;
- no real secret, private token, production provider URL, private log, customer data, or personal data is committed;
- final verification evidence is recorded.

## Final Run Order

1. Confirm the lesson range is complete.
2. Review `.github/FINAL_AUDIT.md`.
3. Review `.github/LINK_AUDIT.md`.
4. Review `.github/RELEASE_CANDIDATE.md`.
5. Review `.github/RELEASE_PROCESS.md`.
6. Review `.github/PAGES.md`.
7. Run the required verification commands.
8. Update `CHANGELOG.md` and release notes draft.
9. Confirm `COURSE_PROGRESS.md` records final evidence.
10. Create the annotated tag only after all checks pass.

## Required Verification

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Expected evidence:

- documentation contract tests pass;
- provider HTTP tests pass;
- full pytest passes;
- static HTML local link audit passes through documentation contract tests;
- `git diff --check` reports no whitespace errors;
- known warnings are documented, including the current `StarletteDeprecationWarning` if still present.

## Final Documentation Sweep

Before announcing completion, verify:

- `README.md` gives learners the course entry and workflow documents;
- `DEVELOPMENT.md` gives maintainers the verification commands;
- `CHANGELOG.md` records the completed course work under `Unreleased` until a tag is created;
- `NOTES.md` records Lesson 0096 and the completion boundary;
- `COURSE_PROGRESS.md` records the final command results;
- `.github/FINAL_AUDIT.md`, `.github/LINK_AUDIT.md`, `.github/RELEASE_CANDIDATE.md`, `.github/RELEASE_PROCESS.md`, and `.github/PAGES.md` remain consistent.

## Release Announcement Draft

The release announcement should include:

- completed range: lessons 0001-0096;
- primary learning path: FastAPI basics, database CRUD, background tasks, frontend fetch, AI provider boundaries, retries, metrics, runbooks, and GitHub workflow;
- verification evidence;
- known warnings;
- local reading instructions;
- GitHub Pages publication status if enabled;
- license and contribution links.

## Do Not Announce Complete If

- any lesson number from 0001-0096 is missing;
- a lesson loses the nine-section structure;
- a quick reference is missing;
- local HTML link audit fails;
- tests fail;
- a real secret or private data sample is present;
- release range or known warnings are unclear.

## After Completion

After announcing completion:

- do not rewrite the completed release silently;
- publish corrections as a new course patch release or follow-up tag;
- keep issues, discussions, and pull requests routed through the documented GitHub workflow;
- keep future course expansions separate from the completed 96-lesson baseline.
