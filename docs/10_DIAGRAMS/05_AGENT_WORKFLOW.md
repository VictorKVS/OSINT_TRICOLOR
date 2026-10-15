# SCH-05 · Visual agent workflow (logical)
```mermaid
flowchart LR
 Trigger[Approved trigger] --> Parser[Parser / sanitize]
 Parser --> Router[Policy-aware router]
 Router --> Collector[Passive source adapter]
 Collector --> Memory[Case memory: scoped]
 Memory --> Retrieval[RAG: citation & ACL checks]
 Retrieval --> LLM[ALINA LLM]
 LLM --> Eval[Groundedness / PII / injection eval]
 Eval --> G{Security + confidence gate}
 G -->|pass| Human[Analyst / Legal review]
 G -->|fail| Reject[Flag / redact / retry offline]
 Human --> Output[Signed case draft]
```
No unrestricted tool execution by model. Separate untrusted content from instructions, capability-scoped tools, audit context, explicit provenance; enforce rights and non-attribution.
