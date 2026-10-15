# SCH-07 · Environment isolation / deployment (candidate)
```mermaid
flowchart TB
 Dev[Developer local, synthetic data] --> CI[Ephemeral CI, no production secrets]
 CI --> Test[Test environment]
 Test --> Staging[Staging / synthetic-authorized data]
 Staging --> Release{Manual approval}
 Release --> Prod[Production cluster or VMs]
 subgraph P[Production protected zone]
  Prod --> Gateway[API + auth]
  Gateway --> Workers[Policy-controlled workers]
  Workers --> CaseDB[(Case DB)]
  Workers --> Vault[(Evidence store)]
  Workers --> SIEM[SIEM + observability]
 end
```
Platform choice VM vs containers vs Kubernetes after load sizing, TCO, RPO/RTO and risk analysis. Diagram does NOT mean Kubernetes was deployed.
