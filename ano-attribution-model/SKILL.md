---
name: ano-attribution-model
description: Use wenn Channel-Attribution gebraucht wird (welcher Touchpoint hat wieviel beigetragen). Default Last-Touch plus Self-Report-Survey-Boost ("Wo hast du uns gefunden?"). Markov-Chain-Attribution NUR für Projekte mit >500 Conversions/Monat (innerhalb Phase 3). Output Channel-Contribution-Share plus CAC-pro-Channel plus Recommendation (Budget-Shift). Nutzt UTM-Tags plus Self-Report-Daten plus Pixel/CAPI-Events. Nicht für kleine N (<100 Conv/Monat) — würde Garbage liefern.
metadata:
  status: STUB
  phase: 3
  build_priority: low
  estimated_effort_days: 5
---

# Ano · Attribution Model (STUB)

**Status:** Noch nicht implementiert. Phase-3-Build.

## Was dieser Skill machen wird

Multi-Touch-Attribution für Projekte mit ausreichender Datendichte. Drei Modelle, gestaffelt nach Conversion-Volumen.

## Modell-Hierarchie

| Modell | Min-Conv/Monat | Eignung |
|---|---|---|
| Last-Touch + Self-Report | 50+ | Default für alle Projekte |
| Position-Based (40/20/40) | 200+ | Wenn Customer-Journey >3 Touches |
| Markov-Chain | 500+ | Phase 3, nur [brand] absehbar |

## Datenquellen

- UTM-Tags aus Klick-Logs (Bitly, Pixel, GA4)
- Pixel/CAPI-Events (Meta, TikTok)
- Self-Report-Survey-Antworten ("Wo hast du uns gefunden?" am Checkout)
- Email-Click-Logs (Klaviyo/Brevo)

## Self-Report-Boost

Self-Report-Antworten überschreiben Last-Touch wenn klar (z.B. Kunde sagt "Empfehlung von Freund" aber Last-Touch war Meta-Ad). Confidence-Gewichtung. Verhindert Over-Attribution auf Performance-Channels.

## Output-Schema

```json
{
  "project": "within-supplements",
  "data_window": "2026-04-10 to 2026-05-10",
  "total_conversions": 247,
  "model_used": "last_touch_plus_self_report",
  "channels": [
    {"name": "meta_ads", "share": 0.42, "cac": 38.50, "conv": 104},
    {"name": "email_organic", "share": 0.28, "cac": 8.20, "conv": 69},
    {"name": "affiliate", "share": 0.18, "cac": 22.10, "conv": 44},
    {"name": "organic_ig", "share": 0.12, "cac": 0, "conv": 30}
  ],
  "recommendation": "Email-Kanal unterausgelastet, CAC 4x niedriger als Meta — Budget für Email-Acquisition prüfen"
}
```

## Was wir NICHT machen

- Attribution für Projekte unter 50 Conv/Monat (Noise > Signal)
- Shapley-Value-Attribution (zu komplex, marginal besser als Markov)
- View-Through-Attribution (zu viele False-Positives ohne Cross-Device-ID)

## Stub-Output

```json
{"skill": "ano-attribution-model", "status": "stub", "message": "Attribution-Modell noch nicht gebaut. Phase-3, 5 Tage. Vorher Pixel/CAPI plus Self-Report-Survey aufsetzen."}
```
