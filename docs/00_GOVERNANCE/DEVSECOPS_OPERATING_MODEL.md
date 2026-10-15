# FATHER OSINT_TRICOLOR — DevSecOps Operating Model v0.1
**Статус:** проект обязательной политики. Дата: 2026-10-15. Никакие контроли не считаются действующими, пока не проверено их исполнение.
## Принцип
DevSecOps начинается до первого коммита: потребность → требования → threat modeling → план архитектуры → код → supply-chain → проверки → release → эксплуатация. Все изменения прослеживаются от business requirement до evidence о тестировании.
## Организация репозитория
- main — защищённая стабильная ветка. Разработка только через PR с reviews и успешными обязательными проверками.
- feature/* и fix/* — короткоживущие ветки; hotfix через ту же проверку и отдельный экстренный approval.
- Conventional Commits; теги SemVer; CHANGELOG; ADR на архитектурные решения; CODEOWNERS.
- Issue templates (requirement/bug/security/change), PR checklist, traceability ID.
- Политика работы с секретами: запрещены ключи, персональные данные, материалы расследований в Git; .env.example без значений; secret manager для prod.
## Security controls by stage
| Stage | Controls | Release-blocking |
|---|---|---|
| Design | data classification, STRIDE, DFD, source legality, RACI | Threat model missing |
| Commit/PR | lint, types, tests, coverage, secret scan, SAST, dependency vulnerability checks | critical vulnerability/secret |
| Build | isolated dependencies, lockfiles, SBOM, provenance, checksums, signature | unknown origin |
| Integration | contract, API authz, RAG prompt-injection tests, data leakage tests, policy tests | contract/security failure |
| Staging | deploy IaC, container scans, DAST on owned staging targets, rollback drill | major exposed risk |
| Release | signed version, approved change, documented exceptions | unapproved gate |
| Production | metrics/logs/traces, SIEM, incident response, vulnerability management, backups, RPO/RTO | absent mandatory controls |
## Environments
LOCAL (synthetic data only) → CI ephemeral → TEST → STAGING → PROD. No real evidence in CI logs or public artifacts; no direct staging→prod state copy. Access via RBAC, minimum privileges, time-bound credentials. Secrets via managed vault. Separate storage and encryption keys.
## Secure SDLC controls
- Application: validate all inputs, prevent SSRF in URL intake/collectors, SQL parameterization, rate caps, egress allowlist, least privilege.
- LLM: untrusted webpages treated as data only, prompt injection containment, output provenance, evaluation sets, human approval for legal decisions.
- Evidence: immutable original, SHA-256, chain-of-custody events, timestamping controls, tamper detection and retention rules.
- Privacy: data minimization, purpose limitation, retention review, redaction, access logging.
- Upstream: reusable security fixes transferred to OSINT_deepseek through PR, tests and compatibility checks.
## Required operational artifacts
CI/CD runbook, vulnerability register, exception/waiver log with expiry, threat model, SBOM inventory, dependency policy, supply-chain provenance, backup/restore tests, incident response plan, disaster recovery, SLO/error budgets, risk register, release dossier and rollback plan.
## Gate principle
If a control has not been installed and measured, status = PLANNED, not IMPLEMENTED. Manual approvals cannot be silently bypassed.
