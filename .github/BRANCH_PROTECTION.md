# Branch Protection Required Checks

This repository uses GitHub Actions as a course quality gate. Configure branch protection for `main` so pull requests cannot be merged until the CI job passes.

## Required Main Branch Rules

1. Require a pull request before merging.
2. Require status checks to pass before merging.
3. Require branches to be up to date before merging.
4. Require conversation resolution before merging.
5. Block force pushes.
6. Block branch deletion.

## Required Status Check

Use this required status check name:

```text
pytest and documentation contracts
```

This check is produced by `.github/workflows/ci.yml` and protects:

- provider HTTP behavior tests;
- course documentation contract tests;
- the full pytest suite;
- committed diff whitespace checks.

## Why This Matters

`DEVELOPMENT.md` tells contributors what to run locally. `.github/workflows/ci.yml` runs those checks automatically. Branch protection makes the CI result merge-blocking, so course pages, reference pages, README links, and FastAPI behavior cannot be merged while the repository is failing its required quality gate.
