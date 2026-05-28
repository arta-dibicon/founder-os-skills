---
name: founder-os-context-harvest
description: Scrappt public Content des Owners (YouTube/IG/TikTok/Website/Podcast/LinkedIn/Newsletter) und synthetisiert daraus voice_sample.md plus voice_skill_draft.md plus business_synthesis.md. Wird nach Owner-Interview im Hintergrund gestartet, läuft 24-72h.
trigger:
  - "Harvest starten", "Public-Content scannen", "Voice lernen"
---

# founder-os-context-harvest

## Zweck

Damit der COO klingt wie der Owner, braucht er Trainings-Material. Dieser Skill holt sich alles öffentlich Verfügbare und synthetisiert daraus eine Voice-DNA.

## Trigger-Logik

- Manuell durch Owner: "Mach den Harvest"
- Automatisch nach Telegram-Interview: COO pingt the Owner "Owner hat Interview durch, soll ich Harvest starten?" → bei Freigabe → start

## Voraussetzung

`~/workspace/_harvest/sources.json` muss existieren (befüllt in Phase D des Onboardings). Format:

```json
{
  "website": "https://example.com",
  "instagram": "@example",
  "youtube": "https://youtube.com/@example",
  "tiktok": "@example",
  "linkedin": "https://linkedin.com/in/example",
  "podcast": "https://example.podbean.com",
  "newsletter": "https://example.substack.com"
}
```

## Ablauf

### Phase 1: Discovery (1-2h)
1. **Website crawlen** via Firecrawl MCP → speichert alle Seiten als .md in `_harvest/website/`
2. **YouTube-Channel** via yt-dlp → lädt letzte 50 Videos als Audio, transkribiert via Whisper → `_harvest/youtube/`
3. **IG-Posts** via Apify Actor → Captions + Comments → `_harvest/instagram/`
4. **TikTok** via Apify → Caption + Transkripte → `_harvest/tiktok/`
5. **Podcast** via yt-dlp + RSS → letzte 20 Folgen transkribiert → `_harvest/podcast/`
6. **Newsletter** via Firecrawl → letzte 50 Issues → `_harvest/newsletter/`
7. **LinkedIn** via Apify → letzte 100 Posts → `_harvest/linkedin/`

### Phase 2: Synthese (4-6h)

Sub-Agent läuft mit allen Files und produziert:

1. **`_harvest/voice_sample.md`** — 30-50 Textauszüge wo der Owner besonders erkennbar klingt
2. **`_harvest/voice_skill_draft.md`** — Ein neuer Voice-Skill (`<owner-name>-voice`) mit:
   - Tonalität in 5-7 Sätzen
   - 20 Lieblings-Hooks aus dem Material
   - 20 Tabu-Wörter / Floskeln die der Owner nie nutzt
   - 10 wiederkehrende Themen / Reibungspunkte
3. **`_harvest/business_synthesis.md`** — Was öffentlich über das Business kommuniziert wird:
   - Positioning
   - Top-Themen
   - Wiederkehrende Stories
   - Gegner / Tabus
4. **`_harvest/audience_signals.md`** — Was die Audience zurückspielt:
   - Top-Kommentar-Themen
   - Wiederkehrende Fragen
   - Sprache der Audience

## Output an Owner

Nach Abschluss:
1. COO pingt Owner+the Owner im Telegram: "Harvest fertig. Voice-Skill liegt unter `_harvest/voice_skill_draft.md` — Review in Call 2."
2. In Call 2 finalisiert der Owner+the Owner den Voice-Skill, dann wird er via `founderos skill add <owner-name>-voice` installiert.

## Failure-Modes

- **Apify-Rate-Limit:** Retry mit Backoff. Bei dauerhaftem Limit: Owner pingen "Apify-Limit, bitte Plan upgraden oder warten."
- **YouTube-Bot-Check:** Wenn yt-dlp bei VPS-IP geblockt wird → über Owner's lokalen Mac via SSH-Tunnel routen.
- **Newsletter-Login:** Wenn Beehiiv/Substack Login braucht → Owner muss Cookie-Header beisteuern.

## Resource-Budget

- Apify: ~2-5 USD pro Harvest
- OpenAI Whisper: ~3-10 USD pro Harvest (je nach Video-Volumen)
- Firecrawl: ~1 USD pro Harvest
- Total: ~6-16 USD pro Customer Harvest. In Setup-Fee enthalten.
