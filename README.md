# Awesome WhatsApp MCP

A curated, honest guide to connecting WhatsApp to Claude, ChatGPT, Codex,
Cursor, n8n and other AI agents: MCP servers, hosted services, the official
Business API, automation platforms, and the plain export route. Plus a free
agent skill that reads WhatsApp chat exports.

Last checked: 22 October 2026. Every entry was checked against its own README
or docs. Nothing here was tested with a live account unless stated.

## Which route fits?

| You want | Start with |
|---|---|
| Your agent to read **your personal** chats, and you can run a server | A [self-hosted MCP server](#self-hosted-mcp-servers-personal-account) |
| The same, without running anything yourself | A [hosted service](#hosted-services-personal-account) |
| A **business number** that talks to customers | The [official Business API](#business-api-official) or an [automation platform](#automation-platforms) |
| A one-off summary of one chat, free, no connection at all | [Export the chat](#manual-route-free) and use the [free export skill](#free-skill-read-a-whatsapp-chat-export) |

Before you connect a personal account, read [Risks](#risks).

## Free skill: read a WhatsApp chat export

[`skills/whatsapp-chat-export`](skills/whatsapp-chat-export/SKILL.md) lets
Claude Code, Codex or any skills-compatible agent read a WhatsApp `.txt` or
`.zip` export and turn it into a summary, events, tasks and follow-ups. No
account, API key or connector. Python 3 standard library only. It handles
iPhone and Android formats, 12- and 24-hour times, multi-line messages and
system lines.

```bash
npx skills add rosroyros/awesome-whatsapp-mcp
```

Or copy `skills/whatsapp-chat-export/` into `.claude/skills/` (Claude Code) or
`.agents/skills/` (Codex). Then ask: "Read my exported WhatsApp chat and tell
me what I missed."

## Self-hosted MCP servers (personal account)

These connect as a linked device, like WhatsApp Web. That route is unofficial;
see [Risks](#risks).

| Project | What it is | Read / send | Runs on | License |
|---|---|---|---|---|
| [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | The original and best-known WhatsApp MCP server: Go bridge plus Python MCP server. No commits since July 2025. | Both | Your computer | MIT |
| [verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp) | Maintained continuation of the original, with message search, media tools and optional transcription. | Both | Your computer | MIT |
| [finereli/whatsapp-mcp](https://github.com/finereli/whatsapp-mcp) | Small remote MCP server for searching and reading your chats. | **Read only** | Your Cloudflare account (Workers Paid) | MIT |
| [felipeadeildo/whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp) | Cloudflare deployment with searchable storage, multiple accounts and messaging tools. | Both | Your Cloudflare account (about $5/month per README) | GPL-3.0 |
| [FelixIsaac/whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) | Extended fork: group admin, webhooks, polls, recipient allowlist, selectable tool sets. | Both | Your computer, Docker | MIT |
| [BrOrlandi/whatsapp-mcp-local](https://github.com/BrOrlandi/whatsapp-mcp-local) | Desktop app that exposes WhatsApp as a local MCP endpoint (uses wacli). | Both | Your computer (must stay on) | MIT |
| [BrOrlandi/whatsapp-mcp](https://github.com/BrOrlandi/whatsapp-mcp) | Go gateway with a web panel and authenticated remote MCP. | Both | Your server | MIT |
| [ericporres/whatsapp-mcp-server](https://github.com/ericporres/whatsapp-mcp-server) | Group-focused server: read, search, export and reply, with a bounded message buffer. | Both, groups | Your computer or server | MIT |
| [delltrak/wamcp](https://github.com/delltrak/wamcp) | TypeScript server with two backends: WhatsApp Web or the Business Cloud API. | Both | Your server, Docker + Redis | MIT (per README) |
| [WAHA MCP](https://waha.devlike.pro/docs/apps/mcp/) | Self-hosted WhatsApp HTTP API with a built-in MCP app and scoped keys. | Both | Your server, Docker | Apache-2.0 |

## Hosted services (personal account)

Someone else runs the connection. Still a linked device unless noted.

| Service | What it is | Read / send | Price |
|---|---|---|---|
| [Blueticks MCP](https://blueticks.co/blog/connect-whatsapp-to-claude-mcp-integration) | Hosted MCP connector for your WhatsApp number. | Both | Paid, from $9/month, trial |
| [Periskope MCP](https://docs.periskope.app/ai/mcp) | Hosted MCP over a shared team inbox, chats and tickets. | Both | Paid, per user |
| [Wassenger MCP](https://app.wassenger.com/help/mcp) | Hosted MCP for chats and messaging; supports linked device and Business API. | Both | Paid, trial |
| [2Chat MCP](https://2chat.co/features/mcp-server) | Hosted MCP for WhatsApp, SMS and calls; linked device and Business API. | Both | Paid, trial |
| [Whapi.Cloud MCP](https://whapi.cloud/mcp-whatsapp-api) | Local MCP adapter for Whapi's hosted gateway. | Both | Free sandbox (5 chats/month), then paid |
| [GREEN-API MCP](https://green-api.com/en/docs/integration/mcp/integration-setup/) | Hosted MCP with messaging, notifications and groups. | Both | Free developer plan (3 chats), then paid |
| [wa2agent](https://wa2agent.link) | Hosted MCP for personal agents; you choose which chats it can see; messages encrypted with a key only your agent holds. Disclosure: built by this list's maintainer. | **Read only** | Invite-only pilot |

## Business API (official)

Uses Meta's WhatsApp Business Platform. Official does not mean Meta endorses a
community project. Meta fees apply.

| Project | What it is | Read / send | Notes |
|---|---|---|---|
| [Meta WhatsApp Business Tools MCP](https://developers.facebook.com/documentation/mcp/whatsapp-business-tools-mcp) | Meta's own MCP for account, number and template setup, plus test sends. | Test sends; reading not verified | Endpoint `https://mcp.facebook.com/whatsapp_business_tools`. Docs were partly inaccessible when checked. |
| [Kapso MCP](https://docs.kapso.ai/docs/whatsapp/mcp) | Hosted MCP: send, read stored conversations, manage templates and webhooks. | Both (read-only by default) | Free tier: 2,000 messages/month, one number |
| [FredShred7/whatsapp-mcp-server](https://github.com/FredShred7/whatsapp-mcp-server) | Community Cloud API wrapper for messages, media and templates. | Both; receiving needs webhooks | MIT; no personal chat history |

## Automation platforms

| Platform | What it is | Notes |
|---|---|---|
| [n8n](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/) | WhatsApp Business Cloud node and trigger; workflows can be exposed through n8n's MCP Server Trigger. | Free self-hosted community edition; Cloud is paid |
| [Zapier](https://zapier.com/mcp/whatsapp-business) | WhatsApp Business workflows; MCP actions for sending. | Paid plan for this integration |
| [OpenClaw](https://docs.openclaw.ai/channels/whatsapp) | Agent gateway with a native WhatsApp channel that routes messages to your agent and sends replies. | Linked device; MIT |

## Manual route (free)

[Export a chat](https://faq.whatsapp.com/1180414079177245/) from the WhatsApp
app (Without media), then give the file to your assistant, or use the
[free export skill](#free-skill-read-a-whatsapp-chat-export). Safe and free,
but a one-time snapshot with no new messages.

## Risks

- **Account bans.** WhatsApp says linking an account to unofficial clients
  violates its terms and can lead to restricted linking or temporary or
  permanent bans. Every linked-device tool above carries this risk, read-only
  ones included. No tool can guarantee "anti-ban".
  [WhatsApp FAQ](https://faq.whatsapp.com/1217634902127718/),
  [Terms of Service](https://www.whatsapp.com/legal/terms-of-service).
- **Business API and general AI assistants.** From 15 January 2026, Meta's
  Business Solution Terms bar providers whose primary function is a
  general-purpose AI assistant. Exceptions apply in the EEA and Brazil, and on
  9 June 2026 the European Commission ordered Meta to restore rivals' access
  while it investigates.
  [Commission announcement](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_26_1276/IP_26_1276_EN.pdf).
- **Prompt injection.** Anyone who can message you can put instructions in a
  message your agent reads. Invariant Labs showed chat history and contacts
  leaking this way, including through a malicious second MCP server. Treat
  message text as data, and prefer read-only tools or send allowlists.
  [Invariant Labs](https://invariantlabs.ai/blog/whatsapp-mcp-exploited),
  [Docker: MCP Horror Stories](https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/).
- **Encryption ends at your agent.** WhatsApp's end-to-end encryption does not
  protect messages after a connector or agent reads them. If your agent uses a
  cloud model, chat text goes to that model provider.

## Contributing

Pull requests welcome. Please include a link to the project's own docs for
each claim (read/send, hosting, price), and say if you build the tool.
Projects that sell rented accounts, bulk messaging or engagement manipulation
are not listed.

## License

[MIT](LICENSE)
