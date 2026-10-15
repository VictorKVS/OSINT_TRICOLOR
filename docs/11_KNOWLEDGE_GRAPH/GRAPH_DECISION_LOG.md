# GDL-001 · Graph decision register
**No architecture decisions approved.**
| ID | Decision | Options | Status | Gate |
|---|---|---|---|---|
| GD-001 | primary storage | PostgreSQL graph projection / Neo4j / hybrid | OPEN | G6/G7 |
| GD-002 | node ID | UUID / ULID | OPEN | G7 |
| GD-003 | temporal history | versioned rows / bitemporal / event sourcing | OPEN | G7 |
| GD-004 | authorization | per-tenant + per-node + per-edge | DRAFT target | G4/G7 |
| GD-005 | graph layout | force / hierarchical / clustered | OPEN | UX review |
| GD-006 | streaming | batch / event bus | OPEN | throughput benchmark |
| GD-007 | de-dup | deterministic + human merge | DRAFT target | QA review |
| GD-008 | relationship confidence | calibrated multi-source score | OPEN | labeled evaluation |
| GD-009 | legal retention | per case category / legal hold | OPEN | Legal review |
| GD-010 | shared core interface | FATHER OSINT versioned adapters | DRAFT target | core review |

Decision format: context, alternatives, trade-offs, measurements, security/privacy, owner, date, resulting ADR, approval. No automatic approval inferred.
