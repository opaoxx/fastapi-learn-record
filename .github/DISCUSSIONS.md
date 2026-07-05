# GitHub Discussions Workflow

This document defines how the course repository should use GitHub Discussions for learner questions, long-form explanations, and community knowledge sharing. Discussions are remote GitHub configuration; this file records the categories and operating rules maintainers should reproduce.

## Purpose

Issues track actionable maintenance work. Discussions host exploratory questions, study notes, implementation ideas, and longer learner support that should not immediately become repository work.

## Recommended Categories

| Category | Use for | Convert to issue when |
| --- | --- | --- |
| Q&A | Learner questions about lessons, code, errors, or concepts. | The answer reveals a reproducible bug, missing lesson section, or broken documentation. |
| Study Notes | Learner summaries, review notes, and solved practice records. | A note identifies a concrete correction or reusable course improvement. |
| Ideas | Proposed course topics, workflow improvements, or learning route suggestions. | The idea has scoped acceptance criteria and maintainer agreement. |
| Show and Tell | Learner projects, adaptations, and implementation demos. | A shared project exposes a course defect or missing production guidance. |
| Announcements | Maintainer updates about new lessons, release checks, or repository workflow changes. | Usually never; announcements should link issues or PRs instead. |

## Issue vs Discussion Decision Rules

| Choose issue when | Choose discussion when |
| --- | --- |
| The work is reproducible, scoped, and should change repository files. | The topic is exploratory, open-ended, or primarily educational. |
| A failing test, broken link, wrong code path, or missing required section exists. | A learner asks why something works, how to study it, or how to extend it. |
| Maintainers can define done. | Maintainers need conversation before defining done. |

## Answer Quality Checklist

1. Link the relevant lesson, reference page, source file, or test file.
2. Explain the principle before giving a shortcut answer.
3. Distinguish teaching demo behavior from production behavior.
4. If the discussion reveals repository work, open or link an issue.
5. Mark a Q&A answer only after it directly resolves the learner's question.
6. Keep announcements tied to concrete course changes, tests, or release notes.

## Conversion Flow

```text
discussion question
  -> answer with lesson/source/test links
  -> identify whether repository work exists
  -> if yes:
       open issue with template
       copy reproduction, learning gap, or documentation evidence
       link discussion and issue both ways
  -> triage labels
  -> project board
  -> pull request
```

## Production Notes

- Enable GitHub Discussions in repository settings before relying on this workflow.
- Discussions are not a private support channel; avoid secrets, credentials, private logs, and personal data.
- Mature repositories often add moderation rules, pinned posts, accepted-answer policy, and category-specific templates.
- Do not use Discussions to bypass branch protection, CI, code review, or issue triage.
