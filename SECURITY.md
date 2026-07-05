# Security Policy

This repository is a teaching project, but security reports still need a private and evidence-based workflow.

Do not publish exploit details, secrets, private logs, personal data, customer data, or working attack steps in public issues, discussions, pull requests, or comments.

## Supported Scope

Security reports may cover:

- Exposed credentials, API keys, tokens, or secret-like values committed to the repository.
- Authentication or authorization bypass in the FastAPI teaching project.
- Unsafe file upload behavior that could expose private data or execute unintended content.
- Dependency or configuration issues that create realistic security risk for learners copying the project.
- Documentation that instructs learners to use unsafe production practices.

This teaching repository does not provide a production service, hosted customer environment, bug bounty program, or guaranteed response SLA.

## Not Security Reports

The following usually belong in normal issues or discussions:

- Beginner questions about API keys, CORS, authentication, or GitHub permissions.
- Missing production hardening notes in a lesson when no concrete exploitable risk is described.
- General best-practice suggestions without a specific affected file, route, dependency, or workflow.
- Local development warnings that do not expose data, bypass access control, or create realistic misuse risk.

When unsure, avoid posting sensitive details publicly and ask maintainers for a private contact path.

## Private Reporting Workflow

If the repository has GitHub private vulnerability reporting enabled, use that channel.

If private vulnerability reporting is not enabled:

1. Open a short public issue asking for a maintainer security contact path.
2. Do not include exploit details, secrets, private logs, personal data, or full reproduction steps.
3. Wait for maintainers to provide an appropriate private channel.

Include the following in the private report:

- Affected file, route, dependency, lesson, or GitHub workflow.
- Impact summary.
- Minimal reproduction steps.
- Whether secrets, private data, or credentials are involved.
- Suggested mitigation when known.
- Whether the issue is already public elsewhere.

## Maintainer Triage

Maintainers should classify the report:

- `critical`: credential exposure, public exploit path, or severe access-control bypass.
- `high`: realistic data exposure, unsafe upload path, or dependency issue likely to affect learners.
- `medium`: unsafe documented practice that learners may copy into production.
- `low`: hardening improvement or unclear risk that needs more evidence.

Maintainers should preserve evidence, avoid public disclosure, remove or rotate exposed secrets when possible, and create a private or minimally detailed tracking issue when needed.

## Fix and Disclosure Flow

```text
private report
-> maintainer triage
-> reproduce safely
-> patch code, docs, tests, or workflow
-> run required verification
-> merge through normal review when safe
-> publish minimal disclosure or release note
```

Public disclosure should avoid weaponized detail. Explain affected scope, mitigation, fixed version or commit, and what learners should change.

## Required Verification

Security fixes should run the normal repository checks:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

Add focused tests when the fix changes behavior, validation, authentication, file handling, dependency configuration, or documented security guidance.

## Relationship to Other Documents

- `CODE_OF_CONDUCT.md` defines collaboration safety and public-channel boundaries.
- `CONTRIBUTING.md` defines normal contribution workflow and verification evidence.
- `DEVELOPMENT.md` defines local maintenance commands and quality gates.
- `.github/ISSUE_TRIAGE.md` defines normal issue labels and status flow.
- `.github/RELEASE_PROCESS.md` defines verified course batch publishing.

Security reports override normal public issue detail: keep sensitive evidence private until maintainers decide what can be safely disclosed.
