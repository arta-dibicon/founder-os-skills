# Ad Copy Engine — Meta-Ready Copy für jedes Creative

## PRE-FLIGHT — Research-Kontext laden

Vor dem Start IMMER prüfen ob Audience-Research existiert (Source-of-Truth: lokal):

1. Lies `[aktives-projekt]/_research/INDEX.md`. Gibt es einen `done`-Run zum aktuellen Topic?
2. Wenn JA: Lade `_research/[topic-slug]/copy_context.md` + `personas.json` als Default-Kontext. Pflicht-Lektüre für Hook/Headline-Generation: `voice_of_customer.md` (verbatim Quotes als Hooks) und `persona_deep_dive.md` (fertige Ad-Headline-Vorlagen pro Persona).
3. Wenn NEIN: Frag the Owner "Soll ich via `Rechit` Sub-Agent ein Research starten oder ohne arbeiten?" Niemals blind ohne Research drauflos schreiben.

Schema/Protokoll: Memory `feedback_research_loading_protocol.md`. Agent: `.claude/agents/rechit.md`.

---

Erstelle komplette Ad-Copy-Pakete für Facebook/Instagram Ads. Pro Creative: 5× Primary Text, 5× Headline, 5× Description + CTA. Output als strukturierte JSON-Datei, ready für den /meta-ads Skill.

---

## WARUM DIESER SKILL EXISTIERT

Der /ad-creative Skill liefert **Bilder**. Dieser Skill liefert die **Worte**.
Meta Flexible Ads erlauben bis zu 5 Varianten pro Textfeld — Meta testet automatisch welche Kombination am besten performt. Je mehr hochwertige Varianten, desto schneller findet der Algorithmus den Winner.

**Copy ≠ Content. Copy = Sales.**

---

## CORE PRINCIPLES

### 1. Research = 80% der Arbeit
Jedes Wort kommt aus den Foundational Docs. VOC-Zitate > eigene Formulierungen. Exact Words der Zielgruppe schlagen Marketing-Sprache. Immer.

### 2. Klarheit > Cleverness
5th-8th Grade Reading Level. Kein Jargon. Kein Marketing-Sprech. Wenn deine Oma es nicht versteht, schreib es um.

### 3. Emotional Delta
Jeder Primary Text hat eine emotionale Reise: Meet them where they are → Raise them → Bring them back with a reason to act. Das ist kein "nice to have" — das ist der Mechanismus der Conversion erzeugt.

### 4. Hook = Alles
Die ersten 125 Zeichen entscheiden ob jemand "Mehr anzeigen" klickt. Wenn der Hook nicht punched, ist der Rest egal. PIG-Test (Punch In the Gut): Würde jemand beim Scrollen stoppen?

### 5. Kongruenz mit dem Creative
Die Copy muss zum Bild passen. Ein WhatsApp-Chat-Screenshot braucht andere Copy als ein Breaking-News-Format. Die Copy erweitert die Geschichte die das Bild anfängt — sie wiederholt sie nicht.

---

## META AD COPY SPECS

### Textfelder & Limits

| Feld | Empfohlen | Max | Varianten | Wo sichtbar |
|---|---|---|---|---|
| **Primary Text** | 125 Zeichen (above fold) | 4.096 | bis 5 | Über dem Bild (Feed), unter dem Bild (Stories) |
| **Headline** | 27-40 Zeichen | ~255 | bis 5 | Fett unter dem Bild |
| **Description** | 25 Zeichen | ~255 | bis 5 | Grau neben CTA (nur Feed, nicht immer sichtbar) |
| **CTA Button** | — | — | 1 | Button rechts unten |
| **URL** | — | — | 1 | Ziel-Link |

### KRITISCH: Above the Fold
Auf Mobile sieht der User nur **~125 Zeichen** bevor "Mehr anzeigen" kommt. Diese 125 Zeichen sind dein Hook. ALLES muss darauf optimiert sein.

### CTA-Optionen (relevanteste)
- `LEARN_MORE` — Standard für Indirect Ads (Listicle/Advertorial/Quiz)
- `SHOP_NOW` — Direct Ads (Checkout)
- `SIGN_UP` — Lead Gen
- `GET_OFFER` — Angebote
- `DOWNLOAD` — Digitale Produkte
- `GET_STARTED` — Quiz Funnel

---

## INPUT ERWARTEN

### Pflicht-Inputs
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **CREATIVES_PATH**: Pfad zum Creatives-Output (z.B. "ads/v4-listicle/")
- **FUNNEL**: Wohin die Ads leiten (Listicle/Advertorial/Quiz/Checkout)
- **FUNNEL_URL**: Die Ziel-URL der Landing Page
- **PRODUKT**: Was wird verkauft?

### Optionale Inputs
- **PERSONA**: Welche Persona (Default: aus Creatives ableiten)
- **PREIS**: Produktpreis (für Direct Ads)
- **SPRACHE**: Default: Deutsch
- **CTA_TYPE**: Default: LEARN_MORE (Indirect) / SHOP_NOW (Direct)
- **TONALITÄT**: Default: aus Persona ableiten

Falls Inputs fehlen → the Owner fragen. Nicht raten bei Funnel-URL oder Produkt.

---

## VORBEREITUNG: RESEARCH LADEN

**BEVOR du eine Zeile Copy schreibst — Foundational Docs lesen:**

```bash
# PFLICHT — ALLE lesen
cat "[projekt]/zielgruppe/03-personas.md"         # Persona-Details, Sprache, Awareness
cat "[projekt]/zielgruppe/07-voice-of-customer.md" # EXACT WORDS — das Gold
cat "[projekt]/zielgruppe/06-offer-brief.md"       # Necessary Beliefs, UMP/UMS, Emotional Delta
cat "[projekt]/zielgruppe/02-before-after.md"      # Pain/Desire Paare
cat "[projekt]/zielgruppe/04-persona-deep-dive.md" # Tiefe psychologische Profile
```

**Zusätzlich — Ad Concepts laden:**
```bash
# Die Creative-Daten brauchen wir für Kongruenz
cat "[projekt]/ads/[creatives_path]/ad-concepts.md"  # Falls vorhanden
ls "[projekt]/ads/[creatives_path]/"                   # Alle Creatives sehen
```

**Daraus extrahieren (intern, nicht als Output):**
1. **VOC-Zitate**: Die 20-30 stärksten Originalzitate der Zielgruppe
2. **Pain Points**: Top 5 Schmerzen, in den Worten der Zielgruppe
3. **Desires**: Top 5 Wünsche, in den Worten der Zielgruppe
4. **Objections**: Top 5 Einwände + wie man sie entkräftet
5. **Necessary Beliefs**: Was muss jemand glauben bevor er kauft?
6. **Emotional Delta**: Von welchem Gefühl → zu welchem Gefühl?
7. **Awareness Stage**: Unaware / Problem-Aware / Solution-Aware / Product-Aware

---

## COPY-ERSTELLUNG: DIE 5 VARIANTEN-STRATEGIE

### Warum 5 Varianten?
Nicht 5× das Gleiche umformuliert. 5 **verschiedene Ansätze** — verschiedene Hooks, verschiedene emotionale Einstiege, verschiedene Längen. Meta testet und findet den Winner.

### Primary Text — 5 Varianten-Typen

**Variante 1: Der Story-Hook (Lang, 300-600 Wörter)**
```
[Persönlicher Erfahrungsbericht / Szenario]
[Problem-Agitation in VOC-Sprache]
[Bridge zur Lösung]
[Social Proof]
[Soft CTA]
```
- Klingt wie ein persönlicher Facebook-Post, nicht wie Werbung
- Ich-Perspektive ODER Du-Perspektive
- Spezifische Details machen es glaubwürdig ("letzten Dienstag um 3 Uhr nachts")

**Variante 2: Der Statistik-Punch (Mittel, 150-300 Wörter)**
```
[Schockierende Statistik / Fakt als Hook]
[Was das für DICH bedeutet]
[Konsequenz wenn du nichts tust]
[Lösung andeuten]
[CTA]
```
- Autorität durch Zahlen und Quellen
- "Laut [Quelle]..." oder "73% der Deutschen..."
- Zahlen sind spezifisch, nicht rund

**Variante 3: Der Kontrast-Opener (Mittel, 100-250 Wörter)**
```
[Zwei Szenarien gegenüberstellen]
[Das eine = dein jetziges Leben]
[Das andere = wie es sein könnte]
[Brücke zwischen den beiden]
[CTA]
```
- "Es gibt zwei Arten von [Menschen/Familien/...]"
- Before/After ohne es explizit so zu nennen
- Emotional Delta maximal spürbar

**Variante 4: Der Listicle-Teaser (Kurz-Mittel, 80-200 Wörter)**
```
[Hook-Frage oder provokante Aussage]
[3-5 Bullet Points / Nummerierung]
[Neugier-Lücke — nicht alles verraten]
[CTA: "Alle X Punkte im Artikel"]
```
- Funktioniert besonders gut für Listicle-Funnels
- Bullets = scannable, pattern-break im Feed
- Neugier-Lücke: Nur 3 von 7 Punkten zeigen

**Variante 5: Der Einzeiler (Ultra-Kurz, 20-80 Wörter)**
```
[1-2 Sätze. Maximum punch. Punkt.]
[Optional: 1 Zeile Social Proof]
[CTA]
```
- Für Leute die nie "Mehr anzeigen" klicken
- Jedes Wort muss sitzen
- Wirkt besonders stark bei visuell starken Creatives

### Headline — 5 Varianten-Typen

| # | Typ | Beispiel | Zeichen |
|---|---|---|---|
| 1 | **Benefit-Statement** | "Deine Familie. 14 Tage sicher." | 25-35 |
| 2 | **Neugier-Frage** | "Hast du einen Plan?" | 15-25 |
| 3 | **Statistik-Punch** | "73% haben keinen Notvorrat" | 25-35 |
| 4 | **Social Proof** | "4.700+ Familien sind vorbereitet" | 30-40 |
| 5 | **Anti-Category** | "Kein Prepper-Quatsch." | 15-25 |

**REGELN:**
- UNTER 27 Zeichen = wird NIE abgeschnitten (optimal)
- 27-40 Zeichen = kann auf manchen Placements abgeschnitten werden
- Über 40 Zeichen = VERBOTEN
- Kein Punkt am Ende (außer bei bewusstem Stilmittel)
- Keine Emojis in Headlines

### Description — 5 Varianten-Typen

| # | Typ | Beispiel | Zeichen |
|---|---|---|---|
| 1 | **CTA-Verstärker** | "Jetzt lesen →" | 12-20 |
| 2 | **Urgency-Trigger** | "Solange verfügbar" | 15-20 |
| 3 | **Preis-Anker** | "Ab 29€ — einmalig" | 15-22 |
| 4 | **Trust-Signal** | "Über 4.700 Familien" | 18-25 |
| 5 | **Benefit-Micro** | "In 3 Wochen vorbereitet" | 20-25 |

**REGELN:**
- UNTER 25 Zeichen (wird sonst abgeschnitten)
- Wird nicht auf allen Placements angezeigt — muss auch ohne funktionieren
- Kein essentieller Content hier — nur Verstärkung

---

## KONGRUENZ-MATRIX: COPY ↔ CREATIVE

Die Copy muss zum Creative-Typ passen. Nicht jeder Primary Text passt zu jedem Bild.

### Foto+Overlay Ads
- Copy **erweitert** die Geschichte des Bildes
- Hook greift auf was im Bild passiert: "Siehst du den Vater auf dem Bild? Das war ich vor 3 Wochen."
- NICHT wiederholen was im Overlay steht — weiterführen

### WhatsApp Chat / Screenshot Ads
- Copy ist **Meta-Kommentar** zum Screenshot
- "Diese Nachricht hat mich wach gerüttelt." / "Kam gestern in unserer Familien-Gruppe."
- Kurz — das Bild erzählt die Geschichte, Copy gibt Kontext

### Statistik / Infografik Ads
- Copy **erklärt die Konsequenz** der Zahl
- "73% klingt abstrakt. Bis du realisierst: Das bist wahrscheinlich du."
- Zahl nicht wiederholen — Bedeutung liefern

### Meme / Humor Ads
- Copy ist **trocken, kurz, relatabel**
- "Kommt dir bekannt vor? Mir auch." / "Kein Kommentar nötig."
- NICHT den Witz erklären

### Breaking News Ads
- Copy **reagiert** auf die "Nachricht"
- "Ich hab das gestern gelesen und sofort gehandelt." / "Und? Was machst du jetzt?"
- Urgency ohne Panik

### Checklist Ads
- Copy **stellt die Frage** die zur Checklist führt
- "Wie viele Punkte hast du abgehakt?" / "Wette: Punkt 4 fehlt bei dir."
- Interaktiv, challengend

### Testimonial Ads
- Copy **validiert** das Testimonial
- "Sandra ist nicht allein. Über 4.700 Familien..." / "Das höre ich jede Woche."
- Social Proof stapeln

---

## PRIMARY TEXT SCHREIBEN — HANDWERK-REGELN

### Hook-Formeln (erste 125 Zeichen)

**Fear/Urgency:**
- "Strom weg. Heizung weg. Kein Wasser. Kein Netz. Was machst du in den ersten 4 Stunden?"
- "Letzte Woche stand meine Nachbarin mit ihren Kindern vor meiner Tür. Stromausfall. 11 Stunden."

**Statistik:**
- "73% der deutschen Familien haben keinen Notvorrat. Nicht mal für 3 Tage."
- "Das BBK empfiehlt 14 Tage Eigenvorsorge. Der Durchschnittsdeutsche hat Vorräte für 1,7 Tage."

**Curiosity:**
- "Ich hab letzten Monat 29€ ausgegeben, die mir mehr Sicherheit gegeben haben als meine Hausratversicherung."
- "Es gibt einen Grund warum deine Oma immer Konserven im Keller hatte. Und es war nicht Geiz."

**Contrast:**
- "Es gibt zwei Arten von Familien: Die, die bei einem Blackout zur Tanke rennen. Und die, die Kerzen anzünden und Abendbrot machen."
- "Dein Netflix-Abo kostet 13€/Monat. Dein Notfallplan: 0€. Null. Nada."

**Social Proof:**
- "Über 4.700 Familien in Deutschland haben sich in den letzten 8 Wochen vorbereitet. Ohne Bunker. Ohne Panik."
- "Sandra K. aus Hamburg: 'Ich dachte mein Mann spinnt. Dann hatten wir 12 Stunden Stromausfall.'"

**Anti-Category:**
- "Ich bin kein Prepper. Ich hab keine Gasmaske. Keinen Bunker. Null Tarnkleidung."
- "Vergiss alles was du über 'Prepper' denkst. Das hier ist Erwachsensein 2026."

**Identity/Shame:**
- "Du hast eine Haftpflicht, eine Zahnzusatz und eine BU. Aber keinen Plan für 72 Stunden ohne Strom?"
- "Du bist 30+ und hast keinen Notvorrat? Nicht mal eine Taschenlampe die funktioniert?"

### Storytelling-Struktur (für lange Varianten)

```
HOOK (1-2 Sätze) — Punch in the gut, spezifisch, emotional
↓
PROBLEM (3-5 Sätze) — Agitate den Pain, VOC-Sprache, "Stell dir vor..."
↓
BRIDGE (2-3 Sätze) — Wie die Lösung entdeckt wurde, glaubwürdig
↓
SOLUTION SEED (2-3 Sätze) — Andeutung, NICHT das Produkt direkt
↓
SOCIAL PROOF (1-2 Sätze) — Zahlen, Testimonials, Autorität
↓
CTA (1 Satz) — Soft, neugierig machend, kein Hard-Sell
```

### VERBOTEN in Primary Text
- ❌ "Klicke hier" / "Kaufe jetzt" (zu direkt, wirkt wie Spam)
- ❌ Marketing-Jargon: "innovativ", "einzigartig", "revolutionär", "Game-Changer"
- ❌ CAPS LOCK für ganze Wörter (Meta filtert das)
- ❌ Übertriebene Emojis (max 3-5 pro Text, thematisch passend)
- ❌ Preis im Primary Text bei Indirect Ads (der Funnel macht den Verkauf)
- ❌ Produkt-Name im Primary Text bei Indirect Ads
- ❌ Clickbait ohne Substanz ("Du wirst nicht glauben...")
- ❌ Falsche Behauptungen / übertriebene Versprechen
- ❌ Fear-Mongering ohne Lösung (Meta Ads Policy!)

### ERLAUBT / ERWÜNSCHT
- ✅ VOC-Zitate direkt einbauen (in Anführungszeichen)
- ✅ Spezifische Zahlen und Fakten
- ✅ Emotionale Szenarien die relatabel sind
- ✅ Fragen an den Leser
- ✅ "Ich"-Perspektive für Story-Hooks
- ✅ Zeilenumbrüche für Lesbarkeit (nicht alles ein Block)
- ✅ 1-3 Emojis als visuelle Ankerpunkte
- ✅ Soft CTA: "Link im Kommentar" / "Mehr dazu im Link"

---

## OUTPUT-STRUKTUR

### Dateistruktur
```
[projekt]/ads/[creatives_path]/
├── ad-copy.json          ← Strukturierte Copy für /meta-ads (Pflicht-Output)
├── ad-copy-preview.html  ← Visuelle Preview aller Copy-Varianten (Pflicht-Output)
└── [bestehende Creatives bleiben unverändert]
```

### ad-copy.json Format

```json
{
  "meta": {
    "projekt": "[Projektname]",
    "produkt": "[Produktname]",
    "persona": "[Persona-Name]",
    "funnel": "[Listicle/Advertorial/Quiz/Checkout]",
    "funnel_url": "[URL]",
    "erstellt": "[Datum]",
    "sprache": "de",
    "total_ads": 23
  },
  "defaults": {
    "cta": "LEARN_MORE",
    "url": "[Funnel-URL]",
    "page_id": "[wird von /meta-ads eingesetzt]",
    "instagram_account_id": "[wird von /meta-ads eingesetzt]"
  },
  "ads": [
    {
      "id": "ad-01",
      "name": "[Creative-Name]",
      "image": "[Dateiname.png]",
      "format": "[Format-Typ]",
      "angle": "[Angle]",
      "awareness": "[Awareness-Stage]",
      "primary_texts": [
        {
          "variant": 1,
          "type": "story-hook",
          "text": "[Kompletter Primary Text]",
          "hook_length": 89
        },
        {
          "variant": 2,
          "type": "statistik-punch",
          "text": "[...]",
          "hook_length": 112
        },
        {
          "variant": 3,
          "type": "kontrast-opener",
          "text": "[...]",
          "hook_length": 95
        },
        {
          "variant": 4,
          "type": "listicle-teaser",
          "text": "[...]",
          "hook_length": 78
        },
        {
          "variant": 5,
          "type": "einzeiler",
          "text": "[...]",
          "hook_length": 65
        }
      ],
      "headlines": [
        { "variant": 1, "type": "benefit", "text": "[...]", "length": 28 },
        { "variant": 2, "type": "neugier", "text": "[...]", "length": 22 },
        { "variant": 3, "type": "statistik", "text": "[...]", "length": 31 },
        { "variant": 4, "type": "social-proof", "text": "[...]", "length": 35 },
        { "variant": 5, "type": "anti-category", "text": "[...]", "length": 19 }
      ],
      "descriptions": [
        { "variant": 1, "type": "cta-verstärker", "text": "[...]", "length": 14 },
        { "variant": 2, "type": "urgency", "text": "[...]", "length": 18 },
        { "variant": 3, "type": "preis", "text": "[...]", "length": 17 },
        { "variant": 4, "type": "trust", "text": "[...]", "length": 22 },
        { "variant": 5, "type": "benefit-micro", "text": "[...]", "length": 24 }
      ],
      "cta": "LEARN_MORE",
      "url": "[Funnel-URL]"
    }
  ]
}
```

### ad-copy-preview.html

Visuelle Preview-Seite die zeigt:
- Jedes Creative mit allen 5 Primary Text Varianten
- Headline/Description Varianten als Chips
- Copy-Länge und Hook-Länge als Metriken
- Filter nach Varianten-Typ (Story/Statistik/Kontrast/Listicle/Einzeiler)
- Click-to-copy für schnelles Testen

---

## ABLAUF (Step by Step)

### Step 0: Inputs klären
- Welches Projekt? Welcher Creatives-Ordner?
- Welcher Funnel + URL?
- Welches Produkt?
- Rückfrage NUR wenn etwas fehlt

### Step 1: Research laden
1. ALLE Foundational Docs lesen (Personas, VOC, Offer Brief, Before/After, Deep Dive)
2. Ad Concepts laden (falls vorhanden) — Format-Typ, Angle, Awareness pro Creative
3. Creative-Dateien listen — jeden Dateinamen + Kontext kennen
4. **Intern extrahieren:** VOC-Zitate, Pain Points, Desires, Objections, Necessary Beliefs
5. **NICHT als Output** — nur als Arbeitsgrundlage

### Step 2: Creative-Mapping erstellen
Für jedes Creative eine interne Zuordnung:

| Creative | Format | Angle | Awareness | Kongruenz-Typ | Best Primary Text Type |
|---|---|---|---|---|---|
| ad-01-kerzenschein-vater | Foto+Overlay | Fear | Unaware | Story-Erweiterer | Story-Hook |
| ad-05-whatsapp-blackout | WhatsApp Chat | Fear | Problem-Aware | Meta-Kommentar | Einzeiler |
| ... | | | | | |

### Step 3: Primary Texts schreiben
- Pro Creative 5 Varianten (verschiedene Typen, NICHT Umformulierungen)
- Kongruenz mit dem Creative-Typ beachten (siehe Kongruenz-Matrix)
- Hook immer unter 125 Zeichen
- VOC-Sprache durchgehend
- Emotional Delta in jeder Variante
- **SOFORT in ad-copy.json schreiben** (incremental save!)

### Step 4: Headlines schreiben
- Pro Creative 5 Headlines (verschiedene Typen)
- UNTER 27 Zeichen optimal, UNTER 40 Pflicht
- Kein Overlap mit Primary Text Hook
- Ergänzt das Bild, wiederholt es nicht

### Step 5: Descriptions schreiben
- Pro Creative 5 Descriptions
- UNTER 25 Zeichen
- Verstärker, kein eigenständiger Content
- Konsistent über alle Ads (Trust-Signal "4.700+ Familien" darf sich wiederholen)

### Step 6: CTA + URL zuweisen
- Default CTA basierend auf Funnel-Typ:
  - Listicle/Advertorial/Quiz → `LEARN_MORE`
  - Checkout → `SHOP_NOW`
  - Lead Gen → `SIGN_UP`
- URL für alle Ads gleich (Funnel-URL) — Override pro Ad möglich
- UTM-Parameter: `?utm_source=facebook&utm_medium=paid&utm_campaign=[campaign]&utm_content=[ad-id]`

### Step 7: JSON generieren
- Komplette ad-copy.json mit allen Ads + allen Varianten
- Validierung:
  - Alle Headlines < 40 Zeichen?
  - Alle Descriptions < 25 Zeichen?
  - Alle Hook-Lengths < 125 Zeichen?
  - 5 Varianten pro Feld pro Ad?
  - Keine doppelten Texte über Ads hinweg?

### Step 8: Preview-Seite bauen
- HTML-Seite mit allen Creatives + Copy
- Bild links, Copy-Varianten rechts
- Tab-System für die 5 Varianten
- Character Count anzeigen
- Click-to-copy Buttons

### Step 9: QA + Präsentation
1. **Kongruenz-Check:** Passt jede Copy zum Creative?
2. **Varianten-Diversität:** Sind die 5 Varianten wirklich verschieden?
3. **VOC-Check:** Klingt es nach der Zielgruppe oder nach Marketing?
4. **Längen-Check:** Alle Limits eingehalten?
5. **Duplikat-Check:** Keine Copy über verschiedene Ads identisch?
6. the Owner die Ergebnisse präsentieren

---

## REGELN

1. **RESEARCH FIRST** — Keine Copy ohne Foundational Docs gelesen zu haben
2. **VOC > eigene Worte** — Immer die exakte Sprache der Zielgruppe bevorzugen
3. **5 verschiedene ANSÄTZE, nicht 5 Umformulierungen** — Jede Variante hat einen anderen psychologischen Einstieg
4. **Hook unter 125 Zeichen** — IMMER. Keine Ausnahme. Das ist Above the Fold auf Mobile.
5. **Headline unter 40 Zeichen** — Optimal unter 27
6. **Description unter 25 Zeichen** — Wird sonst abgeschnitten
7. **Kongruenz mit Creative** — WhatsApp-Chat braucht andere Copy als Breaking News
8. **Kein Produkt-Name in Indirect Ads** — Der Funnel macht den Verkauf
9. **Kein Preis in Indirect Ads** — Erst auf der Landing Page
10. **Incremental Save** — Nach jedem 3-5er Block sofort in JSON speichern
11. **Emotional Delta** — Jeder Primary Text hat eine emotionale Reise (Start → Peak → End)
12. **Soft CTA bei Indirect** — "Mehr dazu im Link" statt "Jetzt kaufen"
13. **Keine CAPS LOCK Wörter** — Meta filtert das
14. **Max 3-5 Emojis pro Primary Text** — Thematisch passend, nicht random
15. **UTM-Parameter** — Jede Ad bekommt eigene utm_content für Tracking

---

## SMART BATCHING

Bei 23 Creatives × 5 Varianten × 3 Felder = **345 Texte**. Das ist viel. Smart batchen:

### Shared Copy Pool
Manche Primary Texts funktionieren für MEHRERE Creatives des gleichen Angles. Statt 23×5 unique Primary Texts:
1. **Pool erstellen:** 15-20 starke Primary Texts (verschiedene Typen + Angles)
2. **Zuordnen:** Jedes Creative bekommt die 5 am besten passenden aus dem Pool
3. **Customizen:** Hook ggf. an das spezifische Creative anpassen (1 Satz Änderung)

### Headlines & Descriptions
- Diese sind KÜRZER und können stärker geshared werden
- 10-15 starke Headlines → 5 pro Creative zuordnen
- 8-10 Descriptions → 5 pro Creative zuordnen (hier ist Wiederholung okay)

### Ergebnis
Statt 345 komplett unique Texte: ~40-50 starke Texte, intelligent zugeordnet. Qualität > Quantität.

---

## QUALITY GATES

Bevor die Copy ausgeliefert wird, prüfe:

### Gate 1: PIG-Test (Punch In the Gut)
Liest du jeden Hook und spürst einen emotionalen Impuls? Wenn nicht → umschreiben.

### Gate 2: Bar-Test
Würde ein normaler Mensch in einer Bar so reden? Wenn es nach Werbung klingt → umschreiben.

### Gate 3: Oma-Test
Versteht deine Oma den Text? Kein Jargon? Reading Level okay? Wenn nicht → vereinfachen.

### Gate 4: Scroll-Test
Würdest DU bei diesem Hook stoppen? Sei ehrlich. Wenn nicht → stärkeren Hook.

### Gate 5: Kongruenz-Test
Passt die Copy zum Bild? Erzählen sie zusammen eine Geschichte? Wenn nicht → anpassen.
