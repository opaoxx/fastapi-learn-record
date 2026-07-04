# Learning Record 0053 - Provider Metrics Runbook Checklist

## Date

2026-07-04

## Context

Lesson 0061 created a provider metrics documentation index. The next useful step was to convert the existing metrics endpoints and outcome taxonomy into a troubleshooting runbook so the learner can answer "what should I inspect next?" when provider metrics change.

## Learned

- A runbook is a conditional investigation checklist, not just another documentation page.
- Provider metrics should be inspected by outcome first, then by failure category, error code, and status code.
- `retry_scheduled` means a retry was planned; it does not prove the final user-visible request failed.
- `fail_fast` usually means the error should not be retried blindly.
- Important runbook pages can be protected with lightweight documentation tests that check required signals, warnings, and links.

## Project change

- Added `reference/provider-metrics-runbook.html` as a durable provider metrics troubleshooting checklist.
- Expanded `tests/test_course_docs_contract.py` to protect the runbook's required endpoints, outcomes, warning text, and links.
- Added Lesson 0062 and Reference 0062 to teach the runbook pattern.

## Retrieval prompt

If `retry_scheduled` samples increase, what two other signals should you check before calling it a final provider outage?

## Next step

Continue with Lesson 0063: Provider Metrics Scenario Fixtures, focused on creating predictable sample scenarios that make the runbook easier to practice and verify.
