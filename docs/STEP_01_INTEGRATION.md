# STEP_01 — Evidence-first OSINT vertical slice

**Status:** local artifact tested (8/8 unit tests); branch created for integration. Do not claim production readiness or verified external threats.

## Verified local scope
- Evidence Vault with content SHA-256 and integrity recheck
- Normalized observations, SQLite, human review and audit log
- Typed provenance graph: observation -> domain, links marked unverified
- Kali/Debian/Ubuntu/Windows compatible Python implementation
- No automatic live crawling; no unauthorized testing

## Integration rule
Keep the existing repository's agent.py and tests intact. The artifact `OSINT_TRICOLOR_STEP01.zip` contains additive modules `src/osint_tricolor/evidence.py`, `knowledge.py`, `scripts/step01.py`, and three unit tests. Review its packaging before merging into the canonical repository; the previous v0.2 distribution is not currently identical to main.

## Next steps
1. Compare repository and package structure without replacing main
2. Add approved public-source collectors with allowlists, throttling, timeout and retention policy
3. Make source-document evidence links explicit; capture immutable originals via secured WORM storage
4. Add graph visualization, case review, KPI and CI
5. Perform one real documented 30–50 object investigation with legal review

No unverified allegation may be labeled confirmed.