# GDB-002 — graph sizing model
**Status:** illustrative parameters only. No sizing claims for Tricolor or external organization.

## Input variables
D = signals/day; u = unique fraction; n = new nodes / unique signal; e = new edges / unique signal; R = retention days; sN, sE = estimated bytes/node and /edge including average property payload; k = index + row overhead multiplier; b = backup multiplier; r = replica count.

Nodes = D × u × n × R. Edges = D × u × e × R.
Raw GB (decimal) = (Nodes × sN + Edges × sE) / 10^9.
Provisioned GB = Raw GB × k × (1+b) × r. All values require benchmark confirmation.

## Synthetic estimates (not vendor prices)
Assume n=3, e=5, sN=500B, sE=350B, k=2.5, b=1, r=1.
| scenario | D/day | u | R days | nodes | edges | raw GB | provisioned GB |
|---|---:|---:|---:|---:|---:|---:|---:|
| lab | 100 | .8 | 30 | 7200 | 12000 | 0.0078 | 0.039 |
| operational example | 2000 | .65 | 180 | 702000 | 1170000 | 0.7605 | 3.8025 |
| scale example | 20000 | .5 | 365 | 10950000 | 18250000 | 11.8625 | 59.3125 |
These figures EXCLUDE source artifacts, evidence binaries, logs and fulltext/vector indices.

## Benchmark protocol
Synthetic corpus; reproducible seed; record p50/p95/p99 read latency, writes/s, CPU/RAM/disk IOPS, fanout and policy filtering; test 1/2/3-hop, time predicates and large-degree nodes. Perform backup/restore and corruption recovery test. Fix data generator and query versions before comparing technologies.

## Economic model
TCO 36m = engineering time + infra (VM/managed/cloud) + licensing + backups + ops + compliance + incident preparedness. Sensitivity +/-50% volume, retention, index size, and staffing. No procurement decision without vendor quotes and baseline.
