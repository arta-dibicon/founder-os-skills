---
name: founder-os-telegram-coo
description: Telegram-Bot der den COO über Sprachnachrichten erreichbar macht. Empfängt Voice, transkribiert via Whisper, antwortet via Claude. Wird im Setup-Tag in Phase C live deployed.
trigger:
  - "Bot setup", "Telegram einrichten", "deploy bot"
  - "Interview-Modus starten", "Block 1 starten"
---

# founder-os-telegram-coo

## Zweck
Der COO ist auch außerhalb von Antigravity erreichbar. Owner sendet Sprachnachricht oder Text an den Telegram-Bot, COO transkribiert, denkt, antwortet zurück. Das große Owner-Interview läuft asynchron über diesen Bot.

## Deployment-Trigger

Wenn im Setup-Tag Phase C der Owner seinen Token paste-d, lädt der COO diesen Skill und führt aus:

```bash
TELEGRAM_BOT_TOKEN=<token> bash ~/workspace/.claude/skills/founder-os-telegram-coo/setup.sh
```

Das Setup-Script:
1. Schreibt `.env.telegram` mit Token + Anthropic-Key + OpenAI-Key
2. Installiert Python-Deps (aiogram, openai-whisper, anthropic) falls fehlend
3. Erzeugt systemd-Unit `founderos-telegram-bot.service`
4. Startet Service und prüft Health über `journalctl`
5. Gibt Bot-Username zurück zum Bestätigen

## Bot-Modi

Der Bot hat zwei Modi, gesteuert durch `~/.founderos-bot-mode`:

- **`chat`** (default) — Normaler COO-Modus. Owner schreibt/spricht, COO antwortet wie in Antigravity.
- **`interview`** — Strukturiertes 6-Block-Interview (Person, Arbeitsstil, Werte, Ventures, Tools, Brennpunkte). Bot stellt eine Frage nach der anderen, wartet auf Voice-Antwort, transkribiert, speichert in `~/workspace/.claude/rules/owner-profile.md`, wechselt zur nächsten Frage.

Mode-Switch via Commands:
- `/interview` — startet Interview-Modus
- `/chat` — zurück zu Chat-Modus
- `/status` — zeigt wo im Interview wir sind
- `/pause` — pausiert Interview (kann später fortgesetzt werden)
- `/resume` — Interview da fortsetzen wo gestoppt

## Voice-Handling

1. Voice-Message empfangen → speichern als `.ogg` in `/tmp/founderos-voice/`
2. Transkribieren via OpenAI Whisper (`whisper-1` API)
3. Transkript an Claude weitergeben mit System-Prompt aus `coo-identity.md`
4. Antwort als Text senden (default) oder als Voice (wenn Owner via `/voice-reply on` aktiviert)

## Sicherheit

- Bot nur für Owner. `ALLOWED_USER_ID` ist die Telegram-User-ID des Owners, wird beim ersten `/start` gespeichert.
- Andere Telegram-Nutzer kriegen "Sorry, dieser Bot ist privat." und werden geloggt.
- API-Keys in `.env.telegram` mit `chmod 600`.

## Files

- `setup.sh` — Installer-Script, wird vom COO ausgeführt
- `bot/main.py` — Bot-Main-Loop mit aiogram
- `bot/interview.py` — Interview-Modus-State-Machine
- `bot/whisper.py` — Voice-zu-Text-Wrapper
- `bot/claude.py` — Claude-API-Wrapper mit Context-Loading
- `bot/founderos-telegram-bot.service` — systemd-Unit-Template

## Erst-Start-Verhalten

Wenn Owner zum allerersten Mal `/start` drückt:
1. Bot fragt: "Hi, ich bin dein neuer COO im Telegram. Bist du der Owner?"
2. Owner antwortet (Voice oder Text "ja")
3. Bot speichert `chat_id` als `ALLOWED_USER_ID`
4. Bot sendet: "Cool. Ich bin ab jetzt für dich erreichbar. Sprich mit mir wie mit einem Kollegen. Sprachnachricht geht auch. Wenn du bereit fürs Interview bist, schreib /interview."
5. COO meldet in Antigravity an Owner+the Owner: "Telegram-Connect ist durch."
