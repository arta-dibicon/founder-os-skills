---
name: copy-vsl
description: VSL-Skripte, Video Sales Letter, Sales-Letter, Webinar-Skript, Long-Form Transformation-Story, Story-Hook-Skripte, Story-Sales-Page, 30-Min Video Script, VSL Script, Video Sales Letter copy, Long-Form Sales Page Story-Arc
---

# Copy-VSL Skill

## PRE-FLIGHT — Research-Kontext laden

Vor dem Start IMMER prüfen ob Audience-Research existiert (Source-of-Truth: lokal):

1. Lies `[aktives-projekt]/_research/INDEX.md`. Gibt es einen `done`-Run zum aktuellen Topic?
2. Wenn JA: Lade `_research/[topic-slug]/copy_context.md` + `personas.json` als Default-Kontext. Für VSL-Story-Arc besonders wichtig: `before_after.md` (liefert die "Vorher"-Welt + Transformation für Beat 2-7) und `voice_of_customer.md` (verbatim Quotes für Story-Hooks und Pain-Beats).
3. Wenn NEIN: Frag the Owner "Soll ich via `Rechit` Sub-Agent ein Research starten oder ohne arbeiten?" Niemals blind ohne Research drauflos schreiben.

Schema/Protokoll: Memory `feedback_research_loading_protocol.md`. Agent: `.claude/agents/rechit.md`.

---

Long-form Video Sales Letter (VSL) und Sales-Letter Copywriting nach dem 9-Beat Story-VSL Arc (Schwartz Backbone A). Default-Output: Deutsch, DACH-Markt, Anti-AI-Voice gefiltert.

## When to use

- Long-form Video-Skript (5-30 Min) wird gebrieft (VSL, Webinar, Story-Hook-Video)
- High-Ticket Transformation-Produkt (€500+, oft €1k-€10k Coaching)
- Long-Form Sales Letter / Sales Page mit Story-Arc gewünscht
- Female-dominant Audience (häufig — coaching, transformation, manifestation)
- [brand] VSL, the Founder Long-Form-Brief, Peptide Story-Funnel, [brand] Coaching-Webinar
- Brief enthält Worte wie "VSL", "Sales Letter", "Story-Skript", "Webinar", "lange Story", "Transformation-Skript"

## When NOT to use

- Kurze Ad Copy (Meta Primary Text, Headlines) → `copy-ad`
- E-Comm Produkt-Sales-Page mit Listicle-Format → `copy-listicle`
- Email Body / Email Subject / Sequenzen → `copy-email`
- Carousel / Short-Form Social → bestehende `carousel-*` Skills
- B2B Enterprise Sales ([brand]-Leads etc.) — kein Story-VSL Format, andere Awareness-Journey
- Quiz-Funnel → bestehender `quizfunnel` Skill

---

## Workflow (7 Steps)

### Step 1: Read Project Context

- Erkenne welches Projekt ([brand] / within-supplements / peptide-venture / team-madsen / pretty-little-cakes etc.) aus Chat-Kontext, working directory, oder explizitem Mention.
- Projekt-`CLAUDE.md` ist auto-loaded. Bewusst nutzen: Brand Voice, Audience, aktuelle Kampagne.
- Audience-Research suchen in:
  - `[project]/zielgruppen/`
  - `[project]/audience-research/`
  - `[project]/research/`
  - `[project]/_memory/INDEX.md`
- Lies was relevant ist. Bei the Founder: gut-skin-bridge, Permission-Pattern. Bei [brand]: Origin-Story-Templates, Testimonial-Pool.
- Note Constraints aus dem Chat: Länge (Min), Channel (YT vs Funnel-Page), Deadline, spezifischer Story-Angle.

### Step 2: Load Foundation

- Read `references/POINTERS.md` für Pfade.
- Lies `_universal-patterns.md` (Sektionen 0, 1, 2 (Pattern 8 Story-VSL Arc!), 5, 6, Section 7 #1+#2 Templates).
- Lies passenden Cluster:
  - within-supplements / the Founder / health-supplements / Mikrobiom → `health-wellness.md`
  - PLC / the Owner / beauty / fitness-baking → `beauty-skincare.md` + `consumer-products.md`
  - [brand] / coaching / Peptide-Story-Funnel → `wealth-coaching.md`
  - [brand] weight-loss / Cobra-Coaching / fitness-coaching → `health-wellness.md` + `wealth-coaching.md`
  - [brand] merch / Junsei / e-commerce → `consumer-products.md` (selten für VSL)

### Step 3: Determine Schwartz Coordinates

- **Awareness Stage** (1 Unaware → 5 Most-Aware) — wo betritt Reader die VSL?
- **Sophistication Stage** (1 First-to-Market → 5 Saturated)
- **Mass Desire activated** (Power / Sex / Survival / Comfort / Approval) — primär + sekundärer Bridge
- **Cluster + projektspezifische Patterns to use/avoid**

Defaults wenn nicht explizit gebrieft:
- [brand]: Stage 5 / Awareness 4-5 / Power+Approval
- the Founder Long-Form: Stage 4 / Awareness 2-3 / Survival+Approval
- Peptide-Venture: Stage 4 / Awareness 3 / Survival+Comfort
- [brand] Coaching-Webinar: Stage 3-4 / Awareness 3 / Power+Approval

Wenn unklar, frag the Owner:
"Reader-Stage ~3-4 und Sophistication ~4 für [Projekt] — passt das oder weicht der Brief ab?"

### Step 4: Apply 9-Beat Story-VSL Arc (Backbone A)

Gerüst (siehe `_universal-patterns.md` Pattern 8). Jeder Beat 100-300 Wörter, mit Patterns benannt:

1. **Origin-State (rock-bottom protagonist)** — spezifisch, namentlich, Origin-Triple (Pattern 7): Vorname + Stadt + Beruf + konkrete Tiefpunkt-Detail.
   - Beispiele: "Hi, ich bin Sandra. 38, Anwältin in einer Großkanzlei in Hamburg, 70-Stunden-Wochen, Bauchkrämpfe morgens vor jedem Mandantentermin."
2. **Failed Conventional Path** — pre-emptet "ich hab schon alles probiert"-Einwand. 3-5 spezifische gescheiterte Versuche mit Namen.
3. **Chance Encounter / Mentor / Found-Document** — Breakthrough-Moment, nicht verdient. Namen + Ort + Detail.
4. **Curiosity-Gap Hook** — Mechanismus andeuten, NICHT erklären. Pattern 4 Numerical-Promise hier reinweben ("3-Schritte-Methode", "27-Tage-Reset").
5. **Mechanism Reveal** — Mechanismus benennen, Vokabular besitzen (Pattern 3). DACH-konform: deutsche Compounds ("Mikrobiom-Reset", "Innenwelt-Methode", "Frequenz-Kohärenz-Prinzip"). KEINE englischen Trademark-Namen für DACH-Brand.
6. **Personal Proof (first-result moment)** — spezifische Zahl + spezifischer Kontext. "Tag 3: erste Mail an alte Kanzlei abgesagt, Bauchkrämpfe weg." NICHT generisch.
7. **Authority-Stack** — DACH-konform (Pattern 6b): Charité, Münchner UniKlinik, Stiftung Warentest, Mt. Sinai, real verifizierbar. KEINE "Ancient Japanese"-Folk-Authority für DACH (Pattern 6a US-only). Brand-Eigenautorität wenn vorhanden (the Founder = Biochemikerin).
8. **Social Proof (3-5 named testimonials)** — Origin-Triple verbatim (Pattern 7): Vorname + Stadt + Ausgangsberuf + Zieldestination.
9. **Scarcity + Anchor + Guarantee + CTA** — DACH-konform: KEINE US-Triple-Cascade (€297→€197→€37). Stattdessen: Single-Klar-Preis + Pattern 11 (Ratenzahlung 0%, "4x €2.750"). Guarantee: 14 Tage Widerrufsrecht + zusätzlich brandspezifische Garantie. Identity-CTA ("Bewirb dich für die Q3-Cohort").

Loss-Aversion-Cascade (Pattern 5) idR zwischen Beat 6 und Beat 7 platzieren — DAYS → WEEKS → MONTHS → YEARS rhythm.

Permission-Layer (Pattern 3 erste Hälfte) idR in Beat 2 oder Beat 5 weben — "Es ist nicht deine Schuld..." wenn die Audience hohe Failure-History hat (chronische Diäten, gescheiterte Coachings).

### Step 5: Generate Variants

Default Output:
- **1 vollständiges VSL-Skript** mit Timestamps (z.B. "0:00-2:30 Beat 1: Origin-State"), Beat-Headers, Copy in Plain Prose (KEINE Bullets im gelieferten VSL-Body)
- **3 alternative Hook-Varianten** für Beat 1+4 (für Split-Test): jede Variante zieht einen anderen dominanten Pattern (z.B. Variante A = Anti-Position-Hook, B = Numerical-Promise-Hook, C = Pure-Story-Hook)

Bei VSL > 15 Min: zusätzlich Outline-Block oben (Beat-Übersicht mit Kern-Aussage je Beat, vor dem Vollskript). Bei VSL < 8 Min: Outline weglassen.

### Step 6: Specificity + Pattern-Check Pass

Self-check vor Delivery:
- Mindestens 1 spezifische Zahl / Datum / Stadt / Beruf pro Beat?
- Beat 1 Origin-Triple komplett (Vorname + Stadt + Beruf + Tiefpunkt-Detail)?
- Beat 5 Mechanismus deutsch benannt (DACH-konform)?
- Beat 8 mindestens 3 Testimonials im Origin-Triple-Format?
- Anti-Position-Hook (Pattern 2) gegen den Stage-3 Mechanism geprüft? "Es ist NICHT [incumbent]"?
- Permission + Mechanization Pair (Pattern 3) wenn Stage 4-5 Audience?
- Loss-Aversion-Cascade (Pattern 5) Tag→Woche→Monat→Jahr?
- Internal-Bridge (Pattern 12) wenn the Founder (Darm → Haut/Haare/Nägel)?
- Beat 9 KEIN US-Cascade? Stattdessen Pattern 11 Convenience-Path?

### Step 7: Anti-AI-Voice Final Filter

Run die QC-Checkliste aus `.claude/rules/anti-ai-voice.md`:

- 0 Em-Dashes (—). `grep "—"` mental.
- Keine "nicht X, sondern Y" Konstruktionen.
- Keine Drei-Adjektiv-Listen (Rule of Three).
- Verbotswort-Scan: ganzheitlich, nahtlos, optimal, revolutionär, beleuchten, eintauchen, hervorheben, robust, nahtlos, cutting-edge.
- Floskel-Opening-Check: keine "In der heutigen schnelllebigen Welt", kein "Lass uns eintauchen".
- Floskel-Closing-Check: kein "Im Endeffekt", kein "Zusammenfassend".
- Satzlängen-Variation: pro Beat mindestens 1× <8 Wörter UND 1× >20 Wörter.
- Konkret-Test: pro Beat 1 spezifische Zahl/Name/Datum/Beispiel.
- Vorlese-Test: laut lesen — stolperst du? klingt LinkedIn-Influencer? → umschreiben.

Wenn AI-Marker gefunden: zugehörige Zeile umschreiben, NICHT liefern.

---

## Output Format

```
# VSL: [Brand / Produkt / Hook-Topic]

**Total Runtime:** ~[X] Min (~[Y] Wörter)
**Awareness Stage:** [N] / **Sophistication Stage:** [N] / **Dominant Mass Desire:** [Power/Sex/Survival/Comfort/Approval]
**Patterns aktiv:** [Pattern 1, 4, 7, 8, 11, ...]

## Outline (nur bei >15 Min)

| Beat | Beat-Name | Kern | Timestamp |
|---|---|---|---|
| 1 | Origin-State | Sandra, 38, Anwältin Hamburg, Bauchkrämpfe | 0:00-2:30 |
| 2 | Failed Path | 5 Coaches, 2 Therapien, nichts hielt | 2:30-4:30 |
| ... | ... | ... | ... |

## Vollskript

### Beat 1 — Origin-State (0:00-2:30)

[Plain Prose, 100-300 Wörter, kein Markdown im Body, KEINE Em-Dashes]

### Beat 2 — Failed Conventional Path (2:30-4:30)

[Plain Prose...]

[... alle 9 Beats ...]

### Beat 9 — Scarcity + Anchor + Guarantee + CTA ([Timestamp])

[Plain Prose mit konkretem Preis, DACH-Garantie, Identity-CTA]

---

## Hook-Varianten für Split-Test

### Variant A — Anti-Position-Hook
**Beat 1 Alternative:**
[100-150 Wörter — Hook über Pattern 2: "Es ist NICHT [incumbent]..."]

**Beat 4 Alternative (Curiosity-Gap):**
[80-120 Wörter — verstärkt Anti-Position]

### Variant B — Numerical-Promise-Hook
**Beat 1 Alternative:**
[Hook über Pattern 4: "27 Tage. 1 Methode. 4 Frauen, die ihr Leben umgeschrieben haben."]

**Beat 4 Alternative:**
[Numerical-stack Promise]

### Variant C — Pure-Story-Hook
**Beat 1 Alternative:**
[Hook startet mitten in der dramatischen Szene — "Es war 6:42 Uhr. Ich saß auf dem Boden des Hamburger Kanzleiklos und..."]

**Beat 4 Alternative:**
[Story-bezogener Curiosity-Gap]

---

## Notes für Producer / Editor

- Beat 1 als On-Camera + b-roll Hamburg-Kanzlei-Establishing
- Beat 5 mit Whiteboard-Animation für Mechanism-Reveal
- Beat 8 Testimonials als Talking-Head-Cuts
- Beat 9 mit klarer Bildschirmeinblendung Preis + Bewerb-Button-CTA
```

---

## Few-Shot Examples

### Example 1: [brand] €10k Coaching VSL (DACH female 28-45 spiritual-business-curious)

**Brief:** 18-Min Sales-VSL für Funnel-Page. Reader: Frau, 28-45, Hamburg/München/Wien, in gut bezahltem Job (Anwältin/Beraterin/Therapeutin), spürt "es ist nicht meins", spirituell offen aber nicht eso. Stage 5, Awareness 4. Power+Approval.

**Beat 1 Verbatim-Sample:**
> Hi, ich bin the Owner. Ich saß bis Mai 2024 in einer Hamburger Kanzlei. Anwältin, 70-Stunden-Wochen, Großmandate. Auf dem Papier alles richtig gemacht. Heute morgen war ich barfuß am Strand in Lissabon, hab mit the Owner Kaffee getrunken, und meinen ersten Klienten in seine eigene Praxis-Eröffnung begleitet. Ich erzähle dir das nicht zum Angeben. Sondern weil eine Frau wie du diesen Sprung gerade nicht traut. Ich kenne das. Ich kenne auch das Datum, an dem ich ihn fast nicht getraut hätte: 14. März 2024, 6:42 Uhr morgens, Boden des Kanzleiklos, Bauchkrämpfe.

(Origin-Triple: the Owner + Hamburg + Anwältin. Dann Detail: 14. März 2024, 6:42 Uhr, Bauchkrämpfe. Spezifizität-Pattern. Asymmetrische Satzlängen. KEIN Em-Dash.)

### Example 2: the Founder Webinar-Opener (Mikrobiom-Reset, female 35-55)

**Brief:** 8-Min Webinar-Opener vor Pitch. Reader: Frau 35-55, hatte SIBO/IBS/Hashimoto-Verdacht oder einfach chronisches Bloating, hat schon 2-3 Probiotika probiert. Stage 4, Awareness 3. Survival+Approval.

**Beat 5 Mechanism-Reveal Sample:**
> Hier ist was die letzten 5 Probiotika in deinem Bauch nicht geschafft haben. Sie haben Stämme reingekippt. Aber die Darmflora braucht keine Stämme. Sie braucht eine bestimmte Reihenfolge. In der Charité-Studie, die ich 2023 mit Prof. Stangl mitbetreut habe, n=487, sahen wir genau drei Phasen: Wandregeneration zuerst, dann Schleim-Schicht, dann Strain-Repopulation. Wir nennen das den 27-Tage-Mikrobiom-Reset. Drei Phasen. Eine Reihenfolge. Kein Stamm wird ausgewürfelt.

(Pattern 3 Mechanization: "27-Tage-Mikrobiom-Reset". Pattern 6b Authority: Charité + Prof. Stangl + n=487 + 2023. Pattern 12 Internal-Bridge: Wand → Schleim → Strain. KEIN Em-Dash, asymmetrische Sätze, deutsche Mechanism-Naming.)

---

## Common Mistakes to Avoid

1. **Beat 9 als US-Cascade liefern** (€297→€197→€37). Falsch für DACH Premium. Pattern 11 Single-Preis + Ratenzahlung verwenden.
2. **Englische Mechanism-Trademark-Namen für DACH-Brand** ("BeardFlex™", "Hero Instinct"). Falsch. Deutsche Compound-Konstruktion verwenden.
3. **Beat 1 ohne Origin-Triple**. "Ich war früher unglücklich" reicht nicht. Vorname + Stadt + Beruf + 1 spezifische Tiefpunkt-Szene Pflicht.
4. **Beat 7 Folk-Authority** ("Alte japanische Methode", "Native American Geheimnis"). Pattern 6a ist US-only. DACH-Replacement: Charité, Stiftung Warentest, etc.
5. **Em-Dash für Identifikations-Asides** ("Ich war 39 — broke, single, drowning"). Klassischer Schwartz, aber Anti-AI-Voice gewinnt. Punkt verwenden.
6. **Floskel-Opener** ("In der heutigen schnelllebigen Welt..."). Stattdessen direkt mit Origin-Triple starten ("Hi, ich bin Sandra...").
7. **Beat 4 Curiosity-Gap, der den Mechanismus schon verrät**. Hook andeuten, NICHT erklären. Reveal kommt erst in Beat 5.
