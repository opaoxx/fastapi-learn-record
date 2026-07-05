# Static Link and Navigation Audit

This document defines the static-link contract for the course repository. The course is a plain HTML learning site, so navigation quality is part of the public API.

## Audit Purpose

- Keep `index.html`, `lessons/`, and `reference/` navigable without a build step.
- Ensure local offline reading and GitHub Pages reading use the same relative paths.
- Catch missing lesson files, missing quick references, broken previous/next links, and broken links to durable repository documents.
- Keep link checks machine-verifiable through `tests/test_course_docs_contract.py`.

## Link Scope

The static link audit covers:

- `index.html`
- all HTML files under `lessons/`
- all HTML files under `reference/`

The audit checks local relative links only. External HTTP links, mail links, and in-page fragments are outside this repository-level contract.

## Required Navigation Pattern

Every protected lesson page should provide:

- a link back to `../index.html`;
- a link to the previous lesson when one exists;
- a link to the next lesson when one exists;
- a link to its matching quick reference under `../reference/`;
- bottom navigation with the same recovery path.

Every protected quick reference page should provide:

- a link back to `../index.html`;
- a link back to the matching lesson under `../lessons/`;
- a link to the previous quick reference when one exists;
- a link to the next quick reference when one exists;
- bottom navigation with the same recovery path.

## Path Rules

- Links from `index.html` are resolved from the repository root.
- Links from `lessons/*.html` are resolved from the `lessons/` directory.
- Links from `reference/*.html` are resolved from the `reference/` directory.
- Do not use absolute local machine paths such as `F:\...` inside course HTML.
- Do not use GitHub blob URLs for internal course navigation.
- Keep file names lowercase, numbered, and stable after publication.

## Test Contract

`tests/test_course_docs_contract.py` must verify that local HTML links resolve to files inside the repository.

Expected exclusions:

- `https://...`
- `http://...`
- `mailto:...`
- `#fragment`

Expected failures:

- a linked lesson file is missing;
- a linked quick reference file is missing;
- a link points outside the repository;
- an internal path contains an incorrect directory level;
- a renamed file is not reflected in `index.html` or adjacent navigation.

## Manual Review Checklist

Before publishing a new lesson:

- Open the new lesson from `index.html`.
- Open the matching quick reference from the lesson.
- Return from the quick reference to the lesson.
- Move back to the previous lesson and previous quick reference.
- Confirm the previous lesson and previous quick reference now link forward.
- Run the documentation contract tests.

## Required Verification

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
git diff --check
```

For a release or final audit, also run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest -q
```

## Production Notes

Production documentation sites often add crawlers, link checkers, redirect maps, canonical URLs, preview deployments, and visual regression checks. This course keeps the mechanism deliberately visible: plain HTML links plus a small repository-local contract test.
