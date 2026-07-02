# Notes

- The learner uses PyCharm and commits lesson progress to GitHub.
- Keep lessons beginner-friendly but tied to backend APIs first, then AI service endpoints and interview-ready projects.
- The learner prefers richer lessons in a classroom / CSDN-blog style: first explain new concepts and underlying principles, then connect them to code and exercises.
- Future lessons should include background, terminology, mechanism, line-by-line code reading, experiments, common errors, and a short quiz.
- Every lesson and reference page should include top and bottom navigation so readers can return to the course index and move between related pages.
- The learner wants future course updates in two-lesson batches when feasible, while keeping each lesson readable for complete beginners.
- The codebase has now moved from a single-file FastAPI app to a multi-file structure using APIRouter and dependency classes.
- The items endpoints now use SQLite and SQLModel instead of the earlier in-memory dictionary. Keep explaining persistence, sessions, commit, and refresh slowly.
- The items API now has full CRUD plus pytest coverage for create/update/delete and invalid update validation.
- The app now has Settings from pydantic-settings and protects item write endpoints with X-API-Key. Any future POST/PATCH/DELETE examples need the header unless a lesson intentionally demonstrates 401.
