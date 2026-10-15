# FATHER OSINT_TRICOLOR — Альбом схем на согласование
Дата 2026-10-15 | версия 0.1 | **все схемы DRAFT / NOT APPROVED**.
До официального решения по Gate G7 реализация целевого комплекса запрещена; существующий offline MVP сохраняет экспериментальный статус.

## Перечень
| ID | Вид | Файл | Ответственный за согласование |
|---|---|---|---|
| SCH-01 | Business BPMN-inspired AS-IS / TO-BE | [01_BUSINESS.md](01_BUSINESS.md) | владелец процесса, аналитик |
| SCH-02 | System C4 Context / Containers | [02_C4.md](02_C4.md) | архитектор |
| SCH-03 | Data Flow / trust boundaries | [03_DATA_SECURITY.md](03_DATA_SECURITY.md) | ИБ, ПД, архитектор |
| SCH-04 | Case / Evidence lifecycle | [04_CASE_EVIDENCE.md](04_CASE_EVIDENCE.md) | OSINT, DFIR, юрист |
| SCH-05 | Agent workflow, LLM RAG guardrails | [05_AGENT_WORKFLOW.md](05_AGENT_WORKFLOW.md) | AI architect, security |
| SCH-06 | DevSecOps pipeline | [06_DEVSECOPS.md](06_DEVSECOPS.md) | DevSecOps, QA |
| SCH-07 | Deployment and operations | [07_DEPLOYMENT.md](07_DEPLOYMENT.md) | SRE, ИБ, архитектор |
| SCH-08 | Data schema and integration | [08_DATA_MODEL.md](08_DATA_MODEL.md) | Data engineer, архитектор |
| SCH-09 | Core ↔ profile upstream transfer | [09_CORE_FEEDBACK.md](09_CORE_FEEDBACK.md) | OSINT core maintainers |
| SCH-10 | Security lab | [10_SECURITY_LAB.md](10_SECURITY_LAB.md) | Security + QA |
| SCH-11 | Economic decision tree | [11_SIZING_DECISION.md](11_SIZING_DECISION.md) | product owner + finance |

## Правила чтения
Mermaid — логические схемы, не утверждённые нотации BPMN 2.0/C4/DFD. После смыслового одобрения подготовить строгие BPMN 2.0 XML, C4 и DFD L1-L2. Запрет выдавать гипотетический процесс работодателя за обследованный.

## Gate G7 — акт согласования
- [ ] G0–G4 завершены, согласован scope и legal basis
- [ ] Бизнес-процессы и RACI утверждены владельцем
- [ ] FR/NFR ↔ схема ↔ тест сопоставлены
- [ ] Threat modeling, ПД, цепочка доказательств прошли review
- [ ] Sizing и TCO обоснованы реальными параметрами
- [ ] Архитектор, ИБ, Legal и эксплуатация согласовали
- [ ] Открытые вопросы закрыты в [REVIEW_REGISTER.md](REVIEW_REGISTER.md)
- [ ] Решение **APPROVED FOR IMPLEMENTATION** записано отдельно

Только после этого планировать product backlog, спецификации компонентов и implementation sprints.
