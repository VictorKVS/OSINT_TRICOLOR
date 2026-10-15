# Threat Intelligence / Detection Engineering / DFIR — командная методика v0.1

## Миссия
Разработка оборонительного продукта, находящего и документирующего внешние признаки угроз и нарушений. Отделять наблюдаемые технические факты, поведенческие гипотезы и юридические выводы.

## Рабочие роли (проектная команда)
- Product Owner: бизнес-эффект, приоритизация, критерии приёмки;
- CTI/OSINT analyst: источники, IOC, enrichment, гипотезы;
- Threat hunter: гипотезы ATT&CK, проверка телеметрии на разрешённых данных;
- Detection engineer: аналитические правила, тестовый корпус, FP/FN;
- AppSec/DevSecOps: secure SDLC, SAST/SCA, chain security;
- DFIR: доказательства, цепочка хранения, расследования и реагирование;
- Data/LLM engineer: RAG, eval, permissioned tool use, explainability;
- QA/SRE: контроль качества, нагрузка, телеметрия, восстановление;
- Legal/Privacy: источники, авторское право, ПД, квалификация, согласование.

## Основные процессы
1. Intake + scope + lawful collection authorization.
2. Priority hypothesis with detection question and ATT&CK (if applicable).
3. Passive collection from approved sources or synthetic feeds.
4. Preserve original material and metadata, verify integrity.
5. Normalize, correlate, enrich with documented confidence.
6. Review and challenge hypotheses, measure false positives.
7. Route high-confidence cases to named human reviewers; no autonomous attribution/enforcement.
8. Produce immutable case export with citations and chain-of-custody.
9. Run post-case retrospective and improve detection rules.
10. Promote reusable code/policies into OSINT_deepseek by tested PR.

## Матрица отдельных методов
- OSINT: passive reconnaissance, brand/domain monitoring, IP rights verification, safe registries.
- CTI: indicators/TTP/confidence, temporal and source reliability, entity graph.
- Threat hunting: hypothesis-driven searches across owned/authorized telemetry.
- DFIR: documented capture, evidence integrity, acquisition log, analyst notes, timeline.
- Detection engineering: Sigma-like rule lifecycle, benign/adversarial synthetic fixtures, evaluation and tuning.
- Security validation: STRIDE, DFD, attack-tree, red/blue/purple exercise ONLY in authorized lab.
- LLM evaluation: injected-page corpus, leakage tests, groundedness, permission checks, human gate.

## Case lifecycle
new → scoped → collected → normalized → analyzed → peer_review → legal_review (if needed) → approved / rejected / needs_info → archived.
Track transitions with actors, UTC time, decision rationale, hashes where relevant.

## Task contract (DoR/DoD)
DoR: owner, objective, source permission, threat hypothesis, mapping, acceptance tests and non-goals.
DoD: trace to requirement, verified data provenance, reproducible tests, security review, metrics, changelog, rollback and upstream classification.

## Operating cadence
Daily intake & triage; weekly detection-review and false-positive analysis; biweekly threat-model review; per-release security gate; monthly retrospective and upstream promotion. Cadence is proposed and must be approved.

## Safety
No unauthorized active scans, credential testing, persistence, malware deployment, scraping around access controls, targeting or deanonymizing people. For adversarial techniques use isolated lab and synthetic data.
