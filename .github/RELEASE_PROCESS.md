# GitHub Release Process

This document defines how maintainers publish course batches with Git tags and GitHub Releases.

GitHub Releases are remote state. This file records the local release contract, required checks, note structure, and rollback path maintainers should reproduce before publishing.

Use `.github/RELEASE_CANDIDATE.md` before creating a tag. A release candidate collects the verification evidence, freeze rules, known warnings, and release range that make the final tag trustworthy.

## Release Purpose

Releases turn a set of lesson, reference, code, test, and workflow changes into a traceable learning checkpoint.

A release is not only a marketing announcement. It is the repository-level evidence that the course index, README, tests, and GitHub workflow documents agree at a known point in history.

## Tag Naming

Use annotated tags for course batch releases:

```text
course-vYYYY.MM.DD-N
```

Rules:

1. `course` identifies this repository as a course artifact rather than a library package.
2. `YYYY.MM.DD` records the release date in UTC or the maintainer's documented release timezone.
3. `N` is a same-day sequence number starting at `1`.
4. Reuse an existing tag only when the release was never pushed.
5. Never move a published tag silently.

Example:

```powershell
git tag -a course-v2026.07.05-1 -m "Course batch 2026.07.05-1"
git push origin course-v2026.07.05-1
```

## Release Notes Structure

Every GitHub Release should use these sections:

```markdown
## Changed Lessons

## Changed References

## Code and Workflow Changes

## Verification

## Known Warnings

## Upgrade or Reading Notes

## Rollback
```

## Verification Checklist

Run these checks before creating the tag:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Required evidence:

- `provider HTTP` checks pass.
- `docs contract` checks pass.
- `full pytest` passes.
- `git diff --check` reports no whitespace errors.
- Windows LF-to-CRLF notices are recorded as known warnings when present.

## Release Flow

```text
finish lesson batch
-> update lessons, references, README, DEVELOPMENT, NOTES, COURSE_PROGRESS, index
-> run targeted tests
-> run docs contract
-> run full pytest
-> run git diff --check
-> review git status and diff
-> create annotated tag
-> push branch and tag
-> create GitHub Release from tag
-> paste release notes with verification evidence
```

## Rollback

If a release is wrong after publication:

1. Do not move the published tag silently.
2. Create a follow-up commit that fixes the issue.
3. Publish a new patch release tag.
4. Mark the old GitHub Release as superseded in the release body.
5. If the tag was pushed by mistake and must be removed, document the reason in `COURSE_PROGRESS.md` before deleting remote state.

## Production Notes

Real production repositories usually add signed tags, changelog generators, release approvals, artifact checksums, SBOMs, dependency scans, and environment-specific deployment gates.

This teaching repository keeps the process intentionally small: release notes must prove that learning content, source code, and tests are synchronized.
