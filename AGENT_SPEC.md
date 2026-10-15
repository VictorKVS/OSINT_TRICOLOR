# Agent specification

**Goal:** triage publicly sourced leads for media/brand protection while preserving provenance and human legal review.

## MVP contract

Input JSONL fields: `url` (http/https), `category`, `title`, `description` (optional), `observed_at` (timezone-aware ISO8601), `source` (optional).

Categories: suspected_restream, suspected_iptv, trademark, suspected_counterfeit, phishing, other.

Output: SQLite findings and audit events; Markdown preliminary report. Dedup key is SHA-256 of normalized URL + category. Scores are heuristic *priorities*, not probability of illegality or attribution.

## Next milestones

- Licensed/approved source adapters with rate limiting, retries and deletion policies.
- Rights/license registry and exception controls.
- Separate original evidence from interpretations; immutable hashes and custody metadata.
- ALINA review queue, entity-linking and SecGraph integration.
- Versioned scoring rules, unit tests, evaluation sets and CI.
- FATHER orchestration and dashboard; no autonomous enforcement.

**Core enhancements belong upstream** into OSINT_deepseek by tested PR; this repo retains configurable industry specifics.
