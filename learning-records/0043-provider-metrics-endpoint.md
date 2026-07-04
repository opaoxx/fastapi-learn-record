# Learning Record 0043 - Provider Metrics Endpoint

## What changed

- Added a read-only teaching metrics endpoint at `GET /provider/metrics`.
- Connected provider prediction outcomes to the in-process `ProviderMetricsCounter`.
- Added response models for metric label and metric sample JSON shape.
- Added tests that prove provider prediction success increments the counter and the endpoint returns the expected snapshot.
- Added Lesson 0052 and Reference 0052, then linked them from Lesson 0051, Reference 0051, and the course index.

## Key idea

Metrics endpoint 是只读观测窗口。业务流程在 service 层记录已经发生的 provider prediction 事件，router 只读取 snapshot 并用 response model 输出稳定 JSON。当前 counter 仍然是教学用进程内实现，不代表生产级多实例 metrics 聚合。

## Files

- `first_api/services/provider_http.py`
- `first_api/schemas.py`
- `first_api/routers/predictions.py`
- `tests/test_provider_http.py`
- `tests/test_ai_client_dependency.py`
- `lessons/0052-provider-metrics-endpoint.html`
- `reference/0052-provider-metrics-endpoint-cheatsheet.html`
- `index.html`
- `NOTES.md`

## Next

Lesson 0053 can deepen Provider Metrics Failure Outcomes by adding focused tests and examples for `retry_scheduled`, `retry_exhausted`, and `fail_fast` samples in the endpoint snapshot.
