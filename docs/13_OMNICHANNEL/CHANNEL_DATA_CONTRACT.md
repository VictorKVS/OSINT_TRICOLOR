# CHANNEL-005 · Canonical channel events
**DRAFT, not a deployed contract.**

## ChannelEvent
event_id, provider [telegram|max|vk|web|email|rss|other], provider_event_id, channel_instance_id, received_at_utc, published_at_utc, actor_ref_pseudonymous, event_kind, payload_type, content_ref, source_uri_if_permitted, consent_basis, access_scope, sensitivity, language, dedup_key, correlation_id, provenance, schema_version.

## ChannelConfig
channel_id, provider, adapter_version, enabled, allowed_event_types, scope, legal_basis_ref, data_class, rate_limit, credential_ref (never secret value), retention_policy_ref, owner, last_verified_at, moderation_or_membership_status.

## NotificationSubscription
id, recipient_pseudonymous, channel_id, topics[], severity_threshold, frequency, consent_timestamp, status, unsubscribe_ref, retention.

## Event graph relationships
ChannelInstance PUBLISHES Event; Event NORMALIZED_TO Observation; Observation SUPPORTED_BY Artifact; Observation INCLUDED_IN Case; Case REVIEWED_BY Decision; Decision AUTHORIZES Notification; Notification DELIVERED_VIA ChannelInstance.

## Invariants
No global correlation of persons across messenger channels without specific lawful basis; no guessing identities from handles. No uncontrolled export of conversations. Provider permissions are not a substitute for privacy assessment. All events auditable and retention-bound.
