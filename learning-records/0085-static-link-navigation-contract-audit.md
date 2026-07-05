# Learning Record 0085 - Static Link Navigation Contract Audit

## Lesson

- Lesson 0094: Static Link Navigation Contract Audit

## What Changed

- Added `.github/LINK_AUDIT.md` to document static HTML link scope, required navigation pattern, path rules, test contract, and manual review checklist.
- Added a full standalone lesson explaining repository-local link parsing, relative path resolution, exclusions, failure modes, and production documentation-site differences.
- Added a quick reference page for static link and navigation audit.
- Extended documentation contract tests so local HTML links in `index.html`, `lessons/`, and `reference/` resolve to files inside the repository.

## Key Learning

- Static HTML navigation is a public API for learners.
- Internal links can be tested deterministically without network access.
- External link checking should be separated from repository-local file existence checks.

## Verification Focus

- Documentation contract catches missing lesson/reference files and broken local links.
- `.github/LINK_AUDIT.md` remains discoverable from README, DEVELOPMENT, CHANGELOG, and final audit documents.
