# SCH-06 · Secure software delivery
```mermaid
flowchart LR
 Req[BRD + FR/NFR + threat model] --> ADR[Architecture decision]
 ADR --> PR[Feature branch + PR review]
 PR --> Check[Lint / tests / SAST / SCA / secret scan]
 Check --> Build[Locked build + SBOM + provenance]
 Build --> Image[Artifact/container scan]
 Image --> Stage[Authorized staging DAST + contract & AI eval]
 Stage --> Gate{Release approval}
 Gate -->|approved| Prod[Controlled production deployment]
 Gate -->|rejected| PR
 Prod --> Observe[Logs / SLO / SIEM / patch cycle]
 Observe --> Req
```
**Current state:** only a limited CI baseline is configured; remaining steps are target controls. Protect main / require PR review in GitHub settings before calling CI enforced. Never test third-party systems without permission.
