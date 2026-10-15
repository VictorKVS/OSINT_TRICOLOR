# FATHER OSINT donor research — initial screening
Date: 2026-10-16. State: **SOURCE SCREENING**, not security-certified, not dependency approval, no code imported.

## Mission and selection
Reuse existing OSINT_deepseek/Telegram TDLib capabilities first. Research alternative projects for reusable patterns of watchers, document acquisition, entity relationships, intelligence enrichment and visual graph. Keep FATHER canvas and OSINT profile separation. Check current upstream state *before any installation*, verify exact release/license/dependencies and run sandbox PoC.

| ID | Project and canonical URL | Capability | Public license evidence | Preliminary action | Security / integration concern |
|---|---|---|---|---|---|
| DN-01 | https://github.com/zoharbabin/telegram-monitor | monitoring, CLI/TUI, Telegram | project metadata MIT; verify LICENSE exact revision | STUDY architecture | uses Telethon and Claude SDK; avoid implicit cloud transfer |
| DN-02 | https://github.com/imranborzov/tg-parser | keyword/exclusion filters, webhooks | NOT VERIFIED | ADAPT PATTERN (clean implementation) | session custody, channels permission and webhook exposure |
| DN-03 | https://github.com/docling-project/docling | PDF/DOCX/OCR/parsing | MIT official site | POC LIBRARY | isolate hostile files, model dependency footprint, OCR quality |
| DN-04 | https://github.com/docling-project/docling-graph | validated entity / relationship extraction | MIT reported by upstream | POC / STUDY | hallucinated or wrongly asserted edges; schema verification |
| DN-05 | https://github.com/apache/tika | multi-format parsing | Apache-2.0 | EVALUATE ALTERNATIVE | Java/ops footprint, parser sandbox, resource caps |
| DN-06 | https://github.com/OpenCTI-Platform/opencti | CTI concepts, graph, indicators, connector model | Community Apache-2.0; Enterprise separate | STUDY INTEROP | enterprise boundaries and complexity; no wholesale copy |
| DN-07 | https://github.com/intelowlproject/IntelOwl | enrichment analyzer plugins, REST | AGPL-3.0 | STUDY PATTERNS / legal review before library or deployment | AGPL obligations; external API data disclosures |
| DN-08 | https://github.com/MISP/MISP | CTI interoperability and event sharing | AGPL core | STUDY STIX/MISP API | feed access, licensing, sharing policy |
| DN-09 | https://github.com/xyflow/xyflow | node workflow canvas | MIT core; Pro resources separate | CANDIDATE use in shared FATHER only | version, licensing of Pro components |
| DN-10 | https://github.com/jacomyal/sigma.js | graph rendering with Graphology | MIT | CANDIDATE analytic graph | no guaranteed performance until benchmark |
| DN-11 | https://github.com/LonamiWebs/Telethon | Telegram MTProto client | exact license to inspect; upstream archived Feb 2026 | HOLD / compatibility only | archived dependency maintenance risk |
| DN-12 | https://github.com/FlowiseAI/Flowise | visual LLM flows and runtime | mixed: Apache-2.0 outside enterprise portions | STUDY patterns only | avoid copying proprietary enterprise code; legal review |
| DN-13 | https://github.com/tdfleming/DocIngest | document→chunk→vector/graph | Apache-2.0 claimed | STUDY / benchmark against Docling | claims need reproduction, deploy complexity |

## Safe reuse classes
A) Direct library dependency only after: verified exact license/version, release history, SCA, SBOM, provenance, update path, sandbox tests and legal review.
B) Adapter to a licensed external service with permissioned API, independent storage and explicit data policy.
C) Architectural concept independently implemented, no copying of protected expression/code.
D) Reject or hold if license unclear, archived with no viable maintainer, exfiltration, exploit-like or improper data collection.

## FATHER shortlist
Priority P1 Docling (books/articles, local extraction); xyflow for shared canvas (FATHER scope, not reimplemented by this OSINT module); Sigma.js for SecGraph view; Tg-parser filter pattern (rewrite under our contracts).
P2 Docling-Graph; OpenCTI schema concepts; MISP compatibility and STIX/TAXII; IntelOwl enrichment adapter patterns (without bundling AGPL code).
P3 alternate Telegram clients only if TDLib comparison proves gap; maintainers, session security, terms and rate-limits verified.
## Entry gate for donor
Canonical repo → exact release and license file → last meaningful activity/issues → dependency/SBOM/SCA → secret/session/data audit → isolated PoC on synthetic/approved data → common benchmark → alternative comparison → reviewer + ADR → approved dependency or concept. Popularity is not evidence.
## Baseline evidence URLs reviewed
https://docling.ai/
https://xyflow.com/open-source
https://github.com/jacomyal/sigma.js
https://github.com/OpenCTI-Platform/opencti/blob/master/LICENSE
https://www.misp-project.org/license/
https://github.com/intelowlproject/IntelOwl
https://github.com/LonamiWebs/Telethon
https://github.com/FlowiseAI/Flowise/blob/main/LICENSE.md
https://github.com/zoharbabin/telegram-monitor/blob/main/pyproject.toml
https://github.com/imranborzov/tg-parser
Additional evidence required for license and current release on individual donor projects. Not a completed license audit.
