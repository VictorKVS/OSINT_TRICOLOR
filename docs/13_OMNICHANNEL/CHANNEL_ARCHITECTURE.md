# CHANNEL-002 · Omnichannel architecture
```mermaid
flowchart TB
 subgraph CH[External channels: untrusted boundary]
  TG[Telegram] 
  MX[MAX]
  VK[VK]
  WEB[Website forms / topic widgets]
  MAIL[Email / RSS]
 end
 TG --> GW[Channel Gateway: per-platform verification]
 MX --> GW
 VK --> GW
 WEB --> GW
 MAIL --> GW
 GW --> POLICY[Consent + source permission + rate caps + privacy filter]
 POLICY --> NORM[Canonical Event Adapter]
 NORM --> QUEUE[Idempotent Queue]
 QUEUE --> ROUTER[FATHER Policy Router]
 ROUTER --> OSINT[OSINT_deepseek shared core]
 ROUTER --> ALINA[ALINA / RAG restricted tools]
 OSINT --> GRAPH[SecGraph / evidence provenance]
 OSINT --> TRICOLOR[TRICOLOR domain rules]
 TRICOLOR --> REVIEW[Human analytical + legal review]
 REVIEW --> OUT[Controlled Outbound Router]
 OUT --> TG
 OUT --> MX
 OUT --> VK
 OUT --> WEB
 OUT --> MAIL
```

## Data boundary and protections
Provider webhook authentication and replay prevention; independent connector credentials; no untrusted raw content as LLM instructions; storage classification & retention; minimize sender identifiers; per-channel outbound allowlist/opt-in and approvals; schema validation; malware/attachment size control; strict egress. Reject if permission or bot membership is absent.

## Patterns
Inbound: webhook validated → event ID → dedup/idempotency → normalize → provenance → policy routing → draft case.
Outbound: analyst/legal approved template → recipient consent/scope check → channel-specific formatter → send → audit result and retries with backoff.
Topic widgets are presentation components and do not independently fetch sensitive source content from browsers.
