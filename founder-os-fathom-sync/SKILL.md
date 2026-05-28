---
name: founder-os-fathom-sync
description: Holt on-demand Meeting-Transkripte + Summaries aus Fathom. Speichert sauber im Workspace und extrahiert Action-Items. Pull-Modell, kein Cron.
trigger:
  - "Fathom-Meeting holen", "Letztes Call-Transkript", "Meeting X synchronisieren"
  - "Was haben wir gestern mit X besprochen?"
---

# founder-os-fathom-sync

## Zweck

Owner-Calls landen in Fathom. Damit der COO daraus arbeiten kann, holt der Skill on-demand:
- Volltext-Transkript
- AI-Summary
- Action-Items (extrahiert per Claude)

Bewusst kein Cron / Auto-Sync. Sonst landen Calls die nichts mit dem Workspace zu tun haben im System.

## Trigger

Owner sagt eine der Phrasen. Wenn unklar welches Meeting:
1. `list_meetings` → letzte 10 zeigen
2. Owner pickt eines (per Index oder Titel)
3. Skill zieht Detail

## Output-Struktur

```
~/workspace/[venture]/_meetings/YYYY-MM-DD_<slug>/
├── transcript.md       → Volltext mit Timestamps
├── summary.md          → Fathom-AI-Summary
├── action_items.md     → Von Claude extrahiert: bullet pro Action mit Owner+Due-Date
└── original.json       → API-Response für Audit
```

## Action-Item-Extraktion

Nach Transcript-Pull läuft Claude mit folgendem Prompt:

```
Aus dem Transkript: extrahiere alle Action-Items.
Pro Item:
- Wer (Name oder Rolle)
- Was (konkret, nicht abstrakt)
- Bis wann (wenn genannt)

Format als Bullet-Liste in action_items.md. Keine Floskeln, kein Em-Dash.
```

## Venture-Routing

Beim ersten Mal fragt der Skill den Owner: "Zu welchem Venture gehört dieser Call?" und speichert das Mapping in `~/.founderos-fathom-mapping.json`. Beim nächsten Call mit gleichem Teilnehmer-Set wird automatisch geroutet.

## Voraussetzung

- Fathom-MCP konfiguriert (`mcp__fathom__*` Tools verfügbar)
- Owner hat Fathom-Account verbunden im Setup
