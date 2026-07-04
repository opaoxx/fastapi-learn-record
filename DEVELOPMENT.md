# Development Workflow

This repository is both a runnable FastAPI project and a course archive. Treat code, tests, lessons, references, and README links as one learning product.

## Before You Change Code

1. Read the related lesson and quick reference in `lessons/` and `reference/`.
2. Check the matching tests under `tests/`.
3. Keep the change small enough to verify with targeted tests.

## Code Change Checklist

- Update the implementation in `first_api/`.
- Add or update tests in `tests/`.
- Run the targeted test file first.
- Run the full test suite before considering the change complete.

Common commands:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_provider_http.py -q
.\.venv\Scripts\python.exe -m pytest tests\test_course_docs_contract.py -q
.\.venv\Scripts\python.exe -m pytest -q
git diff --check
```

## Lesson Change Checklist

Every new lesson should include:

- a complete HTML lesson in `lessons/`;
- a quick reference page in `reference/`;
- an entry in `index.html`;
- a learning record in `learning-records/`;
- an update to `NOTES.md`;
- an update to `COURSE_PROGRESS.md`;
- documentation contract coverage when the lesson becomes part of the protected course path.

Lessons must keep the fixed review structure:

1. `① 本节核心知识框架`
2. `② 核心概念底层原理`
3. `③ 全套代码逐行精读解析`
4. `④ 核心机制运行全流程拆解`
5. `⑤ 重难点、易混淆点对比辨析`
6. `⑥ 开发常见报错+坑点+解决方案`
7. `⑦ 生产环境 vs 教学环境 核心差异`
8. `⑧ 课后记忆习题+标准答案`
9. `⑨ 面试高频真题+解析`

## Documentation Change Checklist

When changing README or course navigation:

- keep `README.md` linked to `index.html`;
- keep `README.md` linked to `first_api/README.md`;
- keep provider metrics links discoverable from `README.md`;
- update `tests/test_course_docs_contract.py` when a new document becomes a public entry point;
- run the documentation contract tests.

## GitHub Release Readiness

Before publishing course updates:

1. Confirm `README.md` gives a clear learning route.
2. Confirm `index.html` lists the new lesson and quick reference.
3. Confirm provider metrics docs link to the latest runbook training package when relevant.
4. Run targeted tests, documentation contract tests, full tests, and `git diff --check`.

This project currently treats Windows LF-to-CRLF notices from Git as non-blocking warnings. Whitespace errors from `git diff --check` are blocking.
