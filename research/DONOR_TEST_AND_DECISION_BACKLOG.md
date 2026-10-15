# Donor validation backlog and decision gates
All tasks PLANNED; no donor installed, no PoC executed.
| ID | Priority | Task | Evidence | Acceptance |
|---|---|---|---|---|
| DB-01 | P0 | Run current Telegram TDLib integration on permitted test channel | logs, metrics, test run, commit | known baseline |
| DB-02 | P0 | Assert collector transport boundary and source permissions | contract + negative tests | no bypass |
| DB-03 | P0 | Repost and edited message regression corpus | synthetic events, expected edges | provenance preserved |
| DB-04 | P0 | Watcher with checkpoints and idempotent alert schema | mock replay | no repeated alerts |
| DB-05 | P1 | Book parser comparison internal vs Docling vs Tika | accuracy and CPU/RAM | select only measured improvement |
| DB-06 | P1 | Graph link extraction vs Docling Graph | expert labeled graph pairs | measurable precision |
| DB-07 | P1 | React Flow interoperability in shared FATHER website | design token and edge contract review | no separate OSINT canvas |
| DB-08 | P1 | Sigma.js graph visualization benchmark | synthetic graph graphs | latency/ACL acceptable |
| DB-09 | P2 | CTI schema and interoperability evaluation | synthetic STIX/MISP events | reversible adapter |
| DB-10 | P0 | Donor license/SCA/security and maintenance audit | versioned security dossier | legal + security approval |
## Blockers
FATHER website and Agent/Model Zoo E2E not yet evidenced. OSINT_TRICOLOR implementation HOLD; do not change live collector or dependencies until approvals.
## Prioritized next design artifact
Event schema for watcher (new/edit/deleted/reposted/cited), diff snapshots, alert subscriptions, propagation edges (verified forwarding vs link vs text similarity), reviewer evidence and safe graph ACL.
