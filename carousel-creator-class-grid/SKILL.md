---
name: carousel-creator-class-grid
description: Rendert Carousels im OACE-Style — Dunkelgrau Pixel-Grid, Inter Bold, Pink-Peach-Gradient-Keywords, rote hand-gezeichnete Kreise, Card-Mockups. Für Creator-Content-Tipps, Hook-Templates, Skripting-Regeln.
---

# Carousel: Creator Class Grid

Style 07 — OACE / Creator-Class-Style. Referenz: IG DXKEWlJjOlK.

## Input-Schema

```json
{
  "style": "creator-class-grid",
  "aspect": "1:1",
  "slides": [
    {
      "headline": [
        {"parts": [
          {"text": "3"},
          {"text": "STORYTELLING", "gradient": "pink-peach"},
          {"text": "REGELN"}
        ]}
      ],
      "sub": "die deine Videos sofort besser machen",
      "cards": [
        {"label": "Analyse", "value": "335.892"},
        {"label": "Analyse", "value": "56 Mio.", "circled": true}
      ],
      "arrow": true
    },
    {
      "headline": [{"parts": [{"text": "ABER & DESHALB"}]}],
      "sub": "die South Park Regel",
      "body": [
        {"parts": [
          {"text": "wenn zwischen deinen Sätzen nur"},
          {"text": "\"und dann\"", "style": "pink"},
          {"text": "steht — wird es"},
          {"text": "langweilig.", "style": "bold"}
        ]}
      ]
    },
    {
      "headline": [{"parts": [{"text": "FOLLOW FÜR MEHR", "gradient": "pink-peach"}]}],
      "sub": "creator class · weekly tips",
      "swipe": false
    }
  ]
}
```

## Gradients

- `pink-peach` — `#FF99E0 → #FFD97D` (Hauptkeyword-Hervorhebung)
- `cyan-blue` — `#6EC6FF → #3D5AFE` (alternativ)

## Body-Styles (Part-Level)

- `bold` — Extra-fett, weiß
- `pink` — Pink (wie Gradient-Start), für Zitate/Keywords

## Cards

- `circled: true` → roter hand-gezeichneter Kreis um den Wert
- `arrow: true` (im Slide) → Pfeil-Kreis zwischen Cards

## Workflow

1. Frag: Topic? Hook-Pattern (3 Regeln / 5 Hacks / X Fehler)? Card-Daten?
2. Input → `_runs/<projekt>/<timestamp>/input.json`
3. `python3 render.py --style creator-class-grid --input … --out …`

## Use-Cases
- Content-Creator-Tipps
- Storytelling-Regeln
- Hook-Libraries, Script-Patterns
- Output-Ratios / Creator-Stats
