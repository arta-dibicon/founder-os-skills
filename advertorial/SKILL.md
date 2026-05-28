---
name: advertorial
description: "Erstelle eine komplette Advertorial-Landing-Page (HTML) für ein Produkt. TRIGGER wenn the Owner sagt 'Advertorial für [X]', 'Editorial für [X]', 'Pre-Sale Page bauen', oder '/advertorial [Produkt]'. Auch bei 'Advertorial erstellen', 'Editorial-Page'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_resize
---

# Advertorial Page Builder — "Die persönliche Erfahrung"

## PRE-FLIGHT — Research-Kontext laden

Vor dem Start IMMER prüfen ob Audience-Research existiert (Source-of-Truth: lokal):

1. Lies `[aktives-projekt]/_research/INDEX.md`. Gibt es einen `done`-Run zum aktuellen Topic?
2. Wenn JA: Lade `_research/[topic-slug]/copy_context.md` + `personas.json` als Default-Kontext. Pflicht für Advertorials: `before_after.md` (Identity-Transformation als Story-Backbone), `voice_of_customer.md` (verbatim Quotes für authentischen Erfahrungs-Ton), `offer_brief.md` (Necessary Beliefs für Objection-Handling).
3. Wenn NEIN: Frag the Owner "Soll ich via `Rechit` Sub-Agent ein Research starten oder ohne arbeiten?" Niemals blind ohne Research drauflos schreiben.

Schema/Protokoll: Memory `feedback_research_loading_protocol.md`. Agent: `.claude/agents/rechit.md`.

---

Erstelle eine komplette, deploybare Advertorial-Landing-Page als einzelne HTML-Datei. Das Advertorial ist eine Pre-Sale-Seite die wie ein persönlicher Erfahrungsbericht aussieht — geschrieben aus der Ich-Perspektive eines "echten Nutzers".

## Abgrenzung: Advertorial vs. Listicle

| Merkmal | Advertorial (dieser Skill) | Listicle (/listicle) |
|---|---|---|
| **Perspektive** | Ich-Erzähler ("Ich war überrascht...") | Redaktionell ("Wir haben getestet...") |
| **Struktur** | Storytelling — Problem → Entdeckung → Test → Ergebnis | Nummerierte Gründe (Zig-Zag) |
| **Awareness Stage** | Product-Aware (kennt Produkt, braucht Überzeugung) | Solution-Aware (sucht Lösung) |
| **Ton** | Persönlich, emotional, "Tagebuch-Style" | Journalistisch, objektiv, "Testbericht" |
| **Vertrauen** | Durch Identifikation ("ist wie ich") | Durch Autorität ("Experten sagen") |
| **Wann einsetzen** | Retargeting, warmer Traffic, Nischen mit hohem Vertrauen | Kalter Traffic, breite Zielgruppen |

## Core Principles (Mark Builds Brands)
- **"Craft arguments, not copy."** Die Story IST das Argument. Jede Szene führt logisch zur nächsten.
- **"Disguise your marketing."** Sieht aus wie ein persönlicher Blog-Post, NICHT wie Werbung.
- **"Emotional Delta."** Start: Pain (wo der Leser gerade ist) → Peak: Hope (die Entdeckung) → Resolution: Proof (es funktioniert) → Urgency: Fear of Missing Out
- **"The magnificence of the argument."** Die Story ist so aufgebaut, dass am Ende nur EINE Schlussfolgerung möglich ist: "Ich muss das haben."
- **Necessary Beliefs als Kapitel.** Jede Sektion der Story kippt eine Belief.

## Input erwarten
Aus der User-Nachricht oder interaktiv extrahieren:

### Pflicht-Inputs
- **PRODUKT**: Was wird verkauft?
- **PROJEKT**: Projektordner
- **ZIELGRUPPE**: Pfad zur Zielgruppenanalyse
- **PERSONA**: Welche Persona aus der ZG-Analyse?

### Optionale Inputs
- **ANGEBOT**: Welches Angebot? (Rabatt, Bundle, Gratis-Zugabe etc.)
- **CHECKOUT_URL**: Wohin führt der CTA?
- **PRODUKTBILDER**: Pfad zu Produktbildern
- **AUTOR_PERSONA**: Wer "schreibt" das Advertorial? (z.B. "Michael, 42, Familienvater aus Hamburg")
- **HOOK_ANGLE**: Spezifischer Angle (z.B. "Whistleblower", "Überraschende Entdeckung", "Mein Mann hat...")
- **SPRACHE**: Default: Deutsch

## Vorbereitung: Research laden

BEVOR du anfängst — die Foundational Docs lesen:

```bash
cat "[projekt]/zielgruppe/03-personas.md"
cat "[projekt]/zielgruppe/06-offer-brief.md"
cat "[projekt]/zielgruppe/07-voice-of-customer.md"
cat "[projekt]/zielgruppe/02-before-after.md"
```

**Ohne diese Dokumente baust du NICHTS.**

---

## STRUKTUR DES ADVERTORIALS

Das Advertorial folgt einem Storytelling-Arc. Es ist KEIN Feature-Listing, sondern eine Geschichte.

### Story-Arc (5 Akte)

```
ACT 1: The Hook (Pain + Curiosity)
  ↓
ACT 2: The Backstory (Identification + Deepening Pain)
  ↓
ACT 3: The Discovery (Hope + Solution Introduction)
  ↓
ACT 4: The Proof (Testing + Results + Social Proof)
  ↓
ACT 5: The Offer (CTA + Urgency + Risk Reversal)
```

### Section-by-Section Aufbau

#### HEADER
```
[Marken-Logo oder Magazin-Name — dezent]
─────────────────────
```
- Kann das gleiche Magazin-Format wie Listicle sein ODER ein persönlicherer Blog-Look
- Weniger prominent als bei Listicle — hier zählt die Person, nicht die Publikation

#### ACT 1: THE HOOK (erste 3-5 Absätze)
```
[Social Proof Headline]
"[Autor] und [Zahl]+ andere [Zielgruppe] schwören auf [Produktkategorie]"

[Subheadline mit Angebot-Teaser]
"[Emotionaler Teaser] mit [Angebot] Aktion"

Von [Autor-Name] | [Datum] | [Lesezeit]
```

**Intro-Absätze:**
- **Absatz 1:** Emotionaler Einstieg — eine Szene, ein Moment, ein Problem. In Ich-Form.
  - "Wussten Sie, dass [überraschende Statistik/Fakt]?"
  - ODER: Direkt in eine Szene: "Es war der dritte Stromausfall in diesem Winter, als ich..."
- **Absatz 2:** Das Problem vertiefen — was es WIRKLICH bedeutet, nicht nur oberflächlich
- **Absatz 3:** Der Wendepunkt — "Als wir von [Lösung] hörten, wurden wir neugierig."
- **Absatz 4:** Teaser — "Warum [Lösung] alles verändert hat, zeige ich Ihnen jetzt:"

**Hook-Patterns (aus Clickrs-Analyse):**
- "Wussten Sie, dass [Problem] — aber auf Kosten von [X]?"
- "[Zahl]+ [Zielgruppe] haben [Problem] gelöst — mit [überraschendem Ansatz]"
- "Ich hätte nie gedacht, dass [Produkt-Kategorie] so [Adjektiv] sein kann"

#### ACT 2: THE BACKSTORY (2-4 Sections)
Hier werden die Pains vertieft — durch persönliche Erfahrung des Autors.

Für jeden Key-Pain eine eigene Section mit:
```
[Nummerierte Sub-Headline]
1. [Benefit-orientierte Headline — max 8 Worte]

[2-3 Absätze]
- Was ich vorher erlebt habe (Pain in ZG-Sprache)
- Was sich verändert hat (Feature → Benefit → Transformation)
- Persönliche Reaktion ("Ich war ehrlich überrascht...")
```

**Layout:** Zig-Zag wie Listicle — Text/Bild abwechselnd.

**Unterschied zu Listicle:** Die Nummerierung ist subtiler (1., 2., 3. statt "GRUND 1"). Der Ton ist persönlich, nicht redaktionell.

**Copy-Regeln:**
- Ich-Perspektive durchgehend ("Ich habe getestet", "Mich hat überrascht")
- Sensorische Details ("Das weiche, stützende Gefühl beim ersten Schritt")
- Verletzlichkeit zeigen ("Ich war skeptisch", "Normalerweise kaufe ich sowas nie")
- Jede Section kippt eine Necessary Belief

#### ACT 3: THE PIVOT (1 Section)
Der Moment wo aus Erfahrung Empfehlung wird:

```
[Zusammenfassung der Erfahrung]

"Am meisten beeindruckt hat mich am Ende des Tages nicht nur [Feature],
sondern auch [emotionaler Payoff]."

"Und durch das aktuelle [Angebot] habe ich [extra Benefit]."
```

- Persönliches Fazit des Autors
- Überleitung zum Angebot (natürlich, nicht pushy)
- Erster Soft-CTA

#### ACT 4: SOCIAL PROOF (2 Sections)

**Testimonials Block 1 (nach Act 3):**
```
Was sagen andere Kunden?

[3 Testimonials mit Foto + Name + "Verifiziert"]
```

**Testimonials Block 2 (vor Final CTA):**
```
Das sagen weitere Kunden:

[3 weitere Testimonials]
```

- Gleiche Testimonial-Struktur wie Listicle
- Zitate aus VOC-Research adaptieren
- Fotos per Recraft AI oder Platzhalter

#### ACT 5: THE OFFER (Dark-Mode Conversion Block)
Der Final CTA ist ein visueller Bruch — **Dark-Mode-Design** (dunkel, fast schwarz) das sich klar vom weißen Artikel abhebt. Identisch zum Listicle-CTA.

**Aufbau (von oben nach unten):**
```
[Urgency-Banner pulsierend] "⚡ Einführungspreis — nur noch heute"

[PRODUCT MOCKUP — groß, Drop-Shadow, "Sofort-Download" Badge]

[Offer-Headline] "Dein kompletter [Plan]. Sofort umsetzbar. Ohne Risiko."
[Offer-Sub] "Der Leitfaden, der [X] Familien in [Y] Wochen [Ergebnis] hat."

✓ Benefit 1 — ✓ Benefit 2 — ... (6 konkrete Inhalte)

[COUNTDOWN: Stunden : Minuten : Sekunden]
[FORTSCHRITTSBALKEN: "412 von 500 vergriffen" + Shimmer]

~~€49~~ €29 "Du sparst 40% — nur noch 88 Exemplare"

[⚡ JETZT SICHERN — nur €29] ← Shine-Animation

⏳ "Bei 500 Downloads steigt der Preis — ohne Vorwarnung."
🛡️ "30 Tage Geld-zurück-Garantie"
```

**Dann: Persönliches Fazit als emotionaler Closer:**
```
Ein letzter Gedanke

[2-3 Sätze in Ich-Perspektive — persönlich, emotional]
[Letzter Satz = starkes Zitat oder Mantra]

[Nochmal CTA-Button]
```

**Scarcity-Elemente (alle 4 müssen drin sein):**
1. Countdown-Timer (resetet täglich, max 4h)
2. Fortschrittsbalken "X von Y vergriffen" (75-90% gefüllt)
3. "Nur noch Z Exemplare" im Preis-Bereich
4. "Bei Y steigt der Preis" — harter Closer unter dem Button

#### DISCLAIMER + FOOTER
- Identisch mit Listicle (Legal Disclaimer, KI-Hinweis, Impressum etc.)

---

## BILD-STRATEGIE

Basiert auf `/listicle` Skill, mit Advertorial-spezifischen Ergänzungen:

1. **Produkt-Mockup (PFLICHT bei digitalen Produkten):** Nano Banana (Gemini) API → iPad/Tablet-Mockup generieren → `images/product-mockup.png`. Wird prominent im Dark-Mode Final CTA platziert.
2. **Lifestyle/Kontext:** Unsplash — IMMER Photo-IDs verwenden (`images.unsplash.com/photo-{ID}`), NIE `source.unsplash.com`. JEDES Bild visuell verifizieren nach Einbau. Keine doppelten URLs.
3. **Testimonial-Porträts:** Recraft AI — 6 diverse Personen, passend zur Persona
4. **Badges:** HTML/CSS

**Zusätzlich für Advertorial:**
- **Autor-Foto:** Recraft AI generiert ein Porträt passend zur Autor-Persona ODER ein Testimonial-Foto wiederverwenden (wie im Live-Test validiert)
  - Muss zur Zielgruppe passen (gleiche Altersgruppe, gleicher "Typ")
  - Wird im Header/Byline neben dem Namen verwendet (kleines Rundbild)
- **"In-Use" Fotos:** Mehr Lifestyle-Situationen als bei Listicle (Produkt im echten Alltag)
- **Tipp:** Bilder aus dem Listicle-Ordner wiederverwenden wenn beide Pages zum gleichen Produkt gehören (Testimonials, Mockup)

---

## TECHNISCHE UMSETZUNG

Identisch mit `/listicle` — Single HTML File, inline CSS/JS, responsive.

### CSS-Unterschiede zum Listicle
```css
/* Advertorial ist persönlicher — mehr Editorial, weniger Magazin */
--font-heading: 'Georgia', serif;        /* Bleibt gleich */
--font-body: 'Georgia', serif;           /* SERIF für Body = mehr "Artikel-Feeling" */
--content-width: 720px;                  /* Etwas schmaler = lesbarer */
--line-height: 1.8;                      /* Mehr Zeilenabstand = entspanntes Lesen */

/* Blockquotes für persönliche Aussagen */
blockquote {
    border-left: 3px solid var(--accent);
    padding-left: 1.5rem;
    font-style: italic;
    color: var(--text-light);
}
```

### Arbeitsverzeichnis
```
[projekt]/advertorial/
├── [produkt-slug].html
├── images/
│   ├── author.jpg               ← Recraft-generiertes Autor-Porträt
│   ├── product-1.jpg
│   ├── lifestyle-1.jpg
│   ├── testimonial-1.jpg
│   └── ...
└── _deploy/
    └── netlify.toml
```

---

## ABLAUF (Step by Step)

### Step 1: Research laden & Story-Arc planen
1. Foundational Docs lesen
2. Persona wählen → Autor-Persona ableiten (gleiche Zielgruppe)
3. Story-Arc planen:

| Act | Was passiert | Welche Belief kippt | Emotionaler State |
|---|---|---|---|
| 1 Hook | [Szene/Problem] | — (Aufmerksamkeit) | Fear/Frustration |
| 2 Backstory | [Pain vertiefen] | Belief #1, #2 | Identification |
| 3 Discovery | [Lösung vorstellen] | Belief #3, #4 | Hope/Curiosity |
| 4 Proof | [Social Proof] | Belief #5, #6 | Trust/Courage |
| 5 Offer | [CTA] | — (Handlung) | Urgency |

### Step 2: Copy schreiben
1. Hook (Headline + erste 3-5 Absätze) — HIER entscheidet sich ob jemand weiterliest
2. Backstory-Sections (3-5 nummerierte Punkte mit persönlichen Erfahrungen)
3. Pivot/Fazit (persönliches Urteil + Überleitung zum Angebot)
4. Testimonials (6 Stück, basierend auf VOC)
5. Offer-Section (CTA + Urgency)
6. Disclaimer + Footer

### Step 3: Bilder beschaffen
1. **Produkt-Mockup** (digitale Produkte): Nano Banana API → `images/product-mockup.png`
2. **Unsplash**: 4-6 Kontext-Bilder per WebSearch, Photo-IDs extrahieren → direkt als URL einbetten
3. **Recraft**: 6 Testimonial-Porträts + 1 Autor-Porträt (oder Testimonial wiederverwenden)
4. **Validierung**: Nach Einbau ALLE Bilder visuell prüfen — keine Duplikate, keine falschen Motive
5. **Tipp:** Bilder aus dem Listicle-Ordner kopieren wenn zum gleichen Produkt

### Step 4: HTML bauen
- Identisch mit Listicle (Single File, inline CSS/JS, responsive)

### Step 5: QA & Deploy
- Identisch mit Listicle

---

## QUALITÄTS-CHECK (vor Abgabe)

### Story & Copy
- [ ] Liest sich wie ein persönlicher Blog-Post, NICHT wie Werbung?
- [ ] Durchgehende Ich-Perspektive (keine Wechsel zu "wir" oder "man")?
- [ ] Story-Arc vollständig (Hook → Backstory → Discovery → Proof → Offer)?
- [ ] Jede Section kippt mindestens 1 Necessary Belief?
- [ ] VOC-Sprache verwendet?
- [ ] Autor-Persona passt zur Zielgruppe?
- [ ] Emotional Delta funktioniert (Pain → Hope → Proof → Urgency)?
- [ ] Persönliche, sensorische Details ("Ich spürte...", "Was mich überraschte...")?
- [ ] Keine Marketing-Buzzwords ("revolutionär", "einzigartig", "sensationell")?
- [ ] Blockquotes für persönliche Highlights?

### Conversion-Elemente
- [ ] Mid-Page CTA vorhanden?
- [ ] 2 Testimonial-Blöcke (à 3 Testimonials mit Recraft-Fotos)?
- [ ] Final CTA im Dark-Mode-Design?
- [ ] Produkt-Mockup im Final CTA (bei digitalen Produkten)?
- [ ] Countdown-Timer tickt korrekt?
- [ ] Fortschrittsbalken mit konkretem Limit ("X von Y")?
- [ ] Scarcity-Text unter dem Button ("Bei Y steigt der Preis")?
- [ ] Garantie-Hinweis mit Shield-Icon?
- [ ] Persönliches Fazit als emotionaler Closer NACH dem CTA?

### Bilder
- [ ] ALLE Bilder visuell geprüft — zeigen sie was sie sollen?
- [ ] Keine doppelten Bild-URLs?
- [ ] Alle Bilder laden korrekt (keine 404)?
- [ ] Autor-Foto im Byline vorhanden?

### Technik
- [ ] Serif-Font für Body (Georgia)?
- [ ] Schmalere Content-Width (720px statt 800px)?
- [ ] Mobile-responsive (besonders Final CTA + Countdown)?
- [ ] CTA-Button führt zur richtigen URL?
- [ ] Disclaimer vorhanden?
- [ ] Footer mit Rechtliches?

---

## WICHTIGE REGELN

1. **Storytelling > Feature-Listing.** Das ist eine Geschichte, keine Produktseite.
2. **Ich-Perspektive durchgehend.** Der "Autor" ist eine Person aus der Zielgruppe, nicht ein Marketer.
3. **Verletzlichkeit = Vertrauen.** "Ich war skeptisch" > "Dieses Produkt ist großartig".
4. **Sensorische Details.** Wie fühlt es sich AN? Wie KLINGT es? Was SIEHT man? Nicht abstrakt.
5. **Jede Szene hat einen Zweck.** Wenn ein Absatz keine Belief kippt und keine Emotion auslöst → streichen.
6. **Der Pivot muss natürlich sein.** Der Übergang von Story zu Angebot darf NICHT abrupt sein.
7. **Fake it til you make it — aber smart.** Der Autor ist fiktiv, aber die Pains und Desires sind REAL (aus Research).
8. **Verschiedene Angles für verschiedene Personas.** Ein Produkt kann 3+ verschiedene Advertorials haben (Mark's BONUS-Methode).
9. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).
10. **Netlify Deploy** nach QA.

## LEARNINGS AUS DEM FELD

### Copy & Ton
1. **Advertorial Copy ist 40-60% länger als Listicle.** Mehr Story = mehr Text. Das ist gewollt.
2. **Der Hook entscheidet alles.** 80% der Leser entscheiden in den ersten 5 Sekunden ob sie weiterlesen.
3. **Serif-Font für Body = mehr Glaubwürdigkeit** bei Editorial-Content. Sans-Serif wirkt zu "digital/werblich".
4. **Blockquotes für persönliche Highlights** ("Das hat mich am meisten überrascht...") → visueller Anker beim Scannen.
5. **Autor muss zur Persona passen.** Ein 42-jähriger Familienvater schreibt anders als eine 28-jährige Studentin.
6. **Highlight-Boxes** (farbiger Kasten mit roter Linie links) funktionieren als "Zusammenfassung für Scanner" — wer nicht alles liest, liest mindestens die Boxen.

### Conversion
7. **"Mein Fazit" NACH dem Dark-Mode CTA** = emotionaler Closer. Persönliche Empfehlung wirkt stärker als ein zweiter identischer CTA-Block.
8. **Dark-Mode Final CTA ist universal** — funktioniert in Listicle UND Advertorial identisch. Gleicher Code, gleiche Scarcity-Elemente.
9. **Triple-Scarcity (Countdown + Fortschrittsbalken + Spots-Left)** erzeugt den stärksten Kaufdruck. Validiert im Live-Test.
10. **Garantie-Hinweis unter dem Button mit Shield-Icon** nimmt das letzte Risiko.

### Bilder
11. **Mockup ist PFLICHT bei digitalen Produkten** — ohne visuelles Bild fehlt die Greifbarkeit.
12. **Unsplash-Bilder IMMER visuell verifizieren** — IDs können Überraschungen liefern.
13. **Testimonial-Bilder aus Listicle wiederverwenden** wenn beide Pages zum gleichen Produkt gehören — spart Recraft-Credits und sorgt für Konsistenz.
14. **Autor-Foto im Byline als kleines Rundbild** (40x40px) erhöht die Glaubwürdigkeit der Ich-Perspektive erheblich.
