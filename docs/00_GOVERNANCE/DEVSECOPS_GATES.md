# DevSecOps Security Gates and DoD
| ID | Event | Evidence required | Owner (role) |
|---|---|---|---|
| SG-00 | Project kickoff | charter, source policy, risk acceptance | Product owner |
| SG-01 | Requirements baseline | FR/NFR traceability, data classes, abuse cases | Analyst + Security |
| SG-02 | Architecture approval | DFD/C4, STRIDE, ADR, secrets and trust-boundary review | Architect + Security |
| SG-03 | Pull request | code review, lint/test, SAST/SCA/secret scan results | Maintainer |
| SG-04 | Build | pinned dependencies, SBOM, artifact hash, build provenance | DevOps |
| SG-05 | Integration | contract tests, security tests, synthetic data, backup review | QA + Security |
| SG-06 | Release | signed artifact, release note, rollback, approvals | Release manager |
| SG-07 | Operations | monitoring, retention, runbooks, alerts, incident drill | SRE + Security |
| SG-08 | Upstream promotion | generalized tests, compatibility review, OSINT_deepseek PR | OSINT core maintainer |

### Waivers
Every exception has risk owner, justification, compensating measure, review and expiry. No permanent blanket bypasses. Confirm actual CI enforcement and branch protection in GitHub settings; documentation alone is not enforcement.

### Minimal required metrics
Pipeline pass rate, test coverage trends, vulnerabilities by severity/age, MTTR, deployment failures and rollback rate, false positives, provenance completeness, unauthorized access attempts, restoration success, LLM hallucination/faithfulness and injection resistance.

### Sequence
Paperwork G0–G7 first; security analysis and documentation run in parallel from day zero; any existing prototype is experimental pending gates.
