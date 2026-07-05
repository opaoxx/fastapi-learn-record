# Release Candidate Checklist

This document defines the release-candidate gate for the 96-lesson FastAPI course. A release candidate is not the final GitHub Release; it is the evidence bundle that proves the repository is ready to be tagged, described in release notes, and optionally promoted through GitHub Pages.

## Release Candidate Purpose

- Freeze the intended lesson range before publishing.
- Verify that source code, tests, lessons, references, and governance documents agree.
- Collect repeatable verification evidence.
- Identify known warnings before creating an annotated tag.
- Prevent incomplete course material from being promoted as a finished learning release.

## Entry Criteria

A release candidate may start only when:

- lessons 0001-0096 are present or the release notes explicitly describe the partial range;
- each included lesson has a matching quick reference;
- `index.html` links the included lessons and references;
- the latest `COURSE_PROGRESS.md` entry records the current verification state;
- `CHANGELOG.md` has accurate `Unreleased` entries;
- `.github/FINAL_AUDIT.md` and `.github/LINK_AUDIT.md` have been reviewed.

## Freeze Rules

During release-candidate review:

- Do not add new lesson topics unless the release candidate is restarted.
- Do not rename lesson or reference files unless navigation and link tests are updated in the same change.
- Do not change public API behavior without rerunning the full test suite and updating lessons that describe the behavior.
- Do not commit real secrets, production provider URLs, private logs, customer data, or personal data.
- Keep fixes small, traceable, and linked to the failed check that required the fix.

## Verification Evidence

Run and record:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Record acceptable known warnings separately. The current known warning class is `StarletteDeprecationWarning` from the test client dependency path.

## Documentation Evidence

Before tagging, verify:

- `README.md` points learners to the course entry, runnable project, workflow documents, and final audit documents.
- `DEVELOPMENT.md` lists the current maintenance and verification commands.
- `CHANGELOG.md` has concise learner-visible entries under `Unreleased`.
- `.github/RELEASE_PROCESS.md` describes tag naming, release notes, rollback, and known warnings.
- `.github/PAGES.md` describes local reading and optional GitHub Pages publication.
- `.github/COURSE_COMPLETION.md` describes the final 96-lesson completion run order.
- `.github/FINAL_AUDIT.md` and `.github/LINK_AUDIT.md` are consistent with the current repository state.

## Tag and Release Notes Readiness

Before creating a tag:

- choose a tag name that follows `course-vYYYY.MM.DD-N`;
- use an annotated tag;
- prepare release notes with changed lessons, changed references, code and workflow changes, verification, and known warnings;
- do not move a published tag silently;
- keep rollback instructions linked to `.github/RELEASE_PROCESS.md`.

## GitHub Pages Readiness

Before promoting through GitHub Pages:

- confirm the intended Pages source is branch `main`, folder `/ (root)`;
- confirm `index.html`, `assets/course.css`, `lessons/`, and `reference/` are included;
- confirm local HTML link tests pass;
- confirm readers know GitHub file view may show raw HTML source.

## Exit Criteria

A release candidate can become a release only when:

- all required verification commands pass;
- known warnings are documented;
- the release range is explicit;
- no release-blocking broken links, missing quick references, or secret leaks remain;
- release notes are ready;
- the maintainer can recreate the evidence from the repository state.
