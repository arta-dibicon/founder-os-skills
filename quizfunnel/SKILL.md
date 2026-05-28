---
name: quizfunnel
description: "Erstelle einen kompletten Quiz-Funnel (HTML/CSS/JS) für ein Produkt. TRIGGER wenn the Owner sagt 'Quizfunnel für [X]', 'Quiz bauen', 'Quiz-Funnel erstellen', oder '/quizfunnel [Produkt]'. Auch bei 'interaktiver Funnel', 'Quiz-Landing-Page'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_resize
---

# Quiz Funnel Builder — "Finde deine Lösung"

Erstelle einen kompletten, deploybare Quiz-Funnel als einzelne HTML-Datei. Der Quiz-Funnel ist eine interaktive Pre-Sale-Seite die den User durch diagnostische Fragen führt, Beliefs seeded, Objections pre-handled und am Ende eine personalisierte Empfehlung + Offer zeigt.

## Abgrenzung: Quizfunnel vs. Listicle vs. Advertorial

| Merkmal | Quizfunnel (dieser Skill) | Listicle | Advertorial |
|---|---|---|---|
| **Format** | Interaktiv (Klick-für-Klick) | Statisch (Scroll) | Statisch (Scroll) |
| **Engagement** | Aktiv (User antwortet) | Passiv (User liest) | Passiv (User liest) |
| **Perspektive** | "Du" — direkte Ansprache | "Wir haben getestet" | "Ich habe erlebt" |
| **Awareness Stage** | Solution-Aware | Solution-Aware | Product-Aware |
| **Stärke** | Micro Commitments + Datensammlung | Breite ZG, Social Proof | Emotionale Identifikation |
| **Traffic** | Kalt bis Warm | Kalt | Warm |
| **CTA auf Ads** | "Mach den Test" (niedrige Invasivität) | "Mehr erfahren" | "Geschichte lesen" |

## Core Principles

### Die 3 psychologischen Mechanismen (Mark Builds Brands)
1. **Micro Commitments** — Jeder Klick = ein Schritt näher zum Kauf. Ja-Ja-Ja-Straße erzeugt "hypnotic state". Der User investiert Zeit und wird dadurch committed.
2. **Seeding** — Beliefs werden ins Unterbewusstsein gepflanzt BEVOR das Angebot kommt. Durch Info-Cards und geschickte Frage-Formulierungen.
3. **Pre-handling Objections** — Einwände werden im Quiz erledigt, BEVOR die Sales Page kommt. Wenn der User auf der Ergebnis-Seite landet, sind die größten Einwände schon vom Tisch.

### Verbindung zu unserer Methodik
- **Necessary Beliefs** (aus Offer Brief) → werden durch Seeding-Fragen und Info-Cards gekippt
- **Key Objections** (aus Offer Brief) → werden durch Pre-Handling-Fragen entschärft
- **Emotional Delta** (aus Personas) → Quiz startet bei Pain, endet bei Empowerment
- **VOC-Sprache** (aus VOC) → Alle Fragen und Texte in der Sprache der Zielgruppe

## Input erwarten

### Pflicht-Inputs
- **PRODUKT**: Was wird verkauft?
- **PROJEKT**: Projektordner
- **ZIELGRUPPE**: Pfad zur Zielgruppenanalyse
- **PERSONA**: Welche Persona(s) aus der ZG-Analyse?

### Optionale Inputs
- **ANGEBOT**: Welches Angebot?
- **CHECKOUT_URL**: Wohin führt der CTA?
- **QUIZ_TYP**: "Diagnose" (Score → Handlungsdruck) oder "Finder" (→ verschiedene Produkte). Default: Diagnose.
- **ANZAHL_FRAGEN**: Default: 12-15 (inkl. Info-Cards)
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

Zusätzlich aus dem Offer Brief extrahieren:
- **6 Necessary Beliefs** → werden zu Seeding-Elementen
- **Key Objections** → werden zu Pre-Handling-Fragen
- **Emotional Delta Map** → bestimmt die emotionale Reise durch den Quiz

---

## QUIZ-STRUKTUR (7 Phasen, 15-18 Slides)

### Phase 1: DIAGNOSTIK (3-5 Fragen)
**Zweck:** Current Situation verstehen. Einfacher Einstieg, nicht invasiv.

| Slide | Typ | Beispiel | Mechanismus |
|---|---|---|---|
| 1 | Visual Identifier | "Wie alt bist du?" / "Wer bist du?" (mit Icons) | Gradualisierung — einfachste Frage zuerst |
| 2 | Pain Location | "Was beschäftigt dich am meisten?" (Multi-Select) | Pain identifizieren |
| 3 | Pain Specification | "Erlebst du [konkretes Symptom]?" (Ja/Nein) | Pain vertiefen |
| 4 | Pain Severity | "Wie stark belastet dich das?" (Slider 1-10) | Urgency triggern |
| 5 | Pain Timeline | "Seit wann beschäftigt dich das?" (Multiple Choice) | Urgency verstärken |

**Regeln:**
- Frage 1 muss EXTREM einfach sein (1 Klick, keine Texteingabe)
- Nie mehr als 2-3 gleiche Frage-Formate hintereinander
- Jede Frage muss sofort verständlich sein (5th grade reading level)

### Phase 2: DESIRED SITUATION + SOCIAL PROOF (2 Slides)
**Zweck:** Von Pain zu Desire wechseln. Social Proof zeigen.

| Slide | Typ | Beispiel |
|---|---|---|
| 6 | Desire-Frage | "Was ist dein Ziel?" (Multi-Select mit emotionalen Optionen) |
| 7 | Info-Card (Social Proof) | "Über [Zahl] [Zielgruppe] haben [Ergebnis] erreicht." + Testimonial/Statistik |

### Phase 3: INDIVIDUALISIERUNG (1-2 Fragen)
**Zweck:** "Das ist speziell für MICH" Feeling erzeugen.

| Slide | Typ | Beispiel |
|---|---|---|
| 8 | Persönliche Frage | "Wie ist deine aktuelle Wohnsituation?" / "Wie groß ist deine Familie?" |
| 9 | Persönliche Frage | Nischen-spezifische Detail-Frage |

### Phase 4: BELIEF SEEDING + OBJECTION HANDLING (2-4 Slides)
**Zweck:** Necessary Beliefs kippen und Einwände pre-handlen.

| Slide | Typ | Beispiel | Mapped auf |
|---|---|---|---|
| 10 | Seeding-Frage | "Wusstest du, dass [Fakt]?" (Ja/Nein) | Necessary Belief #1 |
| 11 | Info-Card | "[Fakt/Statistik] — deshalb empfehlen [Authority]..." | Necessary Belief #2 |
| 12 | Pre-Handling-Frage | "Wie viel Zeit könntest du pro Woche investieren?" | Objection: "Keine Zeit" |
| 13 | Info-Card | "Auch mit [wenig Zeit/Platz/Budget] erreichst du [Ergebnis]" | Objection: "Zu aufwändig" |

**Regeln:**
- Info-Cards sind KEINE Fragen, sondern Trust-Builder zwischen Fragen
- Jede Info-Card seeded genau EINE Belief oder handled EINE Objection
- Design: Visuell anders als Fragen (andere Hintergrundfarbe, Icon, ggf. Bild)

### Phase 5: DIAGNOSE + ERGEBNIS (2-3 Slides)
**Zweck:** "Dein persönliches Ergebnis" — Loading-Animation → Summary → Timeline

| Slide | Typ | Beispiel |
|---|---|---|
| 14 | Loading-Screen | "Wir analysieren deine Antworten..." (Fake-Loading, 3-4 Sekunden) |
| 15 | Diagnose-Summary | "Dein Profil: [Zusammenfassung basierend auf Antworten]" — Pain Level, Situation, Empfehlung |
| 16 | Transformation-Timeline | "Basierend auf deinen Antworten: So sieht dein Weg aus" (Monats-Timeline) |

**Loading-Screen Details:**
- 3-4 Sekunden Fake-Loading (Progress-Balken der sich füllt)
- Text wechselt: "Antworten analysieren..." → "Profil erstellen..." → "Empfehlung berechnen..."
- Erzeugt perceived value — suggeriert echte Berechnung

### Phase 6: EMAIL-CAPTURE (1 Slide, optional)
**Zweck:** Lead einsammeln bevor das Ergebnis/Offer gezeigt wird.

| Slide | Typ | Beispiel |
|---|---|---|
| 17 | Email-Eingabe | "Dein persönlicher Plan ist fertig! Wohin sollen wir ihn schicken?" |

**Regeln:**
- NUR Name + Email (NICHT Telefon, Adresse etc.)
- "Skip" Option anbieten (wer keine Email geben will, sieht trotzdem das Ergebnis)
- Email wird via JS erfasst (später an Webhook/API senden)

### Phase 7: YES-STREET → OFFER (2-3 Slides)
**Zweck:** Letzte Micro Commitments → Angebot zeigen.

| Slide | Typ | Beispiel |
|---|---|---|
| 18 | Yes-Frage | "Bist du bereit, [Problem] endlich zu lösen?" (Ja, absolut!) |
| 19 | Yes-Frage | "Würdest du [Zeitraum] investieren für [Ergebnis]?" (Ja!) |
| 20 | OFFER-PAGE | Dark-Mode CTA Block mit Mockup, Countdown, Triple-Scarcity |

**Die Offer-Page am Ende ist IDENTISCH mit dem Final CTA aus Listicle/Advertorial:**
- Dark-Mode Design (linear-gradient #1a1a1a → #2d2d2d)
- Produkt-Mockup (Nano Banana bei digitalen Produkten)
- Countdown-Timer + Fortschrittsbalken + Spots-Left
- CTA-Button mit Shine-Animation
- Garantie-Hinweis

---

## FRAGE-DESIGN

### Frage-Formate (abwechseln!)

| Format | Wann einsetzen | Max hintereinander |
|---|---|---|
| **Multiple Choice** (1 Auswahl) | Einfache Entscheidungen | 2 |
| **Multi-Select** (mehrere Auswahlen) | Pain-Points, Goals | 2 |
| **Ja/Nein** | Commitment-Fragen, Seeding | 2 |
| **Slider** (1-10) | Severity, Intensität | 1 |
| **Visual Selector** (Bilder/Icons) | Alter, Typ, Kategorie | 1 |
| **Info-Card** (keine Frage) | Trust, Social Proof, Fakten | 1 (immer zwischen Fragen) |

### Dopamine-Design-Regeln
- **Click-Feedback:** Ausgewählte Option ändert sofort Farbe (grün/accent)
- **Progress Bar** oben: Zeigt wie weit der User ist (füllt sich mit jeder Frage)
- **Smooth Transitions:** Fragen sliden rein/raus (translateX oder opacity)
- **Auto-Advance:** Bei Single-Choice nach Klick automatisch zur nächsten Frage (0.5s delay)
- **Zurück-Button:** Immer sichtbar (außer bei Frage 1)

### Frage-Formulierung
- **Immer in Du-Form** ("Wie alt bist du?" nicht "Wie alt sind Sie?")
- **Kurz** — max 10-12 Worte pro Frage
- **Emotional** — "Was belastet dich am meisten?" statt "Welche Probleme hast du?"
- **VOC-Sprache** — exakte Wörter der Zielgruppe verwenden
- **Keine Texteingabe** — nur Klick/Tap (Ausnahme: Email-Capture)

---

## QUIZ-MAPPING (aus Research)

Vor dem Bauen eine Mapping-Tabelle erstellen:

| Phase | Slide | Frage/Content | Format | Seeded Belief / Handled Objection | Antwort-Optionen |
|---|---|---|---|---|---|
| Diagnostik | 1 | "[Einfache Einstiegsfrage]" | Visual Selector | — | [3-4 Optionen] |
| Diagnostik | 2 | "[Pain-Frage]" | Multi-Select | — | [4-6 Optionen] |
| ... | ... | ... | ... | ... | ... |

---

## TECHNISCHE UMSETZUNG

### Single HTML File
Wie Listicle/Advertorial: EINE HTML-Datei, alles inline. Kein Framework.

### CSS Design System
```css
:root {
    --bg: #ffffff;
    --text: #1a1a1a;
    --text-light: #555555;
    --text-muted: #888888;
    --accent: #4f46e5;           /* Indigo statt Rot — weniger "Kauf mich", mehr "Entdecke" */
    --accent-hover: #4338ca;
    --accent-light: #eef2ff;
    --success: #22c55e;
    --success-light: #f0fdf4;
    --border: #e5e5e5;
    --card-bg: #f8fafc;
    --font-heading: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --quiz-width: 640px;         /* Schmaler als Listicle — fokussierter */
    --radius: 12px;
    --transition: 0.3s ease;
}
```

**Wichtig:** Quiz-Accent ist **Indigo (#4f46e5)** statt Rot — der Quiz soll sich wie ein Tool anfühlen, nicht wie ein Shop. Der **CTA am Ende** wechselt dann zu Rot (wie Listicle/Advertorial).

### Quiz-Container Layout
```css
.quiz-container {
    max-width: var(--quiz-width);
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.quiz-step {
    display: none;              /* Alle Steps hidden */
    opacity: 0;
    transform: translateX(20px);
    transition: opacity 0.3s, transform 0.3s;
}
.quiz-step.active {
    display: flex;
    flex-direction: column;
    opacity: 1;
    transform: translateX(0);
}
```

### JavaScript-Architektur
```javascript
const Quiz = {
    currentStep: 0,
    totalSteps: 0,              // Wird dynamisch gesetzt
    answers: {},                 // { step_id: answer_value }

    init() { /* Steps zählen, Event Listeners, Progress Bar */ },
    next() { /* Nächster Step, Animation, Progress Update */ },
    prev() { /* Vorheriger Step */ },
    selectOption(stepId, value) { /* Antwort speichern, visuelles Feedback */ },
    showLoading() { /* Fake-Loading mit Text-Wechsel */ },
    renderDiagnosis() { /* Personalisiertes Ergebnis basierend auf answers */ },
    submitEmail(email) { /* Email an Webhook/API */ },
    trackDropoff(step) { /* Analytics: welcher Step hat Drop-off */ }
};
```

### Answer-Tracking & Personalisierung
```javascript
// Antworten werden gesammelt und am Ende ausgewertet
// Einfaches Scoring-System:
answers: {
    pain_level: 8,          // Slider-Wert
    pain_areas: ["area1", "area2"],
    timeline: "over_1_year",
    goals: ["goal1", "goal3"],
    // ...
}

// Diagnose-Text wird basierend auf Antworten generiert:
function getDiagnosis(answers) {
    let urgency = "mittel";
    if (answers.pain_level >= 7) urgency = "hoch";
    if (answers.timeline === "over_1_year") urgency = "sehr hoch";
    // ...
    return { urgency, recommendation, timeline };
}
```

### Responsive
- Desktop: 640px zentriert, Card-basiertes Layout
- Mobile: Full-Width, große Touch-Targets (min 48px), Bottom-Buttons

---

## BILD-STRATEGIE

Minimaler als Listicle/Advertorial:
1. **Produkt-Mockup** (PFLICHT bei digitalen Produkten) — Nano Banana → für die Offer-Page am Ende
2. **Icons/Illustrationen** — Inline SVG oder Unicode für Frage-Optionen (keine Stock-Fotos im Quiz selbst)
3. **Social Proof Foto** — 1-2 Testimonial-Fotos für Info-Cards (Recraft AI oder aus Listicle wiederverwenden)
4. **Hintergrund-Grafiken** — CSS Gradients, keine Bilder

**Warum wenige Bilder:** Der Quiz muss SCHNELL laden und sich wie ein interaktives Tool anfühlen, nicht wie eine Bildergalerie.

---

## ARBEITSVERZEICHNIS

```
[projekt]/quizfunnel/
├── [produkt-slug].html          ← Die fertige Quiz-Seite
├── images/
│   ├── product-mockup.png       ← Für Offer-Page am Ende
│   └── testimonial-*.jpg        ← Für Info-Cards (optional)
└── _deploy/
    └── netlify.toml
```

---

## ABLAUF (Step by Step)

### Step 1: Research laden & Quiz-Map erstellen
1. Foundational Docs lesen (Personas, Offer Brief, VOC, Before/After)
2. Extrahieren:
   - 6 Necessary Beliefs → Seeding-Elemente
   - Top Objections → Pre-Handling-Fragen
   - Pain-Points → Diagnostik-Fragen
   - Desires → Goal-Fragen
   - VOC-Sprache → Frage-Formulierungen
3. Quiz-Mapping-Tabelle erstellen (Phase, Slide, Frage, Format, Belief/Objection, Optionen)

### Step 2: Quiz-Flow designen
1. 15-18 Slides planen (7 Phasen)
2. Frage-Formate zuweisen (abwechselnd!)
3. Info-Cards platzieren (nach Phase 2 + in Phase 4)
4. Diagnose-Logik definieren (welche Antworten → welches Ergebnis)
5. Offer-Page definieren (Preis, Angebot, CTA)

### Step 3: Bilder beschaffen
1. Produkt-Mockup: Nano Banana API (bei digitalen Produkten)
2. Testimonial-Fotos: Aus Listicle/Advertorial wiederverwenden oder Recraft AI
3. Icons: Inline SVG oder Unicode

### Step 4: HTML/CSS/JS bauen
1. Quiz-Container mit allen Steps
2. CSS Design System (Indigo-Accent, Card-Layout)
3. JavaScript Quiz-Engine (Navigation, Answers, Progress, Diagnose)
4. Offer-Page am Ende (Dark-Mode CTA, identisch zu Listicle)
5. Responsive Design
6. HTML via Bash in Datei schreiben

### Step 5: QA & Deploy
1. Lokal öffnen, komplett durchklicken
2. Jeden Step testen (Vorwärts + Zurück)
3. Mobile-Test
4. Diagnose-Logik verifizieren (verschiedene Antwort-Kombis testen)
5. Offer-Page prüfen (Mockup, Countdown, CTA)

---

## QUALITÄTS-CHECK (vor Abgabe)

### Quiz-Flow
- [ ] Frage 1 ist extrem einfach (1 Klick)?
- [ ] Max 2-3 gleiche Formate hintereinander?
- [ ] Jede Frage hat einen Zweck (Micro Commitment, Seeding, oder Pre-Handling)?
- [ ] Info-Cards zwischen Fragen (nicht nur Fragen am Stück)?
- [ ] Fragen in VOC-Sprache formuliert?
- [ ] Progress Bar zeigt Fortschritt korrekt?
- [ ] Zurück-Button funktioniert (außer Frage 1)?

### Interaktion
- [ ] Click-Feedback sofort sichtbar (Farbe ändert sich)?
- [ ] Auto-Advance bei Single-Choice (0.5s delay)?
- [ ] Smooth Transitions zwischen Steps?
- [ ] Loading-Screen vor Diagnose (3-4 Sekunden)?
- [ ] Text wechselt während Loading?

### Diagnose & Offer
- [ ] Diagnose-Summary greift Quiz-Antworten auf?
- [ ] Transformation-Timeline vorhanden?
- [ ] Dark-Mode CTA am Ende (identisch zu Listicle/Advertorial)?
- [ ] Produkt-Mockup im CTA?
- [ ] Countdown + Fortschrittsbalken + Spots-Left?
- [ ] Garantie-Hinweis?

### Bilder & Technik
- [ ] Alle Bilder laden korrekt?
- [ ] Mobile-responsive (große Touch-Targets)?
- [ ] Keine Texteingabe-Felder (außer Email)?
- [ ] Quiz lädt schnell (keine schweren Bilder)?

---

## WICHTIGE REGELN

1. **Jede Frage muss einen Zweck haben.** Micro Commitment, Seeding, oder Pre-Handling. Sonst raus.
2. **Formate abwechseln.** Multiple Choice → Slider → Ja/Nein → Info-Card → Multi-Select. Nie 3x dasselbe.
3. **Gradualisierung.** Einfach anfangen, invasiver werden. Nie mit der schwersten Frage starten.
4. **Info-Cards sind keine Fragen.** Sie sind Trust-Builder, Social Proof, Fakten. Visuell anders als Fragen.
5. **Loading-Screen ist Pflicht.** 3-4 Sekunden Fake-Loading vor dem Ergebnis. Erhöht perceived value dramatisch.
6. **Quiz-Accent ist Indigo, CTA-Accent ist Rot.** Quiz = Tool. Offer = Verkauf. Verschiedene Farben.
7. **30% Completion Rate ist das Ziel.** Wenn deutlich darunter → Fragen kürzen oder umformulieren.
8. **Email-Capture ist optional aber empfohlen.** Immer "Skip" anbieten.
9. **Die Offer-Page am Ende ist identisch zum Listicle/Advertorial Dark-Mode CTA.** Wiederverwendbar.
10. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).
11. **Netlify Deploy** nach QA.

## LEARNINGS (aus Video-Analyse)

1. **Quiz Funnels funktionieren NICHT wegen Personalisierung** — sondern wegen Micro Commitments + emotionally primed state. (Mark Builds Brands)
2. **Erste 3 Fragen = Hook.** A/B testen. Entscheidet über Completion Rate. (Video 2)
3. **Sweet Spot: 8-20 Fragen.** Unter 8 = zu wenig Priming. Über 20 = zu viel Drop-off. (Mark: 8-12, Tri Spartan: 18)
4. **"Mach den Test" als Ad-CTA** hat deutlich niedrigere Invasivität als "Jetzt kaufen". Senkt CPM. (Mark)
5. **Quiz = bezahlte Marktforschung.** Du bekommst Kunden UND lernst von ihnen gleichzeitig. (Video 2)
6. **Loading-Screen vor Ergebnis** ist kritisch. Suggeriert echte Berechnung, erhöht perceived value. (Tri Spartan)
7. **Yes-Street am Ende** (3x "Bist du bereit?" → Ja) erzeugt finalen Commitment-Push. (Tri Spartan)
8. **Email vor Ergebnis** erfassen — User ist maximal committed, höchste Conversion. (Mark)
9. **Drop-off-Spike bei einzelner Frage = zu invasiv.** Entfernen oder weniger invasiv umformulieren. (Mark)
10. **Quiz-Daten für Ad-Kreatives nutzen.** Welche Pain-Points werden am häufigsten gewählt? → Nächste Ad-Angle. (Video 2)
