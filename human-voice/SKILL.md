---
name: human-voice
description: Macht jeden geschriebenen Output menschlich klingen — entfernt AI-Marker und wendet projektspezifische Brand-Voice an. UNIVERSAL Skill, gilt für alle Projekte. Lädt automatisch die globale Anti-AI-Voice Regel + das passende Projekt-Voice-Profil (z.B. maren-voice, annika-voice, markus-voice) wenn vorhanden. TRIGGER bei "schreib das menschlicher", "ohne AI-Klang", "in [Brand]-Stimme", "Voice-Check", "ist das zu KI-mäßig?". Auch automatisch nach Generierung längerer Texte (Newsletter, Captions, Sales-Pages, Cold-Emails, Advertorials) als Pre-Delivery-Filter.
---

# Human Voice — Universal Brand-Voice Orchestrator

Texte sollen klingen als hätte ein wacher, denkender Mensch sie geschrieben — nicht ein Generator. Bei brand-spezifischen Outputs zusätzlich: klingen wie genau diese Brand spricht.

Dieser Skill ist der **Orchestrator**. Er kombiniert zwei Schichten:

1. **Globale Baseline:** Anti-AI-Voice Regel (`.claude/rules/anti-ai-voice.md`) — was darf NICHT drin sein
2. **Projektspezifische DNA:** das passende Voice-Profil-Skill (wenn vorhanden) — wie spricht diese Brand konkret

---

## SCHRITT 1 — Projekt-Kontext erkennen

Bevor du den Skill anwendest, klär ab in welchem Brand-Kontext der Text ist. Quellen in dieser Reihenfolge:

1. **Expliziter Hinweis** im Prompt: "für the Founder", "in Annikas Stimme", "Markus-Voice"
2. **Pfad-Kontext:** Liegt der Text in `1_aktiv/1_within-supplements/`? → the Founder. `4_pretty-little-cakes/`? → the Owner. `6_liberator-akademie/`? → Markus.
3. **Asset-Typ + Empfänger:** Newsletter für [brand] → the Founder. Caption für PLC Instagram → the Owner. Email an the Owner → keine Brand, normale B2B-Voice.
4. **Im Zweifel fragen:** "Soll das in Marens, Annikas oder Markus' Stimme klingen, oder ist das neutral?"

---

## SCHRITT 2 — Passenden Voice-Skill laden

Mapping Brand → Skill:

| Brand / Projekt | Voice-Skill | Pfad |
|---|---|---|
| [brand] / the Founder | `maren-voice` | `.claude/skills/maren-voice/SKILL.md` |
| [brand] / the Owner | `annika-voice` | `.claude/skills/annika-voice/SKILL.md` |
| [brand] / Markus Streinz | `markus-voice` | `.claude/skills/markus-voice/SKILL.md` |
| Alle anderen | KEIN Brand-Skill → siehe Fallback unten | — |

Wenn ein Voice-Skill existiert: dessen SKILL.md vollständig laden und Regeln anwenden ZUSÄTZLICH zur Anti-AI-Voice Baseline.

---

## SCHRITT 3 — Fallback (kein Brand-Voice-Profil)

Wenn das Projekt keinen eigenen Voice-Skill hat (z.B. [brand], [brand], Peptide, [brand], ZZB, [brand], Longevity, interne the COO-Outputs), gilt nur die Baseline plus diese generischen Human-Voice-Regeln:

### Du-Anrede oder Sie-Anrede?
- Default: **Du** (B2C, Coach-Ton, alles was nach moderner Brand klingt)
- **Sie** nur bei: formellen B2B-Cold-Mails an Konzerne, Behördenkommunikation, juristischen Texten

### Erste-Person-Bezug erlaubt
- "Ich seh das so", "wir bei [Firma]"
- Nicht in jedem Satz, aber wenn es passt: rein damit

### Konkretes vor Abstraktem
- Zahl, Name, Datum, Beispiel statt Allgemeinplatz
- "47 Kunden im Q1" statt "viele Kunden"
- "in 14 Tagen" statt "schnell"

### Position beziehen
- Wenn etwas Mist ist: sag dass es Mist ist
- Keine "einerseits-andererseits"-Balance um der Balance willen
- Mensch hat eine Meinung, AI bedient immer beide Seiten

### Satzlängen variieren
- Mindestens 1 kurzer Satz (<8 Wörter) und 1 langer (>20 Wörter) pro Absatz
- Fragmente sind okay ("Kein Witz." "Wirklich.")
- Sätze dürfen mit "Und", "Aber", "Weil" anfangen

### Aktive Stimme als Default
- "Der Plan zerstört X." statt "X wird durch den Plan zerstört."

### Bullet-Points sparsam
- Wenn <3 wirklich gleichartige Items: kein Bullet-Block, sondern Satz
- Mensch schreibt Fließtext, AI schreibt Powerpoint

---

## SCHRITT 4 — Anti-AI-Voice Baseline (PFLICHT, immer)

Egal ob Brand-Profil geladen oder nicht: die globale Regel aus `.claude/rules/anti-ai-voice.md` läuft IMMER. Hier die 5 schärfsten Marker als Quick-Reference:

1. **Em-Dashes (—) raus.** Stärkstes AI-Signal. Ersatz: Punkt, Komma, Klammern, "und".
2. **"Nicht X, sondern Y"** verboten. Das ist DAS LLM-Cliché.
3. **Rule of Three** (drei Adjektive in Reihe) verboten.
4. **Floskel-Opening/Closing** verboten ("In der heutigen schnelllebigen Welt", "Lass uns eintauchen", "Im Endeffekt", "Zusammenfassend").
5. **Verbotswörter:** ganzheitlich, nahtlos, optimal, revolutionär, beleuchten, eintauchen, hervorheben, leverage, utilize, intricate, pivotal, robust, seamless, cutting-edge, game-changer, synergy, holistic, vibrant.

Vollständige Liste mit ~80 Verbotswörtern + Typografie-Details: `.claude/rules/anti-ai-voice.md`.

---

## SCHRITT 5 — Pre-Delivery Check

Bevor der Text rausgeht, scanne:

- [ ] **Em-Dash-Scan:** 0 Em-Dashes (—) im Text?
- [ ] **Verbotswort-Scan:** Keine Treffer aus der Verbotsliste?
- [ ] **"Nicht X, sondern Y" Scan:** Keine negative Parallelism?
- [ ] **Rule-of-Three Scan:** Keine drei-Adjektiv-Listen?
- [ ] **Opening/Closing-Floskel-Scan:** Erster und letzter Satz frei von Floskeln?
- [ ] **Satzlängen-Test:** Mindestens 1 kurzer und 1 langer Satz pro Absatz?
- [ ] **Konkret-Test:** Mindestens 1 spezifische Zahl/Name/Datum/Beispiel pro Absatz?
- [ ] **Wenn Brand-Profil geladen:** Hat der Text die Brand-DNA? (Du/Sie, typische Phrasen, Struktur-Pattern)
- [ ] **Vorlese-Test:** Stolpert man beim lauten Vorlesen? Klingt es wie LinkedIn-Influencer?

Bei Treffer: zurück zur Werkbank.

---

## WANN DIESER SKILL NICHT GREIFT

- Code-Kommentare (technische Sachlichkeit OK)
- API-Doku, technische READMEs (formal OK)
- JSON-Outputs, strukturierte Daten
- Englische Texte für englische Märkte (anderes Voicing-System nötig — Anti-AI-Voice gilt trotzdem)

---

## WIE NEUE BRAND-VOICE-PROFILE HINZUKOMMEN

Wenn ein neues Projekt genug eigenes Voice-Material hat (mindestens 20 echte Reels/Captions/Mails der Brand-Person):

1. Neuen Skill anlegen unter `.claude/skills/[brand]-voice/SKILL.md`
2. Folgenden Aufbau (Vorlage aus `maren-voice`):
   - Die 3 Gebote (was die Brand IMMER macht)
   - Verbotsliste (was diese Brand SPEZIFISCH nicht macht)
   - Vokabular (typische Wörter/Phrasen/Hooks)
   - Struktur-Patterns (wie Posts/Mails/Captions aufgebaut sind)
   - Quick-Examples (FALSCH vs RICHTIG mit echtem Brand-Beispiel)
3. Mapping-Tabelle in DIESEM Skill (Schritt 2) ergänzen
4. Source-Truth-Pfad dokumentieren (wo das Original-Material liegt für Re-Calibration)

---

## SOURCE-TRUTH-PFADE PRO BRAND

- **the Founder:** `1_aktiv/1_within-supplements/content-analysis/output/knowledgebase.jsonl` (678 Reels-Transkripte) + `1_aktiv/1_within-supplements/_references/maren-profile.md`
- **the Owner:** `1_aktiv/4_pretty-little-cakes/carousel/output/*/caption.txt` (Caption-History) + `1_aktiv/4_pretty-little-cakes/competitor-research/strategy-for-annika-2026-04-22.md`
- **Markus:** `1_aktiv/6_liberator-akademie/_research/02-cla-audit/04-brand-voice.md` + `1_aktiv/6_liberator-akademie/_research/03-internet-research/04-voice-dna.md`

Bei Zweifeln über die Voice: 3 zufällige Quellen ziehen, Tonalität abgleichen.
