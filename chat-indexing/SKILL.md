---
name: chat-indexing
description: Speichert Chat-Sessions strukturiert mit Conversation-Starter. Trigger durch Owner via "Indexier den Chat" oder "Chat speichern".
trigger:
  - "Indexier den Chat", "Indexier", "Chat speichern"
  - "Wo waren wir?", "Letzten Chat fortsetzen"
---

# chat-indexing

## Zweck

Lange Chats verlieren sich. Dieser Skill speichert pro Chat:
- Was gemacht wurde (Bullets)
- Wo wir gerade stehen
- Offene Punkte
- Conversation-Starter für den nächsten Chat
- Link zum vollen Transcript

## Wann triggern

Owner sagt eine der Trigger-Phrasen, oder du erkennst dass der Chat lang wird (>20 Nachrichten) und ein Wechsel sinnvoll wäre.

## Was machen

1. **Session-ID ermitteln:** Neueste JSONL in `~/.claude/projects/<workspace-encoded>/`
2. **Per-Chat-File erstellen:** `infrastruktur/chats/YYYY-MM-DD_<slug>.md` mit Struktur:

```markdown
# Chat: <kurzer Titel>
Datum: YYYY-MM-DD
Venture: <z.B. [brand] oder cross-venture>
Status: in-progress | done | archived

## Was wir gemacht haben
- [Bullet 1]
- [Bullet 2]

## Wo wir stehen
[1-2 Sätze]

## Offene Punkte
- [Bullet]

## Wie weitermachen
**Conversation-Starter:**
> [Den Prompt den Owner im nächsten Chat sagen soll]

**Resume-Befehl:**
```bash
claude --resume <session-id>
```

**Transcript:**
infrastruktur/chats/transcripts/YYYY-MM-DD_<slug>.jsonl
```

3. **INDEX.md updaten:** Neue Zeile oben einfügen
   - Spalten: `Datum | Chat | Was gemacht | Venture | Status | Aktion`
   - "Was gemacht" = 1 Satz, max 120 Zeichen

4. **Transcript-Symlink:** `infrastruktur/chats/transcripts/YYYY-MM-DD_<slug>.jsonl` → originale JSONL

## Status-Updates

Owner kann jederzeit sagen:
- "Chat X auf done setzen" → Status-Spalte in INDEX.md ändern
- "Chat X archivieren" → Status auf `archived`
- "Welche Chats sind noch offen?" → INDEX.md parsen, offene auflisten

## Wichtig

- **Triggert NICHT die Memory-Extraction** — die läuft separat über Hooks falls aktiv
- **Owner entscheidet wann indexiert wird** — nie automatisch, immer auf Befehl
- **Slugs kurz und sprechend:** `takori-launch-plan`, nicht `chat-mit-owner-über-takori`

## Cockpit-Zugang

- Desktop-Symlink: `~/Desktop/Chat-Cockpit.md` → `infrastruktur/chats/INDEX.md`
- Oder direkt: `open ~/workspace/infrastruktur/chats/INDEX.md`
