# Gate checklist · Platform modular intelligence
**Project still ON HOLD for implementation.**

Must approve: business cases and modules; connector legality/capabilities per provider; public/private boundaries; data schema & provenance; evidence and case lifecycle; topic ontology; search budgets & rate limits; AI/RAG prompt injection controls; secret handling; graph ACL; source lifecycle & retention; security lab; cost/performance plan; UI accessibility and error handling.

## Staged approval
G0–G4 paper requirements/security/legal → G5 source/architecture alternatives → G6 sizing economics → G7 design signoff → FATHER Website + Agent Zoo + Model Zoo demonstrated E2E → implementation sprints → actual provider integrations following platform review.

## Suggested dependency graph
Website Visual Designer and Workflow Engine must work first; common Channel Event Contract and policy router next; one synthetic connector pipeline for E2E; then staged Telegram/MAX/VK/web/email; Tor research connector only after dedicated legal and isolation review. No automatic production launch.

## Reuse
Generic blocks graduate to FATHER OSINT_deepseek with tests and PR; legal/content domain rules remain OSINT_TRICOLOR.
