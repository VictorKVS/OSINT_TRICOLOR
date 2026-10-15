# FATHER Dependency & License Guard — policy proposal v0.1
Date 2026-10-16. DRAFT, not implemented.

## Scope
Third-party Python, JavaScript, native libraries, model weights/datasets, SaaS APIs, plugins and their transitive dependencies used by OSINT block and shared FATHER runtime.

## Distinct failure modes
1. Repository disappears or maintainer changes future licensing: pin version and preserve approved source/license evidence; prior legitimate license permissions are generally not retroactively revoked merely by later relicensing, subject to actual license and compliance.
2. License-service / remote activation / SaaS can stop access: always mark remotely dependent; require replaceable adapter and fallback.
3. Copyleft / AGPL / source-available / proprietary: legal review for distribution, hosted network use, linking, modification; no blanket approval.
4. Compromised releases and automatic updates: pin versions and hashes, disable unreviewed auto-upgrades; staged update gates.
5. External telemetry/data processing: network-egress inventory, privacy decision, default deny for sensitive evidence.
6. Models and datasets have separate licenses and use restrictions; review separately from software packages.

## Intake control matrix
Required: canonical source, maintainer, exact commit, artifact SHA256, version, SPDX identifier and original LICENSE/NOTICE copies, dependency graph and SBOM, update source, remote services/activation, network endpoints, hosted/on-prem license constraints, SCA and secret scan, permissioned source use, replacement candidate, incident runbook, reviewer and decision date.

## Dependency lifecycle
DISCOVERED → LICENSE_VERIFIED → TECHNICALLY_VERIFIED → SECURITY_REVIEWED → SANDBOX_BENCHMARKED → APPROVED → PINNED → MONITORED.
Other states: BLOCKED, WATCH, QUARANTINED, DEPRECATED, REPLACED.
No install or runtime import from unreviewed donor into live Telegram collector.

## Operations
- Preserve provenance of *lawfully obtained* source and license text without implying that archival alone grants rights.
- SBOM CycloneDX or SPDX; lockfiles with hashes; mirrored internal packages only if license and distribution terms permit.
- Continuous license/version/security monitoring (proposed): review upstream changes and advisories; alert on change, never auto-disable production simply because license metadata changed.
- For actual security compromise, authorized incident runbook may quarantine a dependency after impact assessment and operator approval.
- Fall back to existing OSINT_deepseek modules; externally hosted service integrations degrade gracefully.
- Test offline operation, provider outage, license-server unavailability and reversible replacement.
- Record false positives and material compatibility obligations. Legal signoff for ambiguity.

## Core priorities
P0: existing TDLib transport dependency/license and transitive artifacts; Docling; React Flow (FATHER platform only); Sigma.js (graph view); external inference models.
P1: Telecom messaging API access terms; parsers and OCR weights; optional enrichment APIs.
P2: experimental donor projects — architecture patterns first.

## References
https://opensource.org/osd
https://opensource.org/faq
https://cyclonedx.org/capabilities/sbom/
