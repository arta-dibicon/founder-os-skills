---
name: carousel-dark-metallic-lab
description: Rendert Carousels im Dark-Metallic-Lab-Stil — Schwarz-Grunge-BG, Gold-Gradient Hero-Term (Oswald), Frosted-Glass-Cards, roter WICHTIG-Footer. Perfekt für Peptide/Supplements/Team-[brand]-Deep-Dives.
---

# Carousel: Dark Metallic Lab

Style 02 — Peptid/Lab-Vibe. Referenz: Team-[brand] TB500 Post.

## Input-Schema

```json
{
  "style": "dark-metallic-lab",
  "aspect": "1:1",
  "slides": [
    {
      "type": "hero",
      "gold_term": "TB500",
      "white_term": "DEEP DIVE",
      "subtitle": "DER HEILENDE PEPTID-GEHEIMTIPP?",
      "brand": "TEAM MADSEN"
    },
    {
      "type": "content",
      "title": "HINWEIS / DISCLAIMER",
      "subtitle": "18+ · HARM REDUCTION & BILDUNG",
      "cards": [
        {"title": "KEIN VERKAUF", "body": "…"},
        {"title": "KEINE VERHERRLICHUNG", "body": "…"}
      ],
      "footer_card": {"title": "WICHTIG", "body": "…"},
      "brand": "TEAM MADSEN"
    }
  ]
}
```

## Slide-Typen

| `type` | Inhalt |
|---|---|
| `hero` | `gold_term` (groß) + `white_term` + `subtitle` |
| `content` | `title` + optional `subtitle` + `cards[]` + optional `footer_card` |

## Regeln

- **Gold-Term:** Das Peptid/der Begriff selbst (TB500, BPC-157, Retatrutid). UPPERCASE wird automatisch forciert
- **Subtitle:** Letter-spaced + Caps, beschreibt Kontext
- **Cards:** 2-4 pro Slide, Gold-Titel + Grau-Body
- **Footer-Card:** Immer rot ("WICHTIG" / "DISCLAIMER" / "CAVEAT")
- **Brand:** Bottom-center, Gold-Wordmark (Default: "TEAM MADSEN")

## Workflow

1. Frag: Topic? Hero-Term? Disclaimer nötig?
2. Input → `_runs/<projekt>/<timestamp>/input.json`
3. `python3 render.py --style dark-metallic-lab --input … --out …`
4. Visual check

## Use-Cases
- Peptid/Supplement Deep-Dives ([brand], [brand], [brand])
- Tech-Reviews, Scientific Breakdowns
- Compliance-Posts (Disclaimer, Harm-Reduction)
