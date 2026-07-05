# Changelog

All notable changes to this course repository are recorded here.

This project uses the changelog as a local release ledger. GitHub Release Notes summarize a published tag; this file accumulates reviewable changes before and after the release is created.

## Unreleased

Use this section for work that has landed in the repository but has not yet been included in a GitHub Release.

### Added

- Add new lesson HTML pages, quick references, GitHub workflow documents, and learning records.
- Add `CONTRIBUTING.md` as the contributor-facing workflow for issue, discussion, branch, pull request, verification, review, changelog, and release readiness.
- Add `CODE_OF_CONDUCT.md` as the collaboration safety layer for beginner-safe discussion, reporting, maintainer response, review norms, and public data-safety boundaries.
- Add `SECURITY.md` as the private vulnerability reporting workflow for supported scope, non-security reports, maintainer triage, fix disclosure, and required verification.
- Add `LICENSE` with MIT License terms for repository reuse, modification, distribution, sublicensing, notice preservation, and disclaimer boundaries.
- Add `.env.example` local configuration hygiene notes for safe teaching defaults, ignored `.env` files, and secret-free GitHub onboarding.
- Add `.github/PAGES.md` to document offline HTML reading, GitHub file-view limitations, GitHub Pages source settings, required static assets, and pre-publish checks.
- Add `.github/FINAL_AUDIT.md` as the final quality gate for lesson coverage, navigation integrity, source/test integrity, governance documents, no-secret checks, required verification, and release decisions.
- Add `.github/LINK_AUDIT.md` to document local HTML link scope, navigation patterns, path rules, test contract, manual review, and production link-audit differences.
- Add `.github/RELEASE_CANDIDATE.md` to document release-candidate entry criteria, freeze rules, verification evidence, documentation evidence, tag readiness, Pages readiness, and exit criteria.
- Add `.github/COURSE_COMPLETION.md` to document the final 96-lesson completion meaning, run order, verification evidence, documentation sweep, announcement draft, blockers, and post-completion governance.

### Changed

- Record lesson rewrites, navigation updates, README route changes, and workflow documentation updates.

### Fixed

- Record broken links, incorrect explanations, missing tests, and course contract regressions.

### Tests

- Record documentation contract, provider HTTP, full pytest, and whitespace-check changes.

### Governance

- Record changes to `.github/`, issue templates, pull request templates, CODEOWNERS, project board rules, discussions, release process, and contribution policy.
- Document contribution rules for lesson structure, PR evidence, CODEOWNERS review, branch protection, changelog updates, and safe public collaboration.
- Document expected behavior, unacceptable behavior, reporting, maintainer response, teaching review norms, and the relationship between conduct, contribution, discussion, issue, and release workflows.
- Document security disclosure boundaries that keep exploit details, secrets, private logs, personal data, customer data, and working attack steps out of public repository channels.
- Document license reuse boundaries so learners and contributors understand public visibility, open-source permission, notice retention, and no-warranty terms.
- Document environment configuration boundaries so learners can copy `.env.example` to `.env` without committing real secrets or production provider settings.
- Document static course publication boundaries so learners know when to use local `index.html`, GitHub Pages, or FastAPI `/app/`.
- Document repository final-audit boundaries so the 96-lesson course can be checked consistently before a tag, GitHub Release, or Pages promotion.
- Document static link and navigation boundaries so internal course links remain testable, offline-friendly, and GitHub Pages compatible.
- Document release-candidate boundaries so course batches are frozen, verified, and evidence-backed before annotated tags and GitHub Release Notes are created.
- Document the completed 96-lesson baseline so future corrections and expansions can be handled as transparent follow-up releases.

## Entry Rules

1. Write changelog entries for learner-visible changes, course structure changes, source behavior changes, test contract changes, and GitHub workflow changes.
2. Do not record every tiny typo unless it changes meaning, navigation, or public contract behavior.
3. Keep entries short enough to scan, but specific enough to find the related files.
4. Move relevant `Unreleased` entries into a release heading when a tag is published.
5. Never use the changelog as a substitute for `COURSE_PROGRESS.md`; progress records preserve run-by-run execution evidence.

## Release Heading Format

Use this heading when publishing a course batch:

```markdown
## course-vYYYY.MM.DD-N - YYYY-MM-DD
```

Example:

```markdown
## course-v2026.07.05-1 - 2026-07-05
```

## Changelog vs Release Notes vs Course Progress

| Document | Scope | Audience | Update Time |
| --- | --- | --- | --- |
| `CHANGELOG.md` | Curated repository changes | Learners and contributors | During normal maintenance |
| GitHub Release Notes | Published tag summary | GitHub readers and downstream users | When creating a release |
| `COURSE_PROGRESS.md` | Detailed work session evidence | Maintainers and future agents | After each course-production run |

## Production Notes

Large production repositories often generate changelogs from conventional commits, pull request labels, release automation, or issue tracker metadata.

This teaching repository keeps `CHANGELOG.md` manual so learners can inspect how maintainers decide which changes are public, which changes are internal progress, and which changes belong in release notes.
