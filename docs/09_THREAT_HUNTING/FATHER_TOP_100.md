# FATHER TOP-100 · каталог проверок v0.1
Дата: 2026-10-15. Статус: авторский предварительный чек-лист, НЕ рейтинг атак и НЕ подтверждённая реализация.

Для каждого контроля: ID, риск/гипотеза, обоснование, источник, владелец, тест, expected result, evidence, статус, related MITRE/OWASP/CWE/NIST, severity и отметка о принятии.

## 1. OSINT governance
- [ ] FTH-001 — цель расследования
- [ ] FTH-002 — правовое основание
- [ ] FTH-003 — границы поиска
- [ ] FTH-004 — допуск источников
- [ ] FTH-005 — классификация данных
- [ ] FTH-006 — минимизация ПД
- [ ] FTH-007 — проверка лицензий
- [ ] FTH-008 — сроки хранения
- [ ] FTH-009 — политика доступа
- [ ] FTH-010 — аудит действий

## 2. External attack surface
- [ ] FTH-011 — инвентаризация доменов
- [ ] FTH-012 — связи DNS
- [ ] FTH-013 — проверка регистрации
- [ ] FTH-014 — публичные сертификаты
- [ ] FTH-015 — брендовые двойники
- [ ] FTH-016 — подозрительные редиректы
- [ ] FTH-017 — поддельные страницы оплаты
- [ ] FTH-018 — имитация поддержки
- [ ] FTH-019 — легальные публичные API
- [ ] FTH-020 — изменения внешних активов

## 3. Threat intelligence
- [ ] FTH-021 — IOC provenance
- [ ] FTH-022 — confidence levels
- [ ] FTH-023 — сопоставление TTP
- [ ] FTH-024 — MITRE ATT&CK mapping
- [ ] FTH-025 — история IOC
- [ ] FTH-026 — источник и достоверность
- [ ] FTH-027 — связи кампаний
- [ ] FTH-028 — false positive
- [ ] FTH-029 — срок актуальности IOC
- [ ] FTH-030 — разделение фактов и гипотез

## 4. Content and brand
- [ ] FTH-031 — товарный знак
- [ ] FTH-032 — связь с правообладателем
- [ ] FTH-033 — проверка лицензии
- [ ] FTH-034 — пиратские трансляции как гипотеза
- [ ] FTH-035 — IPTV предложения как гипотеза
- [ ] FTH-036 — контрафактные объявления
- [ ] FTH-037 — проверка доменных имитаций
- [ ] FTH-038 — дубли объявлений
- [ ] FTH-039 — цепочка контента
- [ ] FTH-040 — юридическая проверка

## 5. Evidence and case management
- [ ] FTH-041 — целостность оригинала
- [ ] FTH-042 — SHA-256
- [ ] FTH-043 — временная метка
- [ ] FTH-044 — URL происхождения
- [ ] FTH-045 — цепочка владения
- [ ] FTH-046 — протокол фиксации
- [ ] FTH-047 — журнал доступа
- [ ] FTH-048 — версионирование отчёта
- [ ] FTH-049 — контроль вложений
- [ ] FTH-050 — проверка перед передачей

## 6. Secure coding
- [ ] FTH-051 — контроль авторизации
- [ ] FTH-052 — аутентификация
- [ ] FTH-053 — управление сессиями
- [ ] FTH-054 — валидация входа
- [ ] FTH-055 — SSRF protection
- [ ] FTH-056 — injection prevention
- [ ] FTH-057 — шифрование
- [ ] FTH-058 — управление секретами
- [ ] FTH-059 — защита логов
- [ ] FTH-060 — security review

## 7. DevSecOps supply chain
- [ ] FTH-061 — защита веток
- [ ] FTH-062 — обязательный PR
- [ ] FTH-063 — SAST
- [ ] FTH-064 — SCA
- [ ] FTH-065 — secret scan
- [ ] FTH-066 — SBOM
- [ ] FTH-067 — фиксированные зависимости
- [ ] FTH-068 — подпись сборки
- [ ] FTH-069 — проверка контейнера
- [ ] FTH-070 — release rollback

## 8. AI LLM RAG security
- [ ] FTH-071 — prompt injection
- [ ] FTH-072 — PII leakage
- [ ] FTH-073 — RAG data poisoning
- [ ] FTH-074 — retrieval ACL
- [ ] FTH-075 — output validation
- [ ] FTH-076 — agent tool permission
- [ ] FTH-077 — model supply chain
- [ ] FTH-078 — hallucination evaluation
- [ ] FTH-079 — adversarial eval
- [ ] FTH-080 — human approval

## 9. Infra and detection
- [ ] FTH-081 — asset ownership
- [ ] FTH-082 — least privilege
- [ ] FTH-083 — network segmentation
- [ ] FTH-084 — audit events
- [ ] FTH-085 — SIEM pipeline
- [ ] FTH-086 — alert tuning
- [ ] FTH-087 — anomaly detection
- [ ] FTH-088 — backup restore
- [ ] FTH-089 — incident exercises
- [ ] FTH-090 — observability SLO

## 10. Investigation QA and response
- [ ] FTH-091 — incident triage
- [ ] FTH-092 — case correlation
- [ ] FTH-093 — evidence sufficiency
- [ ] FTH-094 — analyst peer review
- [ ] FTH-095 — legal approval
- [ ] FTH-096 — notification workflow
- [ ] FTH-097 — playbook validation
- [ ] FTH-098 — postmortem
- [ ] FTH-099 — regression corpus
- [ ] FTH-100 — upstream promotion

## Правила исполнения
Каждая проверка без test-case, результата и доказательства имеет статус planned. Использовать только разрешённые/синтетические данные; активные действия исключительно на собственном полигоне или по письменному разрешению.
Каталог версионируется; ссылки на соответствующие версии MITRE ATT&CK, OWASP Top 10 web/LLM, NIST, CWE и контрольные тесты заполняются на этапе детализации.