---
name: carousel-hand-held-card
description: Rendert Quote-Carousels im atmosphärischen "Late-Night-Desk"-Stil — AI-generiertes warmes Bokeh-Zimmer, Index-Card mit Sharpie-Handschrift, rotem Squiggle-Underline und Flourish-Signoff. Für Quote-Posts, personal-branding, intime Wisdom-Content.
---

# Carousel: Hand-Held Card

Style 05 — Quote-Carousel. Referenz: IG DUpNv8xAFkq.

## Input-Schema

```json
{
  "style": "hand-held-card",
  "aspect": "4:5",
  "slides": [
    {
      "bg_prompt": "Atmospheric close-up photo of a warm dim-lit room at night, amber tungsten lamp glow, framed art in bokeh background, f/1.8 shallow depth, warm tungsten white balance, no people, cinematic mood",
      "rotation": -3.5,
      "lines": [
        "YOU DON'T NEED",
        {"text": "PERMISSION", "underline": true},
        "TO START.",
        "ONLY A DECISION."
      ],
      "signoff": true
    }
  ]
}
```

## Line-Format

- String: Normal-line
- Objekt `{"text": "…", "underline": true}`: Rote Squiggle-Underline drunter (Sharpie-Look)

## Slide-Properties

| Key | Default | Zweck |
|---|---|---|
| `bg_prompt` | required | AI-BG-Prompt (Warm-Bokeh-Szene) |
| `rotation` | -3.5 | Card-Tilt in Grad (zwischen -5° und +5° für Variety) |
| `card_scale` | 1.0 | Größe (0.9 für kleinere Cards, 1.1 für größer) |
| `lines[]` | required | 3-6 Zeilen Quote (all-caps wird auto erzwungen) |
| `signoff` | true | S-Squiggle unten-rechts der Karte |

## BG-Prompt-Patterns

- "Atmospheric warm bokeh photo of a dim-lit [room-type]"
- Pro Slide leichte Variation (gleiche Location, andere Winkel) für Cohesion
- Key-Phrases: "amber tungsten lamp glow", "f/1.8 shallow depth", "warm tungsten white balance", "no people", "cinematic mood"

## Regeln

- **3-6 Zeilen** pro Card (sonst Overflow)
- **1-2 Underlines** pro Card (nicht mehr, sonst optisch laut)
- **Rotation alternieren** zwischen Slides (-3.5°, +2.5°, -1.5°, …)
- **Signoff** auf jeder Slide = Brand-Marker

## Workflow

1. Frag: Topic? Anzahl Quotes? Room-Type (cozy-apartment / library / cabin / coffee-shop)?
2. Baue Quote-Array mit Underlines auf "power-words"
3. Input → `_runs/<projekt>/<timestamp>/input.json`
4. `python3 render.py --style hand-held-card --input … --out …`
5. Visual check — bei schwachem Kontrast: `card_scale` hoch oder BG-Prompt dunkler

## Use-Cases
- Reality-Shift Coaching-Quotes
- Personal-Brand-Wisdom-Posts
- Book-Club-Quote-Series
- Daily-Affirmations
