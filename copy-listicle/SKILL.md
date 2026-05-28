---
name: copy-listicle
description: Advertorial-Listicle, Sales Page, Long-Form Sales Page, X Gründe Pages, Listicle Advertorial, '5 Gründe', '7 Reasons', '9 Reasons Why', Product Sales Page, E-Commerce Long-Form, Listicle Copy, Listicle Article
---

# Copy-Listicle Skill

Long-Form Listicle-Sales-Page Copywriting nach dem 7-Section Listicle Anatomy Backbone (Schwartz Backbone B). Default: DACH-Markt, Deutsch, Anti-AI-Voice gefiltert. Für E-Commerce, Consumer Products und Mid-Ticket Sales-Pages.

## When to use

- Long-Form Produkt-Sales-Page (1500-5000 Wörter) gewünscht
- Listicle-Format ("X Gründe warum...", "7 Reasons Why...", "9 Gründe für...")
- E-Commerce / Consumer Product / Mid-Ticket-Preis (€20-€500)
- Awareness Stage 1-3 (Unaware bis Solution-Aware)
- Junsei Cookware, PLC Bundle-Page, the Founder E-Comm Side, [brand] Merch Listicle
- Brief enthält "Listicle", "Advertorial", "Gründe", "Sales Page", "PDP Long-Form", "E-Comm Page"

## When NOT to use

- Story-VSL / Long-Form Sales Letter mit Story-Arc → `copy-vsl`
- Kurze Ad Copy (Meta Primary Text, Headlines) → `copy-ad`
- Email Body / Email Subject / Sequenzen → `copy-email`
- High-Ticket Coaching €500+ Transformation-Produkt → `copy-vsl` (braucht Story-Backbone, nicht Listicle)
- Quiz-Funnel → bestehender `quizfunnel` Skill
- Carousel / Short-Form Social → bestehende `carousel-*` Skills
- Bestehende `listicle` und `advertorial` Skills gehen auf HTML-Render-Output. Dieser Skill ist NUR Copy (Text), nicht HTML.

---

## Workflow (7 Steps)

### Step 1: Read Project Context

- Erkenne welches Projekt (team-madsen merch / pretty-little-cakes / within-supplements / eCommerce-Junsei / peptide-venture etc.).
- Projekt-`CLAUDE.md` ist auto-loaded.
- Audience-Research suchen in:
  - `[project]/zielgruppen/`
  - `[project]/audience-research/`
  - `[project]/research/`
  - `[project]/_memory/INDEX.md`
- Note Constraints: Reason-Count (5/7/9), Wortzahl, Kanal (Funnel-Page vs Email-Block), Bundle-Pricing-Tier, gesetzliche Constraints (§1 PAngV, UWG §3).

### Step 2: Load Foundation

- Read `references/POINTERS.md` für Pfade.
- Lies `_universal-patterns.md` (Sektionen 0, 1, 2 (Pattern 9 Listicle Anatomy!), 5, 6, Section 7 #5 Taima-Template, Section 7 honorable mention MudWtr).
- Lies passenden Cluster:
  - within-supplements / the Founder / health-supplements → `health-wellness.md`
  - PLC / the Owner / fitness-baking / dessert-product → `beauty-skincare.md` + `consumer-products.md`
  - [brand] merch / Junsei Titanium / e-commerce / coffee / accessories → `consumer-products.md`
  - Peptide-Venture E-Comm-Side → `health-wellness.md`

### Step 3: Determine Schwartz Coordinates

- **Awareness Stage** (Default: Listicle = 1-3 Stage)
- **Sophistication Stage** (Default: Stage 3-4 für Listicle-Format)
- **Mass Desire activated**

Defaults wenn nicht explizit gebrieft:
- Junsei Titanium: Stage 4 / Awareness 2-3 / Survival+Approval (Counterfeit-Moat-Angle)
- the Founder E-Comm-Bundle: Stage 4 / Awareness 2-3 / Survival+Approval
- [brand] Merch: Stage 3 / Awareness 3 / Approval+Power (Identity-Tribe)
- PLC Bundle: Stage 3 / Awareness 2-3 / Comfort+Approval

Wenn unklar, frag the Owner:
"Default Reason-Count = 5/7/9? Awareness ~3 + Sophistication ~4 für [Projekt] — passt das?"

### Step 4: Apply 7-Section Listicle Anatomy (Backbone B)

Gerüst (siehe `_universal-patterns.md` Pattern 9). Sections 1-7:

1. **Quantity-Hook Headline** — Pattern 4 Numerical Promise im Headline. Format: "[Number] Gründe warum [Audience-Identity] [Verb] [Brand/Produkt]". Beispiele:
   - "9 Gründe, warum 14.000 Hamburger Sterne-Köche zu Junsei Titan wechseln"
   - "5 Gründe, warum 487 Frauen das Mikrobiom-Reset von the Founder über jedes Probiotikum stellen"
2. **Pain-Agitation Lead** — Status-Quo zerstören. Spezifisch + sensorisch. 60-150 Wörter. Konkrete Kosten der Untätigkeit. Pattern 1 (Specificity) hier dicht. Optional Pattern 12 (Internal-Bridge) wenn the Founder / Health.
3. **Discovery-Moment / Brand Reveal** — Soft Pivot von Pain → Lösung. "Wir haben uns gefragt, warum noch nie jemand..." / "Das ist [Brand] — gegründet 2023 in Hamburg von [Name]." 80-150 Wörter.
4. **Reasons #1-N** — Bold-Headline + 1-3 Sätze + (optional) Visual-Description + (optional) Micro-CTA.
   - Mindestens 1 Reason = Guarantee oder Social Proof, nicht Feature.
   - **Reason #3 oder #4 = Voice-Break** (Pattern 10): EINE colloquial Zeile als Humanity-Signal. DACH-native: "Endlich keine Speckrolle mehr." / "Tschüss Kaffee-Kater." / "Kein Witz." / "Wirklich." Single fragment + Punkt.
   - Default Reason-Count = 5 wenn nicht spezifiziert. Frag the Owner wenn unklar 5/7/9.
5. **Authority / Social-Proof Block** — Aggregate (z.B. "Trustpilot 4,8/5 bei 12.487 Bewertungen") + 3 namentliche Testimonials im Origin-Triple-Format (Pattern 7).
   - DACH-Adaption: Charité / Stiftung Warentest / Öko-Test / TÜV / Sterne-Koch. KEINE US-Folk-Authority (Pattern 6a).
6. **Bundle-Pricing Stack** — 1x → 3x → 6x mit Spar-Math. Per-Stück-Preis transparent (§1 PAngV-konform).
   - Beispiel: "1 Pfanne: 119 € (119 €/Stück) / 2er-Set: 198 € (99 €/Stück, sparst 40 €) / 4er-Set: 356 € (89 €/Stück, sparst 120 €)"
   - Bei Premium (Pattern 11): kein Discount-Cascade, stattdessen "0% Ratenzahlung über 6 Monate".
7. **Guarantee + CTA + Urgency** —
   - Guarantee: "30 Tage Geld-zurück-Garantie zusätzlich zum gesetzlichen 14-Tage-Widerrufsrecht."
   - CTA: Identity-CTA, kein generisches "Kaufen". Z.B. "Ja, ich will mein Mikrobiom resetten" / "Pfanne sichern".
   - Urgency: REAL, nicht fake-Timer. "Letzte 47 Sets aus dem Frühjahr." / "Aktion bis 31.05.2026, 23:59 Uhr." NIEMALS US-Style "00:00:00" countdown ohne reale Cap (UWG §3 Risiko, BGH I ZR 7/16).

### Step 5: Generate Variants

Default Output:
- **1 vollständige Listicle-Page** (ca. 1500-3500 Wörter je nach Reason-Count)
- **3 alternative Headline-Varianten** (Section 1) für Split-Test, jede zieht anderen Pattern:
  - Variante A: Numerical-Promise-Headline
  - Variante B: Anti-Position-Headline ("Vergiss [incumbent] — [Number] Gründe für [Brand]")
  - Variante C: Permission-Layer-Headline ("Es ist nicht deine Schuld — [Number] Gründe warum [Brand] funktioniert wo [Kategorie] versagt")

Default Reason-Count = 5 wenn nicht spezifiziert.

### Step 6: Specificity + Pattern-Check Pass

- Mindestens 1 spezifische Zahl / Datum / Stadt / Beruf pro Reason?
- Section 1 Headline mit Numerical Promise (Pattern 4)?
- Section 2 mit konkreter Pain-Agitation (Pattern 1 Specificity)?
- Section 4 Voice-Break in Reason #3 oder #4 (Pattern 10) als deutsche Fragment-Zeile?
- Mindestens 1 Reason als Guarantee oder Social Proof, nicht Feature?
- Section 5 Authority DACH-konform (Charité / Stiftung Warentest / etc., NICHT US-Folk)?
- Section 5 Testimonials im Origin-Triple-Format (Vorname + Stadt + Beruf + Ergebnis)?
- Section 6 Per-Stück-Preis transparent (PAngV)?
- Section 7 Urgency real, nicht fake-Timer?
- Internal-Bridge (Pattern 12) wenn the Founder (Darm → Haut/Haare/Nägel)?
- Anti-Position (Pattern 2) wenn Stage 4-5 Markt?

### Step 7: Anti-AI-Voice Final Filter

- 0 Em-Dashes (—)
- Keine "nicht X, sondern Y" Konstruktionen (Voice-Break Fragment ist OK!)
- Keine Drei-Adjektiv-Listen (auch nicht in Reason-Headlines)
- Verbotswort-Scan: ganzheitlich, nahtlos, optimal, robust, cutting-edge, revolutionär, hervorheben, beleuchten
- Floskel-Opening / Closing Check
- Satzlängen-Variation: pro Section min 1× <8 Wörter UND 1× >20 Wörter
- Konkret-Test pro Reason: spezifische Zahl/Name/Datum
- Vorlese-Test
- Voice-Break in Reason #3 oder #4 = deutsche Fragment-Zeile, KEIN englisches Loanword (außer Brand IS English-speaking)

---

## Output Format

```
# Listicle: [Brand / Produkt]

**Total Wortzahl:** ~[X] Wörter
**Awareness Stage:** [N] / **Sophistication Stage:** [N] / **Dominant Mass Desire:** [...]
**Reason-Count:** [N]
**Patterns aktiv:** [...]

## Section 1 — Headline
[Quantity-Hook Headline mit Number]

## Section 2 — Pain-Agitation Lead
[60-150 Wörter Plain Prose]

## Section 3 — Discovery-Moment / Brand Reveal
[80-150 Wörter Plain Prose]

## Section 4 — Reasons

### Reason #1: [Bold Sub-Headline]
[1-3 Sätze]

### Reason #2: [Bold Sub-Headline]
[1-3 Sätze]

### Reason #3: [Voice-Break Fragment]
[1-3 Sätze, einer davon das Voice-Break Fragment]

### Reason #4: [Bold Sub-Headline]
[1-3 Sätze]

### Reason #5: [Bold Sub-Headline = Guarantee oder Social Proof]
[1-3 Sätze]

## Section 5 — Authority + Social Proof
[Aggregate-Stat]
[Testimonial 1: Origin-Triple]
[Testimonial 2: Origin-Triple]
[Testimonial 3: Origin-Triple]

## Section 6 — Bundle-Pricing
| Tier | Stück | Preis | Per Stück | Sparersparnis |
|---|---|---|---|---|
| 1x | 1 | [Preis] | [Preis] | — |
| 3x (Most Popular) | 3 | [Preis] | [Preis] | [€-Beleg] |
| 6x (Biggest Save) | 6 | [Preis] | [Preis] | [€-Beleg] |

## Section 7 — Guarantee + CTA + Urgency
[30-Tage-Garantie + 14-Tage-Widerruf]
[Identity-CTA-Button-Label]
[REAL Scarcity / Cap]

---

## Headline-Varianten für Split-Test

### Variant A — Numerical-Promise
[Headline]

### Variant B — Anti-Position
[Headline]

### Variant C — Permission-Layer
[Headline]
```

---

## Few-Shot Examples

### Example 1: Junsei Titanium Pfanne 7-Gründe (DACH male 30-50 home-cook, Stage 4)

**Section 1 Headline-Sample:**
> 7 Gründe, warum 14.872 deutsche Hobbyköche ihre Teflonpfanne entsorgt und auf Junsei Titan gewechselt sind

**Section 4 Reason #3 (Voice-Break) Sample:**
> ### Reason #3: Endlich keine Mikroplastik-Spuren mehr in deinem Frühstücksei.
> Wir haben unsere ersten Junsei-Pfannen 2023 an 200 Probanden in Hamburg, München und Köln verteilt. Eine Probandin schrieb uns nach 6 Wochen: "Ich konnte heute mein Spiegelei mit der Holzgabel rauskratzen, ohne dass irgendwas am Boden klebte." Wirklich.

(Pattern 1 Specificity: 14.872 Hobbyköche, 2023, 200 Probanden, 3 Städte. Pattern 10 Voice-Break: "Wirklich." als deutsches Fragment. Pattern 7 Origin-Triple light: Probandin + 6 Wochen + konkrete Szene.)

### Example 2: the Founder Mikrobiom-Drink 5-Gründe (DACH female 35-55, Stage 4)

**Section 1 Headline-Sample:**
> 5 Gründe, warum 487 Frauen aus der Charité-Studie das Mikrobiom-Reset über jedes Probiotikum gestellt haben

**Section 2 Pain-Agitation Lead-Sample:**
> Du hast 3 Probiotika probiert. Vielleicht 4. Vielleicht hast du sogar das teure aus der Apotheke gekauft, das die Heilpraktikerin empfohlen hat. Drei Wochen ging es besser. Dann war es wieder da. Dieses Bauch-Druck-Gefühl nach dem Mittagessen. Brüchige Nägel. Haare, die im Abfluss landen. Vielleicht hat dir jemand gesagt, das sei dein Alter. Es ist nicht dein Alter. Es ist die Reihenfolge.

(Pattern 12 Internal-Bridge: Bauch → Nägel → Haare. Pattern 3 Permission-Layer: "Es ist nicht dein Alter." Asymmetrische Sätze: 4 Wörter, dann 12, dann 5. KEIN Em-Dash. Verbotswort-Check sauber.)

---

## Common Mistakes to Avoid

1. **Voice-Break als komplette Headline statt Fragment in Reason #3/#4** — "Endlich keine Speckrolle mehr" als Section-1-Headline ist falsch, gehört in Reason. Section 1 = Quantity-Hook.
2. **Englischer Voice-Break in DACH-Brand** ("Delicious AF" für the Founder). Falsch. Deutsche colloquial Fragment verwenden.
3. **US-Style fake Countdown-Timer** ("00:00:00 — Aktion endet jetzt!"). UWG §3 / §5 Risiko + BGH I ZR 7/16. REAL Cap verwenden.
4. **Per-Stück-Preis nicht transparent in Bundle-Stack** — §1 PAngV verlangt Grundpreis. Tabelle mit Per-Stück-Spalte ist Pflicht.
5. **Authority US-Folk** ("Alte japanische Methode", "5000-jähriges ägyptisches Mysterium"). DACH liest als Kitsch. Charité / Stiftung Warentest / Sterne-Koch verwenden.
6. **Alle 5 Reasons sind Features** — mindestens 1 Reason muss Guarantee oder Social Proof sein.
7. **Em-Dashes** für Reason-Substitches ("Reason #1: Klebt nicht — schmeckt besser — kostet weniger"). 3 AI-Marker auf einmal: Em-Dash + Rule of Three. Komplett umschreiben.
