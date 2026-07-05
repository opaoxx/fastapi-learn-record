# GitHub Pages and Offline HTML Workflow

This repository stores course lessons and quick references as static HTML files.

The course can be read offline by opening `index.html` from a local clone. GitHub Pages is an optional remote publishing layer; enabling it is repository remote state and is not created by committing this file.

## Reading Modes

| Mode | Entry | Use Case | Limitation |
| --- | --- | --- | --- |
| Local file | `index.html` | Offline review after cloning or downloading the repository. | Browser file-path behavior may differ from hosted HTTP behavior. |
| FastAPI app | `http://127.0.0.1:8000/app/` | Testing the runnable backend and tiny frontend. | Not the main course documentation site. |
| GitHub file view | Repository HTML file page | Inspecting source in GitHub. | Usually shows HTML source rather than rendered course page. |
| GitHub Pages | Published site URL | Sharing rendered static course pages. | Must be enabled in repository settings or Pages workflow. |

## Recommended Pages Source

For this teaching repository, publish from:

```text
Branch: main
Folder: / (root)
Entry: index.html
```

This keeps `assets/`, `lessons/`, and `reference/` paths aligned with local offline reading.

## Required Static Assets

The published site must include:

- `index.html`
- `assets/course.css`
- all files under `lessons/`
- all files under `reference/`

Do not publish only a single lesson file; lesson navigation depends on shared relative paths.

## Pre-Publish Checklist

Before enabling or updating GitHub Pages:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Also inspect:

- `index.html` lists the newest lesson and quick reference.
- Previous and next lesson navigation is connected.
- Previous and next quick-reference navigation is connected.
- `assets/course.css` is reachable from lesson and reference pages.
- `README.md` explains that GitHub file view may show raw HTML source.
- `CHANGELOG.md` records learner-visible publication workflow changes.

## Common Failure Modes

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| HTML source is shown instead of a page. | User opened GitHub file view, not Pages or a local file. | Use local `index.html` or the Pages URL. |
| Page has no styling. | `assets/course.css` is missing or relative path is wrong. | Publish from repository root and keep `assets/`. |
| Lesson link returns 404. | `index.html` links a file that was not committed. | Add the lesson/reference file and run docs contract tests. |
| Previous/next navigation breaks. | Adjacent lesson or reference was not updated. | Update both course and reference navigation. |
| Pages content is stale. | Pages deployment has not refreshed yet or branch is wrong. | Check Pages settings, selected branch, and latest deployment status. |

## Production Notes

Production documentation sites often use static-site generators, link checkers, preview deployments, CDN caching, search indexing, analytics, redirects, and versioned docs.

This teaching repository intentionally keeps the course as plain HTML so learners can understand every path and open the material offline.
