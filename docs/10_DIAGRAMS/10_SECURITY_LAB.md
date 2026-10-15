# SCH-10 · Isolated Security Engineering Lab
```mermaid
flowchart LR
 Synthetic[Synthetic cases + benign baselines] --> Lab[Isolated lab]
 Approved[Explicit authorized scenarios] --> Lab
 Lab --> Rules[Detector rules]
 Rules --> Replay[Reproducible replay]
 Replay --> Metrics[Precision / recall / FPR / latency]
 Metrics --> Peer[Peer + security review]
 Peer --> Backlog[Product and upstream backlog]
```
No uncontrolled network paths, no attacking real external systems, no real malware or personal data in public CI, no collection outside scope. Isolation, containment, reset and egress testing require lab acceptance criteria.
