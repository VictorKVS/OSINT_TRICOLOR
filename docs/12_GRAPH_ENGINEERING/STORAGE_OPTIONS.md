# GDB-001 — storage architecture alternatives
**Status DRAFT.** Final choice requires real workload tests.

| Option | Strengths | Weaknesses | Best fit |
|---|---|---|---|
| PostgreSQL with node/edge tables + recursive SQL | consistency, mature RBAC/RLS, unified cases and transactional integrity, lower ops diversity | multi-hop complex traversals require careful indexing and limits | small/medium graphs and evidence/case records |
| Neo4j | mature property-graph traversal and visual query workflows | separate security/ops stack, integration + license/TCO verification needed | deep graph exploration where benchmarks justify it |
| Hybrid PostgreSQL system of record + derived graph engine | strong transactional provenance + deep traversals | syncing, drift, duplication and failure/reconciliation complexity | proven multi-hop demand with enough budget and ops capacity |

**Proposed initial decision:** PostgreSQL SoR + typed relations as provisional baseline, *not a final approval*. Benchmark 1, 2, 3 hops; fanout, time-filtered queries, ACL filtering, write throughput, deletion policies and recovery. Add derived graph only if measurable value justifies complexity.

Decision matrix weights to agree: correctness/provenance 25%, permission isolation 20%, query latency 15%, lifecycle/maintainability 15%, TCO 15%, tooling 10%. These are provisional weights, not measured scores.

ADR blockers: unavailable real query distribution, graph volume, licensing quotes, data residence, team expertise, p95 SLO, evidence retention.
