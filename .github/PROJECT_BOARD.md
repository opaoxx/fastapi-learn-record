# GitHub Projects Board Workflow

This document defines the recommended GitHub Projects board for the course repository. The board itself is configured in GitHub, while this file records the field model, views, and operating rules that maintainers should reproduce in the remote project.

## Board Purpose

The project board turns labeled issues and pull requests into a visible maintenance queue. Issue templates collect facts, issue triage labels classify work, and the project board shows current execution state.

## Required Fields

| Field | Type | Values | Purpose |
| --- | --- | --- | --- |
| Status | Single select | `Intake`, `Needs Repro`, `Needs Design`, `Ready`, `In Progress`, `In Review`, `Blocked`, `Done` | Current execution stage. |
| Priority | Single select | `P0`, `P1`, `P2`, `P3` | Work ordering signal aligned with `priority:*` labels. |
| Area | Single select | `API`, `Tests`, `Lessons`, `Reference`, `GitHub` | Primary repository surface affected. |
| Type | Single select | `Bug`, `Lesson`, `Docs`, `Workflow` | Work category aligned with `type:*` labels. |
| Lesson | Text | Lesson number or range | Course location for lesson and documentation tasks. |

## Views

| View | Grouping | Filter | Use |
| --- | --- | --- | --- |
| Triage Queue | Status | `Status != Done` | Daily or weekly maintenance intake. |
| Ready Work | Priority | `Status = Ready` | Contributor-friendly implementation queue. |
| Course Docs | Area | `Area in Lessons, Reference` | Lesson, reference, README, and navigation work. |
| GitHub Workflow | Status | `Area = GitHub` | CI, branch protection, templates, CODEOWNERS, and issue workflow work. |
| Done Review | Type | `Status = Done` | Recent completion audit before release notes or progress updates. |

## Status Mapping

| Issue label | Project status |
| --- | --- |
| `status:needs-repro` | `Needs Repro` |
| `status:needs-design` | `Needs Design` |
| `status:ready` | `Ready` |
| `status:blocked` | `Blocked` |
| `status:done` | `Done` |

## Operating Rules

1. Every accepted issue should be added to the project board.
2. The project item Status field must agree with the current `status:*` label.
3. A ready item must have one type, at least one area, one priority, and one status signal.
4. Pull requests should be linked to the issue item before review.
5. Move work to `In Review` when a pull request is open and waiting for CI or reviewer feedback.
6. Move work to `Done` only after tests, documentation, navigation, and progress records are complete.
7. Keep the board small enough to act on; close stale or duplicate work instead of stockpiling vague cards.

## Automation Boundary

Start manually. After the process is stable, optional GitHub automation may add new issues to `Intake`, move linked pull requests to `In Review`, or move merged pull requests to `Done`. Automation must preserve the field model in this document.

## Production Notes

- GitHub Projects configuration is remote state and is not created by committing this file.
- Enterprise repositories often add owner, milestone, release, severity, customer impact, and SLA fields.
- Do not treat the project board as the source of truth for code quality; CI, documentation contract tests, CODEOWNERS, and branch protection remain the merge gates.
