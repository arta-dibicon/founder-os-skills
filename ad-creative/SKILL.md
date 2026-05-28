---
name: ad-creative
description: "Erstelle Ad Creatives (statische Bilder + Copy) für Meta/Facebook Ads. TRIGGER wenn the Owner sagt 'Ad Creatives für [X]', 'Werbeanzeigen erstellen', 'Facebook Ads Bilder', 'Creatives bauen', oder '/ad-creative [Produkt]'. Auch bei 'Static Ads', 'Image Ads erstellen', 'Ad-Material'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_resize
---

# Ad Creative Builder — Statische Image Ads für Meta/Facebook

## PRE-FLIGHT — Research-Kontext laden

Vor dem Start IMMER prüfen ob Audience-Research existiert (Source-of-Truth: lokal):

1. Lies `[aktives-projekt]/_research/INDEX.md`. Gibt es einen `done`-Run zum aktuellen Topic?
2. Wenn JA: Lade `_research/[topic-slug]/copy_context.md` + `personas.json` als Default-Kontext. Auch nützlich: `voice_of_customer.md` (Hook-Mining), `persona_deep_dive.md` (Channel-Matrix mit fertigen Ad-Headlines), `market_research.md` (1⭐-Themes der Konkurrenz für Counter-Positioning).
3. Wenn NEIN: Frag the Owner "Soll ich via `Rechit` Sub-Agent ein Research starten oder ohne arbeiten?" Niemals blind ohne Research drauflos schreiben.

Schema/Protokoll: Memory `feedback_research_loading_protocol.md`. Agent: `.claude/agents/rechit.md`.

---

Erstelle komplette Ad-Creative-Pakete (statische Bilder + Copy) für Facebook/Instagram Ads. Basiert auf der Foundational-Docs-Methode von Mark Builds Brands. Nutzt 3 Image-Engines parallel: **GPT-Image-2** (Text-im-Bild), **Nano Banana** (Photorealismus, Edits), **Recraft** (Stil-Illustrationen) — Auswahl je Use-Case (siehe Engine-Selection unten).

## Core Principles (Mark Builds Brands)

### Kontrast
- **"Your goal is to create the most amount of contrast in the mind of the customer."**
- Schau was alle Wettbewerber machen → mach das exakte Gegenteil.
- Ads die aussehen wie alle anderen werden ignoriert. Pattern-Break ist Pflicht.

### Disguised Marketing
- **"Create marketing content that doesn't look like marketing content."**
- Die besten Ads sehen aus wie Posts, Memes, Screenshots, Nachrichten — nicht wie Werbung.
- Gary Halbert Prinzip: Leute sortieren über dem Mülleimer — deine Ad muss aussehen wie etwas das sie behalten würden.

### Ugly Ads = Pretty Profits
- **"What looks best most often is not what converts."**
- Optimiere für Klarheit, NICHT für Ästhetik.
- Die profitabelsten Ads sehen oft "ugly" aus — aber die Copy ist glasklar.

### Research-First
- **"80% of your time should be spent on research."**
- Jede Ad basiert auf VOC (Voice of Customer) und Foundational Docs.
- Exact Words der Zielgruppe > Marketing-Sprache.

### Copy ≠ Content
- **Copy = Sales. Content = Engagement. Sie sind NICHT das Gleiche.**
- Wir schreiben Copy (Direct Response), keinen Content.
- Klarheit > Cleverness. 5th-8th Grade Reading Level.

---

## ZWEI TYPEN VON IMAGE ADS

### Typ A: INDIRECT ADS (Top-of-Funnel / Cold Traffic)

**Zweck:** Massiv breite Reichweite, Leute die das Produkt NICHT kennen.
**Ziel-Awareness:** Unaware → Problem-Aware
**Scaling-Potential:** HOCH — diese Ads skalieren am meisten auf Cold Traffic.

**Merkmale:**
- Bild ist ein **Scroll-Stopper** — man weiß NICHT was verkauft wird
- Bild sieht aus wie ein organischer Post, Meme, Screenshot, Nachricht, UGC
- Kein Produkt im Bild (oder nur minimal)
- Kein Preis im Bild
- Kein CTA im Bild
- Die Verkaufsarbeit passiert in der **Primary Text** (langer Copy-Text unter dem Bild)
- Leitet auf **Listicle, Advertorial oder Quiz-Funnel** weiter (Pre-Sell-Pages)

**16 Format-Typen (VARIANTEN-PFLICHT: min. 2 Varianten pro verwendetem Format!)**

**Foto-basiert (Gemini + HTML/CSS Overlay):**
1. **Native Static** — sieht aus wie ein Social-Media-Post, nicht wie eine Ad
2. **UGC-Still** — sieht aus wie ein User-Foto, nicht professionell, candid
3. **Before/After Split** — Links vorher, rechts nachher (Vorsicht: Meta Policy!)
4. **Nightmare-Scene** — NUR den Pain zeigen, keine Lösung andeuten → maximale Neugier
5. **Transformation-Kontrast** — Links kalt/blau (Problem), rechts warm/orange (Lösung)
6. **Gesicht + Emotion** — Close-up einer Person mit starker Emotion (Angst, Erleichterung, Schock)

**Pure HTML/CSS (kein Gemini nötig):**
7. **WhatsApp/iMessage Chat** — Konversation die das Produkt empfiehlt. MEHRERE Varianten: verschiedene Absender, verschiedene Tonalitäten, verschiedene Chat-Apps
8. **Smartphone-Notifications** — Lock-Screen mit Notification-Stack. MEHRERE Varianten: verschiedene Apps, verschiedene Szenarien (Katastrophe, Shopping, Bank)
9. **Nachrichten-Headline** — Breaking-News-Style mit Ticker. MEHRERE: verschiedene Sender, verschiedene Headlines
10. **Statistik/Infografik** — EINE große Zahl + Erklärung. MEHRERE: verschiedene Zahlen, verschiedene Darstellungen (Kreis, Balken, Prozent)
11. **Checkliste / Self-Assessment** — Haken + Kreuze. MEHRERE: verschiedene Kategorien, verschiedene Perspektiven
12. **Testimonial-Karte** — Foto + Zitat + Sterne. MEHRERE: verschiedene Personen, verschiedene Aussagen
13. **Warnung/Alert** — Alarm-Style, Dringlichkeit. MEHRERE: verschiedene Alarm-Typen (Amber Alert, Wetterwarn, Behörden)
14. **Meme-Format** — kulturelles Template mit Nischen-Twist. MEHRERE: verschiedene Meme-Templates
15. **Frage-Karte** — provokante Frage, große Schrift, simpler Hintergrund
16. **Kosten-Vergleich** — Alltags-Ausgaben vs. Produkt-Kosten (Kaffee, Netflix, etc.)

**VARIANTEN-REGEL:** Pro Format-Typ der verwendet wird → mindestens 2-3 inhaltlich verschiedene Varianten erstellen. NICHT nur 1x WhatsApp-Chat und 1x Notification. Sondern 3x WhatsApp-Chat (verschiedene Gespräche), 2x Notification (verschiedene Szenarien), etc. Das gibt dem Meta-Algorithmus maximale Creative Diversity.

**Primary Text für Indirect Ads:**
- Lang (300-800 Wörter), Direct-Response-Style
- Hook → Story/Problem → Agitate → Solution → CTA
- Klingt wie ein persönlicher Post, nicht wie Werbung
- Nutzt exakte VOC-Sprache
- CTA: "Link in Comments" oder "Mehr in der Bio" (je nach Plattform)

### Typ B: DIRECT ADS (Bottom-of-Funnel / Retargeting / Warm Traffic)

**Zweck:** Leute die bereits Problem/Solution-Aware sind zum Kauf bewegen.
**Ziel-Awareness:** Solution-Aware → Product-Aware → Most-Aware
**Scaling-Potential:** NIEDRIG — profitabel auf kleiner Scale (Retargeting).

**Merkmale:**
- Produkt ist **klar im Bild** sichtbar
- **Benefit-Statement** als Headline im Bild
- Preis/Angebot kann im Bild sein
- Testimonial/Social Proof im Bild
- CTA im Bild ("Jetzt sichern", "Nur noch heute")
- Leitet auf **Checkout/Produktseite** direkt weiter

**Beispiel-Formate (Direct):**
1. **Produkt + Benefit** — Produkt-Bild + 1 starker Benefit-Satz
2. **Angebot/Deal** — Preis, Rabatt, Bundle-Angebot
3. **Testimonial-Karte** — Foto + Zitat + Produkt
4. **Vergleich** — "Ohne [Produkt]" vs "Mit [Produkt]"
5. **Feature-Highlight** — 3-5 Benefits als Checkmarks neben dem Produkt
6. **Social Proof** — "12.000+ Kunden", Sterne-Bewertung, Badges
7. **Garantie-Fokus** — "30 Tage testen — kein Risiko"
8. **Urgency** — Countdown, "Letzte Chance", "Nur noch X verfügbar"

**Primary Text für Direct Ads:**
- Kurz (50-200 Wörter)
- Problem → Solution → Offer → CTA
- Direkt, klar, ohne Story
- Social Proof einbauen (Zahlen, Testimonials)

---

## INPUT ERWARTEN

### SCHRITT 0: FUNNEL-FRAGE (IMMER ZUERST!)

**Bevor IRGENDETWAS generiert wird, MUSS geklärt werden:**

> "Für welchen Funnel sollen die Ads sein?"
> - **Listicle** → Indirect Ads, Cold Traffic, Awareness-Aufbau
> - **Advertorial** → Indirect Ads, Cold Traffic, Story-basiert
> - **Quiz-Funnel** → Indirect Ads, Cold Traffic, Interaktiv
> - **Direct/Checkout** → Direct Ads, Retargeting, Warmer Traffic

**Warum?** Die Ads müssen zum Funnel passen. Ein Listicle-Ad hat einen anderen Ton als ein Quiz-Ad. Die Landing Page bestimmt den Hook, den CTA und die emotionale Brücke.

Nach Funnel-Auswahl:
1. Landing Page lesen (HTML/Content des Funnels)
2. Tonalität + Hook-Stil des Funnels verstehen
3. CTA der Ad auf den Funnel-Einstieg abstimmen
4. Ads so bauen, dass der Übergang Ad → Funnel nahtlos ist

### Pflicht-Inputs
- **FUNNEL**: Welcher Funnel? (Listicle/Advertorial/Quiz/Checkout) — **IMMER ZUERST FRAGEN**
- **PRODUKT**: Was wird verkauft? (z.B. "Krisenvorsorge Masterplan Guide")
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **ZIELGRUPPE**: Pfad zur Zielgruppenanalyse (z.B. "[projekt]/zielgruppe/")
- **PERSONA**: Welche Persona? (z.B. "Persona 1: Der besorgte Familienvater")

### Optionale Inputs
- **ANZAHL**: Wie viele Konzepte? (Default: 20-25 pro Funnel-Kampagne)
- **FUNNEL_URL**: URL der Landing Page (Listicle/Advertorial/Quiz/Checkout)
- **PRODUKTBILDER**: Pfad zu Produktbildern (für Direct Ads)
- **ASPECT_RATIO**: "1:1" (Default), "4:5", "9:16" — oder "all" für alle drei
- **SPRACHE**: Default: Deutsch
- **MARKE/BRAND**: Brand-Name wenn vorhanden (für Direct Ads)
- **FARBEN**: Brand-Farben wenn vorhanden (hex codes)

Falls Inputs fehlen → the Owner fragen. Aber intelligent defaults nutzen wo möglich.

---

## VORBEREITUNG: RESEARCH LADEN

**BEVOR du anfängst — die Foundational Docs lesen:**

```bash
# PFLICHT — diese Dateien MÜSSEN gelesen werden
cat "[projekt]/zielgruppe/03-personas.md"        # → Persona-Details, Awareness Stage, Consciousness Level
cat "[projekt]/zielgruppe/06-offer-brief.md"      # → Necessary Beliefs, UMP/UMS, Emotional Delta
cat "[projekt]/zielgruppe/07-voice-of-customer.md" # → Exact Words, Hooks, Pain-Quotes, Desire-Quotes
cat "[projekt]/zielgruppe/02-before-after.md"     # → Pain/Desire Paare für Ad-Angles
cat "[projekt]/zielgruppe/04-persona-deep-dive.md" # → Channel-Matrix, Ad-Präferenzen
```

Falls `/produkte/` Output existiert:
```bash
cat "[projekt]/produkte/03-product-ranking.md"    # → Pricing, Competitive Advantage
```

**Ohne diese Dokumente erstellst du KEINE Ads.** Jeder Hook, jeder Benefit, jedes Wort kommt aus der Research.

---

## CONCEPT-GENERATION PROZESS

### Phase 1: Ad-Angle-Matrix erstellen

Aus den Foundational Docs extrahieren:

| # | Angle-Typ | Hook-Idee | Awareness-Stage | Consciousness-Level | Necessary Belief | VOC-Zitat | Ad-Typ |
|---|-----------|-----------|-----------------|---------------------|------------------|-----------|--------|
| 1 | Fear/Urgency | "[VOC-Quote]" | Unaware | Fear (100) | Belief #1 | "73% der Deutschen..." | Indirect |
| 2 | Social Proof | "[VOC-Quote]" | Problem-Aware | Courage (200) | Belief #3 | "Mein Nachbar hat..." | Indirect |
| 3 | Transformation | "[Before→After]" | Solution-Aware | Willingness (310) | Belief #5 | "Endlich Klarheit..." | Direct |
| ... | | | | | | | |

**Angle-Typen (aus Research ableiten):**
- **Fear/Urgency** — "Was wenn morgen..." (Level: Fear 100)
- **Shame/Identity** — "Du bist 30 und hast keinen Plan" (Level: Shame 20)
- **Authority/Statistics** — "BBK empfiehlt: 14 Tage" (Level: Reason 400)
- **Social Proof** — "Über X Deutsche haben bereits..." (Level: Courage 200)
- **Curiosity/Pattern-Break** — "Warum Prepper falsch liegen" (Level: Neutrality 250)
- **Transformation** — "Von panisch zu vorbereitet in 7 Tagen" (Level: Willingness 310)
- **Anti-Category** — "Kein Prepper-Quatsch. Erwachsen sein." (Level: Courage 200)
- **Pain-Agitate** — "Strom weg. Heizung weg. Kinder frieren." (Level: Fear 100)
- **Desire/Aspiration** — "Die Ruhe wenn du weißt: Wir sind ready." (Level: Peace 600)
- **Controversy/Polarization** — "Dein Vermieter schuldet dir diesen Plan" (Level: Pride 175)

### Phase 2: Hook-Schärfung

Für jeden Angle den **PIG-Test** (Punch In the Gut) anwenden:

**Guter Hook:** "73% der deutschen Familien sind nicht auf einen Blackout vorbereitet. Deine wahrscheinlich auch nicht."
**Schwacher Hook:** "Sind Sie auf einen Stromausfall vorbereitet?"

**Regeln:**
- Klarheit > Cleverness
- 5th-8th Grade Reading Level
- Exact Words der Zielgruppe (aus VOC)
- Hook muss "Punch in the Gut" Reaktion auslösen
- Spezifisch > Generisch ("73%" schlägt "die meisten")
- Kein Marketing-Jargon

### Phase 3: Emotional Delta Map

Für jeden Ad-Concept die emotionale Reise definieren:

```
Start: [Level] → Peak: [Level] → End: [Level]
Beispiel: Fear (100) → Courage (200) → Fear (100) mit Handlungsimpuls
```

**Das Prinzip:** Meet them → Raise them → Bring them back down = maximaler Emotional Delta = maximale Conversion.

---

## IMAGE-GENERATION

### Engine Selection — Welches Modell wofür?

| Use-Case | Engine | Warum |
|---|---|---|
| **Indirect Ad mit Text-im-Bild** (Headline, Statistik, Quote als Bestandteil des Bildes) | **GPT-Image-2** | ~99% Text-Accuracy auch auf Deutsch (Umlaute, Komposita) — kein HTML-Overlay-Step nötig |
| **Direct Ad mit Produkt + Headline** | **GPT-Image-2** | Layout-Reasoning + Text-Rendering in einem Shot |
| **Indirect Ad: photorealistische Szene OHNE Text** (Person/Situation als Scroll-Stopper) | **Nano Banana** | Photorealismus, natürliches Licht, schnell + günstig |
| **Edit/Reframe/Outpaint** eines bestehenden Bildes | **Nano Banana** | Stärken bei Image-Editing |
| **Testimonial-Porträts** (Headshots) | **Recraft** | `realistic_image`-Modus liefert konsistente Headshots |
| **HTML/CSS-Formate** (Chat, Notification, Statistik-Karte, Checkliste) | **kein AI-Bild** | HTML/CSS + Playwright Screenshot — volle Kontrolle, null Typos |

**Decision-Flow für jedes Concept:**
1. Soll Text präzise IM Bild stehen? → **GPT-Image-2** (`infrastruktur/gpt-image-2/gpt_image2.py`)
2. Photorealistische Szene OHNE Text? → **Nano Banana** (`infrastruktur/nano-banana/nano_banana.py`)
3. Stilisierte Illustration / Headshot? → **Recraft**
4. UI-Mockup (Chat, Notification, etc.)? → **HTML/CSS + Playwright**

### Tool 1: GPT-Image-2 (OpenAI) — Default für Text-im-Bild

GPT-Image-2 ist seit April 2026 unser Default für Ads mit Text-Integration im Bild. Schlägt Nano Banana bei Text-Rendering deutlich (besonders deutsche Umlaute/Komposita).

```python
import sys
sys.path.insert(0, "~/workspace/infrastruktur/gpt-image-2")
from gpt_image2 import generate_image, edit_image

# Indirect Ad mit Text-im-Bild (z.B. Statistik-Hero)
generate_image(
    prompt="Editorial-style social media ad: dark navy background, large bold white serif headline 'Über 73% der Bildungsträger verlieren Teilnehmer durch fehlende Online-Kurse', minimalist composition, professional but candid",
    output_path="[projekt]/ads/indirect/concept-01-statistik.png",
    size="1024x1024",
    quality="medium",
)

# Direct Ad mit Produkt + Headline
edit_image(
    reference_paths=["[projekt]/assets/product.png"],
    prompt="Place product on warm wooden surface, add headline top-left 'Jetzt 30 Tage testen' in bold white sans-serif, subtle drop shadow",
    output_path="[projekt]/ads/direct/concept-01-product.png",
    quality="high",
)
```

**CLI-Variante:**
```bash
python3 ~/workspace/infrastruktur/gpt-image-2/gpt_image2.py \
  "Modern editorial ad: ..." \
  "[projekt]/ads/indirect/concept-01.png" \
  --quality medium --size 1024x1024
```

**Pricing-Quickref** (1024x1024): low $0.006 / medium $0.053 / high $0.21
**Default für Ad-Pipelines:** `quality="medium"` reicht für 95% der Fälle.
**4:5 Format:** `--size 1024x1536` oder `size="1024x1536"` in Python.

### Tool 2: Nano Banana (Gemini)

Nano Banana ist unser Default für photorealistische Indirect Ads OHNE Text und für Image-Edits/Reframing.

```python
from google import genai
from google.genai import types
import os, base64

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="[PROMPT]",
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"]
    )
)

# Bild aus response extrahieren und speichern
for part in response.candidates[0].content.parts:
    if part.inline_data:
        img_data = part.inline_data.data
        if isinstance(img_data, str):
            img_data = base64.b64decode(img_data)
        with open("[output_path]", "wb") as f:
            f.write(img_data)
```

**KRITISCH — Zwei-Schritt-Prozess für JEDES Bild:**

Jede Ad braucht ein fotorealistisches Bild UND einen Text-Overlay (Headline + Subheadline). Der Standard-Workflow ist:

**Schritt 1: Bild generieren (Gemini) — OHNE Text**
```
Photorealistic image for social media ad. [SZENE].
No text overlay. No logos. No captions. No watermarks.
Natural lighting, authentic feel.
Aspect ratio: 1:1.
```

**Schritt 2: Text-Overlay als HTML/CSS + Playwright Screenshot**

**KRITISCH: VARIABILITÄT bei Text-Placement!** Nicht jede Ad bekommt den gleichen Overlay-Style. Nutze die 10 Placement-Styles unten und WECHSLE zwischen ihnen ab. Jede Ad muss visuell ANDERS aussehen als die anderen.

#### 10 TEXT-OVERLAY PLACEMENT STYLES

**Style 1: Bottom Gradient** (Klassiker)
```css
.overlay { position:absolute; bottom:0; left:0; right:0;
  background:linear-gradient(transparent, rgba(0,0,0,0.85));
  padding:60px 50px; }
.headline { font-size:48px; font-weight:800; color:#fff; }
```

**Style 2: Centered Bold + Blur Background**
```css
.overlay { position:absolute; inset:0; display:flex; flex-direction:column;
  align-items:center; justify-content:center; text-align:center;
  backdrop-filter:blur(12px); background:rgba(0,0,0,0.3); padding:60px; }
.headline { font-size:64px; font-weight:900; color:#fff;
  text-shadow:0 4px 20px rgba(0,0,0,0.8); }
```

**Style 3: Top Bar / Header Strip**
```css
.overlay { position:absolute; top:0; left:0; right:0;
  background:rgba(220,38,38,0.95); padding:30px 40px; }
.headline { font-size:42px; font-weight:800; color:#fff; text-transform:uppercase; }
.subheadline { font-size:22px; color:rgba(255,255,255,0.9); margin-top:8px; }
```

**Style 4: Side Panel (Split Layout)**
```css
.container { display:grid; grid-template-columns:55% 45%; height:100%; }
.photo-side { background-image:url('...'); background-size:cover; }
.text-side { background:#1a1a2e; display:flex; flex-direction:column;
  justify-content:center; padding:50px; }
.headline { font-size:44px; font-weight:800; color:#fff; }
```

**Style 5: Floating Glass Card (Frosted)**
```css
.card { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  backdrop-filter:blur(16px) saturate(180%);
  background:rgba(255,255,255,0.15); border-radius:20px;
  border:1px solid rgba(255,255,255,0.25); padding:50px 40px;
  max-width:80%; text-align:center; }
.headline { font-size:52px; font-weight:800; color:#fff; }
```

**Style 6: Full-Screen Dimmed + Giant Text**
```css
.overlay { position:absolute; inset:0; background:rgba(0,0,0,0.6);
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; padding:80px; text-align:center; }
.headline { font-size:72px; font-weight:900; color:#fff; line-height:1.1;
  text-transform:uppercase; letter-spacing:2px; }
```

**Style 7: Corner Badge + Bottom Text**
```css
.badge { position:absolute; top:30px; right:30px;
  background:#ef4444; color:#fff; font-size:18px; font-weight:700;
  padding:12px 20px; border-radius:50px; transform:rotate(5deg); }
.bottom-text { position:absolute; bottom:40px; left:40px; right:40px; }
.headline { font-size:44px; font-weight:800; color:#fff;
  text-shadow:0 2px 12px rgba(0,0,0,0.8); }
```

**Style 8: Diagonal Split**
```css
.photo-side { position:absolute; inset:0;
  clip-path:polygon(0 0, 65% 0, 35% 100%, 0 100%); }
.text-side { position:absolute; right:0; top:0; width:55%; height:100%;
  background:#0f172a; display:flex; flex-direction:column;
  justify-content:center; padding:40px 50px 40px 100px; }
.headline { font-size:44px; font-weight:800; color:#fff; }
```

**Style 9: Bottom Left Compact (Sticker-Style)**
```css
.sticker { position:absolute; bottom:40px; left:40px;
  background:rgba(0,0,0,0.85); padding:24px 32px; border-radius:12px;
  max-width:70%; }
.headline { font-size:36px; font-weight:700; color:#fff; }
.subheadline { font-size:20px; color:#fbbf24; margin-top:8px; }
```

**Style 10: Top + Bottom Sandwich**
```css
.top-bar { position:absolute; top:0; left:0; right:0;
  background:rgba(0,0,0,0.8); padding:24px 40px; }
.top-text { font-size:20px; color:#fbbf24; font-weight:600; text-transform:uppercase; }
.bottom-bar { position:absolute; bottom:0; left:0; right:0;
  background:rgba(0,0,0,0.85); padding:40px; }
.headline { font-size:48px; font-weight:800; color:#fff; }
```

**Zuweisungs-Regel:** Bei 20+ Ads pro Run → JEDER Style mindestens 2x nutzen. Verteilung soll gleichmäßig sein. NIEMALS mehr als 3 Ads mit dem gleichen Style.

#### Base HTML Template (alle Styles nutzen dieses Grundgerüst)
```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1080px; position:relative; overflow:hidden;
    font-family:'Helvetica Neue',Arial,sans-serif; }
  .bg { width:100%; height:100%;
    background-image:url('data:image/png;base64,...');
    background-size:cover; background-position:center; }
  /* === STYLE-SPEZIFISCHES CSS HIER === */
</style></head>
<body>
  <div class="bg"></div>
  <!-- === STYLE-SPEZIFISCHES HTML HIER === -->
</body></html>
```

**Workflow:**
1. Gemini → Bild ohne Text generieren → als PNG speichern
2. PNG base64-encoden → in HTML als background-image einbetten
3. Headline + Subheadline als HTML/CSS Overlay drüber
4. HTTP-Server starten → Playwright screenshot (1080x1080) → Original-PNG überschreiben
5. Read-Tool: Screenshot prüfen ob Text lesbar und korrekt

**NIEMALS deutschen Text direkt in Gemini-Bilder generieren lassen** — Umlaute und Komposita werden fast immer falsch geschrieben.

Für reine Text-Ads (Chat-Screenshots, Statistiken, Checklisten): Komplett als HTML/CSS bauen, kein Gemini-Bild nötig.

**Alternativ via Bash mit curl:**
```bash
GEMINI_API_KEY="${GEMINI_API_KEY}"
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key=${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "PROMPT"}]}],
    "generationConfig": {"responseModalities": ["IMAGE", "TEXT"]}
  }' | python3 -c "
import sys, json, base64
data = json.load(sys.stdin)
for part in data['candidates'][0]['content']['parts']:
    if 'inlineData' in part:
        img = base64.b64decode(part['inlineData']['data'])
        with open('OUTPUT_PATH', 'wb') as f:
            f.write(img)
        print('Image saved')
"
```

### Prompt-Strategie für Image-Generation

#### Indirect Ads (kein Produkt im Bild)
```
Photorealistic image for social media ad. [SZENE-BESCHREIBUNG].
Style: looks like an organic social media post, not an advertisement.
No text overlay. No logos. No product packaging.
Natural lighting, authentic feel, slightly imperfect composition.
Aspect ratio: [1:1 / 4:5 / 9:16].
```

**Varianten für Indirect:**
- **Native Post Style:** "Candid photo of [Person aus Persona], [Situation], taken with smartphone, Instagram-style"
- **Nachrichten-Style:** "Breaking news graphic, dark background, bold white text: '[HEADLINE]', red accent bar, news channel aesthetic"
- **Screenshot-Style:** "Screenshot of a smartphone chat conversation about [Thema], iMessage style, realistic"
- **Statistik/Infografik:** "Minimalist infographic showing [STATISTIK], dark background, one accent color, clean data visualization"
- **Warnung/Alert:** "Emergency alert notification on smartphone screen, amber alert style, [THEMA]"

#### Direct Ads (Produkt im Bild)
```
Product advertisement image. [PRODUKT] shown prominently.
Clean background, professional product photography style.
Include text overlay: "[BENEFIT-STATEMENT]"
Brand colors: [FARBEN]. Font: bold sans-serif.
[Optional: price tag, badge, checkmarks]
Aspect ratio: [1:1 / 4:5 / 9:16].
```

**Für Direct Ads mit Text:**
- Nano Banana Pro kann Text im Bild generieren — aber prüfe IMMER auf Rechtschreibfehler
- Wenn Text fehlerhaft → Bild ohne Text generieren, Text mit HTML/CSS Overlay hinzufügen
- Produkt-PNG auf weißem Hintergrund als Referenz hochladen wenn verfügbar

### Recraft AI für Testimonial-Porträts
```bash
curl -X POST "https://external.api.recraft.ai/v1/images/generations" \
  -H "Authorization: Bearer $RECRAFT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Professional headshot of [ALTER] year old [GESCHLECHT] German person, [BESCHREIBUNG], natural lighting, casual, warm smile, white background, photorealistic",
    "style": "realistic_image",
    "model": "recraftv3",
    "size": "1024x1024"
  }'
```

### Aspect Ratios
| Ratio | Pixel | Verwendung |
|-------|-------|------------|
| 1:1 | 1080x1080 | Feed (Instagram + Facebook) — **Default** |
| 4:5 | 1080x1350 | Feed (mehr Fläche, empfohlen für Scroll-Stopper) |
| 9:16 | 1080x1920 | Stories + Reels Placement |

**Best Practice:** Jedes Konzept in 1:1 generieren. Wenn the Owner "all" wählt → auch 4:5 und 9:16 Varianten.

---

## COPY-ERSTELLUNG (Primary Text, Headline, Description)

### Für INDIRECT Ads (Long-Form Primary Text)

**Struktur (300-800 Wörter):**

```
[HOOK — 1-2 Sätze, PIG-Test bestanden]

[PROBLEM-AGITATION — 3-5 Sätze]
- Beschreibe das Problem in VOC-Sprache
- Agitate: mach es schlimmer, konkreter, persönlicher
- "Stell dir vor..." Szenarien

[STORY/BRIDGE — 3-5 Sätze]
- Wie die Lösung entdeckt wurde
- Glaubwürdige Quelle (Experte, Studie, persönliche Erfahrung)
- "Was die meisten nicht wissen..."

[SOLUTION-SEED — 3-5 Sätze]
- Erste Andeutung der Lösung
- NICHT das Produkt nennen — nur die Kategorie/den Ansatz
- "Es gibt eine Methode die..."

[SOCIAL PROOF — 2-3 Sätze]
- Zahlen, Testimonials, Autorität
- "Über X Personen haben bereits..."

[CTA — 1-2 Sätze]
- Soft CTA: "Link im Kommentar" / "Mehr dazu im Link"
- NICHT hard-sell — der Funnel (Listicle/Advertorial/Quiz) macht den Verkauf
```

**Headline:** 1 Satz, max 40 Zeichen. Benefit oder Curiosity.
**Description:** 1 Satz, max 30 Zeichen. "Jetzt lesen →" oder "Zum Artikel →"

### Für DIRECT Ads (Short-Form Primary Text)

**Struktur (50-200 Wörter):**

```
[HOOK — 1 Satz, Benefit oder Offer]

[BENEFITS — 3-5 Bullet Points]
✅ Benefit 1
✅ Benefit 2
✅ Benefit 3

[SOCIAL PROOF — 1 Satz]

[OFFER — 1-2 Sätze]
Preis, Rabatt, Garantie

[CTA — 1 Satz]
"Jetzt sichern" / "Hier bestellen" / "Link in Bio"
```

**Headline:** Angebot oder stärkster Benefit. Max 40 Zeichen.
**Description:** Urgency oder Garantie. Max 30 Zeichen.

---

## OUTPUT-STRUKTUR

### Dateistruktur
```
[projekt]/ads/
├── ad-concepts.md              ← Alle Konzepte als Übersicht (Copy + Strategie)
├── indirect/
│   ├── concept-01-[name].png   ← Generierte Bilder
│   ├── concept-02-[name].png
│   ├── concept-03-[name].png
│   ├── concept-04-[name].png
│   ├── concept-05-[name].png
│   └── ...
├── direct/
│   ├── concept-01-[name].png
│   ├── concept-02-[name].png
│   ├── concept-03-[name].png
│   └── ...
└── _prompts/
    └── generation-prompts.md   ← Alle Image-Prompts (für Iteration)
```

```bash
mkdir -p "[projekt]/ads/indirect" "[projekt]/ads/direct" "[projekt]/ads/_prompts"
```

### ad-concepts.md Format

```markdown
# Ad Creatives — [Produkt]
Erstellt: [Datum] | Persona: [Name] | Projekt: [Projekt]

## Strategie-Übersicht

| Metrik | Wert |
|--------|------|
| Total Konzepte | X |
| Indirect (Cold) | X |
| Direct (Retargeting) | X |
| Ziel-CPA | €X |
| Funnel-URL | [URL] |
| Awareness-Spectrum | Unaware → Most Aware |

---

## INDIRECT ADS (Cold Traffic → Funnel)

### Konzept 1: [NAME]
**Angle:** [Fear/Urgency/Social Proof/etc.]
**Awareness:** [Unaware/Problem-Aware]
**Consciousness:** [Level] → [Level] → [Level]
**Necessary Belief:** #X — "[Belief]"
**Format:** [Native Static / Screenshot / Statistik / etc.]
**Bild:** `indirect/concept-01-[name].png`

**Image-Prompt:**
> [Der Prompt der für die Bildgenerierung verwendet wurde]

**Primary Text:**
> [Kompletter Ad-Copy — 300-800 Wörter]

**Headline:** [Max 40 Zeichen]
**Description:** [Max 30 Zeichen]
**CTA-Button:** Learn More
**Ziel-URL:** [Listicle/Advertorial/Quiz URL]

**Warum dieses Konzept funktioniert:**
- [Erklärung des psychologischen Mechanismus]
- [Welcher Kontrast wird erzeugt]
- [Welche VOC-Sprache wird genutzt]

---

### Konzept 2: [NAME]
[...]

---

## DIRECT ADS (Retargeting → Checkout)

### Konzept 1: [NAME]
[gleiche Struktur, aber mit kurzem Primary Text]

---

## Testing-Empfehlung

### CBO-Struktur (Post-Andromeda)
| Ad Set | Konzept | Ads | Typ |
|--------|---------|-----|-----|
| AS1 | [Konzept-Name] | 3 Variationen | Indirect |
| AS2 | [Konzept-Name] | 3 Variationen | Indirect |
| AS3 | [Konzept-Name] | 3 Variationen | Indirect |

**Budget:** [Anzahl Ads] × $10 = $[X]/Tag (Minimum $50/Tag)
**Targeting:** Broad (Advantage+, 18-65+, alle Geschlechter)
**Optimierung:** Conversions → Purchases
**Attribution:** 7-Day Click, 1-Day View
**Start:** Nächster Tag, 6:00 Uhr morgens
**Enhancements:** ALLE AUS (kein Overlay, kein Text, keine Animation, keine Musik)

### Variations-Plan
Nach 48-72h Daten → für Gewinner-Konzept(e):
- 3-5 Variationen erstellen (Copy-Tweaks, Bild-Variationen, Hook-Alternativen)
- In eigenen Ad Sets testen
- NICHT Variations spammen — neue Konzepte > Variationen (Post-Andromeda)
```

---

## ABLAUF (Step by Step)

### Step 0: FUNNEL-FRAGE (IMMER ZUERST!)
1. the Owner fragen: "Für welchen Funnel? Listicle / Advertorial / Quiz / Direct?"
2. Landing Page des Funnels lesen (HTML/Content)
3. Tonalität + Hook-Stil + CTA des Funnels verstehen
4. Ad-Copy auf nahtlosen Übergang zum Funnel-Einstieg abstimmen

### Step 1: Research laden & Angles identifizieren
1. Foundational Docs lesen (Personas, Offer Brief, VOC, Before/After, Deep Dive)
2. Aus gewählter Persona die Top-Angles extrahieren:
   - Stärkste Pains (→ Fear/Shame Angles)
   - Stärkste Desires (→ Transformation/Aspiration Angles)
   - Stärkste Objections (→ Anti-Category/Authority Angles)
   - Stärkste Social Proofs (→ Social Proof/Statistics Angles)
3. Ad-Angle-Matrix erstellen (intern) — mindestens 10 verschiedene Angles
4. Für jeden Angle den Hook schreiben + PIG-Test

### Step 2: Format-Verteilungsplan erstellen
1. Aus den 16 Format-Typen 8-10 auswählen die zum Funnel passen
2. **Varianten-Multiplikator:** Pro Format 2-3 inhaltlich verschiedene Varianten planen
3. **Overlay-Style-Verteilung:** 10 Placement-Styles gleichmäßig über alle Ads verteilen
4. Ziel: 20-25 Ads total mit maximaler visueller Diversität
5. Format-Mix dokumentieren: z.B. "3x Chat, 3x Notification, 2x Native Photo, 2x Statistik, 2x Checkliste, 2x Meme, 2x Nachrichten, 2x Before/After, 2x Frage-Karte"

### Step 3: Ad-Concepts erstellen
1. Pro Concept:
   - Format + Overlay-Style zuweisen (aus Step 2 Plan)
   - Image-Prompt formulieren (Foto-Formate) ODER HTML/CSS-Konzept (Text-Formate)
   - Primary Text schreiben (Lang für Indirect, Kurz für Direct)
   - Headline + Description + CTA
2. Emotional Delta Map pro Concept
3. Necessary Belief Mapping
4. **Sicherstellen:** Jede Ad sieht visuell ANDERS aus als alle anderen

### Step 4: Images generieren (Batch-Workflow)
1. **Foto-Ads:** Alle Gemini-Prompts vorbereiten → Batch-Generierung → Text-Overlays mit verschiedenen Placement-Styles
2. **HTML/CSS-Ads:** Templates bauen → Playwright Screenshots
3. Pro Concept mindestens 2 Bild-Varianten generieren → beste auswählen
4. **OVERLAY-STYLE VARIIEREN:** Nicht alle bottom-gradient! Verschiedene Styles nutzen (siehe 10 Placement-Styles)
5. Bilder speichern in `[projekt]/ads/[funnel-name]/`
6. **Testimonial-Porträts** (wenn nötig) → Recraft AI

### Step 5: Preview-Seite bauen
1. HTML-Grid-Preview mit ALLEN Creatives
2. Filter-Buttons: All / Foto / HTML / nach Format-Typ
3. Jede Card zeigt: Bild, Name, Angle, Format, Overlay-Style
4. Über lokalen HTTP-Server ausliefern → Playwright Screenshot für the Owner

### Step 6: Documentation
1. `ad-concepts.md` erstellen mit allen Konzepten
2. Image-Prompts in `_prompts/generation-prompts.md` archivieren
3. Testing-Empfehlung mit CBO-Struktur
4. Format-Verteilung + Overlay-Style-Verteilung dokumentieren

### Step 7: QA & Präsentation
1. Alle Bilder visuell prüfen (Text korrekt? Overlay-Style variiert?)
2. Copy auf VOC-Sprache prüfen (keine Marketing-Buzzwords?)
3. **Visueller Diversitäts-Check:** Sehen die Ads alle UNTERSCHIEDLICH aus? Wenn >3 gleich aussehen → überarbeiten
4. the Owner die Konzepte präsentieren:
   - Preview-Seite zeigen (alle auf einen Blick)
   - Tier-Ranking (welche zuerst testen?)
   - CBO-Budget-Empfehlung

---

## SWIPE-MODUS (Optional)

Wenn the Owner eine Wettbewerber-Ad liefert (Screenshot, URL, oder "schau mal was die machen"):

### Swipe-Prozess
1. **Analysieren:** Was macht die Ad erfolgreich?
   - Welcher Awareness-Stage?
   - Welcher psychologischer Mechanismus?
   - Welches Format?
   - Was ist der Hook?
2. **Philosophie extrahieren (NICHT Copy swipen!):**
   - Framework identifizieren (z.B. "Statistik + Scham + Lösung")
   - Emotional Delta Map der Original-Ad
   - Warum funktioniert der Scroll-Stopper?
3. **Eigene Version erstellen:**
   - Gleiches Framework, aber mit unserer VOC-Sprache
   - Gleiches Format, aber mit unserem Angle
   - Image mit Nano Banana Pro generieren
4. **Kontrast sicherstellen:**
   - Unsere Version muss sich VISUELL unterscheiden
   - Gleiche Philosophie ≠ gleiches Aussehen

**"Swipe philosophy, not copy."** — Wenn du die Philosophie swipst, kannst du sie auf alles anwenden. Wenn du Copy swipst, hast du genau eine Ad.

---

## ITERATION & VARIATIONEN

### Wann neue Variationen erstellen
- Nach 48-72h Laufzeit: Daten auswerten
- Gewinner-Konzepte identifizieren (niedrigster CPC/CPA, höchste CTR)
- Für Gewinner: 3-5 Variationen erstellen

### Was variieren (eine Variable pro Variation)
1. **Hook-Text** — gleicher Angle, andere Formulierung
2. **Bild-Stil** — gleicher Angle, anderer visueller Ansatz
3. **Primary Text Länge** — kurz vs. lang Version
4. **Farb-Schema** — dark vs. light, andere Akzentfarbe
5. **Format** — 1:1 → 4:5, oder umgekehrt
6. **CTA** — "Learn More" vs. "Shop Now" vs. "Sign Up"

### Was NICHT variieren
- NICHT mehrere Variablen gleichzeitig ändern
- NICHT den Angle/die Philosophie ändern (das wäre ein neues Konzept)
- NICHT das Produkt/Angebot ändern

### Post-Andromeda Ratio
- **80% neue Konzepte, 20% Variationen** von Gewinnern
- Creative Diversity > Variation Spamming
- Facebook belohnt frische, diverse Creatives stärker als Variationen

---

## QUALITÄTS-CHECK

### Copy-Qualität
- [ ] Jeder Hook besteht den PIG-Test (Punch in the Gut)?
- [ ] VOC-Sprache verwendet (keine Marketing-Buzzwords)?
- [ ] 5th-8th Grade Reading Level?
- [ ] Klarheit > Cleverness bei JEDEM Satz?
- [ ] Emotional Delta klar definiert pro Konzept?
- [ ] Necessary Beliefs werden adressiert?
- [ ] Indirect = kein Produkt-Pitch im Copy (das macht der Funnel)?
- [ ] Direct = klares Angebot + Social Proof?

### Bild-Qualität
- [ ] Indirect: Sieht NICHT wie eine Ad aus?
- [ ] Direct: Produkt klar erkennbar?
- [ ] Text im Bild fehlerfrei (kein AI-Typo)?
- [ ] Aspect Ratio korrekt (1:1, 4:5, oder 9:16)?
- [ ] Visueller Kontrast zum Feed (Pattern-Break)?
- [ ] Keine Copyright-Probleme (AI-generiert = safe)?

### Strategie
- [ ] Mindestens 3 verschiedene Angles vertreten?
- [ ] Awareness-Spectrum abgedeckt (Unaware → Product-Aware)?
- [ ] Consciousness-Levels variieren (Fear, Courage, Willingness)?
- [ ] Testing-Plan mit CBO-Struktur?
- [ ] Budget-Empfehlung realistisch ($10/ad, min $50/Tag)?
- [ ] Alle Ziel-URLs korrekt (Funnel-Pages für Indirect, Checkout für Direct)?

### Technik
- [ ] Bilder in korrektem Ordner gespeichert?
- [ ] ad-concepts.md vollständig?
- [ ] Prompts archiviert (für Iteration)?
- [ ] Dateien via Bash geschrieben (nicht Write/Edit — VSCode Bug)?

---

## WICHTIGE REGELN

1. **FUNNEL-FRAGE ZUERST.** Bevor eine einzige Ad erstellt wird: Welcher Funnel? Listicle/Advertorial/Quiz/Direct?
2. **Research-First.** Keine Ads ohne Foundational Docs. Jeder Hook kommt aus der VOC-Research.
3. **Kontrast > Ästhetik.** Lieber "ugly" und klar als hübsch und langweilig.
4. **Indirect für Cold, Direct für Retargeting.** Nie verwechseln.
5. **Indirect leitet auf Pre-Sell (Listicle/Advertorial/Quiz).** NIE direkt auf Checkout.
6. **Direct leitet auf Checkout/Produktseite.** Kein Umweg über Pre-Sell nötig.
7. **Swipe Philosophy, not Copy.** Framework extrahieren, nicht Text kopieren.
8. **Engine je Use-Case wählen** (siehe Engine-Selection-Tabelle): GPT-Image-2 für Text-im-Bild, Nano Banana für Photo/Edits, Recraft für Headshots/Stil, HTML/CSS für UI-Mockups. Kein Midjourney, kein DALL-E.
9. **JEDES Bild braucht Text-Overlay.** Kein Foto-Ad ohne Headline + Subheadline. Foto = Scroll-Stopper, Text = Click-Trigger. Beides zusammen = Ad.
10. **Text-im-Bild via GPT-Image-2 ODER HTML/CSS-Overlay.** GPT-Image-2 rendert deutschen Text inkl. Umlaute zuverlässig (~99%) — direkt in einem Shot. Bei Nano Banana / Gemini IMMER Text als HTML/CSS + Playwright-Overlay (sonst Typos). Bei GPT-Image-2-Outputs trotzdem visuell prüfen.
11. **OVERLAY-STYLES VARIIEREN!** NICHT alle Ads mit dem gleichen Bottom-Gradient. 10 verschiedene Placement-Styles nutzen, gleichmäßig verteilen. Max 3 Ads pro Style.
12. **FORMAT-VARIANTEN PFLICHT.** Pro verwendetem Format-Typ mindestens 2-3 inhaltlich verschiedene Varianten. Nicht 1x Chat + 1x Notification. Sondern 3x Chat + 2x Notification + etc.
13. **20-25 Ads pro Funnel-Kampagne.** Meta Andromeda belohnt Creative Diversity. Mehr verschiedene Konzepte > wenige Variationen.
14. **80/20 Post-Andromeda.** 80% neue Konzepte, 20% Variationen von Gewinnern.
15. **CBO Testing.** Min. 3 Ad Sets (= 3 Konzepte), $10/ad, min. $50/Tag, broad targeting.
16. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).
17. **Emotional Delta ist Pflicht.** Ohne die emotionale Reise ist die Ad nur ein Bild mit Text.
18. **Alle Enhancements AUS in Meta.** Kein Overlay, keine Text-Verbesserungen, keine Animation, keine Musik.
19. **Preview-Seite IMMER bauen.** Am Ende jeder Generierung eine HTML-Grid-Preview mit allen Ads.

## NEUE TECHNIKEN (V3 Update — April 2026)

### Aus Video-Analyse (Mark Builds Brands + Alex Cooper)

#### Bild-Prompting: Was echte Scroll-Stopper ausmacht
1. **"High contrast" + "bold composition"** explizit prompten — NICHT "professional" oder "clean" (das produziert technisch perfekte, aber langweilige Bilder)
2. **Overprompting vermeiden:** Kürzere, präzisere Prompts liefern oft bessere Ergebnisse als 15-Zeilen-Monster
3. **Nightmare-Only Bilder:** NUR den Pain zeigen, KEINE Lösung andeuten — erzeugt maximale Neugier (z.B. leerer Kühlschrank, Panik-Szene)
4. **Transformation-Split:** Links Nightmare (blau/kalt), rechts Dream (warm/orange) — visueller Before/After ohne Policy-Risiko
5. **Native-Photography-Style:** "Taken with iPhone, slightly imperfect, candid" → sieht aus wie ein organischer Post
6. **Situational Context:** Immer eine PERSON in einer SITUATION zeigen, nicht nur Objekte. Gesichter stoppen den Scroll.
7. **Emotional Lighting:** Kerzenschein = Angst/Intimität, Sturmwolken = Bedrohung, Warmes Licht = Sicherheit/Lösung

#### Text-Overlay-Strategien die konvertieren
1. **Minimal-Text-Regel:** Max 5-7 Wörter als Headline auf dem Bild. Die Verkaufsarbeit passiert im Primary Text.
2. **Bottom-Gradient-Overlay:** Transparent oben → rgba(0,0,0,0.85) unten = Text lesbar auf JEDEM Hintergrund
3. **Headline-Formate die performen:**
   - Provokante Frage: "Hättest du einen Plan?"
   - Unvollständiger Satz: "Wenn der Strom ausfällt..."
   - Statistik-Schock: "73% der Deutschen..."
   - Identitäts-Trigger: "Du bist 30 und hast keine Taschenlampe."
4. **Subheadline = CTA-Seed:** Nicht "Jetzt kaufen" sondern "Die Wahrheit über..." / "Was die BBK empfiehlt..."
5. **Kein Text > Schlechter Text:** Lieber ein starkes Bild ohne Overlay als ein mittelmäßiges mit generischem Text
6. **4:5 Ratio für mehr Feed-Fläche:** 1080x1350 statt 1080x1080 — nimmt mehr Screen-Raum ein

#### Format-Vielfalt (40-Format-Playbook)
Basierend auf dem Alex Cooper / Mark Builds Brands Framework gibt es 40+ bewährte Static-Ad-Formate. Die Top-10 für Indirect Cold Traffic:

| # | Format | Beschreibung | Wann einsetzen |
|---|--------|-------------|----------------|
| 1 | **Headline-Hero** | Ein großes Bild + eine kurze Headline | Universell, jeder Angle |
| 2 | **Us vs Them** | Zwei Spalten, visueller Vergleich | Vergleich, Differenzierung |
| 3 | **Social Comment Screenshot** | Sieht aus wie ein Social-Media-Kommentar | Social Proof, Testimonial |
| 4 | **Before/After Split** | Links vorher, rechts nachher (animiert = sicherer) | Transformation |
| 5 | **Statistik-Hero** | EINE große Zahl + kurze Erklärung | Authority, Schock |
| 6 | **Chat-Screenshot** | iMessage/WhatsApp-Style Konversation | Native, Personal |
| 7 | **Notification-Stack** | Smartphone-Benachrichtigungen | Urgency, Relatability |
| 8 | **Checkliste** | Grüne Haken + rote Kreuze | Identity, Self-Assessment |
| 9 | **Nachrichten-Headline** | Breaking-News-Style mit Ticker | Authority, Urgency |
| 10 | **Kosten-Vergleich** | Alltags-Ausgaben vs. Produkt-Kosten | Objection-Killer |

#### Qualitäts-Kriterien: "Gut" vs "Krass"

| Kriterium | "Gut" (V2-Level) | "Krass" (V3-Level) |
|-----------|-------------------|---------------------|
| Scroll-Stop | Stoppt das Scrollen | Erzeugt ein GEFÜHL bevor man den Text liest |
| Authentizität | Sieht nicht wie Werbung aus | Sieht aus wie ein Post den man teilen würde |
| Emotional Punch | Triggert einen Pain/Desire | Triggert eine SPEZIFISCHE Erinnerung ("Das war ich letzten Winter") |
| Text-Integration | Text ist lesbar | Text fühlt sich wie Teil des Bildes an, nicht aufgeklebt |
| VOC-Match | Nutzt Zielgruppen-Sprache | Nutzt EXAKTE Zitate aus der VOC-Research |
| Kontrast | Anders als typische Ads | Anders als ALLES im Feed (Posts, Stories, Memes) |

#### Workflow-Optimierungen (V3)
1. **Batch-Generation:** Alle Bild-Prompts vorbereiten → alle Bilder in einem Durchlauf generieren → dann alle Text-Overlays
2. **Quality Gate:** JEDES Bild nach Generierung mit Read-Tool prüfen. Kriterien: Fotorealismus, keine AI-Artefakte, emotionaler Impact
3. **VOC-Headlines statt generische:** Vor der Headline-Erstellung die Top-10 VOC-Zitate rausziehen → als Headline-Basis nutzen
4. **Zwei Generierungen pro Konzept:** Immer 2 Bilder generieren, das bessere nehmen
5. **HTML-Templates wiederverwenden:** Overlay-HTML als Template, nur Bild + Text tauschen
6. **Preview-Seite bauen:** Am Ende IMMER eine HTML-Grid-Preview mit allen Creatives (für the Owner und für eigene QA)

### Aus Web-Research (April 2026)

24. **4:5 Ratio outperformt 1:1** — nimmt mehr Screen-Raum ein, signifikant höhere CTR. Default sollte 4:5 sein.
25. **Meta empfiehlt jetzt 1440px statt 1080px** — 1440x1440 (1:1) oder 1440x1800 (4:5) für High-Density Screens.
26. **Carousel Ads = 30-50% höhere CTR** als Single Image — für zukünftige Iterationen relevant.
27. **Headline unter 27 Zeichen** optimal (Meta truncation). Primary Text 50-150 Zeichen für die Vorschau.
28. **Text-Overlay wird nicht mehr bestraft** (alte 20%-Regel abgeschafft) — aber Algorithmus deprioritisiert trotzdem überladene Bilder.
29. **98% Mobile Users** — ALLES mobile-first designen. Großer Text, simple Komposition, kein Clutter.
30. **UGC-Style outperformt Hochglanz** konsistent — AI-Bilder mit "candid" und "imperfect" prompten.
31. **Faces = Scroll-Stop:** Menschliches Gehirn reagiert auf Gesichter stärker als auf alles andere. IMMER eine Person im Bild wenn möglich.
32. **3-Sekunden-Regel:** Die Ad muss in 3 Sekunden kommunizieren warum jemand weiterlesen soll. Kein Rätsel, kein Mystery — klarer visueller Hook.
33. **Nano Banana 2 = State of the Art (April 2026).** 90-95% der Generierungen sind sofort brauchbar. Produktlabels, Text, Details — alles besser als V1.

---

## LEARNINGS

1. **"Ugly ads = pretty profits"** — Die profitabelsten Ads sehen oft unprofessionell aus. Klarheit schlägt Ästhetik.
2. **Indirect Ads skalieren am meisten auf Cold Traffic.** Direct Ads sind für Retargeting.
3. **Post-Andromeda: Creative Diversity > Variation Spamming.** Facebook belohnt diverse, neue Konzepte stärker.
4. **Deutscher Text im Bild = Achillesferse.** Nano Banana Pro macht bei deutschem Text (Umlaute, Komposita) häufig Typos. Indirect Ads OHNE Text im Bild kommen exzellent raus. Bei Direct Ads mit Text: entweder Bild ohne Text generieren + HTML/CSS Overlay, oder jedes Bild einzeln auf Fehler prüfen.
5. **Indirect Ads ohne Text = beste Qualität.** Fotorealistische Szenen ohne Text-Overlay sind der Sweet Spot von Nano Banana Pro — 1-2MB, magazinqualität, sofort einsetzbar.
6. **Swipe Philosophy:** Wer die Philosophie swipet, kann sie auf jede Nische anwenden. Wer Copy swipet, hat eine Ad.
6. **Hook = 90% des Erfolgs.** Wenn der Hook nicht "puncht", ist der Rest egal.
7. **VOC-Sprache > Marketing-Sprache.** "Stromausfall im Winter, Kinder frieren" schlägt "Stromausfallschutz für Ihre Familie".
8. **$10/ad Minimum-Budget** — unter $50/Tag CBO nicht starten.
9. **Breites Targeting (18-65+, Advantage+)** schlägt Micro-Targeting Post-Andromeda.
10. **Reihenfolge: Indirect zuerst testen** (größeres Skalierungs-Potenzial), dann Direct für Retargeting.
11. **Before/After Ads: Vorsicht mit Meta Policy.** Können restricted/rejected werden — aber extrem effektiv.
12. **Product-PNG auf weißem Hintergrund** als Referenz für Nano Banana hochladen = bessere Ergebnisse bei Direct Ads.
13. **Primary Text bei Indirect ist länger als erwartet** (300-800 Wörter). Das ist gewollt — Direct Response Copy, nicht Ad-Copy.
14. **"Der Typ der am meisten für einen Kunden ausgeben kann, gewinnt."** (Dan Kennedy) — Darum: AOV + LTV maximieren.
15. **Gemini Modell:** `gemini-2.5-flash-image` (NICHT `gemini-2.5-flash-preview-04-17` — das gibt 404). Immer aktuelles Image-Modell nutzen.
16. **HTML/CSS Text-Ads > AI-generierter Text.** Chat-Screenshots, Smartphone-Notifications, Statistik-Karten, Checklisten — alles als HTML/CSS bauen, mit Playwright screenshotten. Null Typos, volle Kontrolle.
17. **Chat-Screenshot-Format** ist einer der stärksten Native-Formate. Sieht aus wie ein weitergeleiteter Chat — maximaler Pattern-Break.
18. **Smartphone-Notification-Format** (Katastrophenwarnung + Bank + Supermarkt Notifications) — extrem relatable, jeder kennt den Alarm.
19. **Versicherungs-Vergleich als Rationalisierungs-Killer.** KFZ, Hausrat, Zahnzusatz = alles gecheckt. Notvorrat = fehlt. Die Absurdität verkauft.
20. **Neues Projekt = NUR Indirect Ads.** Kein Retargeting-Pool vorhanden, also ausschließlich Cold Traffic Konzepte.
21. **Mindestens 15 Konzepte pro Runde.** 5 waren zu wenig — je mehr Angles, desto höher die Chance einen Winner zu finden.
22. **Tier-System für Priorisierung.** Tier 1 = sofort testen, Tier 2 = zweite Runde, Tier 3 = Nische. Nicht alles gleichzeitig launchen.
23. **Port 8892 für HTML-Preview-Server** — fest definiert, keine Konflikte mit anderen Projekten.

## V4 UPDATE (April 2026) — Funnel-First + Creative Diversity

### Neue Prinzipien
24. **Funnel-First-Flow:** Skill fragt IMMER zuerst welcher Funnel (Listicle/Advertorial/Quiz/Direct) → Ads werden auf den Funnel getailored.
25. **Text-Overlay-Variabilität:** 10 verschiedene Placement-Styles (nicht nur bottom-gradient). Gleichmäßig verteilen, max 3 Ads pro Style.
26. **Format-Varianten-Multiplikator:** Pro Format-Typ mindestens 2-3 inhaltlich verschiedene Varianten. 1x Chat reicht nicht — 3x Chat mit verschiedenen Gesprächen.
27. **20-25 Ads pro Funnel-Kampagne:** Meta Andromeda belohnt Diversity. Mehr verschiedene Konzepte schlagen Variationen.
28. **Visueller Diversitäts-Check:** Am Ende jeder Generierung prüfen: Sehen >3 Ads gleich aus? → überarbeiten.
29. **Preview-Seite ist Pflicht:** Am Ende IMMER eine HTML-Grid-Preview mit Filter-Buttons bauen.

### Andromeda-Insights (aus Research April 2026)
- Meta Andromeda erkennt Near-Duplicates und filtert sie → jede Ad MUSS visuell distinct sein
- Algorithmus nutzt Creative als Targeting-Signal → mehr Diversity = mehr Signale = bessere Auslieferung
- 10-20 unique Concepts pro Ad Set ist der Sweet Spot (Jon Loomer, Foxwell Digital, MTM Agency)
- "Blue vs. Red Background" zählt NICHT als visuell different — braucht verschiedene Formate, Angles, Styles
- Creative Refresh alle 7-14 Tage oder bei 15-20% Performance-Drop
- Fewer campaigns, fewer ad sets, MORE creatives per ad set (Post-Andromeda-Struktur)

## V5 UPDATE (April 2026) — GPT-Image-2 als neue Default-Engine für Text-im-Bild

### Was sich geändert hat
- **GPT-Image-2 (OpenAI, Release 2026-04-21) wird neue Default-Engine** für alle Ads bei denen Text präzise im Bild stehen soll (Headlines, Statistiken, Quotes als Bildbestandteil)
- Nano Banana bleibt für photorealistische Indirect Ads OHNE Text + alle Edit/Reframe-Jobs
- Recraft bleibt für Headshots + stilisierte Illustrationen
- HTML/CSS bleibt für UI-Mockup-Formate (Chat, Notification, Statistik-Karte)

### Warum GPT-Image-2 für Text-im-Bild
- ~99% Text-Accuracy auch auf Deutsch (Umlaute, Komposita) — Nano Banana liegt deutlich darunter
- Layout-Reasoning + Multi-Element-Composition in einem Shot — kein HTML-Overlay-Step nötig
- Bis 16 Reference-Images für Brand-Konsistenz/Produktshots

### Wann NICHT GPT-Image-2
- Photorealistische Lifestyle-Szenen → Nano Banana ist besser bei Skin/Lighting
- Story-Serien mit gleichem Charakter über mehrere Frames → Cross-Image-Drift (kein Modell löst das aktuell)
- Hochvolumen-Batch ohne Text → Nano Banana 8x günstiger bei medium quality

### Neue Format-Typen (V4)
- **DM Inbox Flood** — Instagram DM-Inbox mit vielen Nachrichten → FOMO + Demand
- **Forum/Reddit Post** — "Hat jemand Erfahrung mit..." → organische Empfehlung
- **Email-Screenshot** — "FWD: Das musst du sehen" → Personal Recommendation
- **Tweet/X Post** — Viraler Tweet der das Produkt lobt
- **Poll/Quiz-Ergebnis** — "87% haben gewählt..." → interaktives Gefühl
- **Handwritten Note** — Empfehlung auf Notizzettel → persönlich, nicht kommerziell
- **Receipt/Bestellbestätigung** — "Alle kaufen das" → Social Proof durch Transaktion
