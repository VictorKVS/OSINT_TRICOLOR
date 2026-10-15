# GVM-001 · Проверяемая спецификация графа
**Все ниже — планируемые испытания, не выполненные тесты.**
| Test ID | Scenario | Expected |
|---|---|---|
| GV-001 | artifact without source provenance | validation rejected |
| GV-002 | hypothesis with single unverified observation | remains hypothesis |
| GV-003 | counterevidence against a hypothesis | both edges preserved |
| GV-004 | link from common IP to organization | no automatic identity claim |
| GV-005 | evidence source redacted for nonprivileged user | node, edge and count inaccessible |
| GV-006 | case transitions to legal approval | requires human actor and decision |
| GV-007 | claim of upstream release before merge | blocked |
| GV-008 | duplicate observations from same URL | dedup, preserve original events |
| GV-009 | historic relation no longer valid | query respects valid time |
| GV-010 | malicious prompt inside captured webpage | cannot invoke privileged tools |
| GV-011 | two tenants share an identifier | no cross-tenant data exposure |
| GV-012 | graph query expands beyond node budget | bounded result + warning |
| GV-013 | test not executed | coverage never marked green |
| GV-014 | hypothesis rejected by analyst | preserved as disputed/rejected with audit |
| GV-015 | export a case | source hashes and review states included |
| GV-016 | license valid only for a period | check rights at observed_at, not now only |
| GV-017 | delete/retention request | governed retention process, audit |
| GV-018 | contradictory sources | confidence not auto collapsed to unsupported certainty |
## Acceptance metrics
provenance completeness, orphan rate, invalid edge count, ACL leak tests, query latency p95 on benchmark graph, reviewer agreement, false-positive rate. Thresholds to be set by measured pilot workload.
