# CHANNEL-001 · Channel capability matrix (2026-10-15)
| Channel | Inbound | Outbound | Specific boundary | Pilot status |
|---|---|---|---|---|
| Telegram Bot API | updates to bot / accessible chat events | replies and consented alerts | webhook/getUpdates mutually exclusive; secret_token header; not arbitrary private chats | planned |
| Telegram public channels | only lawful accessible updates and channels with proper bot permissions | approved publications | no blanket channel access; distinct client API legal review needed | research |
| MAX Bot API | bot updates and configured chat/channel events | bot messages, channel actions where authorized | verified eligible partner + moderated bot, use current base URL and Authorization header; production webhook | planned |
| VK community API | events/messages for managed community with permissions | replies / approved posts | scope and current API/mode must be checked before implementation | research |
| Website widget | voluntary incident report + context | case status / opt-in notifications | site owner permission, bot protection, privacy notice | planned |
| Site topic columns/blocks | topic cards, threat feeds and search views | curated published summaries | editorial/legal review, avoid exposing unverified claims | planned |
| Website notification bell | user-selected subscriptions | in-app or web-push, if browser opt-in supported | permission prompt, opt-out, consent tracking | planned |
| Email inbox | authorised monitored mailbox and inbound reports | approved mail notifications | OAuth/service account, spam/malware filtering, DKIM/DMARC when applicable | research |
| RSS/Atom | permitted public feeds | export approved public feed | licensing, provenance, feed freshness, polling limits | planned |
| Other platforms | per-platform feasibility | only supported legal API methods | explicit adapter review and API status | backlog |

Official references:
- https://core.telegram.org/bots/api — webhook/getUpdates and secret_token
- https://dev.max.ru/docs-api — MAX base URL platform-api2.max.ru, Authorization header, API
- https://dev.max.ru/docs-api/use-cases/bot-in-chats-and-channels — MAX bot in chats/channels
- https://dev.max.ru/docs — partner eligibility and moderation
All platform-specific permissions must be revalidated at implementation time.

## Core/profile rule
Adapters and event normalization → GENERAL OSINT CORE; TRICOLOR content taxonomy and response templates → PROFILE. All generalized improvements follow upstream tests + PR.
