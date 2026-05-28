---
name: carousel-news-breaking-dark
description: Rendert Carousels im Breaking-News-Stil — Dunkler Grunge-BG, Bebas Neue Headlines, rote "BREAKING NEWS"-Blocks, gelb-gold Keywords. Für Opinion-Pieces, Platform-Updates, Hot-Takes.
---

# Carousel: News Breaking Dark

Style 06 — News/Opinion-Vibe. Referenz: IG DVeC-FgjOUh.

## Input-Schema

```json
{
  "style": "news-breaking-dark",
  "aspect": "1:1",
  "slides": [
    {
      "headline": [
        {"parts": [{"text": "BREAKING NEWS:", "style": "red-block"}]},
        {"parts": [{"text": "NEUES INSTAGRAM FEATURE"}]},
        {"parts": [{"text": "„SECRET FRIENDS\"", "style": "yellow"}]}
      ],
      "logo": true
    },
    {
      "body": [
        {"parts": [{"text": "STORIES WIRKEN"}, {"text": "EXKLUSIV UND PRIVAT.", "style": "red-block"}]},
        {"parts": [{"text": "AUCH WENN"}, {"text": "MILLIONEN MENSCHEN SIE SEHEN.", "style": "red-block"}]}
      ],
      "logo": true
    },
    {
      "headline": [{"parts": [{"text": "WAS DENKST DU DARÜBER?"}]}],
      "body": [{"parts": [{"text": "SCHREIB ES UNS IN DIE KOMMENTARE", "style": "red-block"}]}],
      "logo": true
    }
  ]
}
```

## Part-Styles

- `red-block` — Weißer Text auf rotem Block (Haupt-Highlight)
- `yellow` — Goldgelber Text (Sekundär-Keyword)
- `white-bold` — Weiß Bold (Default wenn kein style)

## Regeln

- **Headlines:** Meist 2-3 Zeilen, Caps, Bebas Neue
- **Body:** Fließtext Caps, mit Red-Block-Highlights für Key-Phrases
- **Logo:** Feather/Wings-Icon Bottom-Right
- **Keine Swipe-Pfeile** — News-Style soll "serious" wirken

## Use-Cases
- Platform-Updates (Meta, IG, YT Changes)
- Hot-Takes / Opinion-Pieces
- Breaking-Content für Team-[brand]-Creator-Channel
- "Was denkst du darüber?"-CTAs zum Engagement-Boost
