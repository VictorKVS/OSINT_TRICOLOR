# RP-001 · Программа исследований FATHER OSINT / TRICOLOR
**Статус: DRAFT, 2026-10-15.** Исследовательская программа, не отчёт о проведённых экспериментах.

## Рабочие пакеты
| ID | Направление | Что изучаем | Результат |
|---|---|---|---|
| R-01 | Бизнес и предметная область | роль внешних угроз, кейсы для медиакомпании, AS-IS, TO-BE, BPMN, RACI | BRD, гипотезы, целевые метрики |
| R-02 | Законодательство | авторские и смежные права, товарный знак, судебная практика, ПД | правовая карта и контроль источников |
| R-03 | OSINT / CTI | доступность источников, provenance, IOC, TTP, классификация, дедуп | реестр источников и набор тестов |
| R-04 | Threat Hunting | гипотезы, ATT&CK, detection engineering, false positive | методики и rule testing |
| R-05 | DFIR | исходные артефакты, хэширование, история доступа, досье | Evidence specification |
| R-06 | TOP-100 | каталог 100 внутренних проверок + официальные OWASP/MITRE/CWE/NIST версии | реестр test cases и покрытий |
| R-07 | AppSec / DevSecOps | secure SDLC, SAST, SCA, secrets, SBOM, CI/CD, Git branch gates | quality & security gates |
| R-08 | AI Security | RAG permission, prompt injection, agent tool access, eval | red/blue safety test corpus |
| R-09 | Data / Graph | entity resolution, SecGraph, ALINA, knowledge lifecycle | ERD, graph model, lineage |
| R-10 | Architectures | core/profile separation, C4, contracts, build vs reuse | ADR alternatives |
| R-11 | Economics | N, storage, CPU/GPU, cloud/on-prem, TCO, ROI | verifiable calculation model |
| R-12 | Security Lab | isolated synthetic scenarios, ATT&CK mapping, replay | authorized polygon design |
| R-13 | Operations | SIEM, observability, incident handling, DR, SLO | runbooks, deployment requirements |
| R-14 | Product Validation | precision, recall, FPR, case quality, performance, UX | pilot acceptance plan |
| R-15 | Generalization | improvements TRICOLOR → OSINT_deepseek | upstream PR backlog and compatibility tests |

## Исследовательские стадии
Discover → Source validation → Hypothesis → Legal/Security review → Experiment (authorized) → Evidence and metrics → Independent review → Decision → BRD/FR/NFR/ADR update → upstream core candidate when reusable.

## Источники и эталоны
OWASP Top 10 (указывать версию), OWASP LLM Top 10, MITRE ATT&CK (версия матрицы), NIST SP 800-61 rev.3, NIST CSF, CWE, ASVS, первичные законодательные источники, разрешённые технические данные. При ссылках фиксировать URL, дату обращения, хэш/архив в случае законного сохранения.

## Gate
Инициирование, бизнес- и правовые исследования предшествуют выбору технологии; Threat Modeling и DevSecOps включаются с первого дня. Результаты пилота не равны промышленному допуску.
