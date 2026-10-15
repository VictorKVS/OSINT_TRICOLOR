# FATHER Visual Graph Designer — проектная спецификация v0.1
Дата: 2026-10-15. Статус: DRAFT, не утверждено к реализации.
## Цель
Интерактивное исследование графа сущностей, происхождения фактов, требований, угроз, кейсов и тестов. Общий движок FATHER, отраслевой профиль OSINT_TRICOLOR как настройка.
## Режимы представления
1. Architecture: Platform→Modules→Agents→Tools→Models.
2. Investigation: Source→Artifact→Finding→Case→Review→Decision.
3. Rights: RightsObject→License→Finding→LegalReference.
4. Security: Threat→Control→Requirement→Test→Result.
5. Delivery: Research→Requirement→ADR→Change→PR→Release.
6. Upstream: TRICOLOR Change→Generalization→Core PR→Core Release.
## UX-контракт
- Canvas pan/zoom, focus node, neighborhood by 1–3 hops, search and filters, minimap.
- Node cards: тип, название, статус, confidence, source, checked-at, owner, tags.
- Edge cards: тип, направление, provenance, evidence, validity interval, reviewed status.
- Side panel: история, документы, источники, связанные проверки и согласования.
- Изолированный режим просмотра для пользователей без прав редактирования.
- Edit только для RBAC-ролей, обязательные validation, diff, audit, undo version (not destructive history).
- Против визуального шума: кластеризация, progressive reveal, группировка, лимиты количества узлов, скрытие неподтверждённых связей настройкой.
## Запрет ложной атрибуции
Сходство доменов, аккаунтов, адресов и сетевых артефактов не приравнивается к единому владельцу. Рёбра hypothesis vs verified визуально отличны; модель не может повышать confidence без evidence.
## Контракты
GraphNode: id, type, label, status, confidence, source_refs[], sensitivity, created_at, updated_at, version.
GraphEdge: id, from_id, to_id, relation, status, confidence, evidence_refs[], valid_from, valid_to, reviewer.
GraphQuery: seed IDs, hop_limit, filter, time_range, permission_context, max_nodes.
GraphView: layout, selected IDs, collapsed clusters, overlays, snapshot version.
## Нефункциональные требования
Ролевой доступ на каждый узел и документ; серверная фильтрация чувствительных рёбер; пагинация; ограничение тяжёлых запросов; отсутствие загрузки произвольных URL браузером; события аудита без PII; graceful degradation.
## Гейты
UX mock → usability review → threat/privacy review → graph API contract → controlled integration with SecGraph → perf benchmark → approval. Для режима редактирования отдельный Security Gate.
## Зависимости
FATHER site и Agent/Model Zoo сначала должны получить реальное end-to-end подтверждение. Данный документ НЕ разрешает начало реализации.
