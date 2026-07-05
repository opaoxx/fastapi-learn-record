# Learning Record 0082 - Env Example Local Config Hygiene

Lesson 0091 strengthened local configuration hygiene for GitHub learners.

Key artifacts:

- `.env.example`
- `.gitignore`
- `lessons/0091-env-example-local-config-hygiene.html`
- `reference/0091-env-example-local-config-hygiene-cheatsheet.html`

Core learning:

- `.env.example` is a committed schema and safe sample file.
- `.env` is local private state and must stay ignored by Git.
- `SettingsConfigDict(env_file=".env", env_prefix="FIRST_API_")` binds local overrides into typed settings.
- Teaching defaults are not production secrets.
