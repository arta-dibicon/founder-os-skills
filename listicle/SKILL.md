---
name: listicle
description: "Erstelle eine komplette Listicle-Landing-Page (HTML) für ein Produkt. TRIGGER wenn the Owner sagt 'Listicle für [X]', 'Baue eine Listicle-Page', '7 Gründe Seite', oder '/listicle [Produkt]'. Auch bei 'Listicle erstellen', 'Gründe-Page bauen'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_resize
---

# Listicle Page Builder — "X Gründe warum..."

Erstelle eine komplette, deploybare Listicle-Landing-Page als einzelne HTML-Datei. Die Listicle ist eine Pre-Sale-Seite die wie ein journalistischer Artikel aussieht, aber zum Kauf führt.

## Core Principles (Mark Builds Brands)
- **"Disguise your marketing."** Die Seite sieht aus wie ein redaktioneller Testbericht, NICHT wie ein Shop.
- **"Craft arguments, not copy."** Jeder Grund ist ein logisches + emotionales Argument, kein Feature-Listing.
- **"The magnificence of the argument, not the magnificence of words."** Klare, einfache Sprache. 5th-8th grade reading level.
- **Necessary Beliefs als North Star.** Jeder Grund muss mindestens eine Necessary Belief adressieren.
- **Emotional Delta.** Meet them at Pain → Raise to Solution → Bring back to Urgency.

## Input erwarten
Aus der User-Nachricht oder interaktiv extrahieren:

### Pflicht-Inputs
- **PRODUKT**: Was wird verkauft? (z.B. "EcoFlow Delta 2 Max Powerstation")
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **ZIELGRUPPE**: Pfad zur Zielgruppenanalyse (z.B. "[projekt]/zielgruppe/")
- **PERSONA**: Welche Persona aus der ZG-Analyse? (z.B. "Persona 1: Der Pragmatische Familienvater")

### Optionale Inputs
- **ANGEBOT**: Welches Angebot? (z.B. "1+1 Gratis", "20% Rabatt", "Bundle €199")
- **CHECKOUT_URL**: Wohin führt der CTA-Button? (Stripe Link, Shopify Checkout, etc.)
- **PRODUKTBILDER**: Pfad zu Produktbildern (wenn vorhanden)
- **MARKENNAME**: Fake-Magazin-Name für den Header (z.B. "Sicherheits-Ratgeber", "Vorsorge-Report")
- **ANZAHL_GRUENDE**: Wie viele Gründe? Default: 7
- **AUTOR_NAME**: Fake-Autor für Byline (wird generiert wenn nicht angegeben)
- **SPRACHE**: Default: Deutsch

Falls Inputs fehlen → the Owner fragen. Aber intelligent defaults nutzen wo möglich.

## Vorbereitung: Research laden

BEVOR du anfängst zu bauen — die Foundational Docs lesen:

```bash
# Diese Dateien MÜSSEN gelesen werden
cat "[projekt]/zielgruppe/03-personas.md"      # → Persona-Details, Awareness Stage
cat "[projekt]/zielgruppe/06-offer-brief.md"    # → Necessary Beliefs, UMP/UMS, Emotional Delta
cat "[projekt]/zielgruppe/07-voice-of-customer.md" # → Exact Words, Sprach-Patterns
cat "[projekt]/zielgruppe/02-before-after.md"   # → Pain/Desire Paare für Gründe
```

Falls `/product-research` Output existiert:
```bash
cat "[projekt]/produkte/03-product-ranking.md"  # → Pricing, Funnel-Empfehlung, Competitive Advantage
```

**Ohne diese Dokumente baust du NICHTS.** Die gesamte Copy kommt aus der Research, nicht aus dem Kopf.

---

## STRUKTUR DER LISTICLE (validiert an Clickrs-Beispielen)

Die Seite ist eine lange, scrollbare Single-Page mit diesem exakten Aufbau:

### Section 1: HEADER
```
[Magazin-Logo/Name]
─────────────────────
```
- Fake-Magazin-Name als "Herausgeber" (z.B. "VORSORGE RATGEBER", "SICHERHEITS-REPORT")
- Clean, minimalistisch, seriös
- Kein Shop-Branding — das ist KEIN Shop, das ist ein "Artikel"

### Section 2: HEADLINE + SUBHEADLINE
```
X Gründe, warum ganz Deutschland auf
[Produkt/Lösung] wechselt.
```
- Headline-Pattern: "X Gründe warum [Social Proof Phrase] [Handlung]"
- Alternative Patterns:
  - "[Zielgruppe] spricht vom Geheimtipp: [Produkt]"
  - "Warum [Zahl] Deutsche auf [Lösung] setzen"
  - "[Zahl] Gründe warum [Experten/Familien/...] [Lösung] empfehlen"
- Subheadline: 2-3 Sätze die das Problem benennen + "wir haben getestet"
- **Byline**: "Von [Autor], [Titel] | [Datum] · Lesezeit: X Min."

### Section 3: INTRO-TEXT
- 2-3 Absätze
- **Absatz 1:** Problem benennen in ZG-Sprache (aus VOC)
- **Absatz 2:** "Doch jetzt sorgt [Lösung] für Aufsehen..." → Brücke
- **Absatz 3:** "Wir haben [Dauer] getestet — das Ergebnis hat uns überrascht."
- Perspektive: Redaktionell ("wir", "unsere Tester") — NICHT werblich

### Section 4: GRÜNDE (Zig-Zag Layout)
Für jeden Grund (default 7):

```
[GRUND N]. [Headline — max 8 Worte]

[2-3 Absätze Text]
- Absatz 1: Konkrete Beobachtung/Feature
- Absatz 2: Warum das wichtig ist (Benefit → Desire)
- Absatz 3: Emotionaler Payoff (Transformation)

[BILD: Produkt-in-Aktion oder Lifestyle]
```

**Layout-Regel:** Bild und Text wechseln die Seite ab:
- Grund 1: Text links, Bild rechts
- Grund 2: Bild links, Text rechts
- Grund 3: Text links, Bild rechts
- ... (Zig-Zag)

**Copy-Regeln pro Grund:**
- Jeder Grund adressiert mindestens 1 Necessary Belief aus dem Offer Brief
- Exact Words der Zielgruppe nutzen (aus VOC)
- Keine Marketing-Superlative ("revolutionär", "einzigartig") — sondern konkrete Aussagen
- Jeder Grund endet mit einem emotionalen Payoff (Before→After)
- Bold-Highlights für Schlüsselbegriffe (max 2-3 pro Absatz)
- Fließtext, KEINE Bulletpoints (das ist ein Artikel, keine Produktseite)

**Der letzte Grund ist IMMER das Angebot:**
- "X+1 Gratis — solange der Vorrat reicht" oder
- "Das exklusive Angebot — nur für kurze Zeit" oder ähnlich
- Hier wird das Offer eingeführt (Preis, Bundle, Garantie)

### Section 5: MID-PAGE CTA (nach Grund 3 oder 4)
```
─────────────────────────────
Dieses exklusive [Angebot] gilt nur für die ersten [Zahl] Kunden.
─────────────────────────────
```
- Urgency-Element (Limit, Countdown, "erste 100")
- Testimonial-Slider mit 3 Kunden (Foto + Text + "Verifiziert" Badge)
- Optional: Social Proof Badge ("12.000+ Kunden vertrauen uns")

### Section 6: TESTIMONIALS (2x auf der Seite)
```
Das sagen unsere [Tester/Kunden]:

[Foto]  [Foto]  [Foto]
Name    Name    Name
"..."   "..."   "..."
Verifiziert  Verifiziert  Verifiziert
```
- 3 Testimonials pro Block, 2 Blöcke auf der Seite (nach Mid-CTA + nach letztem Grund)
- Jedes Testimonial: Foto + Vorname + Initial + Zitat + "Verifiziert" Badge
- Zitate basieren auf VOC-Research — echte Sprach-Patterns verwenden
- Fotos: Werden per Recraft AI generiert oder Platzhalter

### Section 7: FINAL CTA (Dark-Mode Conversion Block)
Der Final CTA ist ein visueller Bruch — **Dark-Mode-Design** (dunkel, fast schwarz) das sich klar vom weißen Artikel abhebt. Hier wird verkauft, nicht informiert.

**Aufbau (von oben nach unten):**

```
[Urgency-Banner: pulsierend, rot] "⚡ Einführungspreis — nur noch heute"

[PRODUCT MOCKUP — groß, zentriert, Drop-Shadow]
                     "Sofort-Download" Badge oben rechts

[Offer-Headline] "Dein kompletter [Plan]. Sofort umsetzbar. Ohne Risiko."
[Offer-Sub] "Der Leitfaden, der [X] Familien in [Y] Wochen [Ergebnis] hat."

✓ Benefit 1 — konkreter Inhalt
✓ Benefit 2 — konkreter Inhalt
✓ Benefit 3 — konkreter Inhalt
✓ Benefit 4 — konkreter Inhalt
✓ Benefit 5 — konkreter Inhalt
✓ Benefit 6 — konkreter Inhalt

┌─────────────────────────────────┐
│  COUNTDOWN: 03 : 47 : 22       │
│  "Einführungspreis endet in"    │
└─────────────────────────────────┘

[Fortschrittsbalken: "412 von 500 Exemplaren vergriffen" — Shimmer-Animation]

         ~~€49~~  €29
    "Du sparst 40% — nur noch 88 Exemplare"

  [ ⚡ JETZT SICHERN — nur €29 ] ← Shine-Animation

  "Sofort-Download · PDF · Auf jedem Gerät · Einmalzahlung"

  ⏳ "Bei 500 Downloads steigt der Preis auf €49 — ohne Vorwarnung."

  🛡️ "30 Tage Geld-zurück-Garantie — kein Risiko, keine Fragen, kein Kleingedrucktes."
```

**Design-Details:**
- Background: `linear-gradient(135deg, #1a1a1a, #2d2d2d)` — Dark Mode
- Roter Gradient-Stripe oben (4px): visueller Anker
- Urgency-Banner: `animation: pulse-badge 2s ease-in-out infinite`
- Fortschrittsbalken: Shimmer-Animation (`translateX` Sweep)
- CTA-Button: Shine-Animation (3s Loop), Box-Shadow `rgba(220,38,38,0.4)`
- Countdown: Rotes Glasmorphism-Panel, tickt live runter (JS)
- Checkmarks: Grüne ✓ Icons, nicht Emoji-Checkboxes
- Garantie: Border-top Separator, Shield-Icon, dezent

**Scarcity-Elemente (alle 4 müssen drin sein):**
1. Countdown-Timer (resetet täglich, max 4h)
2. Fortschrittsbalken "X von Y vergriffen" (75-90% gefüllt)
3. "Nur noch Z Exemplare" im Preis-Bereich
4. "Bei Y steigt der Preis" — harter Closer unter dem Button

**Warum Dark Mode:** Der visuelle Kontrast zum weißen Artikel signalisiert "hier passiert was anderes". Der User merkt unbewusst: Das ist der Moment der Entscheidung. Validiert im Live-Test — the Owner: "echt richtig gut".

### Section 8: FAZIT
- 3-5 Sätze Zusammenfassung
- Emotionaler Closer
- Nochmal CTA-Button

### Section 9: DISCLAIMER
```
Dieses Produkt ist nicht dazu bestimmt, Krankheiten zu diagnostizieren...
[Standard E-Com Legal Disclaimer]
KI-generierte Inhalte Hinweis
```

### Section 10: FOOTER
```
Wichtige Links    Rechtliches    Newsletter
─ Startseite      ─ AGB          [Email-Feld]
─ Produkte        ─ Datenschutz  [EINTRAGEN]
─ Kontakt         ─ Impressum
                  ─ Widerruf
```

---

## BILD-STRATEGIE

### Automatische Bild-Beschaffung

Der Skill generiert/beschafft Bilder in dieser Reihenfolge:

#### 1. Produkt-Mockup (PFLICHT bei digitalen Produkten)
Digitale Produkte (Guides, Checklisten, eBooks) brauchen ein visuelles Mockup — ohne Mockup fehlt die "Greifbarkeit".

**Nano Banana (Gemini) für Mockups:**
```python
from google import genai
from google.genai import types
import os, base64

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="nano-banana-pro-preview",
    contents="Generate a photorealistic product mockup: [BESCHREIBUNG]. Show on iPad/tablet, professional lighting, slight angle, clean background.",
    config=types.GenerateContentConfig(response_modalities=["IMAGE", "TEXT"])
)
# Bild aus response.candidates[0].content.parts extrahieren, base64 → PNG speichern
```
- Mockup zeigt das Produkt auf einem Device (iPad, Laptop, Smartphone)
- Wird im **Final CTA prominent platziert** (groß, zentriert, Drop-Shadow)
- Auch im **Grund 7 (Angebot-Section)** als Bild verwenden
- Kosten: ~$0.01-0.04 pro Bild

**Wenn kein Nano Banana API Key:** Platzhalter-Box mit Text "Produktbild" + Hinweis an the Owner

#### 2. Produkt-Bilder (physische Produkte)
- Wenn the Owner Produktbilder liefert → verwenden
- Wenn nicht → Unsplash-Kontext-Bilder als Platzhalter + Hinweis "Produktbilder ersetzen"

#### 3. Lifestyle/Kontext-Bilder (Unsplash)
```bash
# Unsplash Direct URL Pattern:
# https://images.unsplash.com/photo-{ID}?w=800&q=80&auto=format
```
- Pro Listicle: 5-7 Kontext-Bilder aus Unsplash
- WebSearch: "site:unsplash.com [keyword]" → Bild-IDs extrahieren
- Keywords aus der Nische ableiten (z.B. "emergency preparedness", "family safety", "power outage")

**WICHTIG — Unsplash-Bildvalidierung:**
- **NIEMALS `source.unsplash.com` verwenden** — deprecated, liefert oft falsche Bilder
- **IMMER** die konkrete Photo-ID verwenden: `images.unsplash.com/photo-{ID}`
- **Nach dem Einbetten: Seite öffnen und JEDES Bild visuell prüfen** — Unsplash-IDs können Überraschungen liefern (z.B. Schuhe statt Familie)
- **Keine doppelten Bild-URLs** — vor Einbau alle bestehenden URLs im HTML greppen
- Wenn ein Bild nicht passt oder nicht lädt → sofort ersetzen, nicht hoffen

#### 4. Testimonial-Porträts (Recraft AI)
```bash
# Recraft API Call für Testimonial-Fotos:
curl -X POST "https://external.api.recraft.ai/v1/images/generations" \
  -H "Authorization: Bearer $RECRAFT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Professional headshot photo of a [age] year old [gender] German person, [description], natural lighting, casual clothing, warm smile, white background, photorealistic",
    "style": "realistic_image",
    "model": "recraftv3",
    "size": "1024x1024"
  }'
```
- 6 verschiedene Personen generieren (3 pro Testimonial-Block)
- Diverse Altersgruppen und Geschlechter (passend zur Persona)
- Deutsche/Europäische Gesichter
- Casual/Arbeitskleidung je nach Nische

#### 5. Badges/Infografiken (HTML/CSS)
- "X% leichter", "Getestet", "Verifiziert" Badges → als styled HTML-Elemente
- Fortschrittsbalken → CSS
- Sterne-Bewertung → Unicode ★ + CSS
- KEINE externen Bild-Dateien für UI-Elemente

### Bild-Fallback-Strategie
Wenn Recraft API nicht verfügbar oder kein API-Key:
- Testimonial-Fotos: Initialen-Avatar (CSS Circle + Buchstabe) statt Foto
- Lifestyle-Bilder: Nur Unsplash
- Hinweis an the Owner: "Testimonial-Fotos sind Platzhalter — Recraft API Key setzen für echte Porträts"

---

## TECHNISCHE UMSETZUNG

### Single HTML File
Die gesamte Seite ist EINE HTML-Datei mit eingebettetem CSS und JS. Kein externes Framework.

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Headline] — [Magazin-Name]</title>
    <meta name="description" content="[SEO Description]">
    <!-- Open Graph Tags für Social Sharing -->
    <meta property="og:title" content="[Headline]">
    <meta property="og:description" content="[Subheadline]">
    <meta property="og:image" content="[Hero-Bild URL]">
    <style>
        /* Alles inline — kein externer CSS */
    </style>
</head>
```

### CSS Design System
```css
/* Farben */
--bg: #ffffff;
--text: #1a1a1a;
--text-light: #666666;
--accent: #dc2626;          /* Roter CTA */
--accent-hover: #b91c1c;
--border: #e5e5e5;
--badge-bg: #f0fdf4;
--badge-text: #166534;

/* Typografie */
--font-heading: 'Georgia', serif;
--font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-size-h1: clamp(1.75rem, 4vw, 2.5rem);
--font-size-body: 1.05rem;
--line-height: 1.7;

/* Layout */
--content-width: 800px;
--spacing: 2rem;
--img-radius: 8px;
```

### Responsive Design
- Desktop: 800px Content-Width, Zig-Zag Layout (Text/Bild nebeneinander)
- Tablet (≤1024px): Leicht komprimiert, Zig-Zag bleibt
- Mobile (≤768px): Volle Breite, Bilder über Text (Stack-Layout), größere Touch-Targets

### Performance
- Bilder: `loading="lazy"` für alle Bilder unterhalb des Folds
- Bilder: `width` und `height` Attribute setzen (kein Layout Shift)
- Keine externen Fonts laden (System Fonts)
- Kein JavaScript außer für optionale Interaktionen (Testimonial-Slider, Fortschrittsbalken-Animation)

### JavaScript (minimal, 3 Features)
```javascript
// 1. Fortschrittsbalken Animation (Intersection Observer)
// 2. Countdown-Timer (resetet täglich, max 4h remaining)
// 3. Smooth Scroll für CTA-Buttons
// KEIN jQuery, KEIN Framework
```

**Countdown-Timer Logik:**
```javascript
// Berechnet remaining aus Tagesende, max 4h (14400s)
// Tickt jede Sekunde runter
// Resetet bei 0 auf 14400 (damit er nie bei 00:00:00 stehenbleibt)
```

---

## ARBEITSVERZEICHNIS

```
[projekt]/listicle/
├── [produkt-slug].html          ← Die fertige Seite
├── images/
│   ├── product-mockup.png       ← Nano Banana Produkt-Mockup (digital) oder Hero (physisch)
│   ├── testimonial-1.jpg        ← Recraft-generierte Porträts
│   ├── testimonial-2.jpg
│   ├── testimonial-3.jpg
│   ├── testimonial-4.jpg
│   ├── testimonial-5.jpg
│   ├── testimonial-6.jpg
│   └── ...                      ← Weitere lokale Bilder wenn nötig
└── _deploy/
    └── netlify.toml             ← Deploy-Config
```
**Hinweis:** Lifestyle/Kontext-Bilder werden als Unsplash-URLs direkt eingebettet (kein lokaler Download nötig). Nur Mockups und Testimonial-Porträts werden lokal gespeichert.

```bash
mkdir -p "[projekt]/listicle/images" "[projekt]/listicle/_deploy"
```

---

## ABLAUF (Step by Step)

### Step 1: Research laden & Copy vorbereiten
1. Foundational Docs lesen (Personas, Offer Brief, VOC, Before/After)
2. Aus der gewählten Persona extrahieren:
   - Top 7 Pains → werden zu den 7 Gründen (Pain → Lösung → Benefit)
   - Necessary Beliefs → welche Belief wird pro Grund adressiert?
   - VOC Quotes → welche Zitate werden für Testimonials adaptiert?
   - Emotional Delta Map → wo starten wir, wo enden wir?
3. Grund-Matrix erstellen (intern, nicht als Datei):

| # | Pain (aus Research) | Grund-Headline | Belief die kippt | VOC-Zitat als Basis |
|---|---|---|---|---|
| 1 | "[Pain]" | "[8 Worte max]" | Belief #X | "[Zitat]" |

### Step 2: Copy schreiben
1. Headline + Subheadline (3 Varianten, beste wählen)
2. Intro-Text (Problem → Brücke → "Wir haben getestet")
3. 7 Gründe (jeweils 2-3 Absätze, letzter Grund = Angebot)
4. 6 Testimonials (basierend auf VOC, adaptiert für Kontext)
5. CTAs (Mid-Page + Final)
6. Fazit
7. Disclaimer + Footer

### Step 3: Bilder beschaffen
1. **Produkt-Mockup** (digitale Produkte): Nano Banana API → `images/product-mockup.png`
2. **Unsplash**: 5-7 Kontext-Bilder per WebSearch finden, Photo-IDs extrahieren → direkt als URL einbetten
3. **Recraft**: 6 Testimonial-Porträts generieren (wenn API Key verfügbar) → `images/testimonial-{1-6}.jpg`
4. **Produktbilder** (physische Produkte): Von the Owner geliefert oder Unsplash-Platzhalter
5. **Validierung**: Nach Einbau ALLE Bilder visuell prüfen (Playwright oder manuell) — keine Duplikate, keine falschen Motive

### Step 4: HTML bauen
1. Template mit CSS Design System aufsetzen
2. Copy einsetzen
3. Bilder einbetten (relative Pfade oder URLs)
4. Responsive Design testen (Mental-Check: Mobile-First)
5. HTML via Bash in Datei schreiben

### Step 5: QA & Deploy
1. Playwright: Seite lokal öffnen oder auf Netlify deployen
2. Desktop-Screenshot + Mobile-Screenshot
3. Alle Links prüfen (CTA-Button → Checkout URL)
4. Ladezeit-Check (Bilder zu groß?)
5. Copy-Check: Stimmen die Beliefs? Stimmt die VOC-Sprache?
6. Ergebnis an the Owner präsentieren mit Screenshots

---

## QUALITÄTS-CHECK (vor Abgabe)

### Artikel-Look
- [ ] Sieht aus wie ein Artikel, NICHT wie ein Shop?
- [ ] Headline enthält Social Proof + Zahl?
- [ ] Byline mit Autor + Datum + Lesezeit?
- [ ] Jeder Grund adressiert mindestens 1 Necessary Belief?
- [ ] VOC-Sprache verwendet (keine Marketing-Buzzwords)?
- [ ] Zig-Zag Layout (Text/Bild wechselnd)?

### Conversion-Elemente
- [ ] Mid-Page CTA nach Grund 3 oder 4?
- [ ] 2 Testimonial-Blöcke (à 3 Testimonials mit Recraft-Fotos)?
- [ ] Final CTA im Dark-Mode-Design?
- [ ] Produkt-Mockup im Final CTA (bei digitalen Produkten)?
- [ ] Countdown-Timer tickt korrekt?
- [ ] Fortschrittsbalken mit konkretem Limit ("X von Y")?
- [ ] Scarcity-Text unter dem Button ("Bei Y steigt der Preis")?
- [ ] Garantie-Hinweis mit Shield-Icon?
- [ ] CTA-Button hat Shine-Animation?

### Bilder
- [ ] ALLE Bilder visuell geprüft — zeigen sie was sie sollen?
- [ ] Keine doppelten Bild-URLs?
- [ ] Alle Bilder laden korrekt (keine 404)?
- [ ] Mockup/Testimonial-Bilder lokal gespeichert (nicht nur URL)?

### Technik
- [ ] Mobile-responsive (besonders Final CTA + Countdown)?
- [ ] CTA-Button führt zur richtigen URL?
- [ ] Disclaimer vorhanden?
- [ ] Footer mit Rechtliches?

---

## WICHTIGE REGELN

1. **Research-First.** Keine Listicle ohne Foundational Docs. Jeder Satz muss durch Research gedeckt sein.
2. **Disguised Marketing.** Die Seite sieht aus wie ein Magazin-Testbericht. Kein Logo des Shops im Header.
3. **7 Gründe Default.** 7 funktioniert am besten (psychologisch). Kann auf 5 oder 9 angepasst werden, aber 7 ist Standard.
4. **Letzter Grund = Angebot.** Der letzte Grund ist immer das Angebot selbst ("X+1 Gratis — solange Vorrat reicht").
5. **Einfache Sprache.** Kein Fachjargon, keine Marketing-Sprache. Die Sprache der Zielgruppe verwenden.
6. **Bold sparsam.** Max 2-3 fettgedruckte Stellen pro Absatz. Highlights, keine Dekoration.
7. **Bilder authentisch.** Lifestyle > Freisteller. Menschen mit Produkt > Produkt allein.
8. **Single File Deploy.** Eine HTML-Datei, alles inline. Bilder als URLs oder base64 wenn klein genug.
9. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).
10. **Netlify Deploy** nach QA: `npx netlify-cli deploy --dir=[projekt]/listicle/ --prod`

## LEARNINGS AUS DEM FELD

### Copy & Struktur
1. **"Von [Name], Redakteur [Magazin]" Byline ist Pflicht.** Ohne Byline wirkt es wie Werbung, nicht wie ein Artikel.
2. **"Lesezeit: 1 Min. 10 Sek."** — Immer angeben. Reduziert Bounce weil Leute wissen dass es kurz ist.
3. **Der Intro darf KEIN Produkt nennen.** Erst das Problem, dann die "neue Generation" als Brücke, DANN das Produkt.
4. **Mid-Page CTA ist kritisch.** Wer bis Grund 4 gescrollt hat, ist warm genug zum Klicken. Ohne Mid-CTA verlierst du die.

### Conversion & Scarcity
5. **Final CTA im Dark-Mode-Design konvertiert besser.** Der visuelle Bruch zum weißen Artikel signalisiert "Entscheidungsmoment". Validiert im Live-Test (the Owner: "echt richtig gut").
6. **Fortschrittsbalken mit konkretem Limit ("412 von 500") schlägt vages "82%".** Konkretes Limit = konkreter Handlungsdruck.
7. **Countdown-Timer + Fortschrittsbalken + Spots-Left = Triple-Scarcity.** Alle drei zusammen erzeugen den stärksten Kaufdruck.
8. **"Bei X steigt der Preis auf €Y — ohne Vorwarnung"** ist der härteste Closer. Direkt unter dem CTA-Button platzieren.
9. **Garantie-Hinweis UNTER dem Button mit Shield-Icon** nimmt das letzte Risiko. Immer "kein Kleingedrucktes" ergänzen.

### Bilder
10. **Testimonials mit Fotos performen 3x besser** als Text-only. Recraft-generierte Porträts sind gut genug.
11. **Produkt-Mockup ist PFLICHT bei digitalen Produkten.** Ohne visuelles Bild fehlt die Greifbarkeit — Nano Banana generiert brauchbare iPad/Tablet-Mockups.
12. **Unsplash-Bilder IMMER visuell verifizieren.** IDs können Überraschungen liefern (z.B. Schuhe statt Familie). `source.unsplash.com` ist deprecated und unzuverlässig.
13. **Keine doppelten Bild-URLs.** Vor dem Einbau alle existierenden URLs greppen — sonst sieht der User dasselbe Bild zweimal.
14. **Mockup groß + zentriert im CTA mit Drop-Shadow** — wirkt wie ein physisches Produkt und erhöht perceived value.
