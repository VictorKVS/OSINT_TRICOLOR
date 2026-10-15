# Threat Hunter product requirements v0.1
## Components
1. Source policy registry
2. Passive source adapters
3. Normalization + provenance pipeline
4. IOC / TTP enrichment and ATT&CK mapping
5. Detection rule repository + evaluation harness
6. SecGraph correlation
7. Evidence vault and immutable case audit
8. Analyst workbench, peer review, legal review
9. ALINA RAG with source citations and injection guardrails
10. Incident response handoff, measured workflow

## User stories
TH-001 As analyst I can create hypothesis with source, technique and confidence without treating inference as fact.
TH-002 As detection engineer I can replay anonymized synthetic cases and measure precision/recall and FP.
TH-003 As reviewer I can trace every assertion to original artifact and analyst decision.
TH-004 As security lead I can view coverage mapped to ATT&CK and track untested assumptions.
TH-005 As legal owner I must approve external referrals/takedown claims.
TH-006 As core maintainer I can promote generalized changes through regression-tested upstream PR.

## Acceptance
For each story define synthetic examples, negative cases, reviewer evidence and traceability FR→test→report. No production release before data/privacy/authorization sign-off.
