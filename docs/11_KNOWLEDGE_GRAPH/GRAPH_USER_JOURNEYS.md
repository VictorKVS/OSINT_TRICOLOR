# Graph User Journeys / Acceptance v0.1
Статус: DRAFT. Все данные в примерах синтетические.

## UJ-01 Аналитик расследует сигнал
Search synthetic.example → show source and artifact → finding hypothesis → rights/licensing context → case → human review; every conclusion links to evidence and time.
**Accept:** viewer sees verified/hypothesis contrast, can trace source, cannot issue external action.

## UJ-02 ИБ-архитектор проверяет защиту
Choose Threat → MITRE/CWE mapping → Control → Requirement → TestCase → TestResult → open unresolved gap.
**Accept:** no false green state when test not run.

## UJ-03 Инженер просматривает агента
Agent → Model → Tool → Workflow → RBAC grant → policy → eval run.
**Accept:** tool invocation available only with scoped capability and audit.

## UJ-04 Руководитель оценивает проект
Research → Business need → ADR → Estimate → Gate → Implementation readiness.
**Accept:** blocked gate displayed as blocked, not approved.

## UJ-05 Upstream перенос
Profile change → classification CORE/PROFILE → generalized contract → tests → OSINT_deepseek PR → merged release → downstream upgrade.
**Accept:** proposal not marked promoted before successful merge.

## QA matrix
Functional navigation, authz on nodes/edges/export, PII masking, filter correctness, graph density/performance, keyboard access, layout consistency, provenance and audit, negative/synthetic case replay.
