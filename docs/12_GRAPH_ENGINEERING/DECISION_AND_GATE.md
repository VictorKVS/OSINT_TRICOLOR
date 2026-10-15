# GDB-005 — Decision and acceptance gate
**Candidate ADR, no approval yet.**
Preferred *initial baseline for measurement*: PostgreSQL with typed graph projection, keeping immutable evidence storage separated. Alternative Neo4j/hybrid remains open.
### Required approvals
- [ ] Business case and concrete graph queries verified
- [ ] Actual authorized synthetic or approved pilot dataset and representative cardinalities
- [ ] Full source/evidence rights and privacy analysis
- [ ] Node/edge semantics and temporal model approved
- [ ] p95/p99 benchmark and high-degree traversal test
- [ ] Query ACL/tenant and prompt injection negative tests
- [ ] CI/SAST/SCA and security review evidence
- [ ] TCO against at least two alternatives
- [ ] FATHER Site, Agent Zoo, Model Zoo E2E confirmed
- [ ] Explicit G7 decision with date and accountable signoff
### Stop rule
If any high-risk unresolved blocker or no confirmed E2E prerequisites, status **HOLD**, keep documentation and research only. No implementation or deployment.
