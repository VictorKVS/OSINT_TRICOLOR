# GDB-004 — Security engineering and privacy design
**Draft security review model: not actual deployed controls.**
## Assets
Claims, provenance, original evidence, reporter identity, personal data (if any), agent tool permissions, service tokens, graph topology, case status, legal review decisions.
## Trust boundaries
Internet/public sources → restricted collectors → validation/normalization → protected graph query API → sensitive evidence store → reviewer UI. Separate read-only RAG from administrative graph mutation.
## Threats → controls → verification
| Risk | Control | Proposed test |
|---|---|---|
| data poisoning / false edge | immutable original, provenance, human verification | conflicting synthetic assertions |
| prompt injection via webpages | tool permission boundaries + treat source as data | malicious synthetic source ignored |
| graph authorization bypass | server-side edge/node ACL and case isolation | cross-tenant negative tests |
| graph traversal DoS | limits on depth, result count, complexity, timeout | cyclic/high-degree fixture |
| SSRF through source URLs | restricted resolver/network egress and allowlist | local/private IP rejection tests |
| personal data leakage | purpose limitation, redaction, retention, scoped exports | role-based export tests |
| evidence tampering | hash, append-only audit, controlled originals | hash mismatch and access audit |
| correlation misattribution | confidence, contrary evidence, human review | common-IP false-attribution case |
| supply chain compromise | pinned deps, SCA/SBOM, signature verification | dependency/unsigned build gate |
| bulk case export | quota, logged approvals, split duties | privileged action trail |
## Russian compliance research backlog
152-FZ/149-FZ/187-FZ/FSTEK/FSB as relevant only after classification; do not assert a GIS/KII/ISPDN status or prescribe certification before legal scope determination.
## Review evidence
Threat model owner, data flow diagram, privacy decision, validated least-privilege matrix, retention/hold, secrets lifecycle, incident and restore playbooks. No direct CI job gets actual case evidence.
