# FATHER Visual Node Spec — OSINT Radar
Shared canvas owns styling, credentials, event execution, trace, policy and node registry. Single expandable OSINT block with nested graph. Do not build independent website or CRM.
| Node ID | Inputs | Outputs |
|---|---|---|
| osint.search_job | scoped user topic and source policy | bounded query plan |
| osint.telegram_radar | permitted job, connector credentials ref | message/artifact references |
| osint.document_intake | source URL/ref, rights policy | catalog and safe artifact ref |
| osint.selection | raw normalized events, ruleset | accept/reject with reasons |
| osint.content_extract | safe file and parser config | structured text/pages/links |
| osint.dedup | fingerprints, parsed text | duplicate cluster/version |
| osint.watch | monitored topics/sources | event + change reason |
| osint.propagation | observed forwards/links/reposts | evidence-linked propagation graph |
| osint.knowledge | verified extracted corpus | cited KB candidate |
| osint.verification | observation and counterevidence | review queue and disposition |
| osint.report | reviewed case refs | formatted case report |
Connector data does not grant authorization for other sources. Explicit error ports for limits/timeouts/invalid data/security blocks. Each node carries declared capability scopes, data-class bounds, budget and audit trace. 
First proof of concept should reuse working Telegram ingress (after tests) and synthetic test messages, then introduce source watchers and propagation edges. Other adapters stay pluggable.
