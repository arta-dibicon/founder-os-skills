---
name: product-research
description: "Finde und validiere Produkte für einen Markt — basierend auf Zielgruppenanalyse. TRIGGER wenn the Owner sagt 'Welches Produkt sollen wir verkaufen?', 'Produktrecherche für [X]', 'Was können wir in [Nische] verkaufen?', oder '/product-research [Nische] [Land]'. Auch bei 'Finde Produkte für [X]', 'Validiere dieses Produkt', 'Produktideen für [X]'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__apify__search-actors, mcp__apify__fetch-actor-details, mcp__apify__call-actor, mcp__apify__get-actor-output, mcp__apify__get-actor-run, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot
---

# Product Research & Validation — Produkt finden, validieren, bewerten

Du führst jetzt eine komplette Produktrecherche und -validierung durch. Dieser Skill kommt NACH der Zielgruppenanalyse (`/target-audience`) und liefert die Basis für den Funnel-Skill.

## Core Principles
- **"Winning products are not found — they are CREATED."** (Mark Builds Brands)
- **"Mass desire cannot be created, only transferred."** (Schwartz) → Verkaufe in Märkte mit bewiesener Nachfrage.
- **Purple Ocean:** Bewährter Markt + hyper-spezifisches Segment ownen.
- Validierung mit echten Daten, nicht Bauchgefühl. "Assume nothing. Data is king."
- Produkte sind Commodities — der Wettbewerbsvorteil liegt in Creative, Funnel und Branding.

## Input erwarten
Aus der User-Nachricht extrahieren:
- **NISCHE**: Welcher Markt? (z.B. "Krisenvorsorge", "Fitness-Baking")
- **LAND**: Zielmarkt (z.B. "Deutschland", "USA")
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **ZIELGRUPPE**: Pfad zur bestehenden Zielgruppenanalyse (z.B. "[projekt]/zielgruppe/")

Falls keine Zielgruppenanalyse existiert → the Owner informieren: "Ich brauche erst eine Zielgruppenanalyse. Soll ich `/target-audience` starten?"

## Vorbereitung: Zielgruppen-Research laden
Bevor irgendwas passiert — die bestehende Analyse lesen:
1. `03-personas.md` → Pain Points, Desires, Awareness Stages
2. `06-offer-brief.md` → UMP, UMS, Necessary Beliefs, Big Idea
3. `05-market-research.md` → Competitors, Gaps, Purple Ocean
4. `07-voice-of-customer.md` → Sprach-Patterns, Hook-Zitate

Diese Dokumente sind die GRUNDLAGE für alles was folgt. Ohne sie ist die Produktrecherche wertlos.

## Arbeitsverzeichnis
```
[projekt]/produkte/
├── 01-product-candidates.md
├── 02-validation-report.md
├── 03-product-ranking.md
└── _raw/
    ├── similarweb/
    ├── amazon-data/
    ├── ad-library/
    └── trends/
```

```bash
mkdir -p "[projekt]/produkte/_raw/similarweb" "[projekt]/produkte/_raw/amazon-data" "[projekt]/produkte/_raw/ad-library" "[projekt]/produkte/_raw/trends"
```

---

## PHASE 1: PRODUCT IDEATION

### Ziel
Produktkandidaten identifizieren die aus den Pains, Desires und Gaps der Zielgruppenanalyse abgeleitet sind. NICHT erfinden — ableiten.

### 1a. Pain-to-Product Mapping

Aus den Personas (03-personas.md) die Top-Pains extrahieren und für jeden Pain mögliche Produkte brainstormen:

| Pain Point (aus Research) | Produkt-Typ | Konkretes Produkt | Physical / Digital / Hybrid |
|---|---|---|---|
| "[Pain in ZG-Sprache]" | Bundle / Einzelprodukt / Guide / Kurs / Tool | "[Name/Beschreibung]" | P / D / H |

**Regeln:**
- Minimum 10-15 Produktkandidaten
- Mix aus Physical (Shop/Dropshipping/Eigenmarke), Digital (Guide/Kurs/Membership/Template), und Hybrid (Physical + Digital Bundle)
- Jeder Kandidat muss einen konkreten Pain aus der Research adressieren
- "Wenn du keinen Pain dafür findest, gibt es das Produkt nicht."

### 1b. Competitor Product Scan

Was verkaufen die Competitors aus der Market Research (05-market-research.md)?

**Pro Competitor:**
| Competitor | Top-Produkte | Pricing | Bundle-Strategie | Was fehlt? |
|---|---|---|---|---|
| [Name] | [Produkte] | [Preis-Range] | [Bundles? Upsells?] | [Gap] |

**Tools:**
- WebFetch für Competitor-Shops (Homepage + Bestseller-Seite)
- Amazon Bestseller-Listen in der Kategorie
- Apify für Amazon-Produktdaten wenn nötig

### 1c. Gap-to-Opportunity Mapping

Aus 05-market-research.md die identifizierten Gaps und unbesetzten Positionen nehmen und in konkrete Produktideen übersetzen:

| Gap (aus Market Research) | Opportunity | Produktidee | Warum unbesetzt? |
|---|---|---|---|
| "[Gap]" | [Chance] | [Konkretes Produkt] | [Grund] |

### 1d. Digital Product Assessment

Für digitale Produkte separat prüfen:

| Digitales Produkt | Format | Delivery | Erstellungsaufwand | Skalierbarkeit | Margenpotenzial |
|---|---|---|---|---|---|
| "[Name]" | Guide/Kurs/Template/Membership/Affiliate-Liste | PDF/Video/App/Web | Niedrig/Mittel/Hoch | ★★★★★ | ~100% |

**Digitale Produkte checken gegen:**
- Löst es den "Wo anfangen?"-Pain? (Informationsparalyse)
- Kann es als Lead-Magnet UND als Paid-Produkt funktionieren?
- Gibt es Upsell-Potenzial zu physischen Produkten?
- Ist der Content einzigartig genug oder leicht replizierbar?

### Phase 1 Output
Konsolidierte Kandidatenliste → `01-product-candidates.md`

---

## PHASE 2: CRITERIA CHECK

### Ziel
Jeden Produktkandidaten gegen harte Kriterien prüfen. Wer die Kriterien nicht erfüllt, fliegt raus.

### 2a. Scoring-Kriterien

Jeder Kandidat wird auf einer Skala von 1-5 pro Kriterium bewertet:

#### Kriterium 1: Painful Problem (Gewichtung: 25%)
> "Die schmerzhaftesten Probleme liegen unten in Maslow's Hierarchie."

| Score | Definition |
|---|---|
| 5 | Physiologisch / Sicherheit — lebensnotwendig, akut, dringend |
| 4 | Zugehörigkeit / Beziehung — soziale Angst, Isolation, Familienschutz |
| 3 | Anerkennung — Status, Selbstwert, Stigma |
| 2 | Selbstverwirklichung — Nice-to-have, Optimierung |
| 1 | Kein klarer Pain — Gadget, Impulskauf |

#### Kriterium 2: Margins (Gewichtung: 20%)

**Physische Produkte:**
| Score | Definition |
|---|---|
| 5 | 5x+ COGS, >€40 Gross Profit pro Bestellung |
| 4 | 4x COGS, €30-40 GP |
| 3 | 3x COGS, €25-30 GP (Mark's Minimum) |
| 2 | 2x COGS, €15-25 GP |
| 1 | <2x COGS oder <€15 GP |

**Digitale Produkte:**
| Score | Definition |
|---|---|
| 5 | 90%+ Marge, >€30 pro Verkauf, automatisiert |
| 4 | 80%+ Marge, €20-30 pro Verkauf |
| 3 | 60%+ Marge, €10-20 pro Verkauf |
| 2 | <60% Marge oder <€10 pro Verkauf |
| 1 | Marge unklar oder negativ nach Ad-Spend |

#### Kriterium 3: Shippability / Deliverability (Gewichtung: 10%)
| Score | Definition |
|---|---|
| 5 | Digital (sofort lieferbar) ODER passt in Briefkasten |
| 4 | Passt in Schuhkarton, <2kg |
| 3 | Kleines Paket, 2-5kg |
| 2 | Großes Paket, 5-15kg, Versandkosten spürbar |
| 1 | Spedition nötig, fragil, kompliziert |

#### Kriterium 4: Evergreen (Gewichtung: 10%)
| Score | Definition |
|---|---|
| 5 | Ganzjährig stabil, kein saisonaler Einfluss |
| 4 | Leichte Saisonalität, aber ganzjährig verkaufbar |
| 3 | Klare Saison, aber 8+ Monate aktiv |
| 2 | Starke Saisonalität, 4-6 Monate aktiv |
| 1 | Reines Saison-/Trend-Produkt |

#### Kriterium 5: LTV / Upsell-Potenzial (Gewichtung: 20%)
| Score | Definition |
|---|---|
| 5 | Subscription-Modell möglich, wiederkehrend, Cross-Sell-Ökosystem |
| 4 | Consumable (Nachkauf nötig) ODER starke Cross-Sell-Produkte |
| 3 | Einmalkauf aber mit 2-3 logischen Upsells |
| 2 | Einmalkauf mit 1 möglichem Upsell |
| 1 | Einmalkauf ohne Upsell-Potenzial |

#### Kriterium 6: Competitive Advantage (Gewichtung: 15%)
> "Wo können WIR gewinnen — Creative, Funnel, Branding oder Segment?"

| Score | Definition |
|---|---|
| 5 | Wir haben 3+ Vorteile (z.B. besseres Branding + besserer Funnel + unbesetztes Segment) |
| 4 | 2 klare Vorteile |
| 3 | 1 klarer Vorteil |
| 2 | Gleiche Ebene wie Competitors |
| 1 | Competitors haben uns in allem voraus |

**Vorteilstypen (aus Video 2):**
- **Creative:** Wir können bessere/mehr Ads produzieren als der Wettbewerb
- **Funnel:** Wir nutzen Advertorial/Quiz/Pre-Sale statt Basic PDP
- **Branding:** Anti-Stigma, Purple Ocean Segment, Clean Design vs. Army-Look
- **Segment:** Wir bedienen eine Zielgruppe die NIEMAND bedient
- **Content:** Wir bauen Authority via Blog/Video (Content-to-Commerce)

### 2b. Scoring-Matrix

| Kandidat | Pain (25%) | Margins (20%) | Ship (10%) | Evergreen (10%) | LTV (20%) | Competitive (15%) | **TOTAL** |
|---|---|---|---|---|---|---|---|
| Produkt A | 4 | 3 | 5 | 5 | 4 | 4 | **4.00** |
| Produkt B | 3 | 5 | 4 | 4 | 3 | 3 | **3.55** |

**Minimum-Score für Weiterqualifikation: 3.0**

Alles unter 3.0 wird eliminiert. Die Top 5-8 Kandidaten gehen weiter in Phase 3.

---

## PHASE 3: VALIDATION MIT DATEN

### Ziel
Harte Daten sammeln die beweisen, dass der Markt für dieses Produkt REAL ist und dass Leute JETZT dafür zahlen. "Don't sell something that's not proven to sell."

### 3a. Search Volume Validation

**Tool:** WebSearch für Keyword-Daten, Google Keyword Planner via WebFetch

Pro Produktkandidat:
| Keyword | Monatliches Suchvolumen | Trend | CPC (€) | Intention |
|---|---|---|---|---|
| "[Haupt-Keyword]" | [Volumen] | ↗/→/↘ | [CPC] | Informational/Transactional |

**Minimum:** 5.000 Suchen/Monat für das Haupt-Keyword (DACH-Markt). Für EN-Märkte: 10.000+.

**Hinweis:** Informationelle Keywords zählen MIT — wer Content-to-Commerce macht, nutzt auch informationelle Suchanfragen.

### 3b. Google Trends Validation

**Tool:** WebSearch/WebFetch für Google Trends Daten

Pro Produktkandidat:
- Haupt-Keyword auf Google Trends, Zeitraum 5 Jahre
- **Was wir sehen wollen:** Stabiler oder steigender Trend. KEIN abfallender Trend.
- **Spike-Check:** Event-getriebene Spikes (z.B. Blackout → "Notstromaggregat") sind okay WENN der Baseline-Trend auch steigt
- Related Queries: Aufsteigende Suchanfragen = zusätzliche Opportunity

Speichere Screenshots/Daten in `_raw/trends/`

### 3c. Competitor Revenue Validation (SimilarWeb)

> "Ich will beweisen können, dass ein Competitor mindestens €300.000/Monat macht." (Mark)

**Methode:** SimilarWeb (Free Extension, 3 Checks/Tag) oder WebSearch "site:similarweb.com [competitor]"

Pro Top-Competitor:
| Competitor | Monthly Visits | Est. CR | Est. AOV | **Est. Revenue** |
|---|---|---|---|---|
| [URL] | [Visits] | 2% (Default) | €[AOV] | Visits × CR × AOV |

**Revenue-Formel:**
```
Estimated Revenue = Monthly Visits × Conversion Rate (2% Default) × Average Order Value
```

**Minimum:** Mindestens 1 Competitor muss >€100.000/Monat machen (für DACH). Für US/EN: >$300.000/Monat.

**Für digitale Produkte:** SimilarWeb + zusätzlich prüfen:
- Gibt es Paid-Kurse/Guides zum Thema? Was kosten sie?
- Udemy/Skillshare/elopage Bestseller in der Kategorie?
- Amazon Kindle: Top-Bücher zum Thema + Bewertungsanzahl

Speichere Daten in `_raw/similarweb/`

### 3d. Ad Library Research

> "Wer Ads schaltet, verdient Geld. Wer VIELE Ads schaltet, verdient VIEL Geld."

**Meta Ad Library:**
- WebFetch/Playwright: facebook.com/ads/library → nach Competitor-Brands suchen
- Pro Competitor: Wie viele aktive Ads? Welcher Typ (Video/Image/Carousel)? Wie lange laufen sie?

**Heuristik:**
| Aktive Ads | Interpretation |
|---|---|
| 50+ | Skaliert aggressiv, validiert |
| 20-50 | Aktiv am Testen, wahrscheinlich profitabel |
| 5-20 | Testet, noch nicht skaliert |
| <5 | Entweder gerade erst gestartet oder keine Paid-Strategie |

**Was wir suchen:**
- Ads die >30 Tage laufen → Beweis dass sie profitabel sind (sonst wären sie abgeschaltet)
- Engagement-Ratio: 10k+ Likes mit 5k+ Shares = virales Potenzial (2:1 Ratio)
- Ad-Typ: Video/UGC/Native Static → zeigt was im Markt funktioniert

**TikTok Creative Center:**
- WebSearch: "TikTok Creative Center [Nische] [Land]"
- Top Ads im Markt finden, Hooks analysieren

Speichere Daten in `_raw/ad-library/`

### 3e. Amazon Validation

**Tool:** Apify Amazon Scraper oder WebSearch

Pro Produktkandidat:
| Produkt | BSR (Best Seller Rank) | Reviews | Preis | Rating |
|---|---|---|---|---|
| [Name] | #[Rank] in Kategorie | [Anzahl] | €[Preis] | [★] |

**Heuristik BSR → Verkäufe (Schätzung):**
| BSR Range | Geschätzte Verkäufe/Tag (Hauptkategorie) |
|---|---|
| #1-100 | 50-300+ |
| #100-500 | 15-50 |
| #500-2000 | 5-15 |
| #2000-10000 | 1-5 |
| #10000+ | <1 |

**Review-Volumen als Proxy:**
- 1.000+ Reviews = bewiesener Bestseller
- 500-1.000 = solide Nachfrage
- 100-500 = Nischen-Produkt mit Potenzial
- <100 = zu früh oder zu klein

Speichere Daten in `_raw/amazon-data/`

### 3f. Validation Score

Jeder Kandidat bekommt einen Validation-Score:

| Dimension | Gewichtung | Score 1-5 |
|---|---|---|
| Search Volume | 20% | 1=<1k, 2=1-5k, 3=5-10k, 4=10-50k, 5=50k+ |
| Google Trends | 15% | 1=fallend, 2=stagnierend, 3=stabil, 4=steigend, 5=stark steigend |
| Competitor Revenue | 30% | 1=<€30k/mo, 2=€30-100k, 3=€100-300k, 4=€300k-1M, 5=€1M+ |
| Ad Activity | 20% | 1=keine Ads, 2=<5, 3=5-20, 4=20-50, 5=50+ |
| Amazon Demand | 15% | 1=kein Amazon, 2=BSR>10k, 3=BSR 2k-10k, 4=BSR 500-2k, 5=BSR<500 |

**Minimum Validation Score: 2.5** — darunter ist die Nachfrage nicht bewiesen genug.

---

## PHASE 4: COMPETITIVE ADVANTAGE ASSESSMENT

### Ziel
Für jeden validierten Kandidaten klären: WO genau können wir den Wettbewerb schlagen? Produkt allein reicht nicht — "winning products are created."

### 4a. Competitive Advantage Matrix

Pro Kandidat:

| Vorteilstyp | Status | Beschreibung | Impact |
|---|---|---|---|
| **Creative** | ✅/⚠️/❌ | Können wir bessere/mehr Ads als der Wettbewerb? | Hoch/Mittel/Niedrig |
| **Funnel** | ✅/⚠️/❌ | Nutzen Competitors Basic Funnels die wir schlagen können? | |
| **Branding** | ✅/⚠️/❌ | Können wir uns visuell/tonallich differenzieren? | |
| **Segment** | ✅/⚠️/❌ | Bedienen wir eine Zielgruppe die niemand bedient? | |
| **Content** | ✅/⚠️/❌ | Können wir via Content Authority aufbauen? | |
| **Preis** | ✅/⚠️/❌ | Können wir günstiger anbieten ODER besser framen? | |
| **Backend/LTV** | ✅/⚠️/❌ | Haben wir ein stärkeres Upsell/Cross-Sell-System? | |

### 4b. Funnel-Architektur Vorschlag

Basierend auf Awareness Stage der Haupt-Persona und Competitive Advantages:

**Unaware → Problem-Aware:**
```
Content (Blog/Video/Social) → Lead Magnet → Email Nurture → Offer
```

**Problem-Aware → Solution-Aware:**
```
Ad (Pain-Hook) → Advertorial/Listicle → Sales Page → Order Page + Bumps → Upsell
```

**Solution-Aware → Product-Aware:**
```
Ad (Solution-Hook) → Quiz Funnel → Personalisierte Empfehlung → PDP → Checkout + Bumps
```

**Product-Aware → Most-Aware:**
```
Retargeting Ad → Testimonial-LP → Offer mit Urgency → Direct Checkout
```

Pro Kandidat eine Empfehlung welcher Funnel-Typ passt.

---

## PHASE 5: FINAL RANKING & OUTPUT

### 5a. Combined Score

| Kandidat | Criteria Score (50%) | Validation Score (30%) | Competitive Advantage (20%) | **FINAL** |
|---|---|---|---|---|
| Produkt A | 4.00 | 3.80 | 4.20 | **3.96** |
| Produkt B | 3.55 | 4.10 | 3.50 | **3.68** |

### 5b. Output-Dokumente

#### `01-product-candidates.md`
Alle Kandidaten mit Pain-to-Product Mapping, Competitor-Scan, Gap-Mapping, Digital Assessment.

#### `02-validation-report.md`
Rohdaten + Analyse: Search Volume, Google Trends, SimilarWeb Revenue-Schätzungen, Ad Library Findings, Amazon Data.

#### `03-product-ranking.md`
```markdown
# Product Ranking — [Nische] ([Land])

## Executive Summary
- X Kandidaten identifiziert, Y validiert, Z empfohlen
- Top-Empfehlung: [Produkt] mit Score [X.XX]
- Begründung in 2-3 Sätzen

## Ranking

### #1: [Produktname] — Score: X.XX
- **Was:** [Beschreibung]
- **Typ:** Physical / Digital / Hybrid
- **Target Persona:** [Persona aus ZG-Analyse]
- **Pain:** "[Pain in ZG-Sprache]"
- **Pricing:** €[Preis] (COGS: €[X], GP: €[X], Margin: X%)
- **Validation:** [Zusammenfassung der harten Daten]
- **Competitive Advantage:** [Wo wir gewinnen]
- **Empfohlener Funnel:** [Typ + kurze Beschreibung]
- **Risiken:** [Was könnte schiefgehen?]
- **Nächste Schritte:** [Was muss als nächstes passieren?]

### #2: [Produktname] — Score: X.XX
[...]

## Abgelehnte Kandidaten
| Kandidat | Grund für Ablehnung |
|---|---|
| [Name] | [Warum rausgeflogen] |

## Strategische Empfehlung
[2-5 Sätze: Welche Kombination von Produkten ergibt das stärkste Geschäftsmodell?
Z.B. "Lead Magnet (Gratis-Checkliste) → Einstiegsprodukt (€45 Kit) → Premium-Bundle (€199) → Subscription (€29/Monat)"]
```

---

## PHASE 6: PRÄSENTATION

Zeige the Owner eine Zusammenfassung:

```
✅ Produktrecherche für [Nische] ([Land]) abgeschlossen.

📁 Ordner: [projekt]/produkte/

📊 Ergebnisse:
- X Produktkandidaten identifiziert
- Y davon validiert (Score ≥ 2.5)
- Z finale Empfehlungen

🏆 Top-Empfehlung: [Produktname]
   Score: X.XX | Typ: [Physical/Digital/Hybrid]
   Validation: [Key-Daten]
   Advantage: [Wo wir gewinnen]

💡 Strategische Empfehlung: [Kurzfassung Produkt-Ökosystem]

📝 Nächster Schritt: Funnel-Skill mit dem gewählten Produkt starten.
```

---

## WICHTIGE REGELN

1. **IMMER mit Zielgruppenanalyse starten.** Ohne `/target-audience` Output ist dieser Skill wertlos. Pain-to-Product, nicht Product-to-Pain.
2. **Validation mit echten Daten.** "Assume nothing." Kein Produkt empfehlen das nicht mit SimilarWeb, Trends, Search Volume oder Ad Activity validiert ist.
3. **Digitale Produkte gleichwertig behandeln.** Nicht alles muss physisch sein. Ein €29 Guide mit 95% Marge kann besser sein als ein €45 Kit mit 3x COGS.
4. **Revenue reverse-engineeren.** Visits × CR (2%) × AOV = geschätzter Umsatz. Nicht raten.
5. **Competitive Advantage > Produkt.** Ein mittelmäßiges Produkt mit starkem Funnel schlägt ein Top-Produkt mit Basic-Funnel. Immer fragen: "Wo können WIR gewinnen?"
6. **Scoring-System strikt anwenden.** Keine Bauchgefühl-Empfehlungen. Zahlen entscheiden.
7. **Purple Ocean prüfen.** Passt das Produkt zum hyper-spezifischen Segment das wir in der ZG-Analyse identifiziert haben?
8. **Funnel-Architektur mitdenken.** Jede Empfehlung enthält einen Funnel-Vorschlag — das ist die Übergabe an den nächsten Skill.
9. **Agent-Tool nutzen** für parallele Validierung (z.B. 3 Agents für SimilarWeb, Amazon, Ad Library gleichzeitig).
10. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).

## LEARNINGS & HEURISTIKEN

1. **"The guy that can spend the most to acquire a customer wins."** (Kennedy) → LTV/Upsell-Potenzial ist wichtiger als niedriger Einstiegspreis.
2. **Ugly Ads = Pretty Profits.** Aesthetic ist überbewertet. Clarity > Cleverness. Das gilt auch für Produktpräsentation.
3. **Content-to-Commerce schlägt Shop-First** in Märkten mit >80% informationellen Keywords. Prüfe das Keyword-Verhältnis.
4. **Amazon BSR ist der schnellste Demand-Proxy.** Wenn ein Produkt auf Amazon gut läuft, gibt es Nachfrage. Punkt.
5. **Ad-Laufzeit > Ad-Engagement.** Eine Ad die seit 60 Tagen läuft ist ein stärkerer Beweis als eine mit 50k Likes die nach 3 Tagen abgeschaltet wurde.
6. **Für DACH-Märkte: €100k/Monat Competitor-Revenue reicht.** Die $300k-Regel ist US-Markt. DACH ist kleiner — €100k/Monat ist bereits ein validierter Markt.
7. **One Relaunch Rule:** Wenn ein Produkt beim Testen nicht performt → einmal anpassen (Creative oder Funnel). Wenn es dann immer noch nicht läuft → nächstes Produkt. Opportunity Cost > Sunk Cost.
8. **Subscription > Einmalkauf.** Immer prüfen ob das Produkt in ein Abo-Modell überführt werden kann (Consumable, Membership, Box).
