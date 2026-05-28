---
name: carousel-cinematic-wisdom
description: Rendert Carousels im "Book of Wisdom"-Stil — AI-generierte cinematische BGs (Tempel/Göttinnen/Ancient-Vibes), Gold-Zahl Cinzel, Serif-Titel, Magenta-CTA-Banner. 1 Hero-Slide oder IG-Listicle.
---

# Carousel: Cinematic Wisdom

Style 01 — Lore/Ancient-Knowledge-Feeling. Referenz: @bookofwisdom3 YT Community Posts.

## Input-Schema

```json
{
  "style": "cinematic-wisdom",
  "aspect": "1:1",
  "slides": [
    {
      "bg_prompt": "Cinematic egyptian temple, golden hour, volumetric light, lens flare, photorealistic, 8k",
      "number": "301",
      "title": "POWER & WEALTH SECRETS",
      "sub_label": "Most People Never Study",
      "bullets": ["Hidden pattern 1", "Hidden pattern 2", "Hidden pattern 3"],
      "cta_text": "UNLOCK THE FULL LIST!",
      "cta_domain": "bookofwisdom.app"
    }
  ]
}
```

## Regeln

- **BG-Prompt:** Immer "cinematic, photorealistic, 8k, epic, volumetric light" einfügen. Motive: Egyptian, Greek, Roman, mystical ruins, ancient libraries, starry skies über Tempeln
- **Number:** Hero-Zahl, 3-stellig, wird gold-gradient
- **Title:** All-Caps, max 30 Zeichen pro Zeile, Cinzel Serif
- **Sub-Label:** Kursiv, Gold, hint-y ("Most People Never Study", "Only The Elite Know")
- **Bullets:** 3 Zeilen, je max ~40 Zeichen, Creme-Color
- **CTA:** Magenta-Banner Bottom, immer Main-Call + Domain

## Workflow

1. Frag the Owner: Topic? Anzahl Items (1 Hero oder X-Slide-Listicle)? CTA-Domain?
2. Baue BG-Prompt passend zum Thema (z.B. "wealth secrets" → Göttin-Statue vor Gold; "discipline" → Spartaner-Tempel)
3. Input → `_runs/<projekt>/<timestamp>/input.json`
4. Run: `python3 render.py --style cinematic-wisdom --input … --out …`
5. Visual check

## Output

PNGs 1080×1080. AI-BGs werden gecacht in `styles/cinematic-wisdom/bgs/` (Prompt-Hash).

## Nicht vergessen

- GEMINI_API_KEY muss gesetzt sein
- Erste Generation pro Prompt ~5-10s, danach cached
- Bei schwachem Kontrast zwischen BG und Text: Gradient-Overlay schon im Template, aber bei hellen BGs text-shadow boost nötig
