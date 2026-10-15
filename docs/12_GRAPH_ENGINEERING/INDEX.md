# FATHER OSINT — Graph Engineering Decision Pack v0.1
**2026-10-15 | DRAFT / NO IMPLEMENTATION APPROVAL**

Цель: обоснованный выбор хранилища графа и интеграционных контрактов, не кодирование.

1. [STORAGE_OPTIONS.md](STORAGE_OPTIONS.md): PostgreSQL, Neo4j, hybrid; trade-offs and recommendation conditions.
2. [SIZING_MODEL.md](SIZING_MODEL.md): baseline assumptions, formulas, sensitivity and measurement plan.
3. [GRAPH_API_CONTRACT.md](GRAPH_API_CONTRACT.md): proposed read/write interface, provenance, authorization, failure responses.
4. [SECURITY_AND_PRIVACY.md](SECURITY_AND_PRIVACY.md): trust boundaries, threat model, least privilege and evidentiary safeguards.
5. [DECISION_AND_GATE.md](DECISION_AND_GATE.md): ADR candidate and mandatory approval checklist.

Dependencies: research/ program, diagrams 01–11, graph data contract, security operating model. This is a FATHER shared-core candidate, not a TRICOLOR-specific fork.

Hard gate: FATHER site and Agent/Model Zoo E2E validation + G0–G7 approval. **No new production implementation now.**
