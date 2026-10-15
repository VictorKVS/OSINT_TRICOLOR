# Donor evaluation and safe integration plan
State: planned only. No installation or deployment.

## Prototype 1: document extractor
Compare existing father_osint/book_corpus vs Docling vs Apache Tika on 20 synthetic/openly licensed files: OCR/layout tables, page citations, malicious/corrupted formats, runtime CPU/RAM, provenance preservation. Decide use adapter not monolithic replacement.

## Prototype 2: Telegram watcher
Replay 100 synthetic or consented Telegram records with duplicates, edits, explicit forward metadata, disappearing source, rate-limit cases and prompt injection string. Compare existing TDLib flow to studied filter strategies. Never transfer messages to cloud SDK by default.

## Prototype 3: propagation graph
Model 1k, 10k, 100k synthetic nodes; compare Sigma.js/Graphology rendering to current FATHER/SecGraph views; relations VERIFIED_FORWARD / LINK / TEXT_SIMILARITY and contradictory evidence must stay distinct.

## Prototype 4: CTI interoperability
Evaluate STIX 2.1/MISP/OpenCTI interchange with synthetic IOC data; accuracy, source reliability, retention, terms and access control.

## Measuring
Coverage, false-positive precision, provenance completeness, parser correctness, resource consumption, external API cost, latency, vulnerability findings, privacy and maintainability.
Only recommend adoption with exact version, published license obligations, source commit SHA, acceptable risks and recorded ADR.

## Gates
Research artifacts preserved in GitHub; do not change working Telegram collectors or add dependencies now. FATHER Site + Agent/Model Zoo practical E2E and architecture approval remain prerequisites for implementation. Upstream generalized improvements go to OSINT_deepseek through reviewed PR.
