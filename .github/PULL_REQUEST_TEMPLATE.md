# Pull Request Checklist

## Summary

- What changed:
- Why it changed:

## Change Type

- [ ] Code behavior
- [ ] Lesson or reference page
- [ ] README, DEVELOPMENT, or GitHub documentation
- [ ] Tests or CI

## Verification

- [ ] Ran provider HTTP tests: `.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q`
- [ ] Ran documentation contract tests: `.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q`
- [ ] Ran full test suite: `.\.venv\Scripts\python.exe -m pytest -q`
- [ ] Ran whitespace check: `git diff --check`

## Course Documentation Checklist

- [ ] Updated the lesson HTML in `lessons/` when lesson content changed.
- [ ] Updated the quick reference page in `reference/` when lesson content changed.
- [ ] Updated `index.html` navigation when adding or renaming lessons.
- [ ] Updated `NOTES.md` and `COURSE_PROGRESS.md`.
- [ ] Added or updated documentation contract tests when public links, commands, or required structures changed.

## Risk Notes

- Breaking API or schema changes:
- Documentation or navigation risks:
- Follow-up work:
