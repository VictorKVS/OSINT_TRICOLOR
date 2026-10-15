# CHANNEL-004 · Security & QA gates
**Planned tests, not executed.**

| ID | Test | Expected |
|---|---|---|
| CH-01 | Telegram webhook without/with invalid secret token | reject |
| CH-02 | MAX webhook untrusted request | reject according to documented verification mechanism |
| CH-03 | replayed event message ID | no duplicated case or outbound action |
| CH-04 | unapproved/private channel requested | no collection |
| CH-05 | opt-out recipient receives an alert | delivery prevented |
| CH-06 | user-provided localhost URL | no SSRF/private destination access |
| CH-07 | malicious attachment | quarantined/rejected |
| CH-08 | prompt injection in Telegram/MAX/web form | remains untrusted data; no privileged tool calls |
| CH-09 | confidential graph included in public website card | data blocked server-side |
| CH-10 | outbound allegation not human approved | never published |
| CH-11 | rate limit / provider outage | bounded retries, DLQ, audited backoff |
| CH-12 | token leaked in log | test must fail, logs redacted |
| CH-13 | role with only public rights views private case | denied, no existence leak |
| CH-14 | platform API breaking change | contract tests flag incompatibility |
| CH-15 | browser notification permission denied | no web push |

## DevSecOps
CI: adapter contract tests, mock provider fixtures, SAST/SCA/secrets, SBOM, dependency pinning, API schema snapshots, negative security tests, threat model. Staging uses only test bots/channels with authorization. Release gates require consent/privacy review and operational runbooks.
