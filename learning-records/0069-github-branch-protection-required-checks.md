# Learning Record 0069 - GitHub Branch Protection Required Checks

## What changed

- Added `.github/BRANCH_PROTECTION.md` to document the main branch protection policy.
- The documented required status check is `pytest and documentation contracts`.
- Added Lesson 0078 and Reference 0078 to explain branch protection, required checks, up-to-date branches, force-push blocking, and production governance differences.

## Why it matters

GitHub Actions can report failures, but branch protection turns those failures into merge-blocking rules. The course repository now documents how to keep `main` from accepting broken tests, broken documentation contracts, or unsafe direct writes.

## Verification focus

- `.github/BRANCH_PROTECTION.md`
- `.github/workflows/ci.yml`
- `tests/test_course_docs_contract.py`
- `lessons/0078-github-branch-protection-required-checks.html`
- `reference/0078-github-branch-protection-required-checks-cheatsheet.html`
