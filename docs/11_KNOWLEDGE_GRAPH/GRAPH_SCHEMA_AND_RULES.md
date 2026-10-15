# Graph Schema · типизированные связи v0.1
Статус: DRAFT, семантические правила на утверждение.

## Сущности
Project, Component, Agent, Model, Tool, Workflow, Research, Requirement, Threat, Control, TestCase, TestResult, Source, Artifact, Finding, Case, RightsObject, License, PersonOrOrganization, Review, Decision, Change, PullRequest, Release.

## Формальная матрица отношений
| Source | Relationship | Target | Rule |
|---|---|---|---|
| Project | CONTAINS | Component | parent version is recorded |
| Workflow | USES | Agent | trace runtime version |
| Agent | RUNS_MODEL | Model | record actual configuration |
| Agent | INVOKES | Tool | deny unless permissioned |
| Research | DERIVES | Requirement | reference research ID |
| Control | MITIGATES | Threat | link evidence and scope |
| Requirement | VERIFIED_BY | TestCase | test coverage links |
| TestCase | PRODUCES | TestResult | immutable result ID |
| Artifact | COLLECTED_FROM | Source | mandatory provenance |
| Finding | SUPPORTED_BY | Artifact | confidence not sufficient without source |
| Case | INCLUDES | Finding | reviewer + reason |
| Case | CONCERNS | RightsObject | may remain unverified |
| RightsObject | SUBJECT_TO | License | valid time interval |
| Case | REVIEWED_BY | Review | versioned decision |
| Change | IMPLEMENTS | Requirement | PR trace |
| PullRequest | PROMOTES_TO | Release | must be merged and tested |
| Component | DEPENDS_ON | Component | must not self-loop |
## Состояния
proposed → under_review → verified or rejected → superseded; no automated promotion to verified for legal claims.
## Quality
Orphan nodes identified; provenance completeness; duplicate edge detection; invalid relationship/type checks; stale confidence; broken evidence URL; access-leak tests. Validate cycles according to relationship type, not a blanket ban.
## Security
All graph queries enforce server-side ACL; encrypt restricted assets; no direct live public graph containing PII, secrets, or case evidence.
