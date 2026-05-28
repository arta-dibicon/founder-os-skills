---
name: target-audience
description: "Erstelle eine komplette Zielgruppenanalyse für einen neuen Markt. TRIGGER wenn the Owner sagt 'Analysiere die Zielgruppe für [X]', 'Wir gehen in den Markt [X]', 'Zielgruppenanalyse für [X]', oder '/target-audience [Nische] [Land]'. Auch bei 'Wer kauft [X]?', 'Wer ist unsere Zielgruppe für [X]?'"
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__apify__search-actors, mcp__apify__fetch-actor-details, mcp__apify__call-actor, mcp__apify__get-actor-output, mcp__apify__get-actor-run
---

# Target Audience Analysis — Vollständige Zielgruppenanalyse

Du führst jetzt eine komplette Zielgruppenanalyse durch. Der gesamte Prozess läuft strukturiert in 5 Phasen.

## Core Principle
"We don't sell products. We sell by understanding our persona. We sell a transformation."

## Input erwarten
Aus der User-Nachricht extrahieren:
- **NISCHE**: Was wird verkauft / welcher Markt? (z.B. "Survival-Ausrüstung", "Titanium Pfannen")
- **LAND**: Zielland/Zielmarkt (z.B. "Deutschland", "DACH", "USA")
- **PROJEKT**: In welchen Projektordner gehört das? (z.B. "3_archiv/eCommerce/survival-shop")

Falls PROJEKT unklar → the Owner fragen: "In welchen Projektordner soll die Analyse?"

## Sprache der Analyse
- Analyse-Dokumente: **Deutsch**
- Voice-of-Customer Zitate: **In der Sprache des Zielmarkts** (DE für Deutschland, EN für USA etc.)
- Research-Quellen: **NUR aus dem Zielland.** Deutscher Markt = deutsche Subreddits, Amazon.de, deutsche Social Media. KEINE englischen Quellen adaptieren.

## Arbeitsverzeichnis
```
[projekt]/zielgruppe/
├── 01-persona-research.md
├── 02-before-after.md
├── 03-personas.md
├── 04-persona-deep-dive.md
├── 05-market-research.md
├── 06-offer-brief.md
├── 07-voice-of-customer.md
└── _raw/
```

Erstelle den Ordner zu Beginn:
```bash
mkdir -p "[projekt]/zielgruppe/_raw"
```

---

## PHASE 1: DATA COLLECTION

### Ziel
Rohdaten aus echten Quellen sammeln. Exact Words der Zielgruppe. Keine Interpretation, nur sammeln.

### 1a. Forum & Reddit Research

**DACH-Märkte: Nischen-Foren sind oft BESSER als Reddit.**
Deutsche Nischen-Foren (PREVIVAL, Tactical Forum, Urban-Prepping, DogForum, Frugalisten, Mamacommunity, Parents.at etc.) liefern tiefere, emotionalere Zitate als Reddit — weil die Nutzer dort länger und ausführlicher schreiben.

**Strategie (Priorität):**
1. **Nischen-Foren identifizieren:** WebSearch: "[Nische] Forum deutsch", "[Nische] Community deutsch", "[Nische] Erfahrungen Forum"
2. **Reddit als Ergänzung:** WebSearch: "[Nische] site:reddit.com deutsch"
3. **Apify nur wenn Reddit-Volumen hoch:** Actor: `trudax/reddit-scraper` o.ä.

**Für EN-Märkte:** Reddit ist Primärquelle. Subreddits direkt suchen + scrapen.

**Forum-Threads laden:**
- WebSearch findet die Threads, WebFetch lädt sie
- Pro Forum: 10-20 relevante Threads + deren Antworten
- **WICHTIG:** Auch die Antworten/Kommentare sind Gold — dort steht die echte Sprache
- Lange Threads komplett lesen — die emotionalsten Zitate stehen oft ab Seite 2+

**Falls Reddit blockiert oder Apify-Limits erreicht:** Kein Problem — Foren-Research ist gleichwertig oder besser für DACH.

**Extrahieren (pro Quelle):**

| Spalte | Was sammeln |
|--------|------------|
| Exact Words / Quotes | Wörtliche Zitate, Formulierungen, Slang |
| Deepest Pains | Die tiefsten Schmerzen hinter den Aussagen |
| Core Desires | Was sie WIRKLICH wollen (nicht was sie sagen) |
| Patterns / Insights | Wiederkehrende Muster, überraschende Erkenntnisse |

### 1b. Amazon Review Mining

**Produkte identifizieren:**
- WebSearch: "beste [Produkt-Kategorie] Amazon.de" oder direkt Amazon.de durchsuchen
- Top 5-10 Produkte der Nische finden
- Apify Actor für Amazon Reviews suchen (`junglee/amazon-reviews-scraper` o.ä.)

**Reviews sammeln:**
- **1-Stern Reviews:** Zeigen echte Frustration, unerfüllte Erwartungen, Deal-Breaker
- **5-Stern Reviews:** Zeigen was funktioniert, welche Transformation erlebt wurde, emotionale Payoffs
- Pro Produkt: mindestens 20 Reviews (10x 1★, 10x 5★)

**Extrahieren:** Gleiche 4-Spalten-Matrix wie Reddit

### 1c. Social Media & Blog Comment Research

**Accounts/Hashtags identifizieren:**
- WebSearch: Top Creator/Influencer in der Nische im Zielland
- Top Hashtags identifizieren

**Daten sammeln (Multi-Source):**
- Apify Actors für Instagram/TikTok Comments nutzen
- Top 10-15 virale Posts/Videos in der Nische
- Comments scrapen (dort steht ungefilterte Sprache)
- **YouTube-Kommentare** sind oft Gold (längere, emotionalere Beiträge als IG/TikTok)
- **Blog-Kommentare** und **Studien/Artikel mit Zitaten** (Uni-Studien, bpb, Fachpresse) ergänzen die Perspektive
- **Wissenschaftliche Quellen** liefern Statistiken die als Authority-Proof dienen

**Extrahieren:** Gleiche 4-Spalten-Matrix

### 1d. Google Trends & Search Intent

**Google Trends:**
- WebSearch oder WebFetch: Google Trends für die Haupt-Keywords
- Trend-Richtung (steigend/fallend/stabil)
- Related Queries (aufsteigende Suchanfragen = Opportunity)
- Saisonalität erkennen

**Search Intent:**
- WebSearch: Die Top-10 Keywords der Nische googeln
- Was rankt? Shops? Blogs? Foren? YouTube?
- Welche Fragen werden gestellt? (People Also Ask)

### 1e. Competitor Deep Scan

**Competitors identifizieren (6 Stück):**
- 2x Industry Leader (größte Player im Markt)
- 2x Direct Competitor (vergleichbare Größe/Angebot)
- 1x Amazon Competitor (Top Amazon-Seller)
- 1x Indirect Competitor (anderer Ansatz, gleiche Zielgruppe)

**Pro Competitor erfassen:**

| Feld | Was |
|------|-----|
| Brand Name | Name |
| Type | Industry Leader / Direct / Amazon / Indirect |
| URL | Website |
| Niche | Genaue Nische |
| Target Customer | Wen sprechen sie an? |
| Branding / Tone | Wie kommunizieren sie? |
| Marketing Angle | Welcher Hauptwinkel? |
| Marketing Appeal | Emotionaler vs. rationaler Appeal? |
| Homepage URL | Link |
| Product Page URL | Beispiel-Produktseite |
| Front-End Offer | Was wird zuerst angeboten? |
| Pricing / Shipping / Bonuses | Preisstruktur |
| Other Products / Upsells | Backend-Angebot |
| What makes product different | USP/Differenzierung |
| Review Summary | Was mögen Kunden? |
| 1★ Review Themes | Häufigste Beschwerden |
| 5★ Review Themes | Häufigste Lobes |
| Facebook/Instagram Ads | Headline, Text, Media-Typ (via Meta Ad Library) |
| TikTok Ads | Hook, Style, Format |

**Tools:** WebFetch für Websites, Apify für Ad Library wenn verfügbar, WebSearch als Fallback

### Phase 1 Output
Speichere alle Rohdaten in `_raw/`:
- `_raw/reddit-research.md`
- `_raw/amazon-reviews.md`
- `_raw/social-media-comments.md`
- `_raw/google-trends.md`
- `_raw/competitors/[name].md`

---

## PHASE 2: SYNTHESIS

### 2a. Persona Research Sheet → `01-persona-research.md`

Konsolidiere alle Rohdaten in die 3-Spalten-Matrix:

```markdown
# Persona Research — [Nische] ([Land])

## Reddit Deep Pain Research
| Exact Words / Quotes | Deepest Pains | Core Desires | Patterns / Insights |
|---|---|---|---|
| "[wörtliches Zitat]" | [Schmerz dahinter] | [Wunsch dahinter] | [Muster] |
...

## Amazon Review Mining (1★ vs 5★)
### 1-Stern (Frustration, Deal-Breaker)
| Exact Words / Quotes | Deepest Pains | Core Desires | Patterns / Insights |
...

### 5-Stern (Transformation, Payoff)
| Exact Words / Quotes | Deepest Pains | Core Desires | Patterns / Insights |
...

## Social Media Comment Research
| Exact Words / Quotes | Deepest Pains | Core Desires | Patterns / Insights |
...
```

**Minimum:** 15 Einträge pro Quelle. Qualität > Quantität, aber eine kritische Masse ist nötig.

### 2b. Before & After → `02-before-after.md`

Aus den Pain/Desire-Paaren der Research erstellen:

```markdown
# Before & After — Emotionale Transformation

| # | BEFORE (Pain) | AFTER (Desire) |
|---|---|---|
| 1 | [Schmerz in ZG-Sprache] | [Wunschzustand in ZG-Sprache] |
...
```

**Regeln:**
- Minimum 15-20 Paare
- In der **exakten Sprache der Zielgruppe** schreiben, nicht Marketing-Deutsch
- Konkret und bildlich, nicht abstrakt
- Beispiel RICHTIG: "Nachts wachliegen und sich fragen ob der Strom morgen noch geht"
- Beispiel FALSCH: "Unsicherheit bezüglich der Energieversorgung empfinden"

### 2c. Persona Match → `03-personas.md`

Erstelle 3-5 Personas basierend auf der Research. Jede Persona folgt diesem Schema:

```markdown
# Personas — [Nische] ([Land])

## Persona 1: [Name]

### Demografisch
- **Alter:** [Range]
- **Geschlecht:** [M/W/Divers]
- **Lebenssituation:** [Beruf, Familie, Wohnsituation]
- **Einkommen:** [Range]

### Awareness & Consciousness
- **Awareness Stage (Schwartz):** [Unaware / Problem-Aware / Solution-Aware / Product-Aware / Most-Aware]
- **Level of Consciousness (Hawkins):** [Fear / Anger / Courage / Neutrality / Willingness etc.]
- **Stage of Sophistication:** [1-5]

### Psychografie
- **Core Beliefs:** [Was glaubt diese Person über das Problem?]
- **Emotional Triggers:** [Was löst Handlung aus?]
- **Wants & Desires:** [Was will sie WIRKLICH?]
- **Pain Points:** [Top 3-5 Schmerzen]
- **Things They Hate:** [Was nervt sie / was lehnt sie ab?]

### Empathy Snapshot
> [2-3 Sätze: Wie fühlt sich ein typischer Tag für diese Person an? In Ich-Form.]

### Before → After Story
> **Vorher:** [Konkreter Zustand]
> **Nachher:** [Konkreter Wunschzustand]

### Proof They Need
- [Welcher Beweis überzeugt diese Person?]

### Key Objections → Rebuttals
| Objection | Rebuttal |
|---|---|
| "[Einwand]" | [Entkräftung] |

### Recommended Angle
- **Landing Page Angle:** [Welcher Typ LP funktioniert?]
- **Hook Type:** [Problem-First / Desire-First / Guarantee-First / Identity-First]

---
```

**Persona-Typen orientieren sich an Awareness:**
- **Completely Unaware Persona** — Weiß nicht dass sie ein Problem hat. Lifestyle-Triggered.
- **Problem-Aware Persona** — Kennt den Schmerz, keine Lösung. Pain-Driven.
- **Solution-Aware Persona** — Kennt Lösungen, hat sich noch nicht entschieden. Solution-Seeking.
- **Product-Aware Persona** — Kennt das Produkt, ist skeptisch. Trust-Hesitant.
- **Identity-Driven Persona** — Will eine neue Version von sich selbst werden. Future-Self.

Nicht alle 5 müssen erstellt werden — nur die die für die Nische relevant sind (typisch 3).

### 2d. Persona Deep Dive → `04-persona-deep-dive.md`

Für jede Persona eine Channel-Matrix:

```markdown
# Persona Deep Dive

## [Persona Name]

| Element | Facebook/Instagram | Ad Headline | Ad Body | Website Copy | Email Angle | TikTok/Reels Hook | Testimonial-Format |
|---|---|---|---|---|---|---|---|
| Who (Beschreibung) | | | | | | | |
| Pain Point | | | | | | | |
| Wants/Desires | | | | | | | |
| Hates | | | | | | | |
| Product Feature | | | | | | | |
| Benefit | | | | | | | |
| Transformation | | | | | | | |
| Social Proof | | | | | | | |
| Emotional Trigger | | | | | | | |
```

### 2e. Market Research → `05-market-research.md`

Konsolidiere die Competitor-Daten aus Phase 1e in ein Vergleichs-Grid:

```markdown
# Market Research — [Nische] ([Land])

## Marktübersicht
- **Marktgröße/Trend:** [Google Trends Daten]
- **Stage of Sophistication:** [1-5 mit Begründung]
- **Dominante Marketing-Angles:** [Was machen alle?]
- **Gaps / Opportunities:** [Was macht KEINER?]

## Competitor Grid
| Feld | Leader 1 | Leader 2 | Direct 1 | Direct 2 | Amazon | Indirect |
|---|---|---|---|---|---|---|
| Brand | | | | | | |
| URL | | | | | | |
| Target | | | | | | |
| Tone | | | | | | |
| Angle | | | | | | |
| Front-End Offer | | | | | | |
| Pricing | | | | | | |
| USP | | | | | | |
| Review Themes (+) | | | | | | |
| Review Themes (-) | | | | | | |
| Ad Style | | | | | | |

## Purple Ocean Opportunity
- **Red Ocean (was alle machen):** [Beschreibung]
- **Unser Purple Ocean Segment:** [Wie grenzen wir uns ab?]
- **Contrast-Strategie:** [Was machen wir ANDERS als alle?]
```

### 2f. Offer Brief → `06-offer-brief.md`

Marks Framework angewandt auf unsere Nische:

```markdown
# Offer Brief — [Nische]

## Produkt
- **Name-Ideen:** [3-5 Vorschläge]
- **Was es ist:** [Konkret]
- **Für wen:** [Persona-Referenz]

## Positioning
- **Level of Consciousness:** Low / High
- **Level of Awareness:** [Stage]
- **Stage of Sophistication:** [1-5]

## Big Idea
[Die eine zentrale Idee/Story]

## Metapher
[Bildliche Darstellung des Konzepts]

## Unique Mechanism
- **UMP (Unique Mechanism of Problem):** [Warum das Problem existiert — was die meisten nicht wissen]
- **UMS (Unique Mechanism of Solution):** [Warum unsere Lösung anders/besser funktioniert]

## Discovery Story
[Wie wurde die Lösung "entdeckt"? Narrativ.]

## Necessary Beliefs
Welche Überzeugungen muss der Prospect haben bevor er kauft? (Max. 6)

1. "Ich glaube, dass..."
2. "Ich glaube, dass..."
3. "Ich glaube, dass..."
4. "Ich glaube, dass..."
5. "Ich glaube, dass..."
6. "Ich glaube, dass..."

## Belief Chain
[In welcher Reihenfolge müssen die Beliefs kippen?]

## Emotional Delta Map
- **Meet them at:** [Welches Bewusstseinslevel? z.B. Fear (100)]
- **Raise them to:** [Wohin heben? z.B. Courage (200)]
- **Bring them back to:** [Zurück zum Ausgangspunkt → Kauf-Trigger]

## Key Objections
| Objection | Unsere Antwort |
|---|---|
| | |

## Headline/Subheadline-Ideen
1. [Idee]
2. [Idee]
3. [Idee]

## Funnel Architecture
[Empfohlener Funnel-Aufbau basierend auf Research]
```

### 2g. Voice of Customer → `07-voice-of-customer.md`

Die destillierten Top-Zitate aus ALLEN Quellen, sortiert nach Nutzbarkeit:

```markdown
# Voice of Customer — [Nische] ([Land])

## Hook-würdige Zitate (direkt als Ad-Hook verwendbar)
1. "[Zitat]" — Quelle: [Reddit/Amazon/Social]
2. ...

## Pain-Zitate (für Problemdarstellung)
1. "[Zitat]" — Quelle
2. ...

## Desire-Zitate (für Wunschzustand)
1. "[Zitat]" — Quelle
2. ...

## Objection-Zitate (für Einwandbehandlung)
1. "[Zitat]" — Quelle
2. ...

## Sprach-Patterns (wiederkehrende Formulierungen)
- "[Pattern]" — Häufigkeit: [oft/mittel/selten]
- ...
```

---

## PHASE 3: OUTPUT & REVIEW

### Qualitäts-Check vor Abschluss
Bevor du the Owner die Ergebnisse präsentierst, prüfe:

- [ ] Alle 7 Dokumente erstellt?
- [ ] Minimum 15 echte Zitate pro Quelle in `01-persona-research.md`?
- [ ] Minimum 15 Before/After Paare?
- [ ] 3-5 Personas mit vollständigem Schema?
- [ ] 5+ Competitors analysiert?
- [ ] Necessary Beliefs definiert (max. 6)?
- [ ] Voice of Customer mit mindestens 10 hook-würdigen Zitaten?
- [ ] Alles in der Sprache des Zielmarkts (Zitate)?
- [ ] Keine eigenen Annahmen als "Research" verkauft?

### Präsentation
Zeige the Owner eine Zusammenfassung:

```
✅ Zielgruppenanalyse für [Nische] ([Land]) abgeschlossen.

📁 Ordner: [projekt]/zielgruppe/

📊 Ergebnisse:
- X Quellen ausgewertet (Reddit, Amazon, Social, Competitors)
- X echte Zitate gesammelt
- X Personas erstellt
- X Competitors analysiert
- X Necessary Beliefs identifiziert

🔑 Top-Insight: [Die überraschendste Erkenntnis]

🎯 Purple Ocean Opportunity: [Kurzfassung]

📝 Nächste Schritte: Die Analyse ist die Basis für Produktauswahl, 
   Advertorials, Landing Pages und Ads.
```

---

## WICHTIGE REGELN

1. **NUR echte Daten.** Keine erfundenen Zitate, keine "typischen" Aussagen. Wenn eine Quelle nichts hergibt, dokumentiere das ehrlich.
2. **Zielland = Datenquelle.** Deutscher Markt → nur deutsche Quellen. Keine englischen Insights "übersetzen".
3. **Exact Words > Interpretation.** Die wörtliche Sprache der Zielgruppe ist wertvoller als jede Analyse.
4. **Tiefe > Breite.** Lieber 3 Personas richtig gut als 5 oberflächliche.
5. **Keine Execution.** Dieser Skill erstellt KEINE Ads, Landing Pages, Shops. Nur Research.
6. **Apify sparsam nutzen.** Nur Actors laden die wirklich gebraucht werden. Nicht alles parallel starten.
7. **Rohdaten behalten.** Alles in `_raw/` speichern — man braucht sie später.
8. **Agent-Tool nutzen** für parallele Recherchen (z.B. 3 Agents für Reddit, Amazon, Social gleichzeitig).
9. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).

## LEARNINGS AUS DEM FELD (validiert)

1. **DACH: Nischen-Foren > Reddit.** Deutsche Foren (PREVIVAL, DogForum, Frugalisten, Mamacommunity etc.) liefern tiefere, emotionalere Zitate. Reddit ist Ergänzung, nicht Primärquelle für DACH.
2. **Wissenschaftliche Quellen als Bonus.** Uni-Studien (z.B. RUB), bpb-Artikel, Bitkom-Studien liefern Statistiken die als Authority-Proof in Copy funktionieren.
3. **Before/After als Narrative, nicht als Tabelle.** Ausformulierte Absätze mit konkreten Szenarien (Name, Alter, Situation) funktionieren besser als trockene Tabellenzeilen.
4. **Empathy Snapshots in 4 Dimensionen.** Was ich DENKE / FÜHLE / TUE / SAGE — gibt jeder Persona sofort Leben.
5. **Sprach-Patterns zweigeteilt: USE vs. AVOID.** Nicht nur sammeln was die ZG sagt, sondern explizit auflisten was sie NICHT sagt / ablehnt. Das verhindert Copy-Fehler.
6. **Kanal-Priorisierung pro Persona.** Am Ende von 04-persona-deep-dive.md eine Matrix: Welcher Kanal ist PRIMÄR/SEKUNDÄR/LOW pro Persona.
7. **Raw-Daten großzügig sammeln.** 50+ Zitate pro Quelle in _raw/ — die Synthesis-Phase destilliert dann die besten 15+ pro Dokument.
8. **BBK/Regierungs-Empfehlungen immer als Trust-Anker nutzen** wenn verfügbar — gilt analog für jede Nische (offizielle Stellen als Authority).
