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

Want to sort or filter? [tools.csv](tools.csv) has every entry in one table;
GitHub shows it with a search box.

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
see [Risks](#risks). The software is free, but something must stay online to
receive messages: your own computer ($0, must stay on) or a small VPS (typically
about $4–6 a month). Your message history stays with you.

| Name | What it is | Reads / sends | Where history is kept | Runs on | License |
|---|---|---|---|---|---|
| [finereli/whatsapp-mcp](https://github.com/finereli/whatsapp-mcp) | Small remote MCP server for searching and reading your chats. | **Read only** | Your Cloudflare account | Your Cloudflare account (Workers Paid plan) | MIT |
| [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) | The original and best-known WhatsApp MCP server: Go bridge plus Python MCP server. No commits since July 2025. | Reads and sends | Your computer | Your computer | MIT |
| [verygoodplugins/whatsapp-mcp](https://github.com/verygoodplugins/whatsapp-mcp) | Maintained continuation of the original, with message search, media tools and optional transcription. | Reads and sends | Your computer | Your computer | MIT |
| [felipeadeildo/whatsapp-mcp](https://github.com/felipeadeildo/whatsapp-mcp) | Cloudflare deployment with searchable storage, multiple accounts and messaging tools. | Reads and sends | Your Cloudflare account | Your Cloudflare account (about $5/month per README) | GPL-3.0 |
| [FelixIsaac/whatsapp-mcp-extended](https://github.com/FelixIsaac/whatsapp-mcp-extended) | Extended fork: group admin, webhooks, polls, recipient allowlist, selectable tool sets. | Reads and sends | Your computer | Your computer, Docker | MIT |
| [BrOrlandi/whatsapp-mcp-local](https://github.com/BrOrlandi/whatsapp-mcp-local) | Desktop app that exposes WhatsApp as a local MCP endpoint (uses wacli). | Reads and sends | Your computer | Your computer (must stay on) | MIT |
| [BrOrlandi/whatsapp-mcp](https://github.com/BrOrlandi/whatsapp-mcp) | Go gateway with a web panel and authenticated remote MCP. | Reads and sends | Your server | Your server | MIT |
| [ericporres/whatsapp-mcp-server](https://github.com/ericporres/whatsapp-mcp-server) | Group-focused server: read, search, export and reply. | Reads and sends (groups) | Your machine, last 1,500 messages per group | Your computer or server | MIT |
| [delltrak/wamcp](https://github.com/delltrak/wamcp) | TypeScript server with two backends: WhatsApp Web or the Business Cloud API. | Reads and sends | Your server | Your server, Docker + Redis | MIT (per README) |
| [WAHA MCP](https://waha.devlike.pro/docs/apps/mcp/) | Self-hosted WhatsApp HTTP API with a built-in MCP app and scoped keys. | Reads and sends | Your server | Your server, Docker | Apache-2.0 |

## Hosted services (personal account)

Someone else runs the connection, so your messages pass through their servers.
Still a linked device unless noted. "Where history is kept" comes from each
service's own privacy policy or docs.

| Name | What it is | Reads / sends | Where history is kept | Runs on | Price |
|---|---|---|---|---|---|
| [wa2agent](https://wa2agent.link) | Hosted MCP for personal agents; you choose which chats it can see. Disclosure: built by this list's maintainer. | **Read only** | Theirs: 30 days, encrypted with a key only your agent holds ([privacy](https://wa2agent.link/privacy)) | Hosted | Invite-only pilot |
| [Blueticks MCP](https://blueticks.co/blog/connect-whatsapp-to-claude-mcp-integration) | Hosted MCP connector for your WhatsApp number. | Reads and sends | Theirs, until you ask for deletion ([policy](https://blueticks.co/privacy-policy)) | Hosted | Paid, from $9/month, trial |
| [Periskope MCP](https://docs.periskope.app/ai/mcp) | Hosted MCP over a shared team inbox, chats and tickets. | Reads and sends | Theirs, while you use it; deleted within 30 days after ([DPA](https://periskope.app/legal/dpa)) | Hosted | Paid, per user |
| [Wassenger MCP](https://app.wassenger.com/help/mcp) | Hosted MCP for chats and messaging; linked device or Business API. | Reads and sends | Theirs, up to 1,000 messages per chat ([FAQ](https://app.wassenger.com/help/category/faq)) | Hosted | Paid, trial |
| [2Chat MCP](https://2chat.co/features/mcp-server) | Hosted MCP for WhatsApp, SMS and calls; linked device or Business API. | Reads and sends | Theirs, while your account is open; deleted within 6 months of closing ([policy](https://2chat.co/legal/privacy-policy)) | Hosted | Paid, trial |
| [Whapi.Cloud MCP](https://whapi.cloud/mcp-whatsapp-api) | Local MCP adapter for Whapi's hosted gateway. | Reads and sends | Theirs: short-lived caches; media 30 days ([help](https://support.whapi.cloud/help-desk/receiving/file-expiration-period)) | Hosted gateway, local adapter | Free sandbox (5 chats/month), then paid |
| [GREEN-API MCP](https://green-api.com/en/docs/integration/mcp/integration-setup/) | Hosted MCP with messaging, notifications and groups. | Reads and sends | Theirs, period not stated ([policy](https://green-api.com/en/privacy-policy)) | Hosted | Free developer plan (3 chats), then paid |

## Business API (official)

Uses Meta's WhatsApp Business Platform. It needs a verified Meta business and
Meta's approval of your use case; reviews can take weeks and can be rejected.
It is built for businesses messaging customers, not for reading your personal
chats. Meta fees apply. Official does not mean Meta endorses a community project.

**The 24-hour window:** a business can only send free-form messages within 24
hours of the customer's last message. After that, only pre-approved templates
go through. This is where agent replies usually break, so the table shows
whether each tool handles it for you.

| Name | What it is | Reads / sends | Handles the 24-hour window? | Where history is kept | Runs on | Price / license |
|---|---|---|---|---|---|---|
| [Meta WhatsApp Business Tools MCP](https://developers.facebook.com/documentation/mcp/whatsapp-business-tools-mcp) | Meta's own MCP for account, number and template setup, plus test sends. Endpoint `https://mcp.facebook.com/whatsapp_business_tools`. | Test sends; reading not verified | Not verified | Not a chat store | Meta | Not verified |
| [Kapso MCP](https://docs.kapso.ai/docs/whatsapp/mcp) | Hosted MCP: send, read stored conversations, manage templates and webhooks. | Reads and sends (read-only by default) | Not documented for MCP; the inbox flags failed sends | Theirs, period not stated | Hosted | Free tier: 2,000 messages/month, one number |
| [SendFromChat](https://sendfromchat.com/docs) | Hosted Cloud API platform with remote MCP (Claude, ChatGPT, Claude Code, Cursor and others) and a REST API. | Reads and sends | Yes: checks the window and blocks free-form sends when closed; the assistant picks a template ([docs](https://sendfromchat.com/guides/whatsapp-cloud-api-error-codes)) | Theirs, while your account is active; deleted within 30 days of workspace deletion ([privacy](https://sendfromchat.com/privacy)) | Hosted | 30-day trial, then from $19/month plus Meta fees |
| [FredShred7/whatsapp-mcp-server](https://github.com/FredShred7/whatsapp-mcp-server) | Community Cloud API wrapper for messages, media and templates. Receiving needs webhooks. | Reads and sends | Not documented | In memory only, while it runs | Your computer or server | MIT |

## Automation platforms

Business Cloud API unless noted. None of these documents automatic handling of
the [24-hour window](#business-api-official): n8n and Zapier leave the choice of
template to you, and a Zapier send outside the window can fail while the Zap
still shows success.

| Name | What it is | Reads / sends | Where history is kept | Runs on | Price / license |
|---|---|---|---|---|---|
| [n8n](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/) | WhatsApp Business Cloud node and trigger; workflows can be exposed through n8n's MCP Server Trigger. | Reads and sends | Wherever your workflow saves it | Self-hosted or n8n Cloud | Free community edition; Cloud is paid |
| [Zapier](https://zapier.com/mcp/whatsapp-business) | WhatsApp Business workflows; MCP actions for sending. | Mostly sends; incoming via triggers | Zapier task history | Hosted | Paid plan for this integration |
| [OpenClaw](https://docs.openclaw.ai/channels/whatsapp) | Agent gateway with a native WhatsApp channel that routes messages to your agent and sends replies. Linked device. | Reads and sends | Your gateway | Self-hosted | MIT |

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
