# SCH-04 · Case + Evidence state machine
```mermaid
stateDiagram-v2
 [*] --> New
 New --> Scoped: authorization & purpose
 Scoped --> Collected: permitted acquisition
 Collected --> Enriched: integrity + metadata
 Enriched --> AnalystReview
 AnalystReview --> NeedsInfo
 NeedsInfo --> Enriched
 AnalystReview --> Rejected
 AnalystReview --> LegalReview: sufficiently supported
 LegalReview --> Rejected
 LegalReview --> Authorized: approved
 Authorized --> ActionRecorded: human-only external action
 ActionRecorded --> Archived
 Rejected --> Archived
 Archived --> [*]
```
Every transition records actor, timestamp, reason, evidence IDs, hash and provenance as applicable. Raw artifacts immutable; interpretation versioned and reviewable. No model-triggered irreversible action.
