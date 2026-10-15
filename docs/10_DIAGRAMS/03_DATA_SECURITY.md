# SCH-03 · DFD-inspired Trust Boundaries
```mermaid
flowchart LR
 subgraph Internet[UNTRUSTED external]
  SRC[Lawfully accessible source]
 end
 subgraph Intake[DMZ / constrained collector]
  Allow{Allowlist & scope}
  Fetch[Sanitized acquisition]
 end
 subgraph Internal[Protected application]
  Parse[Parser / untrusted data treatment]
  Queue[Review queue]
  Policy[Policy engine]
 end
 subgraph Restricted[Restricted data zone]
  Evidence[(Encrypted evidence)]
  Events[(Audit events)]
 end
 SRC --> Allow
 Allow -->|approved| Fetch
 Allow -->|denied| Stop[Reject and log]
 Fetch --> Parse
 Parse --> Queue
 Queue --> Policy
 Policy --> Evidence
 Policy --> Events
```
SECURITY: prohibit SSRF/private destinations, credential forwarding, prompt-injected commands; enforce outbound allowlist, data minimization, isolation, retention and audited human approval. This diagram is not a complete STRIDE threat model.
