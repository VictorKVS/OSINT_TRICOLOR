# Modular capability catalog
| ID | Module | Input | Output | Reuse |
|---|---|---|---|---|
| HUB-01 | CRM & Omnichannel | consented messages, tickets | contacts, cases, tasks | FATHER core |
| HUB-02 | Channel Zoo | approved credentials/scopes | normalized events | FATHER core |
| HUB-03 | Search Agent Zoo | target/source plan | scoped findings | OSINT core |
| HUB-04 | Search Planner | topics, queries, constraints | authorized search jobs | OSINT core |
| HUB-05 | Source Filter | raw source events | accepted/rejected signals, reasoning | OSINT core |
| HUB-06 | Content Normalizer | heterogeneous records | canonical event, lang/media | OSINT core |
| HUB-07 | Dedup & Entity Resolution | events and evidence | grouped entities with confidence | OSINT core |
| HUB-08 | ALINA Analyst | cited observations and rules | draft hypothesis and analysis | shared AI |
| HUB-09 | SecGraph | nodes/edges/evidence | permission-filtered graph | shared |
| HUB-10 | Evidence Vault | lawful originals + metadata | immutable references and hashes | shared |
| HUB-11 | Case Management | hypotheses and evidence | review and legal workflow | shared |
| HUB-12 | Notifications & Reports | approved messages | consented outbound actions | shared |
| HUB-13 | Workflow Engine | typed node graph | audited run state | FATHER core |
| HUB-14 | Policy & DevSecOps | actor identity / action / context | allow or deny and audit | shared |
| HUB-15 | Monitoring & Evaluation | traces, tests, latency/cost | SLO and security gates | shared |

## Connector versus agent
A Connector implements API authorization, request limits, webhook validation, message/media parsing, pagination and event provenance. An Agent uses one or more approved connectors to execute scoped search strategy, classify results and prepare case hypotheses; it cannot bypass connector policy.

## Independent modules
Telegram Connector + Telegram Search Agent; MAX Connector + MAX Search Agent; VK Connector + VK Search Agent; Website Connector + Web Search Agent; Email Connector + Mail Search Agent; Tor research adapter + Dark Web Intelligence Agent; Legal Registry Connector + Legal Intelligence Agent. Each has separate rate policy and provider capability matrix, and uses common contracts.

## Domain overlays
Media rights and brand protection are configured only in TRICOLOR profile; reusable connectors/search graph/provenance remain in general OSINT core.

## Non-goals
Mass private chat surveillance, unauthorized scraping, attribution of people solely via handles/IP, automated enforcement. 
