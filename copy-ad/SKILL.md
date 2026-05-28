---
name: copy-ad
description: Meta Ad, Facebook Ad, Instagram Ad, Primary Text, Ad Copy, Werbeanzeige, FB-Ad-Text, IG Ad Text, Headline für Ad, Ad Hook, Hook für Werbung, Werbetext kurz, Paid Social Copy, Meta Ads, FB/IG Primary Text
---

# Copy-Ad Skill

## PRE-FLIGHT — Research-Kontext laden

Vor dem Start IMMER prüfen ob Audience-Research existiert (Source-of-Truth: lokal):

1. Lies `[aktives-projekt]/_research/INDEX.md`. Gibt es einen `done`-Run zum aktuellen Topic?
2. Wenn JA: Lade `_research/[topic-slug]/copy_context.md` + `personas.json` als Default-Kontext. Für Hook-First Ad Copy besonders wichtig: `voice_of_customer.md` (verbatim Quotes als Hook-Material — die besten Ad-Hooks sind 1:1 das, was die Zielgruppe selber schreibt) und `before_after.md` (Transformation als Body-Promise).
3. Wenn NEIN: Frag the Owner "Soll ich via `Rechit` Sub-Agent ein Research starten oder ohne arbeiten?" Niemals blind ohne Research drauflos schreiben.

Schema/Protokoll: Memory `feedback_research_loading_protocol.md`. Agent: `.claude/agents/rechit.md`.

---

Hook-First Short-Form Ad Copy für Meta (Facebook + Instagram). Default-Output: Deutsch, DACH-Markt, Anti-AI-Voice gefiltert. Liefert Primary Text, Headlines (40 chars) und Descriptions (25 chars) pro Ad-Variant.

## When to use

- Meta Ad Primary Text wird gebrieft (typ. 80-300 Zeichen vor "Mehr anzeigen"-Fold bei 125 Zeichen)
- Headlines (40-Zeichen-Limit) für FB/IG Ads
- Description-Lines (25-Zeichen-Limit)
- Werbeanzeigen-Copy für Paid Social (FB, IG)
- Kurze, Hook-getriebene Copy für Cold-Audience-Targeting
- Brief enthält "Ad-Copy", "Primary Text", "Werbetext", "FB Ad", "IG Ad", "Hook", "Headline für Ad"

## When NOT to use

- Long-Form Sales Page / Listicle → `copy-listicle`
- Long-Form VSL / Sales Letter / Webinar Story-Skript → `copy-vsl`
- Email Subject / Email Body / Sequenzen → `copy-email`
- Organische IG Caption oder organischer Post → kein Skill, frei schreiben oder `gm-social-content`
- Carousel-Slide-Texte → bestehende `carousel-*` Skills
- TikTok / Reels Video-Skripte → andere Skills (separate Hook-Logik bei 3-Sekunden-Frame)
- **Visual Ad Creative (Bilder, Layout, Design):** Bestehender `/ad-creative` Skill rendert Visuals + generiert Bilder. **Dieser `copy-ad` Skill liefert NUR den Text.** Wenn the Owner sowohl Copy als auch Bild will: erst `copy-ad` für Text, dann `/ad-creative` für Bild. Wenn the Owner "Ad Creative" sagt ohne explizit "nur Text" → `/ad-creative` nutzen.
- Bestehender `ad-copy` Skill: Macht Copy für ein bereits gebautes Creative. Dieser `copy-ad` Skill ist breiter — Copy ohne Vorbedingung Creative-First.

---

## Workflow (7 Steps)

### Step 1: Read Project Context
- Detect project from chat context, working directory, or explicit mention.
- Read project's `CLAUDE.md` (auto-loaded) — Brand-Voice, Audience, aktive Kampagnen.
- Audience-Research suchen in `[project]/zielgruppen/`, `[project]/audience-research/`, `[project]/research/` oder `[project]/_memory/INDEX.md`. Nur das Relevante lesen.
- Constraints aus dem Brief notieren: Plattform (FB/IG), Audience (Cold/Warm/Retarget), Funnel-Stage, Produkt-Preis, Hook-Angle wenn vorgegeben, Deadline.

### Step 2: Load Foundation
- `_universal-patterns.md` lesen (Sektion 0, 1 Patterns 1-2-4-7-10-12, 2 — vor allem die Hook-relevanten).
- Cluster-Datei nach Projekt:
  - [brand] / the Founder / health-supplements → `health-wellness.md`
  - [brand] / the Owner / beauty / fitness-baking → `beauty-skincare.md` + `consumer-products.md`
  - [brand] / coaching / Peptide-Story-Funnel → `wealth-coaching.md`
  - [brand] merch / [brand] / e-commerce → `consumer-products.md`
  - [brand] weight-loss / fitness-coaching → `health-wellness.md` + `wealth-coaching.md`

### Step 3: Determine Schwartz Coordinates
Basierend auf Projekt-Kontext:
- **Awareness Stage** (1 Unaware → 5 Most-Aware) — wo betritt der Reader die Ad?
- **Sophistication Stage** (1 First-to-Market → 5 Saturated) — wo ist der Markt?
- **Mass Desire activated** (Power / Sex / Survival / Comfort / Approval)
- **Cold vs. Warm Audience** — Cold braucht stärkere Pattern-Interrupt-Hook, Warm darf direkter zur Mechanik
- **Cluster + Projekt-spezifische Patterns** zum Anwenden/Vermeiden

Wenn unklar, the Owner fragen: "Reader-Stage [...] und Sophistication [...] — passt das oder weicht das ab? Cold oder Retarget?"

### Step 4: Apply Hook-First Short Ad Backbone
Backbone für jede Variante (4-Block-Struktur):

1. **Hook-Line (vor 125-Char-Fold):** Pattern-Interrupt. Muss vor "Mehr anzeigen" sitzen. Eine der 5 Hook-Approaches:
   - Numerical-Promise-Hook (Pattern 4): "Sandra (38, Hamburg) hat in 21 Tagen 4,7 kg verloren..."
   - Anti-Position-Hook (Pattern 2): "Es ist NICHT dein Stoffwechsel. Und auch nicht zu wenig Sport."
   - Story-Origin-Hook (Pattern 8 Beat 1): "Ich war 38, Anwältin in Hamburg, mit Bauchkrämpfen morgens..."
   - Permission-Layer-Hook (Pattern 3): "Es ist nicht deine Schuld, dass dein Bauch dich aufbläht."
   - Curiosity-Gap-Hook (Pattern 8 Beat 4): "Warum die meisten Diäten genau ab Tag 14 zusammenbrechen..."

2. **Pain/Identification (1-2 Zeilen):** Reader erkennt sich. Concrete-not-abstract.

3. **Mechanismus-Tease oder Curiosity-Gap (1-2 Zeilen):** Hint ohne Reveal. "Es geht um die Darm-Haut-Achse." / "Eine 3-Schritt-Methode, die ich von the Founder (Charité) kenne." Niemals den ganzen Mechanismus auspacken — die Ad verkauft den Klick, nicht das Produkt.

4. **Single Proof Point + CTA:** Eine Zahl, ein Name, ein Datum + klare Action.
   - Proof: "47 Frauen, 21 Tage, Charité-Studie." / "150.000 Athleten haben damit gestartet."
   - CTA: "Hier mehr lesen →" / "Quiz starten →" / "Jetzt bewerben →"

### Step 5: Generate 5 Variants
Default-Output pro Brief:

**5 Primary-Text Variants** — jede mit anderem Hook-Pattern:
- Variant 1: Numerical-Promise-Hook
- Variant 2: Anti-Position-Hook
- Variant 3: Story-Origin-Hook
- Variant 4: Permission-Layer-Hook
- Variant 5: Curiosity-Gap-Hook

**5 Headlines** (je 40 Zeichen max — strikt, da Meta abschneidet):
- Variieren in Verb-Form (Question / Imperative / Promise / Negation / Fragment)

**5 Description-Lines** (je 25 Zeichen max):
- Sub-Promise oder Risk-Reversal oder Specificity-Anchor

Wenn the Owner mehr will: bis zu 8 Variants erweitern. Wenn weniger Patterns sinnvoll für Audience (z.B. Cold ohne Permission-Layer): Variants reduzieren und begründen.

### Step 6: Specificity + Pattern-Check Pass
Self-Check vor Lieferung:
- Mindestens 1 spezifische Zahl / Datum / Stadt / Beruf pro Variant?
- Hook sitzt VOR dem 125-Char-Fold? Zählen.
- Anti-Position-Hook (wenn Stage 4-5) gegen den dominanten Stage-3-Mechanismus geprüft?
- Permission + Mechanization Pair (wenn Stage 4-5)?
- Loss-Aversion oder Numerical-Promise (wenn Power/Survival-Desire)?
- Internal-Bridge wenn the Founder (Darm → Haut/Haare/Energie)?
- DACH-Filter geprüft? (Keine Geographic-Folk-Authority außer Tesla, keine Conspiracy-Frames, keine Pseudo-Frequency, keine US-Triple-Cascade.)

### Step 7: Anti-AI-Voice Final Filter
QC-Checkliste aus `.claude/rules/anti-ai-voice.md` durchlaufen:
- 0 Em-Dashes (—) — `grep "—"` mental
- Keine "nicht X, sondern Y" Konstruktionen
- Keine Drei-Adjektiv-Listen
- Verbotswort-Scan (ganzheitlich, nahtlos, optimal, revolutionär, leverage, seamless, etc.)
- Satzlängen-Variation (1× <8 Wörter, 1× >20 Wörter pro Block — bei Ad-Copy in den 5 Variants insgesamt erreichen, nicht jede Variant einzeln)
- Konkret statt abstrakt (Zahlen, Namen, Daten, Beispiele)
- Headline (40 chars) und Description (25 chars) auf Char-Count testen

Wenn AI-Marker entdeckt → die Zeile umschreiben, NICHT ausliefern.

---

## Output Format

```
## Ad-Brief: [Projekt / Produkt / Audience]
**Awareness Stage:** [1-5]
**Sophistication Stage:** [1-5]
**Audience:** [Cold/Warm/Retarget — kurze Beschreibung]
**Hauptdesire:** [Power/Sex/Survival/Comfort/Approval]

---

### Ad-Variant 1: Numerical-Promise

**Primary Text:**
[Hook-Line — vor 125-Char-Fold]
[Body 2-3 Zeilen]
[CTA-Line]

**Headline (40 chars):** [text] [(XX/40)]
**Description (25 chars):** [text] [(XX/25)]
**Pattern angewendet:** Pattern 4 (Numerical Promise) + Pattern 1 (Specificity)
**Schwartz Hebel:** Specific Numerical Promise + Identification

---

### Ad-Variant 2: Anti-Position

[gleiche Struktur]

---

### Ad-Variant 3: Story-Origin

[gleiche Struktur]

---

### Ad-Variant 4: Permission-Layer

[gleiche Struktur]

---

### Ad-Variant 5: Curiosity-Gap

[gleiche Struktur]

---

## Headlines-Pool (40 chars max)
1. [text] (XX/40)
2. [text] (XX/40)
3. [text] (XX/40)
4. [text] (XX/40)
5. [text] (XX/40)

## Description-Pool (25 chars max)
1. [text] (XX/25)
2. [text] (XX/25)
3. [text] (XX/25)
4. [text] (XX/25)
5. [text] (XX/25)

## Test-Empfehlung
[1-2 Sätze: welche 2 Variants als A/B-Test gegen welche, mit Begründung. Z.B.: "Variant 2 (Anti-Position) gegen Variant 4 (Permission-Layer) — beide Stage-5-Patterns, testen ob Cynicism oder Empathy stärker zieht."]
```

---

## Few-Shot Examples

### Example 1 — the Founder Mikrobiom-Drink, Anti-Position-Hook

**Brief:** Cold IG Ad für the Founder's neuen Mikrobiom-Drink. Audience: Frauen 35-55, Aufgeblähter Bauch, haben 3+ Probiotika probiert. Stage 5.

**Output (Variant 2 — Anti-Position):**
```
Primary Text:
Es ist NICHT dein Stoffwechsel. Und auch nicht zu wenig Sport.

Wenn dein Bauch nach JEDEM Essen aufgebläht ist, liegt das in 7 von 10 Fällen am Mikrobiom — nicht am Magen.

the Founder (Charité, 12 Jahre Darm-Forschung) hat einen 21-Tage-Reset entwickelt. 47 Frauen, mittlere Bauchumfang-Reduktion 4,2 cm.

Das ganze Protokoll lesen →

Headline (40): Was wirklich aufbläht (nicht Stoffwechsel) (39/40)
Description (25): 47 Frauen, 21 Tage Reset (24/25)
```

### Example 2 — [brand] Cobra-Coaching, Story-Origin-Hook

**Brief:** Retarget IG Ad für the Founder Cobra-Coaching (€397/Monat). Audience: Männer 25-40, schon auf der Webseite gewesen, nicht gekauft. Stage 4.

**Output (Variant 3 — Story-Origin):**
```
Primary Text:
Ich war 27, 12% KFA, und konnte trotzdem keine 5 Klimmzüge.

Stand jeden Morgen im Spiegel, sah definiert aus, fühlte mich wie Pudding. Bis Don mir 2018 das Cobra-Protokoll gezeigt hat.

3 Wochen später: 12 Klimmzüge sauber. Ohne mehr Trainingszeit. Anderes Programm.

Wie das Protokoll funktioniert →

Headline (40): Definiert + schwach. Kennst du das? (38/40)
Description (25): Cobra-Protokoll erklärt (23/25)
```

### Example 3 — [brand] Fitness-Cake-Bundle, Numerical-Promise-Hook

**Brief:** Cold FB Ad für the Owner's neues 12-Rezepte-Fitness-Backbuch (€39). Audience: Frauen 28-45, Fitness + süß, Backen-Hobby. Stage 3.

**Output (Variant 1 — Numerical-Promise):**
```
Primary Text:
12 Cake-Rezepte unter 280 kcal — und keines schmeckt nach "Diät".

the Owner (Konditormeisterin, 7 Jahre Patisserie) hat alle in ihrer eigenen Backstube getestet. 6 davon ohne Mehl, 4 ohne Industriezucker.

Fertig in unter 45 Minuten. Mit Fotos pro Schritt.

Bundle ansehen →

Headline (40): 12 Cakes unter 280 kcal — alle getestet (40/40)
Description (25): the Owner's Backstuben-Set (24/25)
```

---

## Common Mistakes to Avoid

1. **Hook hinter dem 125-Char-Fold:** Wenn der Pattern-Interrupt erst in Zeile 3 kommt, liest niemand bis dahin. Hook = Wort 1-15.
2. **Em-Dash benutzen für "Identification-Aside":** Ist klassisch Schwartz, aber Anti-AI-Voice killt es. Punkt oder Doppelpunkt nutzen.
3. **"Nicht X, sondern Y" Floskel:** Auch wenn es wie Anti-Position klingt — verboten. Stattdessen: "Es ist NICHT X." (Punkt. Neuer Satz.)
4. **Drei-Adjektiv-Listen ("schnell, einfach, lecker"):** Klassischer AI-Tell. Auf 2 oder 4 ändern oder anders formulieren.
5. **Generische Zahlen ohne Quelle ("Tausende Kunden"):** AI-Move. Konkret werden ("47 Frauen", "150.000 Athleten") oder weglassen.
6. **Voice-Break in Englisch in DACH-Ad:** "Damn good!" / "It's a vibe!" — instant AI-LinkedIn-Cringe. Nativ Deutsch ("Kein Witz." / "Ehrlich.") oder weglassen.
7. **CTA-Floskel ("Erfahre mehr!"):** Schwach. Spezifischer: "Quiz starten →", "21-Tage-Plan ansehen →", "Bewerbungs-Call buchen →".
8. **Headline überschreitet 40 Zeichen:** Meta schneidet ab. IMMER nach Build die Char-Counts angeben in Klammern.

---

## Loading Pointers
Foundation-Datei-Pfade siehe `references/POINTERS.md` in diesem Skill-Ordner.
