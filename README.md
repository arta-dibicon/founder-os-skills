# founder-os-skills

Marketplace of skills for **Founder OS** — the Done-with-you "Persönliche Superintelligenz" stack for Founders and Executives.

Each skill is a self-contained module that extends the COO with a specific capability: writing, designing, analyzing, marketing, building.

## Installation

Use the `founderos` CLI on your Founder OS server:

```bash
founderos sync                  # refresh marketplace cache
founderos skills list           # show all available skills
founderos skill add <name>      # install one skill
founderos skills installed      # show what is installed
```

Auto-install skills (universal foundation, installed during bootstrap):

- `human-voice` — Anti-AI-Voice editor
- `chat-indexing` — Chat-session save system
- `workspace-setup` — Workspace hygiene + folder structure
- `transcribe` — Audio → text via Whisper
- `autoresearch` — Web research with source synthesis
- `dream` — Memory consolidation / overnight mode
- `token-efficiency` — Token-cost optimization
- `founder-os-telegram-coo` — Telegram bot for voice-message COO access
- `founder-os-context-harvest` — Public-content scraping for owner voice

## Manifest

`manifest.json` is the source of truth for what is available. Each entry has:

- `name` — folder slug
- `tier` — universal / core / growth_marketing / content_creation / ecommerce / diagnostics / tooling
- `description` — what the skill does and when to use it
- `auto_install` — whether bootstrap installs it without asking

## Skill structure

Each skill folder contains at minimum:

```
<skill-name>/
  SKILL.md           # frontmatter + instructions, loaded by Claude Code
  scripts/           # optional helper scripts
  references/        # optional reference docs
  templates/         # optional templates
```

`SKILL.md` frontmatter format:

```
---
name: <skill-name>
description: <trigger pattern + what it does>
allow_tools: <comma-separated tool list, optional>
---

<skill instructions>
```

## Privacy

Skills are sanitized of personal names, brand-specific references, and hardcoded
workspace paths. Generic placeholders are used (`the Owner`, `the Founder`,
`a partner`, `[brand]`, `[entity]`, `~/workspace/`).

## License

Proprietary. Internal use within Founder OS customer deployments only.
