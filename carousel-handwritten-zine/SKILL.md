---
name: carousel-handwritten-zine
description: Rendert Instagram/LinkedIn-Carousels im "Handwritten Zine"-Stil (Creme-BG, Kalam-Handschrift, Gelb+Grün-Highlighter, blaue Hand-Frames um Screenshots). Liefert PNGs pro Slide.
---

# Carousel: Handwritten Zine

Blueprint-Skill für carousel-system. Rendert Slides im Style 03 (cream + Kalam + highlighters).

## Input

the Owner beschreibt den Carousel (Topic + Slide-Inhalte). Du baust daraus JSON nach folgendem Schema:

```json
{
  "style": "handwritten-zine",
  "aspect": "1:1",
  "cta_word": "swipe",
  "slides": [
    {
      "title": [
        {"text": "step 1: create a", "highlight": "yellow"},
        {"text": "claude API key", "highlight": "yellow"}
      ],
      "screenshots": ["https://..."],
      "body": {"text": "optional body", "highlight": "green"}
    }
  ]
}
```

Details: `infrastruktur/carousel-system/styles/handwritten-zine/schema.md`

## Workflow

1. Frag the Owner kurz: Topic, Anzahl Slides, ob CTA-Slide am Ende (+Wort), ob Screenshots beigesteuert werden
2. Baue slide-Array. **Regeln:**
   - Alles lowercase (wird per CSS erzwungen, aber schreib es schon so)
   - Titel max 2 Zeilen à ~24-30 Zeichen (sonst Overflow bei 1080px)
   - Yellow = Step-Titel & Hooks. Green = Confirmations & Insights. Kein Highlight = Body-Info.
   - Max 2 Screenshots pro Slide (sonst zu eng)
   - Letzte Slide immer CTA (z.B. "save this", "follow for more")
3. Schreibe Input-JSON nach `infrastruktur/carousel-system/_runs/<timestamp>/input.json`
4. Run:
```bash
cd infrastruktur/carousel-system
python3 render.py --style handwritten-zine \
  --input _runs/<timestamp>/input.json \
  --out _runs/<timestamp>/output
```
5. Zeige PNGs zur Validierung, Output-Ordner mit `open -R <path>` im Finder

## Output

- PNGs: `slide-01.png` … `slide-NN.png` in `_runs/<timestamp>/output/`
- HTML-Debug-Files nebendran (für Iteration)

## Nicht vergessen

- HCTI Free Plan = 50 Renders/Monat → sparsam
- Google Font `Kalam` wird per CDN geladen, HCTI wartet 2s
- Bei sehr langen Titles: kürzen statt zwei Zeilen werden zu 4 wrappen
