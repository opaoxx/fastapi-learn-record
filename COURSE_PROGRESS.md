# Course Progress

# 2026-07-05 Run: Lesson 0096 Full Course Completion Release Runbook

## Completed

- Completed Lesson 0096: Full Course Completion Release Runbook.
- Added `.github/COURSE_COMPLETION.md` documenting the final 96-lesson completion meaning, final run order, required verification, documentation sweep, release announcement draft, release blockers, and post-completion governance.
- Added documentation contract coverage for the completion runbook, README links, DEVELOPMENT links, CHANGELOG linkage, final-audit linkage, release-candidate linkage, the new lesson's fixed review structure, and the complete lessons 0001-0096 no-gap range.
- Added Lesson 0096, Reference 0096, learning record 0087, updated Lesson 0095 navigation, Reference 0095 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 30 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 125 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/COURSE_COMPLETION.md`
- `.github/FINAL_AUDIT.md`
- `.github/RELEASE_CANDIDATE.md`
- `CHANGELOG.md`
- `lessons/0096-full-course-completion-release-runbook.html`
- `lessons/0095-release-candidate-versioned-publishing-readiness.html`
- `reference/0096-full-course-completion-release-runbook-cheatsheet.html`
- `reference/0095-release-candidate-versioned-publishing-readiness-cheatsheet.html`
- `learning-records/0087-full-course-completion-release-runbook.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Completion status

The planned 96-lesson course baseline is now complete and verified.

# 2026-07-05 Run: Lesson 0095 Release Candidate Versioned Publishing Readiness

## Completed

- Completed Lesson 0095: Release Candidate Versioned Publishing Readiness.
- Added `.github/RELEASE_CANDIDATE.md` documenting RC purpose, entry criteria, freeze rules, verification evidence, documentation evidence, tag and Release Notes readiness, GitHub Pages readiness, and exit criteria.
- Added documentation contract coverage for the release-candidate checklist, README links, DEVELOPMENT links, CHANGELOG linkage, release-process linkage, final-audit linkage, and the new lesson's fixed review structure.
- Added Lesson 0095, Reference 0095, learning record 0086, updated Lesson 0094 navigation, Reference 0094 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 28 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 123 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/RELEASE_CANDIDATE.md`
- `.github/RELEASE_PROCESS.md`
- `.github/FINAL_AUDIT.md`
- `CHANGELOG.md`
- `lessons/0095-release-candidate-versioned-publishing-readiness.html`
- `lessons/0094-static-link-navigation-contract-audit.html`
- `reference/0095-release-candidate-versioned-publishing-readiness-cheatsheet.html`
- `reference/0094-static-link-navigation-contract-audit-cheatsheet.html`
- `learning-records/0086-release-candidate-versioned-publishing-readiness.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0096 after user review; the final topic should be the full course completion release runbook.

# 2026-07-05 Run: Lesson 0094 Static Link Navigation Contract Audit

## Completed

- Completed Lesson 0094: Static Link Navigation Contract Audit.
- Added `.github/LINK_AUDIT.md` documenting static HTML link scope, required navigation pattern, path rules, test contract, manual review checklist, required verification, and production link-audit differences.
- Extended documentation contract tests to scan local links in `index.html`, `lessons/`, and `reference/`, resolve them relative to each source page, reject paths outside the repository, and fail on missing local targets.
- Added Lesson 0094, Reference 0094, learning record 0085, updated Lesson 0093 navigation, Reference 0093 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 27 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 122 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/LINK_AUDIT.md`
- `.github/FINAL_AUDIT.md`
- `CHANGELOG.md`
- `lessons/0094-static-link-navigation-contract-audit.html`
- `lessons/0093-repository-final-quality-audit-checklist.html`
- `reference/0094-static-link-navigation-contract-audit-cheatsheet.html`
- `reference/0093-repository-final-quality-audit-checklist-cheatsheet.html`
- `learning-records/0085-static-link-navigation-contract-audit.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0095 after user review; a natural next topic is release candidate checklist and versioned publishing readiness.

# 2026-07-05 Run: Lesson 0093 Repository Final Quality Audit Checklist

## Completed

- Completed Lesson 0093: Repository Final Quality Audit Checklist.
- Added `.github/FINAL_AUDIT.md` documenting 96-lesson coverage, fixed nine-section structure, navigation integrity, source/test integrity, governance documents, no-secret checks, required verification, and release decision rules.
- Added documentation contract coverage for the final audit document, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0093, Reference 0093, learning record 0084, updated Lesson 0092 navigation, Reference 0092 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 25 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 120 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/FINAL_AUDIT.md`
- `CHANGELOG.md`
- `lessons/0093-repository-final-quality-audit-checklist.html`
- `lessons/0092-github-pages-offline-html-workflow.html`
- `reference/0093-repository-final-quality-audit-checklist-cheatsheet.html`
- `reference/0092-github-pages-offline-html-workflow-cheatsheet.html`
- `learning-records/0084-repository-final-quality-audit-checklist.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0094 after user review; a natural next topic is static link and navigation contract deep audit.

# 2026-07-05 Run: Lesson 0092 GitHub Pages Offline HTML Workflow

## Completed

- Completed Lesson 0092: GitHub Pages Offline HTML Workflow.
- Added `.github/PAGES.md` documenting static HTML reading modes, recommended GitHub Pages source, required static assets, pre-publish checks, common failure modes, and production documentation-site differences.
- Added documentation contract coverage for Pages publication documentation, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0092, Reference 0092, learning record 0083, updated Lesson 0091 navigation, Reference 0091 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 24 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 119 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/PAGES.md`
- `CHANGELOG.md`
- `lessons/0092-github-pages-offline-html-workflow.html`
- `lessons/0091-env-example-local-config-hygiene.html`
- `reference/0092-github-pages-offline-html-workflow-cheatsheet.html`
- `reference/0091-env-example-local-config-hygiene-cheatsheet.html`
- `learning-records/0083-github-pages-offline-html-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0093 after user review; a natural next topic is repository final quality audit checklist.

# 2026-07-05 Run: Lesson 0091 Env Example Local Config Hygiene

## Completed

- Completed Lesson 0091: Env Example Local Config Hygiene.
- Strengthened `.env.example` with comments that explain copying it to `.env`, keeping `.env` out of Git, avoiding real secrets, production URLs, private tokens, and customer data, and treating sample values as safe teaching defaults only.
- Added documentation contract coverage for `.env.example`, `.gitignore`, `first_api/settings.py`, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0091, Reference 0091, learning record 0082, updated Lesson 0090 navigation, Reference 0090 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 23 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 118 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.env.example`
- `CHANGELOG.md`
- `lessons/0091-env-example-local-config-hygiene.html`
- `lessons/0090-license-reuse-boundary.html`
- `reference/0091-env-example-local-config-hygiene-cheatsheet.html`
- `reference/0090-license-reuse-boundary-cheatsheet.html`
- `learning-records/0082-env-example-local-config-hygiene.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0092 after user review; a natural next topic is GitHub Pages or offline HTML publication workflow.

# 2026-07-05 Run: Lesson 0090 License Reuse Boundary

## Completed

- Completed Lesson 0090: License Reuse Boundary.
- Added root `LICENSE` with MIT License terms for repository reuse, modification, distribution, sublicensing, notice preservation, and no-warranty/no-liability boundaries.
- Updated `CHANGELOG.md` with license entries under `Unreleased`.
- Added documentation contract coverage for license content, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0090, Reference 0090, learning record 0081, updated Lesson 0089 navigation, Reference 0089 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 22 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 117 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `LICENSE`
- `CHANGELOG.md`
- `lessons/0090-license-reuse-boundary.html`
- `lessons/0089-security-policy-workflow.html`
- `reference/0090-license-reuse-boundary-cheatsheet.html`
- `reference/0089-security-policy-workflow-cheatsheet.html`
- `learning-records/0081-license-reuse-boundary.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0091 after user review; a natural next topic is `.env.example` and local configuration hygiene for GitHub learners.

# 2026-07-05 Run: Lesson 0089 Security Policy Workflow

## Completed

- Completed Lesson 0089: Security Policy Workflow.
- Added root `SECURITY.md` documenting private vulnerability reporting, supported scope, non-security reports, report fields, maintainer triage, fix and disclosure flow, required verification, and links to conduct, contribution, issue, and release workflow documents.
- Updated `CHANGELOG.md` with security policy entries under `Unreleased`.
- Added documentation contract coverage for security policy content, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0089, Reference 0089, learning record 0080, updated Lesson 0088 navigation, Reference 0088 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 21 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 116 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `SECURITY.md`
- `CHANGELOG.md`
- `lessons/0089-security-policy-workflow.html`
- `lessons/0088-code-of-conduct-workflow.html`
- `reference/0089-security-policy-workflow-cheatsheet.html`
- `reference/0088-code-of-conduct-workflow-cheatsheet.html`
- `learning-records/0080-security-policy-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0090 after user review; a natural next topic is LICENSE for open-source reuse boundaries.

# 2026-07-05 Run: Lesson 0088 Code of Conduct Workflow

## Completed

- Completed Lesson 0088: Code of Conduct Workflow.
- Added root `CODE_OF_CONDUCT.md` documenting beginner-safe collaboration, expected behavior, unacceptable behavior, scope, reporting, maintainer response, teaching review norms, safety boundary, and relationships to repository workflow documents.
- Updated `CHANGELOG.md` with code of conduct entries under `Unreleased`.
- Added documentation contract coverage for code of conduct content, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0088, Reference 0088, learning record 0079, updated Lesson 0087 navigation, Reference 0087 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 20 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 115 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`
- `lessons/0088-code-of-conduct-workflow.html`
- `lessons/0087-contributing-guide-workflow.html`
- `reference/0088-code-of-conduct-workflow-cheatsheet.html`
- `reference/0087-contributing-guide-workflow-cheatsheet.html`
- `learning-records/0079-code-of-conduct-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0089 after user review; a natural next topic is SECURITY.md for vulnerability reporting and private disclosure boundaries.

# 2026-07-05 Run: Lesson 0087 Contributing Guide Workflow

## Completed

- Completed Lesson 0087: Contributing Guide Workflow.
- Added root `CONTRIBUTING.md` documenting contribution scope, pre-work checks, branch and commit workflow, fixed lesson structure, documentation checklist, required verification, PR evidence, review ownership, changelog and release notes, and public safety boundaries.
- Updated `CHANGELOG.md` with contribution workflow entries under `Unreleased`.
- Added documentation contract coverage for contributor workflow content, README links, DEVELOPMENT links, CHANGELOG linkage, and the new lesson's fixed review structure.
- Added Lesson 0087, Reference 0087, learning record 0078, updated Lesson 0086 navigation, Reference 0086 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 19 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 114 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `lessons/0087-contributing-guide-workflow.html`
- `lessons/0086-changelog-maintenance-workflow.html`
- `reference/0087-contributing-guide-workflow-cheatsheet.html`
- `reference/0086-changelog-maintenance-workflow-cheatsheet.html`
- `learning-records/0078-contributing-guide-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0088 after user review; a natural next topic is CODE_OF_CONDUCT or SECURITY policy for public collaboration boundaries.

# 2026-07-05 Run: Lesson 0086 Changelog Maintenance Workflow

## Completed

- Completed Lesson 0086: Changelog Maintenance Workflow.
- Added root `CHANGELOG.md` as the local release ledger for notable course, source, test, documentation, and GitHub governance changes.
- Defined `Unreleased`, Added, Changed, Fixed, Tests, Governance, entry rules, release heading format, and the boundary between changelog, GitHub Release Notes, and `COURSE_PROGRESS.md`.
- Added documentation contract coverage for changelog content, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0086, Reference 0086, learning record 0077, updated Lesson 0085 navigation, Reference 0085 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 18 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 113 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `CHANGELOG.md`
- `lessons/0086-changelog-maintenance-workflow.html`
- `lessons/0085-github-release-notes-tags-workflow.html`
- `reference/0086-changelog-maintenance-workflow-cheatsheet.html`
- `reference/0085-github-release-notes-tags-workflow-cheatsheet.html`
- `learning-records/0077-changelog-maintenance-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0087 after user review; a natural next topic is CONTRIBUTING.md for contributor onboarding.

# 2026-07-05 Run: Lesson 0085 GitHub Release Notes and Tags Workflow

## Completed

- Completed Lesson 0085: GitHub Release Notes and Tags Workflow.
- Added `.github/RELEASE_PROCESS.md` documenting course batch tag naming, annotated tag rules, Release Notes structure, verification checklist, known warnings, release flow, rollback, and production notes.
- Added documentation contract coverage for the release process, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0085, Reference 0085, learning record 0076, updated Lesson 0084 navigation, Reference 0084 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 17 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 112 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/RELEASE_PROCESS.md`
- `lessons/0085-github-release-notes-tags-workflow.html`
- `lessons/0084-github-discussions-course-qa-workflow.html`
- `reference/0085-github-release-notes-tags-workflow-cheatsheet.html`
- `reference/0084-github-discussions-course-qa-workflow-cheatsheet.html`
- `learning-records/0076-github-release-notes-tags-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0086 after user review; a natural next topic is CHANGELOG maintenance or repository contribution policy.

# 2026-07-05 Run: Lesson 0084 GitHub Discussions Course Q&A Workflow

## Completed

- Confirmed Lesson 0083 content is normal: nine-section structure, project board field model, status mapping, operating rules, and remote-configuration boundary are all present.
- Re-ran documentation contract tests and whitespace check for Lesson 0083 before continuing.
- Completed Lesson 0084: GitHub Discussions Course Q&A Workflow.
- Added `.github/DISCUSSIONS.md` documenting recommended discussion categories, issue-vs-discussion decision rules, answer quality checklist, conversion flow, and production notes.
- Added documentation contract coverage for Discussions workflow, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0084, Reference 0084, learning record 0075, updated Lesson 0083 navigation, Reference 0083 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 16 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 111 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/DISCUSSIONS.md`
- `lessons/0084-github-discussions-course-qa-workflow.html`
- `lessons/0083-github-projects-board-workflow.html`
- `reference/0084-github-discussions-course-qa-workflow-cheatsheet.html`
- `reference/0083-github-projects-board-workflow-cheatsheet.html`
- `learning-records/0075-github-discussions-course-qa-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0085 after user review; a natural next topic is GitHub release notes or tags for publishing course batches.

# 2026-07-05 Run: Lesson 0083 GitHub Projects Board Workflow

## Completed

- Completed Lesson 0083: GitHub Projects Board Workflow.
- Added `.github/PROJECT_BOARD.md` documenting the recommended GitHub Projects board for the course repository.
- Defined required project fields: Status, Priority, Area, Type, and Lesson.
- Added recommended views: Triage Queue, Ready Work, Course Docs, GitHub Workflow, and Done Review.
- Added status mapping from `status:*` issue labels to Projects Status values, plus operating rules, automation boundaries, and production notes.
- Added documentation contract coverage for the project board workflow, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0083, Reference 0083, learning record 0074, updated Lesson 0082 navigation, Reference 0082 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 15 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 110 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/PROJECT_BOARD.md`
- `lessons/0083-github-projects-board-workflow.html`
- `lessons/0082-github-issue-triage-labels-workflow.html`
- `reference/0083-github-projects-board-workflow-cheatsheet.html`
- `reference/0082-github-issue-triage-labels-workflow-cheatsheet.html`
- `learning-records/0074-github-projects-board-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0084 after user review; a natural next topic is GitHub Discussions for course Q&A and long-form learner support.

# 2026-07-05 Run: Lesson 0082 GitHub Issue Triage Labels Workflow

## Completed

- Completed Lesson 0082: GitHub Issue Triage Labels Workflow.
- Added `.github/ISSUE_TRIAGE.md` documenting type, area, priority, and status label dimensions.
- Added priority rules, status flow, triage checklist, course-specific examples, and production notes for label governance.
- Added documentation contract coverage for issue triage labels, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0082, Reference 0082, learning record 0073, updated Lesson 0081 navigation, Reference 0081 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 14 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 109 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/ISSUE_TRIAGE.md`
- `lessons/0082-github-issue-triage-labels-workflow.html`
- `lessons/0081-github-issue-templates.html`
- `reference/0082-github-issue-triage-labels-workflow-cheatsheet.html`
- `reference/0081-github-issue-templates-cheatsheet.html`
- `learning-records/0073-github-issue-triage-labels-workflow.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0083 after user review; a natural next topic is GitHub Discussions or Projects board workflow after issue triage labels are defined.

# 2026-07-05 Run: Lesson 0081 GitHub Issue Templates

## Completed

- Completed Lesson 0081: GitHub Issue Templates.
- Added `.github/ISSUE_TEMPLATE/` with Issue Forms for bug reports, lesson requests, and documentation fixes.
- Added `.github/ISSUE_TEMPLATE/config.yml` to disable blank issues and keep feedback structured.
- Added documentation contract coverage for issue templates, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0081, Reference 0081, learning record 0072, updated Lesson 0080 navigation, Reference 0080 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Verification

- `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q` -> 13 passed.
- `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q` -> 54 passed.
- `.\.venv\Scripts\python.exe -m pytest -q` -> 108 passed, 1 existing StarletteDeprecationWarning.
- `git diff --check` -> no whitespace errors; Windows LF-to-CRLF warnings only.

## Files touched

- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/lesson_request.yml`
- `.github/ISSUE_TEMPLATE/documentation_fix.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `lessons/0081-github-issue-templates.html`
- `lessons/0080-github-codeowners-review-ownership.html`
- `reference/0081-github-issue-templates-cheatsheet.html`
- `reference/0080-github-codeowners-review-ownership-cheatsheet.html`
- `learning-records/0072-github-issue-templates.md`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `tests/test_course_docs_contract.py`
- `COURSE_PROGRESS.md`

## Next suggested step

Run documentation, provider, full pytest, and whitespace checks. Continue with Lesson 0082 after user review; a natural next topic is GitHub issue triage labels and project board workflow.

# 2026-07-05 Run: Lesson 0080 GitHub CODEOWNERS Review Ownership

## Completed

- Completed Lesson 0080: GitHub CODEOWNERS Review Ownership.
- Added `.github/CODEOWNERS` as a teaching template for repository review ownership.
- The CODEOWNERS template maps backend code, tests, lessons, references, learning records, root docs, and GitHub governance files to placeholder owner teams.
- Added documentation contract coverage for the CODEOWNERS file, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0080, Reference 0080, learning record 0071, updated Lesson 0079 navigation, Reference 0079 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Files touched

- `.github/CODEOWNERS`
- `tests/test_course_docs_contract.py`
- `lessons/0079-github-pull-request-template.html`
- `lessons/0080-github-codeowners-review-ownership.html`
- `reference/0079-github-pull-request-template-cheatsheet.html`
- `reference/0080-github-codeowners-review-ownership-cheatsheet.html`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `learning-records/0071-github-codeowners-review-ownership.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0081 after user review. A natural next topic is GitHub issue templates, so bug reports, lesson requests, and documentation fixes enter the repository with enough structure.

# 2026-07-05 Run: Lesson 0079 GitHub Pull Request Template

## Completed

- Completed Lesson 0079: GitHub Pull Request Template.
- Added `.github/PULL_REQUEST_TEMPLATE.md` as the repository pull request checklist.
- The template asks contributors for summary, change type, verification evidence, course documentation checklist, and risk notes.
- Added documentation contract coverage for the PR template, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0079, Reference 0079, learning record 0070, updated Lesson 0078 navigation, Reference 0078 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Files touched

- `.github/PULL_REQUEST_TEMPLATE.md`
- `tests/test_course_docs_contract.py`
- `lessons/0078-github-branch-protection-required-checks.html`
- `lessons/0079-github-pull-request-template.html`
- `reference/0078-github-branch-protection-required-checks-cheatsheet.html`
- `reference/0079-github-pull-request-template-cheatsheet.html`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `learning-records/0070-github-pull-request-template.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0080 after user review. A natural next topic is CODEOWNERS or issue templates, so ownership and contribution intake are explicit after PR templates and branch protection are in place.

# 2026-07-05 Run: Lesson 0078 GitHub Branch Protection Required Checks

## Completed

- Completed Lesson 0078: GitHub Branch Protection Required Checks.
- Added `.github/BRANCH_PROTECTION.md` to document the `main` branch protection policy and required status check name.
- Documented `pytest and documentation contracts` as the required check produced by the Course CI workflow.
- Added documentation contract coverage for the branch protection policy, README links, DEVELOPMENT links, and the new lesson's fixed review structure.
- Added Lesson 0078, Reference 0078, learning record 0069, updated Lesson 0077 navigation, Reference 0077 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Files touched

- `.github/BRANCH_PROTECTION.md`
- `tests/test_course_docs_contract.py`
- `lessons/0077-github-actions-ci-workflow.html`
- `lessons/0078-github-branch-protection-required-checks.html`
- `reference/0077-github-actions-ci-workflow-cheatsheet.html`
- `reference/0078-github-branch-protection-required-checks-cheatsheet.html`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `learning-records/0069-github-branch-protection-required-checks.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0079 after user review. A natural next topic is GitHub pull request templates or CODEOWNERS, so new contributors know what evidence to provide when CI and branch protection are active.

# 2026-07-05 Run: Lesson 0077 GitHub Actions CI Workflow

## Completed

- Completed Lesson 0077: GitHub Actions CI Workflow.
- Added `.github/workflows/ci.yml` as the repository-level CI workflow.
- The workflow runs provider HTTP tests, documentation contract tests, the full pytest suite, and committed diff whitespace checks.
- Added documentation contract coverage to ensure the CI workflow keeps the required quality gates.
- Added Lesson 0077, Reference 0077, learning record 0068, updated Lesson 0076 navigation, Reference 0076 navigation, README, DEVELOPMENT.md, main course index, and `NOTES.md`.

## Files touched

- `.github/workflows/ci.yml`
- `tests/test_course_docs_contract.py`
- `lessons/0076-github-development-workflow.html`
- `lessons/0077-github-actions-ci-workflow.html`
- `reference/0076-github-development-workflow-cheatsheet.html`
- `reference/0077-github-actions-ci-workflow-cheatsheet.html`
- `README.md`
- `DEVELOPMENT.md`
- `index.html`
- `NOTES.md`
- `learning-records/0068-github-actions-ci-workflow.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0078 after user review. A natural next topic is GitHub branch protection and required status checks, explaining how CI results become merge-blocking project governance.

# 2026-07-05 Run: Quality Audit Lessons 0071-0076

## Completed

- Continued the user-requested quality review without producing new lessons.
- Re-audited Lessons 0071-0076 against the required "Final Review + CSDN Deep Dive" standard.
- Lightly refactored each lesson with explicit review reinforcement blocks:
  - Lesson 0071 now emphasizes validation vs repair, complete error collection, and safe mathematical consistency checks.
  - Lesson 0072 now clarifies practice sessions as traceable orchestration packages rather than duplicated business logic.
  - Lesson 0073 now distinguishes Markdown export from session execution and documents visibility boundaries for cards, answer keys, and reports.
  - Lesson 0074 now frames release checklists as machine-readable quality gates with per-check evidence.
  - Lesson 0075 now treats README as a GitHub-facing public interface protected by documentation contract tests.
  - Lesson 0076 now treats `DEVELOPMENT.md` as a maintainable collaboration contract for code, lesson, documentation, and release work.
- Expanded the documentation contract test so audited Lessons 0065-0076 must retain both "复核补强" and "逐行精读补充" content.

## Files touched

- `lessons/0071-provider-metrics-grading-summary-validation.html`
- `lessons/0072-provider-metrics-practice-session-package.html`
- `lessons/0073-provider-metrics-practice-session-markdown.html`
- `lessons/0074-provider-metrics-practice-release-checklist.html`
- `lessons/0075-github-readme-learning-entry.html`
- `lessons/0076-github-development-workflow.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Wait for user review. If approved, continue with the next requested audit batch or resume forward production from Lesson 0077.

# 2026-07-05 Run: Quality Audit Lessons 0065-0070

## Completed

- Paused forward lesson production per user request.
- Re-audited Lessons 0065-0070 against the required "Final Review + CSDN Deep Dive" standard.
- Lightly refactored each lesson with explicit review reinforcement blocks:
  - Lesson 0065 now emphasizes renderer purity, field-contract failure behavior, stable ordering, and Markdown injection boundaries.
  - Lesson 0066 now separates visible prompt facts from hidden grading anchors and explains why prompt leakage destroys training value.
  - Lesson 0067 now treats the answer key as the training baseline, not an optional appendix, and documents empty-input behavior.
  - Lesson 0068 now clarifies deterministic anchor grading, explainable failure fields, and extensible pass-condition design.
  - Lesson 0069 now hardens summary formulas, failed/unanswered semantics, and extra-response handling.
  - Lesson 0070 now clarifies Markdown as a projection of summary data, not a replacement machine-readable source.
- Added a documentation contract test requiring the audited lessons to keep both "复核补强" and "逐行精读补充" content.

## Files touched

- `lessons/0065-provider-metrics-findings-markdown-report.html`
- `lessons/0066-provider-metrics-runbook-exercise-cards.html`
- `lessons/0067-provider-metrics-exercise-answer-key.html`
- `lessons/0068-provider-metrics-exercise-grading-anchors.html`
- `lessons/0069-provider-metrics-grading-summary.html`
- `lessons/0070-provider-metrics-grading-summary-markdown.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Wait for user review. If approved, either continue auditing the next requested batch or resume forward lesson production from Lesson 0077.

# 2026-07-05 Run: Lesson 0076 GitHub Development Workflow

## Completed

- Completed Lesson 0076: GitHub Development Workflow.
- Added root `DEVELOPMENT.md` documenting code-change, lesson-change, documentation-change, and GitHub release-readiness workflows.
- Updated root `README.md` to link the development workflow.
- Added documentation contract coverage for `DEVELOPMENT.md` required commands and fixed lesson structure.
- Added Lesson 0076, Reference 0076, learning record 0067, updated Lesson 0075 navigation, Reference 0075 navigation, main course index, and `NOTES.md`.

## Files touched

- `DEVELOPMENT.md`
- `README.md`
- `tests/test_course_docs_contract.py`
- `lessons/0075-github-readme-learning-entry.html`
- `lessons/0076-github-development-workflow.html`
- `reference/0075-github-readme-learning-entry-cheatsheet.html`
- `reference/0076-github-development-workflow-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0067-github-development-workflow.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0077 after user review. A natural next topic is repository release checklist integration or CI workflow planning for the documented maintenance commands.

# 2026-07-05 Run: Lesson 0075 GitHub README Learning Entry

## Completed

- Completed Lesson 0075: GitHub README Learning Entry.
- Upgraded root `README.md` into a GitHub-friendly learning entry with course index, learning route, run commands, test commands, provider metrics docs, and runbook practice package links.
- Added `test_root_readme_guides_github_learners_to_course_and_runbook()` to protect README links and commands as documentation contract.
- Added Lesson 0075, Reference 0075, learning record 0066, updated Lesson 0074 navigation, Reference 0074 navigation, main course index, `NOTES.md`, and lesson structure contract coverage.

## Files touched

- `README.md`
- `tests/test_course_docs_contract.py`
- `lessons/0074-provider-metrics-practice-release-checklist.html`
- `lessons/0075-github-readme-learning-entry.html`
- `reference/0074-provider-metrics-practice-release-checklist-cheatsheet.html`
- `reference/0075-github-readme-learning-entry-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0066-github-readme-learning-entry.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0076 after user review. A natural next topic is repository structure cleanup and GitHub contribution/development workflow documentation.

# 2026-07-05 Run: Lesson 0074 Provider Metrics Practice Release Checklist

## Completed

- Completed Lesson 0074: Provider Metrics Practice Release Checklist.
- Added `build_provider_metrics_runbook_practice_release_checklist()` as a pure GitHub release-readiness checker for complete practice packages.
- Added provider HTTP tests for complete package readiness and incomplete package failure reporting.
- Added Lesson 0074, Reference 0074, learning record 0065, updated Lesson 0073 navigation, Reference 0073 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0073-provider-metrics-practice-session-markdown.html`
- `lessons/0074-provider-metrics-practice-release-checklist.html`
- `reference/0073-provider-metrics-practice-session-markdown-cheatsheet.html`
- `reference/0074-provider-metrics-practice-release-checklist-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0065-provider-metrics-practice-release-checklist.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0075 after user review. A natural next topic is GitHub project README integration and final repository learning path organization.

# 2026-07-05 Run: Lesson 0073 Provider Metrics Practice Session Markdown

## Completed

- Completed Lesson 0073: Provider Metrics Practice Session Markdown.
- Added `render_provider_metrics_runbook_practice_session_markdown()` as a pure export helper for complete practice sessions.
- Added provider HTTP test coverage for Markdown package sections, exercise-card table output, answer key inclusion, grading report inclusion, and trailing newline.
- Added Lesson 0073, Reference 0073, learning record 0064, updated Lesson 0072 navigation, Reference 0072 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0072-provider-metrics-practice-session-package.html`
- `lessons/0073-provider-metrics-practice-session-markdown.html`
- `reference/0072-provider-metrics-practice-session-package-cheatsheet.html`
- `reference/0073-provider-metrics-practice-session-markdown-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0064-provider-metrics-practice-session-markdown.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0074 after user review. A natural next topic is preparing the GitHub release checklist or course README integration for the completed runbook training package.

# 2026-07-05 Run: Lesson 0072 Provider Metrics Practice Session Package

## Completed

- Completed Lesson 0072: Provider Metrics Practice Session Package.
- Added `build_provider_metrics_runbook_practice_session()` as a pure orchestration helper for the complete runbook training pipeline.
- Added provider HTTP test coverage for end-to-end session artifacts, counts, validation, answer key, findings report, and grading report.
- Added Lesson 0072, Reference 0072, learning record 0063, updated Lesson 0071 navigation, Reference 0071 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0071-provider-metrics-grading-summary-validation.html`
- `lessons/0072-provider-metrics-practice-session-package.html`
- `reference/0071-provider-metrics-grading-summary-validation-cheatsheet.html`
- `reference/0072-provider-metrics-practice-session-package-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0063-provider-metrics-practice-session-package.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0073 after user review. A natural next topic is exporting or documenting the complete practice session for GitHub release readiness.

# 2026-07-05 Run: Lesson 0071 Provider Metrics Grading Summary Validation

## Completed

- Completed Lesson 0071: Provider Metrics Grading Summary Validation.
- Added `validate_provider_metrics_runbook_grading_summary()` as a pure summary contract checker.
- Added provider HTTP tests for accepting valid summaries and reporting multiple contract errors in malformed summaries.
- Added Lesson 0071, Reference 0071, learning record 0062, updated Lesson 0070 navigation, Reference 0070 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0070-provider-metrics-grading-summary-markdown.html`
- `lessons/0071-provider-metrics-grading-summary-validation.html`
- `reference/0070-provider-metrics-grading-summary-markdown-cheatsheet.html`
- `reference/0071-provider-metrics-grading-summary-validation-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0062-provider-metrics-grading-summary-validation.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0072 after user review. A natural next topic is packaging a complete runbook practice session from samples through validation and Markdown report rendering.

# 2026-07-05 Run: Lesson 0070 Provider Metrics Grading Summary Markdown

## Completed

- Completed Lesson 0070: Provider Metrics Grading Summary Markdown.
- Added `render_provider_metrics_runbook_grading_summary_markdown()` as a pure report renderer over grading summaries.
- Added provider HTTP test coverage for stable summary Markdown rendering.
- Added Lesson 0070, Reference 0070, learning record 0061, updated Lesson 0069 navigation, Reference 0069 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0069-provider-metrics-grading-summary.html`
- `lessons/0070-provider-metrics-grading-summary-markdown.html`
- `reference/0069-provider-metrics-grading-summary-cheatsheet.html`
- `reference/0070-provider-metrics-grading-summary-markdown-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0061-provider-metrics-grading-summary-markdown.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0071 after user review. A natural next topic is exporting a complete practice package or adding schema validation for grading report inputs.

# 2026-07-05 Run: Lesson 0069 Provider Metrics Grading Summary

## Completed

- Completed Lesson 0069: Provider Metrics Grading Summary.
- Added `summarize_provider_metrics_runbook_exercise_grades()` as a pure batch summary helper over existing single-card grading.
- Added provider HTTP test coverage for total, answered, passed, failed, unanswered, per-card answered flags, and missing-anchor details.
- Added Lesson 0069, Reference 0069, learning record 0060, updated Lesson 0068 navigation, Reference 0068 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0068-provider-metrics-exercise-grading-anchors.html`
- `lessons/0069-provider-metrics-grading-summary.html`
- `reference/0068-provider-metrics-exercise-grading-anchors-cheatsheet.html`
- `reference/0069-provider-metrics-grading-summary-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0060-provider-metrics-grading-summary.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0070 after user review. A natural next topic is rendering the grading summary as a Markdown report or exporting graded practice results while keeping raw response text out of the report.

# 2026-07-05 Run: Lesson 0068 Provider Metrics Exercise Grading Anchors

## Completed

- Completed Lesson 0068: Provider Metrics Exercise Grading Anchors.
- Added `grade_provider_metrics_runbook_exercise_answer()` as a pure teaching-grade scoring helper.
- Added provider HTTP tests for passing exact grading anchors and reporting missing grading anchors.
- Added Lesson 0068, Reference 0068, learning record 0059, updated Lesson 0067 navigation, Reference 0067 navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0067-provider-metrics-exercise-answer-key.html`
- `lessons/0068-provider-metrics-exercise-grading-anchors.html`
- `reference/0067-provider-metrics-exercise-answer-key-cheatsheet.html`
- `reference/0068-provider-metrics-exercise-grading-anchors-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0059-provider-metrics-exercise-grading-anchors.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0069 after user review. A natural next topic is provider metrics grading report rendering or graded practice datasets, while keeping teaching-grade grading separate from production exercise platforms.

# 2026-07-05 Run: Lessons 0065-0067 Provider Metrics Runbook Training

## Completed

- Manually executed the requested `00:30` continuation task after the heartbeat did not visibly start on time.
- Completed three new lessons after Lesson 0064:
  - Lesson 0065: Provider Metrics Findings Markdown Report.
  - Lesson 0066: Provider Metrics Runbook Exercise Cards.
  - Lesson 0067: Provider Metrics Exercise Answer Key.
- Added pure helpers in `first_api/services/provider_http.py`:
  - `render_provider_metrics_runbook_findings_markdown()`.
  - `build_provider_metrics_runbook_exercise_cards()`.
  - `render_provider_metrics_runbook_exercise_answer_key()`.
- Added provider HTTP tests for Markdown rendering, exercise card generation, and answer-key rendering.
- Added Lesson and Reference pages for 0065-0067, updated navigation, provider metrics index, provider metrics runbook, main course index, `NOTES.md`, learning records, and documentation contract coverage.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0064-provider-metrics-runbook-findings.html`
- `lessons/0065-provider-metrics-findings-markdown-report.html`
- `lessons/0066-provider-metrics-runbook-exercise-cards.html`
- `lessons/0067-provider-metrics-exercise-answer-key.html`
- `reference/0064-provider-metrics-runbook-findings-cheatsheet.html`
- `reference/0065-provider-metrics-findings-markdown-report-cheatsheet.html`
- `reference/0066-provider-metrics-runbook-exercise-cards-cheatsheet.html`
- `reference/0067-provider-metrics-exercise-answer-key-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0056-provider-metrics-findings-markdown-report.md`
- `learning-records/0057-provider-metrics-runbook-exercise-cards.md`
- `learning-records/0058-provider-metrics-exercise-answer-key.md`
- `COURSE_PROGRESS.md`

## Next task

At the scheduled `06:00` follow-up, first inspect this run's files and test results, then continue from Lesson 0068 with the same standard and avoid overwriting Lessons 0065-0067.

## Blockers

- The original `00:30` heartbeat did not visibly start on time, so the task was executed manually in this thread.

# 2026-07-05 Run: 00:30 Manual Takeover Checkpoint

## Context Compression / Handoff

- The scheduled heartbeat did not visibly start by `2026-07-05 00:34 +08:00`, so this thread manually took over the same requested task.
- Current course standard remains the fixed nine-section "Final Review + CSDN Deep Dive" style: framework, principles, line-by-line code reading, runtime flow, confusion comparisons, common errors, production-vs-teaching differences, exercises with answers, and interview Q&A.
- Latest completed lesson before this takeover: Lesson 0064 Provider Metrics Runbook Findings.
- Latest core code area: `first_api/services/provider_http.py`, especially provider metrics scenario samples and runbook findings helpers.
- Verification before takeover from the prior run: provider HTTP tests, course docs contract tests, full pytest, and `git diff --check` passed with only the existing Starlette/FastAPI TestClient warning and Windows LF/CRLF notices.

## Next task

Produce the next three lessons, starting from Lesson 0065, without overwriting Lessons 0063-0064.

# 2026-07-04 Run: Lesson 0064 Provider Metrics Runbook Findings

## Completed

- Completed Lesson 0064: Provider Metrics Runbook Findings.
- Added `build_provider_metrics_runbook_findings()` as a pure explanation helper that translates metric samples into teaching-level `severity`, `finding`, and `next_action` fields.
- Added tests for core scenario findings, unknown outcome handling, and malformed sample validation.
- Added Reference 0064 and updated Lesson 0063, Reference 0063, the provider metrics index, the provider metrics runbook, the main course index, and the documentation contract test.
- Updated `NOTES.md` and added `learning-records/0055-provider-metrics-runbook-findings.md`.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0063-provider-metrics-scenario-fixtures.html`
- `lessons/0064-provider-metrics-runbook-findings.html`
- `reference/0063-provider-metrics-scenario-fixtures-cheatsheet.html`
- `reference/0064-provider-metrics-runbook-findings-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0055-provider-metrics-runbook-findings.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0065 after user review. A natural next topic is provider metrics finding presentation or scenario-driven exercises, while keeping metrics labels and human explanations separated.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Lesson 0063 Provider Metrics Scenario Fixtures

## Completed

- Resumed forward course production after completing the first 62-lesson review pass.
- Completed Lesson 0063: Provider Metrics Scenario Fixtures.
- Added `build_provider_metrics_runbook_scenario_samples()` as a pure helper that returns stable provider metrics practice samples without mutating the in-process metrics counter.
- Added provider HTTP tests proving the scenario samples cover `success`, `retry_scheduled`, `retry_exhausted`, and `fail_fast`, and render correctly through the Prometheus text-style export helper.
- Added Reference 0063 and updated Lesson 0062, Reference 0062, the provider metrics index, the provider metrics runbook, and the main course index for navigation.
- Updated `tests/test_course_docs_contract.py` so Lesson 0063 is protected by the same nine-section review structure contract.
- Updated `NOTES.md` and added `learning-records/0054-provider-metrics-scenario-fixtures.md`.

## Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `tests/test_course_docs_contract.py`
- `lessons/0062-provider-metrics-runbook-checklist.html`
- `lessons/0063-provider-metrics-scenario-fixtures.html`
- `reference/0062-provider-metrics-runbook-checklist-cheatsheet.html`
- `reference/0063-provider-metrics-scenario-fixtures-cheatsheet.html`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `index.html`
- `NOTES.md`
- `learning-records/0054-provider-metrics-scenario-fixtures.md`
- `COURSE_PROGRESS.md`

## Next task

Continue with Lesson 0064 after user review. A natural next topic is provider metrics scenario rendering or scenario-driven runbook exercises, keeping the same high-density standard.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Refactor Batch 11 Lessons 0061-0062

## Completed

- Rebuilt Lessons 0061-0062 into the required "Final Review + CSDN Deep Dive" structure.
- Covered provider metrics documentation indexing and runbook checklist design: docs-as-contract, HTMLParser-based document contract tests, operational metric facts, traceability links, outcome-based troubleshooting, and the teaching-vs-production alert boundary.
- Kept the lessons tied to current project artifacts: `reference/provider-metrics-index.html`, `reference/provider-metrics-runbook.html`, `/provider/metrics`, `/provider/metrics/prometheus`, `provider_prediction_total`, `get_provider_prediction_metric_contract()`, and the provider metrics documentation contract tests.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0062.
- Updated `NOTES.md` to record the final refactor batch for the first 62 lessons.

## Files touched

- `lessons/0061-provider-metrics-documentation-index.html`
- `lessons/0062-provider-metrics-runbook-checklist.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

First 62-lesson review pass is complete. Await user quality review or next course direction.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Refactor Batch 10 Lessons 0055-0060

## Completed

- Rebuilt Lessons 0055-0060 into the required "Final Review + CSDN Deep Dive" structure.
- Covered provider metrics export and governance topics: Prometheus text-style export shape, export contract tests, snapshot boundary isolation, production-vs-teaching metrics boundaries, stable metric naming contracts, and safe naming refactor boundaries.
- Kept the lessons tied to current project code: `render_provider_metrics_prometheus_text()`, `escape_prometheus_label_value()`, `get_provider_metrics_prometheus_text()`, `GET /provider/metrics/prometheus`, `ProviderMetricsCounter.snapshot()`, `PROVIDER_PREDICTION_METRIC_NAME`, `PROVIDER_PREDICTION_METRIC_LABEL_NAMES`, and `get_provider_prediction_metric_contract()`.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0060.
- Updated `NOTES.md` to record the tenth refactor batch.

## Files touched

- `lessons/0055-provider-metrics-export-shape.html`
- `lessons/0056-provider-metrics-export-tests.html`
- `lessons/0057-provider-metrics-snapshot-boundary.html`
- `lessons/0058-provider-metrics-production-boundary.html`
- `lessons/0059-provider-metrics-naming-contract.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0061-0062 after user review, then the first 62-lesson review pass will be complete.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Refactor Batch 9 Lessons 0049-0054

## Completed

- Rebuilt Lessons 0049-0054 into the required "Final Review + CSDN Deep Dive" structure.
- Covered provider metrics foundations: provider error taxonomy, low-cardinality provider metric labels, teaching-only counters, read-only metrics endpoint design, failure outcome samples, and metrics test isolation.
- Kept the lessons tied to current project code: `classify_provider_http_status()`, `ProviderMetricLabels`, `build_provider_metric_labels()`, `ProviderMetricsCounter`, `record_provider_metric()`, `get_provider_metrics_snapshot()`, `GET /provider/metrics`, `reset_provider_metrics()`, and the autouse metrics reset fixture.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0054.
- Updated `NOTES.md` to record the ninth refactor batch.

## Files touched

- `lessons/0049-provider-error-taxonomy.html`
- `lessons/0050-provider-metrics-basics.html`
- `lessons/0051-provider-metrics-counters.html`
- `lessons/0052-provider-metrics-endpoint.html`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `lessons/0054-provider-metrics-test-isolation.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0055-0060 after user review.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Refactor Batch 8 Lessons 0043-0048

## Completed

- Rebuilt Lessons 0043-0048 into the required "Final Review + CSDN Deep Dive" structure.
- Covered provider retry reliability and observability topics: backoff before retry, honoring Retry-After, retry jitter, retry scheduled observability, retry exhaustion, and fail-fast observability.
- Kept the lessons tied to current project code: `parse_retry_after_delay()`, `build_retry_delay_plan()`, `RetryDelayPlan`, `calculate_retry_jitter()`, `wait_before_retry()`, `provider_prediction_retry_scheduled`, `provider_prediction_retry_exhausted`, and `provider_prediction_fail_fast`.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0048.
- Updated `NOTES.md` to record the eighth refactor batch.

## Files touched

- `lessons/0043-backoff-before-retry.html`
- `lessons/0044-honor-retry-after.html`
- `lessons/0045-retry-jitter.html`
- `lessons/0046-retry-observability.html`
- `lessons/0047-retry-exhaustion.html`
- `lessons/0048-fail-fast-observability.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0049-0054 after user review.

## Blockers

- No project blocker found.

# 2026-07-04 Run: Refactor Batch 7 Lessons 0037-0042

## Completed

- Rebuilt Lessons 0037-0042 into the required "Final Review + CSDN Deep Dive" structure.
- Covered provider prediction adapters, provider predict endpoint wiring, prediction backend switching, prediction observability, prediction service orchestration, and provider retry policy.
- Kept the lessons tied to current project code: `ProviderPredictionPayload`, `ProviderPredictionBody`, `request_provider_prediction()`, `POST /provider/predict`, `FIRST_API_AI_PREDICTION_BACKEND`, `X-Prediction-*` headers, `run_prediction()`, and retry classification for provider failures.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0042.
- Updated `NOTES.md` to record the seventh refactor batch.

## Files touched

- `lessons/0037-provider-prediction-adapter.html`
- `lessons/0038-provider-predict-endpoint.html`
- `lessons/0039-prediction-backend-switch.html`
- `lessons/0040-prediction-observability.html`
- `lessons/0041-prediction-service-orchestration.html`
- `lessons/0042-provider-retry-policy.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0043-0048 after user review.

## Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0048 Fail-fast Observability

### Completed

- Located current course progress from `NOTES.md`, `learning-records/0038-retry-exhaustion.md`, and the latest Lesson/Reference 0047 files.
- Completed Lesson 0048: Fail-fast Observability.
- Added fail-fast structured logging for provider prediction non-retryable HTTP errors and invalid provider response bodies.
- Added tests proving HTTP 400 and invalid response body paths do not retry and do not emit retry-exhausted logs.
- Added Reference 0048 and updated course index/navigation from Lesson 0047 and Reference 0047.
- Updated `NOTES.md` and added `learning-records/0039-fail-fast-observability.md`.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0047-retry-exhaustion.html`
- `lessons/0048-fail-fast-observability.html`
- `reference/0047-retry-exhaustion-cheatsheet.html`
- `reference/0048-fail-fast-observability-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0039-fail-fast-observability.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice, including one code behavior improvement, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: extending into Lesson 0049 in the same run would risk compressing the explanation quality and weakening verification. The next run should continue with exactly one new lesson slice.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 23 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 57 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0049: Provider Error Taxonomy. Suggested scope:

- Organize provider failure classes into a clear taxonomy: timeout, request error, retryable HTTP status, non-retryable HTTP status, invalid response, scheduled retry, retry exhaustion, and fail fast.
- Prefer a small, verifiable slice. A good candidate is a lesson/reference pair plus tests or documentation that ensure the taxonomy names stay stable.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0049 Provider Error Taxonomy

### Completed

- Continued from the Lesson 0048 checkpoint without re-planning the whole course.
- Completed Lesson 0049: Provider Error Taxonomy.
- Added `ProviderFailureCategory` and `classify_provider_http_status()` to make HTTP status retry taxonomy explicit.
- Added a provider HTTP test that protects taxonomy names for retryable and non-retryable status codes.
- Added Reference 0049 and updated course index/navigation from Lesson 0048 and Reference 0048.
- Updated `NOTES.md` and added `learning-records/0040-provider-error-taxonomy.md`.
- Updated automation rule: after every 3 completed lessons, stop and save a checkpoint; this continuation batch has completed 1 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0048-fail-fast-observability.html`
- `lessons/0049-provider-error-taxonomy.html`
- `reference/0048-fail-fast-observability-cheatsheet.html`
- `reference/0049-provider-error-taxonomy-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0040-provider-error-taxonomy.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one compact but complete course slice, including a small taxonomy helper, focused test coverage, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this is lesson 1 of the new 3-lesson continuation batch. Continue with at most two more complete lessons before forcing a checkpoint/compaction stop. If quota becomes risky earlier, stop with a checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 24 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 58 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0050: Provider Metrics Basics. Suggested scope:

- Explain the difference between logs and metrics for provider failures.
- Prefer a small, verifiable implementation such as in-process counters or a metrics-shape helper if it fits the project without adding dependencies.
- Keep the lesson tied to the provider error taxonomy from Lesson 0049.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0050 Provider Metrics Basics

### Completed

- Continued from the Lesson 0049 checkpoint.
- Completed Lesson 0050: Provider Metrics Basics.
- Added `ProviderMetricLabels` and `build_provider_metric_labels()` to define stable low-cardinality provider prediction metric labels.
- Added tests for success labels and fail-fast failure labels, including a guard that raw request text is not used as a metric label value.
- Added Reference 0050 and updated course index/navigation from Lesson 0049 and Reference 0049.
- Updated `NOTES.md` and added `learning-records/0041-provider-metrics-basics.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0049-provider-error-taxonomy.html`
- `lessons/0050-provider-metrics-basics.html`
- `reference/0049-provider-error-taxonomy-cheatsheet.html`
- `reference/0050-provider-metrics-basics-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0041-provider-metrics-basics.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one focused lesson slice covering metric label shape rather than a full metrics backend. This keeps the lesson complete without adding deployment or monitoring-platform complexity.

Reason for split: this is lesson 2 of the current 3-lesson continuation batch. One more complete lesson can be produced before the required checkpoint/compaction stop, unless quota becomes risky earlier.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 26 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 60 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0051: Provider Metrics Counters. Suggested scope:

- Add a small dependency-free in-process counter or counter-shape helper for provider prediction outcomes.
- Keep it explicitly educational and avoid presenting in-memory counters as a production multi-process metrics solution.
- After Lesson 0051, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0051 Provider Metrics Counters

### Completed

- Continued from the Lesson 0050 checkpoint.
- Completed Lesson 0051: Provider Metrics Counters.
- Added teaching-only `ProviderMetricsCounter` to demonstrate count accumulation by stable provider metric label sets.
- Added tests for repeated label accumulation and rejecting non-positive increments.
- Added Reference 0051 and updated course index/navigation from Lesson 0050 and Reference 0050.
- Updated `NOTES.md` and added `learning-records/0042-provider-metrics-counters.md`.
- Completed the current 3-lesson continuation batch: Lessons 0049, 0050, and 0051.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0050-provider-metrics-basics.html`
- `lessons/0051-provider-metrics-counters.html`
- `reference/0050-provider-metrics-basics-cheatsheet.html`
- `reference/0051-provider-metrics-counters-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0042-provider-metrics-counters.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one focused counter-semantics lesson using a dependency-free teaching helper, plus tests, lesson, reference, navigation, and progress records.

Reason for stopping after this lesson: user requested automatic context checkpointing after every 3 completed lessons. This run completed the 3-lesson batch after Lesson 0048: Lessons 0049, 0050, and 0051.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 28 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 62 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0052: Provider Metrics Endpoint. Suggested scope:

- Expose a read-only teaching endpoint or service-level snapshot for provider metrics.
- Keep clear that in-process metrics are educational and not production multi-instance aggregation.
- Start a new 3-lesson batch from Lesson 0052.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0052 Provider Metrics Endpoint

### Completed

- Continued from the Lesson 0051 checkpoint and started a new 3-lesson batch.
- Completed Lesson 0052: Provider Metrics Endpoint.
- Connected provider prediction success, retry scheduled, retry exhausted, and fail-fast outcomes to the teaching-only in-process metrics counter.
- Added `GET /provider/metrics` as a read-only snapshot endpoint with response models for metric labels and samples.
- Added tests proving provider prediction success records a metric and the endpoint returns the expected snapshot shape.
- Added Reference 0052 and updated course index/navigation from Lesson 0051 and Reference 0051.
- Updated `NOTES.md` and added `learning-records/0043-provider-metrics-endpoint.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `first_api/schemas.py`
- `first_api/routers/predictions.py`
- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0051-provider-metrics-counters.html`
- `lessons/0052-provider-metrics-endpoint.html`
- `reference/0051-provider-metrics-counters-cheatsheet.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0043-provider-metrics-endpoint.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice, including a small code path for metrics recording and snapshot exposure, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson was already a complete vertical slice from provider event to HTTP response. Extending into Lesson 0053 would risk weakening failure-outcome examples and would exceed the intended one-slice automation cadence. Continue with at most two more complete lessons before the next forced checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 37 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 64 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0053: Provider Metrics Failure Outcomes. Suggested scope:

- Add focused tests and examples for `retry_scheduled`, `retry_exhausted`, and `fail_fast` samples appearing in `GET /provider/metrics`.
- Keep the endpoint read-only and the counter explicitly teaching-only.
- Avoid introducing Prometheus/OpenTelemetry dependencies until the course is ready to discuss production exposition formats.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0053 Provider Metrics Failure Outcomes

### Completed

- Continued from the Lesson 0052 checkpoint without re-planning the whole course.
- Completed Lesson 0053: Provider Metrics Failure Outcomes.
- Added endpoint-level tests proving `GET /provider/metrics` exposes retry failure outcome samples after retryable provider HTTP 503 paths.
- Added endpoint-level tests proving non-retryable provider HTTP 400 paths produce a `fail_fast` metrics sample without scheduled retry samples.
- Added Reference 0053 and updated course index/navigation from Lesson 0052 and Reference 0052.
- Updated `NOTES.md` and added `learning-records/0044-provider-metrics-failure-outcomes.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons: 0052 and 0053.

### Files touched

- `tests/test_ai_client_dependency.py`
- `lessons/0052-provider-metrics-endpoint.html`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0044-provider-metrics-failure-outcomes.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on failure-outcome visibility through the existing metrics endpoint, with two endpoint-level tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson completes the failure-outcome testing story without introducing new metrics backend concepts. Lesson 0054 should stay separate and can focus on test isolation for process-level teaching state. One more complete lesson can be produced before the required 3-lesson checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_ai_client_dependency.py tests\test_provider_http.py -q`
- Result: 39 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 66 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0054: Provider Metrics Test Isolation. Suggested scope:

- Make the `reset_provider_metrics()` pattern explicit as a teaching topic.
- Explain why in-process global state is convenient for lessons but needs strict test boundaries.
- Consider a small pytest fixture if it improves clarity without over-refactoring.
- After Lesson 0054, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0054 Provider Metrics Test Isolation

### Completed

- Continued from the Lesson 0053 checkpoint.
- Completed Lesson 0054: Provider Metrics Test Isolation.
- Added an autouse pytest fixture in `tests/test_ai_client_dependency.py` to reset the in-process provider metrics counter before and after each test in that file.
- Removed repeated manual `reset_provider_metrics()` calls from provider metrics endpoint tests while preserving endpoint behavior coverage.
- Added Reference 0054 and updated course index/navigation from Lesson 0053 and Reference 0053.
- Updated `NOTES.md` and added `learning-records/0045-provider-metrics-test-isolation.md`.
- Completed the current 3-lesson continuation batch: Lessons 0052, 0053, and 0054.

### Files touched

- `tests/test_ai_client_dependency.py`
- `lessons/0053-provider-metrics-failure-outcomes.html`
- `lessons/0054-provider-metrics-test-isolation.html`
- `reference/0053-provider-metrics-failure-outcomes-cheatsheet.html`
- `reference/0054-provider-metrics-test-isolation-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0045-provider-metrics-test-isolation.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on test isolation for the existing in-process provider metrics counter, with a small pytest fixture refactor, one full lesson, one quick reference, navigation, and progress records.

Reason for stopping after this lesson: this run completes the 3-lesson batch that started at Lesson 0052. Per the user's checkpoint rule, the next run should start a fresh batch from Lesson 0055 after this saved checkpoint rather than continuing immediately into another lesson in the same context.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_ai_client_dependency.py tests\test_provider_http.py -q`
- Result: 39 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 66 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0055: Provider Metrics Export Shape. Suggested scope:

- Explain the difference between the current JSON teaching snapshot and production metrics exposition formats.
- Keep the first step dependency-free if possible, such as a helper that renders a simple Prometheus-like text shape from the existing snapshot.
- Preserve the warning that in-process counters are teaching-only and not multi-instance aggregation.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0055 Provider Metrics Export Shape

### Completed

- Started a fresh 3-lesson batch after the Lessons 0052-0054 checkpoint.
- Completed Lesson 0055: Provider Metrics Export Shape.
- Added a dependency-free Prometheus text-style renderer for provider metrics snapshots.
- Added `GET /provider/metrics/prometheus` using `PlainTextResponse` for a teaching text export shape.
- Added tests for stable text rendering, label value escaping, text content type, and endpoint output.
- Added Reference 0055 and updated course index/navigation from Lesson 0054 and Reference 0054.
- Updated `NOTES.md` and added `learning-records/0046-provider-metrics-export-shape.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

- `first_api/services/provider_http.py`
- `first_api/routers/predictions.py`
- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0054-provider-metrics-test-isolation.html`
- `lessons/0055-provider-metrics-export-shape.html`
- `reference/0054-provider-metrics-test-isolation-cheatsheet.html`
- `reference/0055-provider-metrics-export-shape-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0046-provider-metrics-export-shape.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on metrics export shape, including a text renderer, one read-only endpoint, focused tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: this lesson explains the first export-shape step without mixing in deeper production concerns. Lesson 0056 should separately cover export edge-case tests and preserve depth.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 41 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 68 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0056: Provider Metrics Export Tests. Suggested scope:

- Add tests and lesson material for empty snapshots, multiple failure outcomes, label escaping edge cases, and response headers for the text export endpoint.
- Keep the implementation dependency-free and explicitly teaching-only.
- Current batch will be 2 of 3 after Lesson 0056.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lessons 0056-0057 Provider Metrics Export Tests and Snapshot Boundary

### Completed

- Continued from the Lesson 0055 checkpoint without re-planning the whole course.
- Completed Lesson 0056: Provider Metrics Export Tests.
- Added text export tests for empty snapshots, special label escaping, empty endpoint output, and retry failure outcome endpoint output.
- Completed Lesson 0057: Provider Metrics Snapshot Boundary.
- Added a counter boundary test proving mutating a returned snapshot does not change `ProviderMetricsCounter` internal state.
- Added References 0056 and 0057, updated course index/navigation from Lesson 0055 and Reference 0055.
- Updated `NOTES.md` and added learning records 0047 and 0048.
- Completed the current 3-lesson continuation batch: Lessons 0055, 0056, and 0057.

### Files touched

- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0055-provider-metrics-export-shape.html`
- `lessons/0056-provider-metrics-export-tests.html`
- `lessons/0057-provider-metrics-snapshot-boundary.html`
- `reference/0055-provider-metrics-export-shape-cheatsheet.html`
- `reference/0056-provider-metrics-export-tests-cheatsheet.html`
- `reference/0057-provider-metrics-snapshot-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0047-provider-metrics-export-tests.md`
- `learning-records/0048-provider-metrics-snapshot-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: two complete course slices to finish the active 3-lesson batch. Lesson 0056 focused on metrics text export edge-case tests. Lesson 0057 stayed intentionally smaller and focused on snapshot boundary testing to avoid starting a larger production metrics topic mid-batch.

Reason for stopping after this run: the batch that started at Lesson 0055 is now complete. Per the user's context-safety rule, save this checkpoint before continuing into the next batch.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py tests\test_ai_client_dependency.py -q`
- Result: 46 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 73 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0058: Provider Metrics Production Boundary. Suggested scope:

- Explain why the current in-process teaching counter is not a production metrics pipeline.
- Discuss multi-process, multi-instance, restart, scrape, storage, and alerting boundaries.
- Keep the next implementation slice small and verifiable, such as documentation/tests around existing endpoint descriptions or an explicit production-boundary note.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0058 Provider Metrics Production Boundary

### Completed

- Started a fresh 3-lesson batch after the Lessons 0055-0057 checkpoint.
- Completed Lesson 0058: Provider Metrics Production Boundary.
- Added an OpenAPI contract test protecting the provider metrics endpoint descriptions:
  - `GET /provider/metrics` remains documented as an in-process teaching snapshot, not production multi-instance aggregation.
  - `GET /provider/metrics/prometheus` remains documented as an educational text export shape, not a production multi-instance metrics pipeline.
- Added Reference 0058 and updated course index/navigation from Lesson 0057 and Reference 0057.
- Updated `NOTES.md` and added `learning-records/0049-provider-metrics-production-boundary.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons.

### Files touched

- `tests/test_openapi_contract.py`
- `lessons/0057-provider-metrics-snapshot-boundary.html`
- `lessons/0058-provider-metrics-production-boundary.html`
- `reference/0057-provider-metrics-snapshot-boundary-cheatsheet.html`
- `reference/0058-provider-metrics-production-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0049-provider-metrics-production-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on the production boundary of the existing teaching metrics endpoints, with one OpenAPI contract test, one full lesson, one quick reference, navigation, and progress records.

Reason for split: production metrics is broad. This lesson intentionally stopped at the documentation and contract boundary instead of adding Prometheus/OpenTelemetry dependencies or deployment instructions. Two more complete lessons can follow in this batch before the next required checkpoint.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_openapi_contract.py -q`
- Result: 4 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 74 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0059: Provider Metrics Naming Contract. Suggested scope:

- Protect the metric name and label names used by the teaching metrics export.
- Explain why stable names and low-cardinality labels matter for dashboards, alerts, and long-term queries.
- Keep the implementation small and verifiable, likely with tests around metric constants and label keys.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0059 Provider Metrics Naming Contract

### Completed

- Continued from the Lesson 0058 checkpoint without re-planning the whole course.
- Completed Lesson 0059: Provider Metrics Naming Contract.
- Added tests protecting `PROVIDER_PREDICTION_METRIC_NAME`, `PROVIDER_PREDICTION_METRIC_HELP`, and the stable provider metric label keys.
- Added a representative retry-exhausted label set test to keep low-cardinality metric dimensions stable.
- Added Reference 0059 and updated course index/navigation from Lesson 0058 and Reference 0058.
- Updated `NOTES.md` and added `learning-records/0050-provider-metrics-naming-contract.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons: 0058 and 0059.

### Files touched

- `tests/test_provider_http.py`
- `lessons/0058-provider-metrics-production-boundary.html`
- `lessons/0059-provider-metrics-naming-contract.html`
- `reference/0058-provider-metrics-production-boundary-cheatsheet.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0050-provider-metrics-naming-contract.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on metrics naming stability, with two small provider HTTP tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: naming contract is a complete slice by itself. The next lesson should separately discuss rename/refactor boundaries so compatibility and migration can be taught without diluting this lesson's core idea.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 35 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 76 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0060: Provider Metrics Naming Refactor Boundary. Suggested scope:

- Explain how to handle metric or label renames safely.
- Discuss compatibility windows, duplicate export periods, documentation updates, dashboard/alert migration, and contract tests.
- After Lesson 0060, stop and save a checkpoint because the current 3-lesson batch will be complete.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0060 Provider Metrics Naming Refactor Boundary

### Completed

- Continued from the Lesson 0059 checkpoint.
- Completed Lesson 0060: Provider Metrics Naming Refactor Boundary.
- Added `PROVIDER_PREDICTION_METRIC_LABEL_NAMES` to make the exported provider metric label-name contract explicit.
- Added `get_provider_prediction_metric_contract()` to expose metric name, HELP text, and label names as a small rename-sensitive contract snapshot.
- Added a provider HTTP test proving the metric contract snapshot contains the fields that must be reviewed before any future metric rename.
- Added Reference 0060 and updated course index/navigation from Lesson 0059 and Reference 0059.
- Updated `NOTES.md` and added `learning-records/0051-provider-metrics-naming-refactor-boundary.md`.
- Completed the current 3-lesson continuation batch: Lessons 0058, 0059, and 0060.

### Files touched

- `first_api/services/provider_http.py`
- `tests/test_provider_http.py`
- `lessons/0059-provider-metrics-naming-contract.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `reference/0059-provider-metrics-naming-contract-cheatsheet.html`
- `reference/0060-provider-metrics-naming-refactor-boundary-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0051-provider-metrics-naming-refactor-boundary.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on safe metrics rename boundaries, with a small contract helper, one provider HTTP test, one full lesson, one quick reference, navigation, and progress records.

Reason for stopping after this lesson: this run completes the 3-lesson batch that started at Lesson 0058. Per the user's checkpoint rule, the next run should start a fresh batch from Lesson 0061 after this saved checkpoint rather than continuing immediately into another lesson in the same context.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- Result: 36 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 77 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Start a fresh batch with Lesson 0061: Provider Metrics Documentation Index. Suggested scope:

- Create or protect a single documentation entry that points to the provider metrics endpoints, naming contract, production boundary, and tests.
- Keep the implementation small and verifiable, such as a docs/reference index page or an OpenAPI/documentation consistency test.
- Start a new 3-lesson batch from Lesson 0061.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0061 Provider Metrics Documentation Index

### Completed

- Started a fresh 3-lesson batch after the Lesson 0058-0060 checkpoint.
- Completed Lesson 0061: Provider Metrics Documentation Index.
- Added `reference/provider-metrics-index.html` as a single provider metrics documentation entry for endpoints, metric contract fields, production boundary notes, related lessons, and tests.
- Added `tests/test_course_docs_contract.py` with HTML parsing tests that protect the documentation entry's required contract terms and links.
- Added Reference 0061 and updated course index/navigation from Lesson 0060 and Reference 0060.
- Updated `NOTES.md` and added `learning-records/0052-provider-metrics-documentation-index.md`.
- Current 3-lesson continuation batch has completed 1 of 3 lessons: 0061.

### Files touched

- `tests/test_course_docs_contract.py`
- `reference/provider-metrics-index.html`
- `lessons/0060-provider-metrics-naming-refactor-boundary.html`
- `lessons/0061-provider-metrics-documentation-index.html`
- `reference/0060-provider-metrics-naming-refactor-boundary-cheatsheet.html`
- `reference/0061-provider-metrics-documentation-index-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0052-provider-metrics-documentation-index.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on provider metrics documentation indexing, with one static documentation entry, one small HTML parser contract test file, one full lesson, one quick reference, navigation, and progress records.

Reason for split: documentation index is a complete and verifiable slice by itself. The next lesson should separately cover a runbook/checklist for investigating metric anomalies, because operational troubleshooting would add a different workflow and should not be compressed into the documentation-index lesson.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 2 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 79 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0062: Provider Metrics Runbook Checklist. Suggested scope:

- Turn the provider metrics endpoints and tests into a small troubleshooting checklist.
- Teach how to inspect success, retry scheduled, retry exhausted, and fail-fast samples.
- Keep it verifiable with a focused test or docs check if the runbook becomes a durable reference page.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Lesson 0062 Provider Metrics Runbook Checklist

### Completed

- Continued from Lesson 0061 in the current 3-lesson batch.
- Completed Lesson 0062: Provider Metrics Runbook Checklist.
- Added `reference/provider-metrics-runbook.html` as a durable troubleshooting checklist for provider metrics endpoints, outcomes, failure labels, and related tests.
- Expanded `tests/test_course_docs_contract.py` with runbook contract tests that protect required endpoints, metric name, outcome names, warning text, and traceability links.
- Added Reference 0062 and updated course index/navigation from Lesson 0061 and Reference 0061.
- Updated `reference/provider-metrics-index.html` to point readers from the documentation index to the runbook.
- Updated `NOTES.md` and added `learning-records/0053-provider-metrics-runbook-checklist.md`.
- Current 3-lesson continuation batch has completed 2 of 3 lessons: 0061 and 0062.

### Files touched

- `tests/test_course_docs_contract.py`
- `reference/provider-metrics-index.html`
- `reference/provider-metrics-runbook.html`
- `lessons/0061-provider-metrics-documentation-index.html`
- `lessons/0062-provider-metrics-runbook-checklist.html`
- `reference/0061-provider-metrics-documentation-index-cheatsheet.html`
- `reference/0062-provider-metrics-runbook-checklist-cheatsheet.html`
- `index.html`
- `NOTES.md`
- `learning-records/0053-provider-metrics-runbook-checklist.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: one complete course slice focused on turning provider metrics into an operational runbook, with one durable runbook page, two small documentation contract tests, one full lesson, one quick reference, navigation, and progress records.

Reason for split: runbook structure is a complete slice. The next lesson should separately create scenario fixtures or predictable sample data so learners can practice the runbook against concrete metric states without mixing scenario generation into the checklist lesson.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 4 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 81 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue with Lesson 0063: Provider Metrics Scenario Fixtures. Suggested scope:

- Create predictable sample scenarios for success, retry scheduled, retry exhausted, and fail-fast metrics.
- Use the scenarios to make the runbook easier to practice and verify.
- After Lesson 0063, save a 3/3 checkpoint for the current batch.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Foundation Lesson Refactor Batch 0001-0006

### Completed

- Paused forward course production after Lesson 0062 per user request.
- Audited the early foundation lessons against the new quality target: "university CS final-review notes + top CSDN technical article" style.
- Rebuilt Lessons 0001-0006 as complete standalone HTML review pages with the required nine-section structure:
  - core knowledge framework;
  - underlying principles;
  - line-by-line code reading;
  - runtime/data-flow breakdown;
  - confusing-point comparisons;
  - common errors and fixes;
  - production vs teaching differences;
  - review exercises with answers;
  - interview questions with analysis.
- Updated the content to match the current project state, including the modular router layout, SQLModel-backed item endpoints, dependency-injected sessions, API-key-protected writes, and provider-ready prediction boundary.
- Added a documentation contract test to ensure the rebuilt 0001-0006 lesson pages keep the required review structure.
- Updated `NOTES.md` with the new refactor direction and completed first batch.

### Files touched

- `lessons/0001-first-fastapi-api.html`
- `lessons/0002-request-body-pydantic.html`
- `lessons/0003-path-and-query-parameters.html`
- `lessons/0004-response-models-and-errors.html`
- `lessons/0005-project-structure-apirouter.html`
- `lessons/0006-dependencies-depends.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: six early lessons, each rewritten as a dense standalone HTML review page. Each page needed principle explanation, source-code binding, runtime flow, production contrast, exercises, and interview material.

Reason for split: the user requested processing six lessons per review batch. Rebuilding more than six lessons in this run would risk reducing the depth of code-reading and production-boundary sections. This batch therefore stops at Lessons 0001-0006 and leaves Lessons 0007-0012 for the next review batch.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 5 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 82 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue the refactor with Lessons 0007-0012:

- 0007 SQLite and SQLModel basics.
- 0008 Database Session and CRUD.
- 0009 Update/Delete CRUD.
- 0010 API Testing with TestClient.
- 0011 Settings and environment variables.
- 0012 API Key authentication.

Keep the same nine-section high-density review structure and align every lesson with the current codebase rather than obsolete early demo code.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Foundation Lesson Refactor Batch 0007-0012

### Completed

- Continued the user-requested review/refactor of the first 62 lessons; did not resume forward production of Lesson 0063.
- Rebuilt Lessons 0007-0012 as complete standalone HTML review pages in the required "university CS final-review notes + top CSDN technical article" style.
- Covered the required nine-section structure in each lesson:
  - core knowledge framework;
  - underlying principles;
  - line-by-line code reading;
  - runtime/data-flow breakdown;
  - confusing-point comparisons;
  - common errors and fixes;
  - production vs teaching differences;
  - review exercises with answers;
  - interview questions with analysis.
- Updated the content to match the current project state:
  - SQLite and SQLModel persistence;
  - request-level Session lifecycle and CRUD transaction flow;
  - PATCH partial-update semantics and DELETE 204 behavior;
  - TestClient, in-memory SQLite, StaticPool, and dependency override isolation;
  - Settings, `.env`, environment-variable prefixing, and public config leakage boundaries;
  - API Key authentication through `APIKeyHeader`, `require_api_key`, and protected write routes.
- Expanded `tests/test_course_docs_contract.py` so the rebuilt structure is now protected for Lessons 0001-0012.
- Updated `NOTES.md` with the completed second refactor batch.

### Files touched

- `lessons/0007-sqlite-sqlmodel-basics.html`
- `lessons/0008-database-session-crud.html`
- `lessons/0009-update-delete-crud.html`
- `lessons/0010-api-testing-testclient.html`
- `lessons/0011-settings-env-vars.html`
- `lessons/0012-api-key-auth.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: six database/testing/config/security lessons, each needing dense principle explanation, source-code binding, lifecycle flow, production boundary, exercises, and interview material.

Reason for split: the user requested six lessons per review batch. Lessons 0007-0012 form a coherent backend-foundation block around persistence, tests, configuration, and authentication. Extending into Lesson 0013 would start the background-task track and risk weakening the required depth.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 5 passed.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 82 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.

### Next task

Continue the refactor with Lessons 0013-0018:

- 0013 BackgroundTasks.
- 0014 Task status API.
- 0015 UploadFile text files.
- 0016 File summary tasks.
- 0017 CORS and browser frontend.
- 0018 Static frontend fetch.

Keep the same nine-section high-density review structure and align every lesson with the current codebase rather than obsolete early demo code.

### Blockers

- No project blocker found.

## 2026-07-04 Run: Foundation Lesson Refactor Batch 0013-0018

### Completed

- Continued the user-requested review/refactor of the first 62 lessons; did not resume forward production of Lesson 0063.
- Rebuilt Lessons 0013-0018 as complete standalone HTML review pages in the required "university CS final-review notes + top CSDN technical article" style.
- Covered the required nine-section structure in each lesson:
  - core knowledge framework;
  - underlying principles;
  - line-by-line code reading;
  - runtime/data-flow breakdown;
  - confusing-point comparisons;
  - common errors and fixes;
  - production vs teaching differences;
  - review exercises with answers;
  - interview questions with analysis.
- Updated the content to match the current codebase:
  - `BackgroundTasks` with `202 Accepted`, persisted queued tasks, response-after scheduling, and independent worker `Session` usage;
  - task status APIs with `SummaryTaskListResponse` envelope, `items/count/limit/offset`, status filtering, and `404`/`422` distinction;
  - `UploadFile` text uploads through `multipart/form-data`, size/UTF-8 validation, `413` vs `422`, and minimal response exposure;
  - file-backed summary tasks using `source_file_id` to connect uploaded input resources with processing task resources;
  - CORS browser mechanics, preflight `OPTIONS`, origin whitelisting, and the distinction between CORS and authentication;
  - static frontend `fetch`, `FormData`, `parseJsonResponse`, `URLSearchParams`, and task-history pagination state.
- Expanded `tests/test_course_docs_contract.py` so the rebuilt structure is now protected for Lessons 0001-0018.
- Updated `NOTES.md` with the completed third refactor batch.

### Files touched

- `lessons/0013-background-tasks.html`
- `lessons/0014-task-status-api.html`
- `lessons/0015-uploadfile-text-files.html`
- `lessons/0016-file-summary-tasks.html`
- `lessons/0017-cors-browser-frontend.html`
- `lessons/0018-static-frontend-fetch.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

### Token budget and split decision

Estimated scope before writing: six asynchronous-workflow and browser-integration lessons, each requiring dense principle explanation, current-source binding, runtime flow, production boundary, exercises, and interview material.

Reason for split: the user requested six lessons per review batch. Lessons 0013-0018 form a coherent async/file/browser integration block. Extending into Lesson 0019 would start the service-layer refactor track and risk weakening the required depth for the browser/frontend material.

### Verification

- Ran `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- Result: 5 passed.
- Ran `.\.venv\Scripts\python.exe -m pytest -q`
- Result: 82 passed, 1 existing Starlette/FastAPI TestClient deprecation warning.
- Ran `git diff --check`
- Result: no whitespace errors; Git reported normal Windows LF-to-CRLF working-copy warnings.

### Next task

Continue the refactor with Lessons 0019-0024:

- 0019 Service layer and thin routers.
- 0020 AI client boundary.
- 0021 AI client error handling.
- 0022 through 0024: continue from the latest lesson files and current codebase state.

Keep the same nine-section high-density review structure and align every lesson with the current codebase rather than obsolete early demo code.

### Blockers

- No project blocker found.
# 2026-07-04 Run: Refactor Batch 6 Lessons 0031-0036

## Completed

- Rebuilt Lessons 0031-0036 into the required "Final Review + CSDN Deep Dive" structure.
- Covered real AI provider boundaries, async/await fundamentals, async HTTP provider adapter error mapping, FastAPI lifespan HTTP client management, app.state-to-Depends dependency bridging, and provider health endpoint design.
- Kept the lessons tied to current project code: `AIClient`, `AIClientConfig`, `async_wait`, `check_provider_health()`, `httpx.AsyncClient`, FastAPI lifespan, `get_provider_http_client()`, and `GET /provider/health`.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0036.
- Updated `NOTES.md` to record the sixth refactor batch.

## Files touched

- `lessons/0031-real-ai-provider-boundary.html`
- `lessons/0032-fastapi-async-basics.html`
- `lessons/0033-async-http-provider-adapter.html`
- `lessons/0034-lifespan-http-client.html`
- `lessons/0035-app-state-dependency-bridge.html`
- `lessons/0036-provider-health-endpoint.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0037-0042 after user review.

# 2026-07-04 Run: Refactor Batch 5 Lessons 0025-0030

## Completed

- Rebuilt Lessons 0025-0030 into the required "Final Review + CSDN Deep Dive" structure.
- Covered list response envelopes, count queries, frontend task-history rendering, frontend pagination and status filtering, OpenAPI as a machine-readable contract, and schema evolution/backward compatibility.
- Kept the lessons tied to current project code: `SummaryTaskListResponse`, `func.count()`, `historyState`, `URLSearchParams`, OpenAPI contract tests, and response-envelope compatibility tests.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0030.
- Updated `NOTES.md` to record the fifth refactor batch.

## Files touched

- `lessons/0025-list-response-envelope.html`
- `lessons/0026-count-query.html`
- `lessons/0027-frontend-task-history.html`
- `lessons/0028-frontend-pagination-status-filter.html`
- `lessons/0029-openapi-api-contract.html`
- `lessons/0030-schema-evolution-compatibility.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0031-0036 after user review.

# 2026-07-04 Run: Refactor Batch 4 Lessons 0019-0024

## Completed

- Rebuilt Lessons 0019-0024 into the required "Final Review + CSDN Deep Dive" structure.
- Covered the mandatory nine sections for each lesson: knowledge framework, underlying principles, line-by-line code reading, runtime flow, confusing-point comparisons, common errors, production-vs-teaching differences, memory exercises, and interview questions.
- Updated `tests/test_course_docs_contract.py` so the documentation contract now protects Lessons 0001-0024.
- Updated `NOTES.md` to record the fourth refactor batch.

## Files touched

- `lessons/0019-service-layer-thin-routers.html`
- `lessons/0020-ai-client-dependency.html`
- `lessons/0021-ai-client-errors.html`
- `lessons/0022-task-failure-status.html`
- `lessons/0023-task-list-pagination.html`
- `lessons/0024-task-status-filter.html`
- `tests/test_course_docs_contract.py`
- `NOTES.md`
- `COURSE_PROGRESS.md`

## Next task

Continue the same refactor standard with Lessons 0025-0030 after user review.
