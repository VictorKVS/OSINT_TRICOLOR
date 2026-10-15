# GDB-003 — Proposed Graph API contract (design only)
**Not a deployed endpoint or finalized OpenAPI.**

## Endpoints (proposal)
- GET /v1/graph/nodes/{id} — node metadata subject to ABAC/RBAC
- POST /v1/graph/query — typed seed IDs, hop_limit 1..3, max_nodes ≤500, filters, time_window; server-enforced policy
- GET /v1/cases/{id}/graph — graph projection of authorized case
- POST /v1/graph/assertions — append a proposed claim with evidence and actor context (not directly verified)
- POST /v1/graph/reviews/{id}/decisions — human-only approval or rejection
- GET /v1/graph/versions/{id} — authorized history
- GET /v1/graph/exports/{id} — permission-filtered export with provenance manifest

## Response envelope
request_id, snapshot_version, data:{nodes, edges}, pagination:{cursor,has_more}, warnings, evidence_coverage.
Avoid leaking hidden records via aggregate counts, error text or timing; never return raw restricted EvidenceVault URLs.

## Semantics
Node ID and type must be registered; edge must obey source/relation/target schema. All timestamps ISO8601 UTC with original observation time separately. Query depth bounded; no user arbitrary Cypher/SQL. Unknown or unavailable provenance cannot be silently upgraded. Writes append versioned assertions with idempotency keys. Actions require authenticated roles and audit.

## Failure codes
400 malformed; 401 unauthenticated; 403 unauthorized; 404 absent/inaccessible (avoid enumeration); 409 version conflict; 413 traversal budget exceeded; 422 invalid relationship; 429 quota; 503 dependency unavailable.
## Contracts and consumers
SecGraph adapter, ALINA retrieval-only read, FATHER Visual Graph Designer. Compatibility and test fixtures required before any upstream integration.
