# Learning Record 0047 - Provider Metrics Export Tests

## What changed

- Added focused tests for provider metrics text export edge cases.
- Protected empty snapshot rendering so it still returns HELP and TYPE lines.
- Protected special label value escaping for backslash, newline, and double quote characters.
- Added endpoint coverage for empty text export and retry failure outcome text export.
- Added Lesson 0056 and Reference 0056.
- Linked Lesson 0055, Reference 0055, and the course index to the new materials.

## Key idea

Text metrics export is a machine-readable contract. Status code alone is not enough; tests should protect the exact text shape, Content-Type, empty state, failure outcomes, and escaping rules.

## Files

- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0055-provider-metrics-export-shape.html`
- `lessons/0056-provider-metrics-export-tests.html`
- `reference/0055-provider-metrics-export-shape-cheatsheet.html`
- `reference/0056-provider-metrics-export-tests-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Lesson 0057 can explain the provider metrics snapshot boundary: callers should receive a detached data snapshot, not a mutable reference into the counter's internal state.
