# Search Surfaces & Methodologies
Status: research catalog; no active source access initiated.
| Category | Examples | Access pattern | Controls |
|---|---|---|---|
| Open web | search engines, sites, RSS, news | approved API or public pages | terms, provenance, rate limits |
| Messaging | Telegram, MAX, VK managed/public accessible content | authorized bots/APIs with scope | no private chat surveillance |
| Developer ecosystem | public Git repositories, package registries | official API where possible | verified provenance |
| Infrastructure | DNS, RDAP, CT logs, permitted passive services | passive queries and datasets | no scanning outside authorized scope |
| Corporate/legal | registry of marks, public business/court records | published lawful records | legal review, redaction |
| Media | open images/videos/text OCR | approved original media | rights and content provenance |
| Threat intel | CERT feeds, abuse feeds, MISP/STIX/TAXII where authorized | licensed/approved feeds | IOC lifetime, license, confidence |
| Dark Web/Tor | lawfully accessible onion publications, legitimate intelligence feeds | isolated, read-only controlled research via Tor or licensed reports | legal basis, containment, malware safety; no illicit purchases or access bypass |
| Archives | permitted cached/archived snapshots | original provenance + collection date | rights, retention |

## Dark web research gate
Pre-approved purpose and scope; separate egress identity/isolated sandbox; restricted content types/no execution of untrusted binaries; no logging of unnecessary PII; malware scanning; no live interaction with illegal marketplaces; legal escalation if incidental unlawful material; evidence integrity; analyst confirmation. Investigations only where authorized.
## Planner requirements
Search job: purpose, query DSL, channels, temporal window, budget, permitted source IDs, data classes, analyst owner, stop conditions, retention and review. Discovery can propose additions but cannot autonomously change source allowlist.
