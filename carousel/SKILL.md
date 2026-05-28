---
name: carousel
description: Orchestrator-Skill für das Carousel-System. the Owner liefert Topic/Content + wählt einen der 7 Stile, ich route auf den Style-Skill und rendere PNGs. Frag nach Stil wenn unklar.
---

# /carousel — Orchestrator

Master-Skill für cross-projekt Carousel-Posts (IG/LinkedIn/YT Community). Routes an einen der 7 Style-Sub-Skills.

## Verfügbare Stile

| Slug | Look | Typische Nutzung |
|---|---|---|
| `handwritten-zine` | Cream-BG, Kalam-Handschrift, Gelb+Grün-Highlighter | Tutorials mit Screenshots |
| `dark-metallic-lab` | Dunkel-Grunge, Gold-Gradient (Oswald), Frosted-Glass-Cards | Peptid/[brand], Disclaimer-Content |
| `creator-class-grid` | Dunkelgrau Pixel-Grid, Inter Bold, Pink-Peach-Gradient, rote Kreise | Creator-Tipps, Regel-basierter Content |
| `cinematic-wisdom` | AI Egyptian/Mystical BG, Gold-Zahl Cinzel, Magenta-CTA | "Ancient knowledge", Listicle-Hero |
| `desk-paper-note` | Green Cutting-Mat (AI), Paper-Cards mit Sharpie | Gannon-Meyer-Vibe, DIY-Feeling |
| `hand-held-card` | Warm Bokeh (AI), Sharpie-Index-Card + rotes Squiggle | Quote-Carousels, atmosphärisch |
| `news-breaking-dark` | Dunkler Grunge-Newsroom, Bebas Neue, rote Blocks | Breaking-News, Opinion-Pieces |

## Workflow

1. **Stil-Discovery** (wenn nicht explizit gewählt):
   - Frag the Owner kurz: "Welcher Stil?" + zeig die Tabelle oben
   - ODER: aus Kontext ableiten (Peptid → metallic-lab, Reel-Tipps → creator-class-grid, etc.)

2. **Content-Gathering:**
   - Topic / Hauptbotschaft
   - Anzahl Slides (default 3-8)
   - CTA-Slide am Ende? (+ CTA-Wort)
   - Bildformat: `1:1` (IG/LI) oder `4:5` (IG Stretch, YT Community)
   - Style-spezifische Extras (Screenshots für zine, BG-Prompts-Overrides für AI-BG-Stile)

3. **JSON-Build + Render:**
   - Nutze Schema aus `infrastruktur/carousel-system/styles/<slug>/examples/sample-input.json` als Vorlage
   - Speichere Input in `_runs/<projekt>/<timestamp>/input.json`
   - Run:
   ```bash
   cd infrastruktur/carousel-system
   python3 render.py --style <slug> \
     --input _runs/<projekt>/<timestamp>/input.json \
     --out _runs/<projekt>/<timestamp>/output
   ```

4. **Validate + Liefern:**
   - Zeig die ersten 1-2 PNGs zur Visual-Prüfung
   - `open -R <output-ordner>` für Finder-Link
   - Bei Feedback: iteriere am Input oder Style-Template

## Rendering

- **Default:** Playwright/Chromium local (unbegrenzt, schnell)
- **Fallback:** HCTI API (`--renderer hcti`) bei Playwright-Problemen
- **AI-BG-Stile** (cinematic-wisdom, desk-paper-note, hand-held-card): Erste Runde generiert BGs via Gemini 3 Pro Image API (GEMINI_API_KEY aus ~/.zshrc), gecacht per Prompt-Hash in `styles/<slug>/bgs/`

## Output-Konvention

Pro Run:
```
_runs/<projekt>/<YYYY-MM-DD-HHMM>-<topic-slug>/
  input.json
  output/
    slide-01.png … slide-NN.png
    slide-01.html … (debug)
```

## Style-Skills

Jeder Stil hat einen eigenen Skill für tiefere Details:
- `/carousel-handwritten-zine`
- `/carousel-dark-metallic-lab`
- `/carousel-creator-class-grid`
- `/carousel-cinematic-wisdom`
- `/carousel-desk-paper-note`
- `/carousel-hand-held-card`
- `/carousel-news-breaking-dark`

Wenn the Owner direkt nach einem Stil fragt ("Bau mir einen Cinematic-Wisdom-Post"), route direkt dorthin.

## Speicherort

- System-Root: `infrastruktur/carousel-system/`
- Projektspezifische Inputs/Outputs: `_runs/<projekt>/…` (gitignored, bleibt beim System)
- Bei Publish: User kopiert in `<projekt>/social-assets/…`
