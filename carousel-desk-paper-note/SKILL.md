---
name: carousel-desk-paper-note
description: Rendert Carousels im Gannon-Meyer-Flatlay-Style — AI-generiertes grünes Cutting-Mat mit Props, Paper-Notes mit Sharpie-Handschrift, 4:5-Format. Für Tutorial-Content, Indie-Vibe, Hand-made-Feeling.
---

# Carousel: Desk Paper Note

Style 04 — Tactile Flatlay. Referenz: @gannon.meyer IG DVJbKCAALAm.

## Input-Schema

```json
{
  "style": "desk-paper-note",
  "aspect": "4:5",
  "slides": [
    {
      "type": "title",
      "bg_prompt": "Overhead flatlay green self-healing cutting mat with grid lines, eucalyptus leaves top-left, Sharpie marker top-right, Rubik's cube bottom-right, photorealistic, Gannon Meyer aesthetic",
      "headline": "3 CONTENT RULES",
      "handle": "gannon.meyer"
    },
    {
      "type": "content",
      "bg_prompt": "Green cutting mat flatlay, props at corners (succulent, pencil, ruler), empty center, photorealistic",
      "cards": [
        {"title": "RULE 01", "body": "Write the title FIRST. If you can't sell it in 5 words, the idea isn't sharp enough."}
      ],
      "handle": "gannon.meyer"
    },
    {
      "type": "cta",
      "bg_prompt": "Green cutting mat, bookmark icon sketched bottom-right, eucalyptus top-left, mostly empty",
      "cta_text": "save for later",
      "handle": "gannon.meyer"
    }
  ]
}
```

## Slide-Typen

| `type` | Inhalt |
|---|---|
| `title` | Torn-Paper-Strips mit `headline` (Sharpie-Big) |
| `content` | 1-2 `cards[]` mit `title` + `body` |
| `cta` | Big Sharpie-`cta_text` auf leerem Mat |

## Cards

```json
{"title": "RULE 01", "body": "...", "rotation": -1.5, "width": 80}
```

- `rotation` (deg): Subtiler Tilt — Default alterniert -0.75°/+0.75°
- `width` (%): Card-Breite vom Slide — Default 78

## BG-Prompts

- IMMER "photorealistic" + "Gannon Meyer aesthetic" + "green self-healing cutting mat with grid lines" einfügen
- Props variieren pro Slide für Variety (Eukalyptus, Sharpie, Rubik, Succulent, Pencil, Ruler, Eraser)
- Mat-Center muss **LEER** sein, sonst überlagert die Paper-Card mit Props

## Workflow

1. Frag: Topic? Anzahl Regeln/Steps? Handle?
2. Generiere pro Slide einen variierenden BG-Prompt (unterschiedliche Props)
3. Input → `_runs/<projekt>/<timestamp>/input.json`
4. `python3 render.py --style desk-paper-note --input … --out …`
5. AI-BG-Generation: ~5-10s/Slide (gecacht)

## Use-Cases
- Content-Creator-Tutorials (DIY-Vibe)
- Tipp-Carousels für [brand] (Baking-Rules, Foodie-Aesthetic)
- Reality-Shift "Wisdom"-Posts im Analog-Look
- Anti-Corporate, Indie-Feeling
