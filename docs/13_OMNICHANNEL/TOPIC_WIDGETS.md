# CHANNEL-003 · Thematic website sections and widgets
Статус: проектный UX, не готовые виджеты. Пользовательская фраза «колоки на сайтах» интерпретируется как тематические колонки/блоки и колокольчик уведомлений; окончательная форма уточняется при UX-review.

## Website components
1. **Threat digest column:** curated safe topics with category, time, source citations, reviewer status; no accusations without expert validation.
2. **Topic cards:** Media piracy / brand imitation / fraudulent sites / external asset exposure / legal updates / AI Security.
3. **Report a suspected incident:** user voluntarily submits URL, description, consent and optionally attachment; visible ticket ID.
4. **Bell / subscriptions:** topic, severity and frequency filters; in-app/email/web-push only with applicable consent and browser permission.
5. **Search and graph widget:** permission-filtered graph snapshots with source attribution, 1–2 hop limit for public views.
6. **Feedback panel:** false-positive corrections and appeal workflow handled by staff.
7. **Partner widget / iframe:** only for explicitly allowed domains with CSP, iframe sandbox, API token scoping, CORS restrictions, clickjacking analysis.
8. **Internal analyst dashboard:** full RBAC, status board, evidence access only per role, no public exposure.

## UX + editorial guards
Public website never displays private case identifiers or original evidence. Distinguish confirmed notices vs hypotheses. Alert unsubscribe always available. Protect forms against abuse/spam, SSRF via URLs, malicious upload files, prompt injection in inbound descriptions.
## Data interaction
Web UI → API Gateway → signed session → service-side scoped graph/case data; no API keys in frontend.
