# RT-001 · Матрица трассировки исследования в продукт
| Исследование | Контроль/стандарт | Решение | Требования | Верификация |
|---|---|---|---|---|
| R-01 | BPMN / RACI | business process model | BRD, FR | expert process review |
| R-02 | ГК РФ/149-ФЗ/152-ФЗ (при применимости) | rights + lawful source policy | FR-001/004 | legal review |
| R-03 | CTI methods, provenance | common core | FR-002/003/005 | intake tests |
| R-04 | MITRE ATT&CK | detection rules | proposed TH-001 | rule corpus replay |
| R-05 | chain-of-custody | Evidence Vault | FR-006/007/013 | integrity test |
| R-06 | FATHER TOP-100 + OWASP/CWE | security coverage | NFR | coverage mapping |
| R-07 | Secure SDLC, supply chain | GitHub gates | SG-00 to SG-08 | CI / review evidence |
| R-08 | OWASP LLM | ALINA guardrails | LLM NFR | adversarial synthetic eval |
| R-09 | graph / data model | SecGraph integration | FR-008 | graph contract tests |
| R-10 | C4/ADR | profile architecture | NFR-007 | architecture review |
| R-11 | TCO/sizing | alternative choice | NFR capacity | measured load test |
| R-12 | isolated security lab | safe ATT&CK cases | NFR security | containment drill |
| R-13 | NIST IR / SLO | operational design | NFR-005/006 | recovery exercises |
| R-14 | QA metrics | pilot gate | FR acceptance | signed pilot report |
| R-15 | OSINT_deepseek | upstream lifecycle | FR-014 | merged PR+regression |

Статусы: проектная связь, не подтверждение фактического выполнения. Проверки, методологии, нормативы версионировать.
