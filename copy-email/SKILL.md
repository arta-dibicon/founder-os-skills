---
name: copy-email
description: Email, Email-Sequenz, Email Subject Line, Newsletter, Email Body, Welcome-Sequenz, Launch-Sequenz, Reaktivierungs-Email, Email Marketing Copy, Subject Line, Pre-Header, Newsletter-Text, Email-Funnel, Email-Sales-Sequenz
---

# Copy-Email Skill

Email-Copywriting nach 6-Block Email Anatomy. Default-Output: Deutsch, DACH-Markt, Anti-AI-Voice gefiltert. Liefert Subject Line + Pre-Header + Body + CTA + optional PS, plus 3 Subject-Alternatives für Split-Test. Sequenzen mit Rolle pro Email.

## When to use

- Email Subject Line wird gebrieft
- Email-Body / Newsletter-Text gewünscht
- Email-Sequenzen: Welcome, Launch, Abandoned-Cart, Re-Activation, Sales, Nurture
- Pre-Header / Preview-Text
- Brief enthält "Email", "Newsletter", "Subject Line", "Sequenz", "Welcome-Mail", "Launch-Mail", "Reaktivierungs-Mail"
- Klaviyo / Brevo / Mailchimp / Resend Body-Texte

## When NOT to use

- Long-Form Sales Page / Listicle → `copy-listicle`
- Long-Form VSL / Sales Letter → `copy-vsl`
- Meta Ad / FB / IG Primary Text → `copy-ad`
- WhatsApp / Telegram DM / SMS → kein Skill, frei schreiben (anderes Format)
- ManyChat Flow → bestehender `manychat-flow` Skill
- Cold Outreach B2B → bestehender `gm-cold-email` Skill (eigene B2B-Logik)

---

## Workflow (7 Steps)

### Step 1: Read Project Context
- Detect project from chat context, working directory, oder explicit mention.
- Read project's `CLAUDE.md` (auto-loaded) — Brand-Voice, Audience, aktive Kampagnen, Tonalität.
- Audience-Research suchen in `[project]/zielgruppen/`, `[project]/audience-research/`, `[project]/research/` oder `[project]/_memory/INDEX.md`.
- Constraints aus dem Brief notieren: Sequenz-Typ (welcome / launch / re-activation / etc.), Anzahl Emails, Produkt, Preis, Audience-Stage (Subscriber-fresh oder Subscriber-cold), Deadline, Tool (Klaviyo / Brevo / Resend).
- Bei [brand]-Kontext: `arta@example.com` als Sender, Brevo als Tool. Bei the Founder / PLC / [brand]: nicht Brevo (siehe `feedback_brevo_madsen_only`).

### Step 2: Load Foundation
- `_universal-patterns.md` lesen (Sektion 0, Pattern 1-2-4-5-7-8-10-12, 5).
- Cluster-Datei nach Projekt:
  - within-supplements / the Founder / health-supplements → `health-wellness.md`
  - PLC / the Owner / beauty / fitness-baking → `beauty-skincare.md` + `consumer-products.md`
  - [brand] / coaching / Peptide-Story-Funnel → `wealth-coaching.md`
  - [brand] merch / Junsei / e-commerce → `consumer-products.md`
  - [brand] weight-loss / fitness-coaching → `health-wellness.md` + `wealth-coaching.md`

### Step 3: Determine Schwartz Coordinates
Basierend auf Projekt-Kontext + Sequenz-Typ:
- **Awareness Stage** (1 Unaware → 5 Most-Aware) — wo ist der Subscriber?
- **Sophistication Stage** (1-5) — wo ist der Markt?
- **Mass Desire activated** (Power / Sex / Survival / Comfort / Approval)
- **Sequence-Stage:** Welcome (Trust-Build) / Value (Pure-Give) / Story (Identification) / Soft-Pitch / Hard-Pitch / Urgency / Last-Call
- **Cluster + Projekt-spezifische Patterns**

Wenn unklar, the Owner fragen: "Welche Sequenz (Welcome / Launch / Re-Activation)? Wie viele Emails (3 / 5 / 7)? Stage des Subscribers?"

### Step 4: Apply 6-Block Email Anatomy Backbone

Pro Email:

1. **Subject Line:** Loop opening. Curiosity-Gap oder Pattern-Interrupt oder Specific-Number. 4-7 Wörter ideal. KEINE Floskel ("Hey!", "Wichtige News", "Du musst das sehen"). Beispiele:
   - Curiosity-Gap: "Sandra hat aufgehört zu zählen (Tag 14)"
   - Anti-Position: "Es ist nicht dein Stoffwechsel"
   - Numerical: "47 Frauen, 21 Tage, 4,2 cm"
   - Story-Tease: "Ich war 27 und konnte keine 5 Klimmzüge"

2. **Pre-Header:** Schließt den unvollständigen Subject-Gedanken ab oder verstärkt Curiosity. 40-90 Zeichen. Nicht den Subject wiederholen.
   - Subject: "Sandra hat aufgehört zu zählen (Tag 14)"
   - Pre-Header: "Was an Tag 14 passiert ist, hat sie nicht erwartet."

3. **Personal Opener:** 1-2 Zeilen. Direct-Address. Konkret. Keine "Hi du!" Floskel. Beispiele:
   - "Letzte Woche schrieb mir Sandra, 38 aus Hamburg."
   - "Heute ist mir was passiert, was ich kurz teilen will."
   - "Vor 3 Jahren saß ich in einem Café in Lissabon und..."

4. **Story / Identification Beat:** 2-4 Absätze, Plain Prose. Reader sieht sich. Specificity-Pflicht (Pattern 1). Bei Story: Pattern 8 Beat 1+3+6 verkürzt. Bei Value-Drop: Mechanism-Tease (Pattern 12, Internal-Bridge). Bei Permission-Layer (Pattern 3): "Es ist nicht deine Schuld..."

5. **Mechanism Reveal oder Value Drop:** 1-2 Absätze. Bei Sales-Email: Mechanismus benennen (Pattern 3) + Beweis (Pattern 6 Authority oder Pattern 7 Testimonial). Bei Value-Email: Konkreter Tipp / Insight, der allein schon Wert hat.

6. **CTA:** EINE Action. Klar formuliert. Kein Multi-Choice. Beispiele:
   - "Ganzen Plan ansehen →"
   - "Hier dein 21-Tage-Reset"
   - "Bewerbungs-Call buchen"
   - **Optional PS:** Second-Hook-Line. Re-emphasizes Urgency oder fügt Specific-Detail hinzu. PS wird MIT GELESEN — oft mehr als der Body. Nicht verschwenden.

### Step 5: Generate Variants

**Single Email:** 1 vollständige Email + 3 Subject-Alternatives für Split-Test.

**Sequenz:** Default 5 Emails wenn Brief nicht spezifiziert. Sonst the Owner fragen wie viele (3 / 5 / 7) und welcher Sequenz-Typ.

**Sequenz-Rollen-Reihenfolge (Standard):**

3-Email Welcome-Sequenz:
- Email 1: Welcome + Permission-Layer + erste Value (sofort nach Opt-in)
- Email 2: Story / Identification (Tag 1)
- Email 3: Soft-Pitch + CTA (Tag 3)

5-Email Launch-Sequenz:
- Email 1: Story-Hook + Tease (Pre-Launch -3 Tage)
- Email 2: Pure Value + Mechanism-Tease (Pre-Launch -2 Tage)
- Email 3: Launch + Identification (Launch-Tag)
- Email 4: Social Proof + Soft-Push (Launch +1 Tag)
- Email 5: Urgency + Last-Call (Launch +3 Tage, Cart-Close)

7-Email Sequenz (Sales-Funnel):
- Email 1: Welcome + Big Idea
- Email 2: Story (Origin)
- Email 3: Permission-Layer + Mechanism-Reveal
- Email 4: Authority / Social Proof
- Email 5: Soft-Pitch + Bonus-Reveal
- Email 6: Hard-Pitch + Loss-Aversion
- Email 7: Last-Call + Urgency

Re-Activation Sequenz (3 Emails):
- Email 1: Curiosity-Gap Subject + "Wir haben uns lange nicht gehört"
- Email 2: Permission-Layer + neuer Value-Hook
- Email 3: Pattern-Interrupt + "Letzte Mail aus dieser Reihe"

### Step 6: Specificity + Pattern-Check Pass
Self-Check vor Lieferung:
- Mindestens 1 spezifische Zahl / Datum / Stadt / Beruf pro Email?
- Subject Line passt Schwartz-Stage? (Stage 5 → Anti-Position oder Story-Tease, Stage 3 → Numerical-Promise, Stage 1-2 → Curiosity-Gap)
- Pre-Header verstärkt Subject ohne zu wiederholen?
- Body in plain prose (kein Bullet-Bombing — siehe Common Mistakes)?
- EINE klare CTA? Keine Multi-Choice-CTAs ("Mehr lesen ODER Demo buchen")?
- Bei Sequenzen: Rolle pro Email klar, Übergänge logisch, Loss-Aversion (Pattern 5) in der Schluss-Email?
- Internal-Bridge wenn the Founder (Darm → Haut/Haare/Energie)?
- Permission-Layer wenn Audience chronic-attempt-history?
- DACH-Filter: Keine US-Cascade-Pricing, keine Pseudo-Frequency, keine Geographic-Folk-Authority außer Tesla.

### Step 7: Anti-AI-Voice Final Filter
QC-Checkliste aus `.claude/rules/anti-ai-voice.md`:
- 0 Em-Dashes (—)
- Keine "nicht X, sondern Y" Konstruktionen
- Keine Drei-Adjektiv-Listen
- Verbotswort-Scan
- Satzlängen-Variation pro Block: 1× <8 Wörter, 1× >20 Wörter
- Konkret statt abstrakt
- Vorlese-Test: klingt es wie ein Mensch oder wie LinkedIn-Influencer?
- Kein Markdown im Body (Email-Bodies sind plain prose, keine `**bold**` oder `# heading` außer du weißt das Tool rendert es)

Wenn AI-Marker entdeckt → die Zeile umschreiben, NICHT ausliefern.

---

## Output Format

### Single Email

```
## Email-Brief: [Projekt / Sequenz-Rolle / Audience]
**Awareness Stage:** [1-5]
**Sophistication Stage:** [1-5]
**Hauptdesire:** [Power/Sex/Survival/Comfort/Approval]

---

### Email: [Role — z.B. "Welcome Email 1 of 3"]

**Subject:** [text — Loop opening, 4-7 Wörter]
**Pre-Header:** [text — schließt Subject ab, 40-90 chars]

**Body:**
[Plain prose, 80-300 Wörter, kein Markdown im Body]

**CTA:** [text oder Button-Label]

**PS:** [optional — Second-Hook-Line, Specificity oder Urgency]

---

**Subject-Alternatives für Split-Test:**
- [Alt 1 — anderer Hook-Approach]
- [Alt 2 — anderer Hook-Approach]
- [Alt 3 — anderer Hook-Approach]

**Pattern angewendet:** [z.B. Pattern 8 Beat 1 + Pattern 12 Internal-Bridge]
```

### Sequenz

```
## Email-Sequenz-Brief: [Projekt / Sequenz-Typ / N Emails / Audience]
**Awareness Stage:** [1-5]
**Sophistication Stage:** [1-5]
**Hauptdesire:** [...]
**Sequenz-Schema:** [welche Rolle pro Email]

---

### Email 1 of [N]: [Role]

[gleiche Struktur wie Single Email]

---

### Email 2 of [N]: [Role]

[gleiche Struktur]

[...]

---

## Sequenz-Notizen
- **Versand-Timing:** [z.B. "Email 1 sofort, Email 2 +1 Tag, Email 3 +3 Tage"]
- **Tag-Logik:** [z.B. "Bei Klick auf CTA in Email 3 → Tag 'engaged-launch', skip Email 5"]
- **Tool-Hinweis:** [z.B. "Klaviyo Flow oder Brevo Automation — Pre-Header in beiden als 'Preview Text' Field"]
```

---

## Few-Shot Examples

### Example 1 — the Founder Welcome-Email 1 of 3 (Permission-Layer-Hook)

**Brief:** [brand] Welcome-Sequenz für neue Subscriber nach Quiz-Funnel. Audience: Frauen 35-55, aufgeblähter Bauch, haben mehrfach probiert.

**Output:**
```
Subject: Es ist nicht deine Schuld
Pre-Header: Wenn 3 Probiotika nicht geholfen haben, liegt es an was anderem.

Body:
Hi, hier ist the Founder.

Wenn du mein Quiz gemacht hast, weißt du schon: dein Bauch erzählt dir was. Und meistens nicht das, was du denkst.

Ich habe 12 Jahre an der Charité Darm-Mikrobiom erforscht. In dieser Zeit habe ich tausende Frauen wie dich gesehen — Frauen, die schon das fünfte Probiotikum probiert haben und sich fragen, warum nichts funktioniert.

Es liegt nicht an dir. Es liegt daran, dass die meisten Probiotika genau die falschen Stämme enthalten. Oder die richtigen, aber in einer Dosis, die dein Magen nie überlebt.

In den nächsten 3 Tagen schicke ich dir die 3 wichtigsten Sachen, die ich aus 12 Jahren Forschung gelernt habe. Keine Werbung. Echte Wissenschaft, einfach erklärt.

Morgen früh: warum dein Mikrobiom nicht "kaputt" ist. Es schreit nur nach was anderem.

Bis dann,
the Founder

CTA: Quiz-Ergebnis ansehen →

PS: Falls du das Quiz noch nicht gemacht hast — hier ist der Link. Dauert 2 Minuten und du bekommst ein personalisiertes Profil deines Mikrobioms.

---

Subject-Alternatives für Split-Test:
- Was dein aufgeblähter Bauch dir sagt (und was nicht)
- Warum 87% der Probiotika nicht wirken
- Sandra hat 5 Probiotika probiert. Dann das hier.

Pattern: Pattern 3 Permission-Layer + Pattern 12 Internal-Bridge (Mikrobiom→Symptom)
```

### Example 2 — [brand] Launch-Sequenz Email 3 of 5 (Story-Beat)

**Brief:** [brand] €10k Coaching Launch. Email 3 = Launch-Tag, Story-Identification.

**Output:**
```
Subject: Sandra hat 700.000 € aufgegeben
Pre-Header: Was sie an Tag 47 ihrer Großkanzlei-Karriere getan hat.

Body:
Sandra war 38, Anwältin in einer Hamburger Großkanzlei. 700.000 € Jahresgehalt. Bauchkrämpfe morgens.

An einem Mittwoch im März hat sie ihre Kündigung geschrieben. Nicht aus Verzweiflung. Aus Klarheit.

Ich habe 8 Wochen mit ihr gearbeitet. Wir haben nicht über Karrierecoaching geredet. Wir haben über das geredet, was sie eigentlich macht, wenn sie keine Erwartung erfüllt. Über das, was bleibt, wenn der Tag kein Plan hat.

Heute hat sie ihre eigene Praxis in Lissabon. 4 Mandate. Sie verdient ein Drittel von früher und schläft das erste Mal seit 12 Jahren ohne Wecker.

[brand] ist heute live. 6 Plätze für die Q3-Cohort. Ich arbeite 1:1, 8 Wochen. Investition 10.000 € oder 4 mal 2.750 €.

Kein "Lifecoaching". Kein Manifestation-Hokuspokus. Acht Wochen mit jemandem, der dir hilft, deine eigene Klarheit zu finden — bevor die Außenwelt dir sagt, wer du bist.

CTA: Bewerbungs-Call buchen →

PS: Die Bewerbung ist 4 Fragen. Ich lese jede selbst. Wenn ich denke, wir sind kein Match, sage ich das direkt — bevor du Zeit investierst.

---

Subject-Alternatives für Split-Test:
- Anwältin, 700.000 €, gekündigt
- Tag 47 in der Großkanzlei
- Warum Sandra ein Drittel verdient (und schläft)

Pattern: Pattern 8 Beat 1+6 (Origin + Personal Proof) + Pattern 7 (Origin-Triple) + Pattern 11 (Convenience-Path Urgency, kein Discount)
```

### Example 3 — PLC Reactivation Email (Curiosity-Gap Subject)

**Brief:** PLC Re-Activation für Subscriber, die 90 Tage nicht geöffnet haben. Audience: Frauen 28-45, Backen + Fitness, abgekühlt.

**Output:**
```
Subject: Hast du das Schoko-Lava-Update gesehen?
Pre-Header: 280 kcal, kein Mehl, fertig in 12 Minuten.

Body:
Hi,

ich weiß nicht, ob du in den letzten paar Wochen viel von mir gelesen hast. Liegt vielleicht an mir — ich habe lange kein neues Rezept geschickt.

Das ändert sich heute.

Letzten Monat habe ich in der Backstube 9 Versionen von einem Schoko-Lava-Cake getestet. Jede unter 280 kcal. Ohne Industriezucker. Mit Skyr statt Butter. Bei Version 7 hat selbst mein Mann gefragt, was da reingehört.

Das Rezept (mit Step-by-Step Fotos) ist seit gestern in der Bibliothek. Plus 4 weitere, die ich diesen Monat fertig gestellt habe.

Wenn du keine Lust mehr hast — kein Problem, dann meld dich unten ab. Mache ich dir auch nicht übel. Aber wenn du noch dabei sein willst, klick einfach hier.

CTA: Zur Rezept-Bibliothek →

PS: Falls du dich fragst, wo ich war — the Owner hatte ihre erste Pop-Up-Backstube in Hamburg. 3 Wochen Vollgas. Erzähl ich dir nächste Woche.

---

Subject-Alternatives für Split-Test:
- Wir haben uns 87 Tage nicht gehört
- Ein Schoko-Lava unter 280 kcal (kein Witz)
- Letzte Mail von mir, falls du nicht antwortest

Pattern: Pattern 4 (Numerical Promise) + Pattern 10 (Voice-Break "kein Witz") + Permission-Layer ("kein Problem")
```

---

## Common Mistakes to Avoid

1. **Subject Line zu lang:** Mobile schneidet bei ~30-40 Zeichen ab. 4-7 Wörter ist die Sweet Spot. "Hey du! Schau dir das mal an, du wirst es lieben!" — instant Spam-Vibe.
2. **Pre-Header wiederholt Subject:** Verschwendete Zeile. Pre-Header ist die zweite Chance auf Klick — nutzt einen anderen Aspekt.
3. **Bullet-Bombing im Body:** Email-Body ist Brief, kein Pitch-Deck. Plain prose. Bullets nur wenn echt 3+ gleichartige Items.
4. **Multi-Choice-CTA:** "Klick hier ODER buche einen Call ODER lies das PDF." Reader klickt nichts. EINE Action pro Email.
5. **PS leer lassen oder "Schöne Woche!":** PS wird oft mehr gelesen als der Body. Specific-Hook oder Urgency oder Story-Detail. Nicht verschwenden.
6. **Em-Dash für Identification-Aside:** Klassisch Schwartz, aber Anti-AI-Voice killt es. Punkt oder Doppelpunkt.
7. **"Liebe [Vorname]" / "Hi du!" als Opener:** Fühlt sich an wie Mass-Mail. Direkter Einstieg in eine Beobachtung oder Story zieht stärker.
8. **Markdown im Body bei Klaviyo / Mailchimp / Brevo:** Wird oft nicht gerendert. Plain prose oder das Tool's eigenes Format nutzen. Wenn unsicher: kein Markdown.
9. **Sequenz ohne Rollen-Logik:** Wenn alle 5 Emails dasselbe Ziel haben, ist es keine Sequenz, ist Spam. Jede Email hat genau eine Rolle (Trust / Story / Mechanism / Pitch / Urgency).
10. **Vor allem bei the Founder: Permission-Layer vergessen.** the Founder-Audience ist chronic-attempt-history. Erste 2 Emails IMMER Permission ("nicht deine Schuld"), sonst klingt es wie das fünfte Supplement, das ihnen gepitcht wird.

---

## Loading Pointers
Foundation-Datei-Pfade siehe `references/POINTERS.md` in diesem Skill-Ordner.
