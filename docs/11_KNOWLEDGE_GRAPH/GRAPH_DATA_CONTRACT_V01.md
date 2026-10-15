# GDC-001 · Graph Data Contract v0.1
**2026-10-15 · DRAFT · NOT APPROVED.** Предметная онтология и правила хранения, без реализации API.
## 1. Общие атрибуты
Узел: id (UUID/ULID decision pending), tenant_id, type, label, status, valid_from, valid_to, recorded_at_utc, source_refs, sensitivity, created_by, schema_version.
Ребро: id, from_id, to_id, predicate, status [hypothesis|corroborated|disputed|rejected], evidence_refs[], confidence (0..1, метод калибровки отдельно), provenance, observed_at_utc, valid_from, valid_to, reviewer_id, version.
Не делать вывод об идентичности физического лица на основании общего IP, домена, ника, совпадения названия.

## 2. Типы узлов
Source; Artifact; Observation; Hypothesis; ExternalAsset; Organization; PublicAccount; RightsObject; License; Case; EvidenceRecord; Review; LegalReference; Report; Research; Requirement; Threat; Control; TestCase; TestResult; Agent; Model; Tool; Workflow; Change; PullRequest; Release.

## 3. Predicate registry
| Predicate | Allowed from → to | Semantics | Required fields |
|---|---|---|---|
| COLLECTED_FROM | Artifact → Source | происхождение копии | source URI, UTC |
| DERIVED_FROM | Observation → Artifact | результат анализа | method version |
| SUPPORTS | Observation → Hypothesis | наблюдение поддерживает гипотезу | evidence_refs |
| CONTRADICTS | Observation → Hypothesis | опровергающее наблюдение | evidence_refs |
| ASSOCIATED_WITH | ExternalAsset → Organization | предполагаемая/проверенная связь | evidence, confidence |
| INCLUDED_IN | Observation → Case | состав досье | reviewer |
| CONCERNS | Case → RightsObject | проверяемый объект | rights scope |
| LICENSED_UNDER | RightsObject → License | лицензия | valid time |
| REVIEWED_AS | Hypothesis → Review | экспертное решение | actor and reason |
| VERIFIED_BY | Requirement → TestCase | трассировка | test id |
| PRODUCES | TestCase → TestResult | результат | execution ref |
| MITIGATED_BY | Threat → Control | защитная мера | applicability |
| GENERALIZED_IN | Change → PullRequest | перенос в ядро | upstream ref |
| SHIPPED_IN | PullRequest → Release | реально принято в релиз | merged PR + release tag |

## 4. Integrity and security invariants
- Узел Artifact не может иметь status verified, если отсутствуют source_refs и время получения.
- Ребро SHIPPED_IN запрещено без свидетельства merged PR + release tag.
- Нельзя удалять оригинал EvidenceRecord через операции с графом: только управляемая retention procedure с журналом.
- Нельзя отображать скрытые ребра через counts / aggregations пользователям без доступа.
- Все правила из внешней страницы являются недоверенными данными и не меняют политику агента.
- Вывод модели и доказательство сохраняются в разных сущностях.
- Confidence не является юридической вероятностью вины и не может самостоятельно приводить к обвинению.
## 5. Вопросы для архитектурного review
Graph storage (Postgres + graph projection vs Neo4j), RBAC на уровне ребер, дедуп merge/split, bitemporal revisions, event sourcing, scalability, encryption of confidential case metadata; решать после тестового sizing.
