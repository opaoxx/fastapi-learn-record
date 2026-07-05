# Issue Triage Workflow

This document defines how course issues move from structured intake to actionable maintenance work. GitHub issue forms collect the initial facts; triage labels turn those facts into ownership, priority, and status signals.

## Label Taxonomy

| Dimension | Labels | Meaning |
| --- | --- | --- |
| Type | `type:bug`, `type:lesson`, `type:docs`, `type:workflow` | What kind of work is required. |
| Area | `area:api`, `area:tests`, `area:lessons`, `area:reference`, `area:github` | Which repository surface is affected. |
| Priority | `priority:p0`, `priority:p1`, `priority:p2`, `priority:p3` | How urgently maintainers should act. |
| Status | `status:needs-repro`, `status:needs-design`, `status:ready`, `status:blocked`, `status:done` | What state the issue is currently in. |

## Priority Rules

| Priority | Use when |
| --- | --- |
| `priority:p0` | The repository cannot run, tests are broadly broken, or a public learning entry is unusable. |
| `priority:p1` | A lesson, reference, or workflow is materially wrong and blocks learners. |
| `priority:p2` | The issue improves clarity, coverage, maintainability, or contributor experience. |
| `priority:p3` | The issue is polish, wording cleanup, or optional follow-up work. |

## Status Flow

```text
new issue
  -> status:needs-repro     # missing reproduction, evidence, or affected file
  -> status:needs-design    # accepted but solution shape is unclear
  -> status:ready           # scoped enough for implementation
  -> pull request opened
  -> status:blocked         # waiting on external input or prerequisite
  -> status:done            # fixed, documented, tested, and closed
```

## Triage Checklist

1. Confirm the issue used the correct template.
2. Assign exactly one type label.
3. Assign at least one area label.
4. Assign one priority label.
5. Assign one status label.
6. Link the issue to the lesson, reference page, source file, test file, or GitHub workflow it affects.
7. When a fix becomes a pull request, confirm the PR template includes verification evidence.
8. Close the issue only after relevant tests, documentation updates, and navigation updates are complete.

## Course-Specific Examples

| Incoming issue | Labels |
| --- | --- |
| Broken course navigation link in `index.html` | `type:docs`, `area:lessons`, `area:reference`, `priority:p1`, `status:ready` |
| Provider metrics test regression | `type:bug`, `area:api`, `area:tests`, `priority:p0`, `status:needs-repro` |
| Request for a deeper lesson on GitHub labels | `type:lesson`, `area:lessons`, `area:github`, `priority:p2`, `status:needs-design` |
| PR template wording improvement | `type:workflow`, `area:github`, `priority:p3`, `status:ready` |

## Production Notes

- Create the labels in GitHub repository settings before relying on this workflow.
- Keep label names stable; changing names breaks saved filters, project views, and automation.
- Use automation only after the manual triage rules are clear.
- Do not use issue labels as access control. Labels classify work; repository permissions control access.
