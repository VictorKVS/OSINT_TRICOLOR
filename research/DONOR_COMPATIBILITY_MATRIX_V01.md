# FATHER OSINT — compatibility matrix, code-inspected v0.1
Date 2026-10-16. DRAFT. This is a file-level capability mapping, not runtime security certification.
## Verified internal code evidence (main branch)
- father_osint/collectors/telegram.py: transport-neutral TelegramTransport Protocol, TelegramCollector, message schema.
- father_osint/search_planning.py: deterministic Telegram search planner, bounded collection and duplicate/repost methods in search plan.
- father_osint/reliability.py: SourceCheckpoint and JSON checkpoint storage.
- father_osint/book_corpus.py: BookSource, rights_basis, integrity hash and book lifecycle.
- father_osint/knowledge_factory.py: knowledge pipeline stages D0-D15, source classifications, validation states.
- father_osint/ui_contracts.py: GraphNodeView / GraphEdgeView, graph/table/document views, design color tokens.
- tests/: tests for Telegram collector, TDLib, restart, evidence, knowledge, book corpus and related modules are present; passing status not checked.
Links: https://github.com/VictorKVS/OSINT_deepseek/tree/main/father_osint and https://github.com/VictorKVS/OSINT_deepseek/tree/main/tests

| Workstream | Existing internal baseline | Candidate | Recommendation | Verification gap |
|---|---|---|---|---|
| Telegram collection | TelegramTransport, TDLib related tests | telegram-monitor, tg-parser, Telethon | RETAIN CORE; study watchers/filters without importing wholesale | end-to-end run, API limits, status of dependencies |
| Search planning | DeterministicTelegramSearchPlanner | donor search patterns | EXTEND INTERNAL | broad topic and backfill edge cases |
| Watchers | planner/reliability primitives | telegram-monitor concepts | DESIGN ADD-ON | alert lifecycle, change monitoring, backpressure |
| Dedup/reposts | planned in search, existing evidence pipeline | tg-parser filter patterns | BENCHMARK internal first | reliable forwarded metadata versus similarity |
| Books/document intake | BookSource and lifecycle | Docling, Tika | ISOLATED POC | parser coverage, license, memory, hostile file handling |
| Knowledge pipeline | D0-D15 stages | Docling Graph | ADAPT only validated gaps | false edge rate, source citation |
| Graph canvas | internal UI view contracts | React Flow | shared FATHER only, not duplicate in OSINT | actual FATHER design tokens and deployment |
| Graph visualization | GraphNodeView/EdgeView | Sigma.js | possible SecGraph renderer | 100k node view and access filtering |
| Threat intelligence | OSINT evidence workflows | OpenCTI / MISP / IntelOwl | study schemas and adapters | licensing, data exchange, API policy |
| Case/provenance | evidence quality and reports | CTI platforms | maintain ownership in FATHER | legal review, chain-of-custody test |

## Impact scale
L = adapter/config; M = new modular component requiring contract tests; H = major runtime replacement.
Priority: internal reuse (L/M) before donor dependency (M/H). Do not import unreviewed AGPL code, closed-source components or abandoned clients.

## Mandatory donor acceptance
Canonical license and exact commit; dependencies and SBOM; security/credential handling; synthetic benchmark; vulnerability review; privacy; interface mapping; architecture ADR; upstream-generalizable changes promoted via reviewed PR.
