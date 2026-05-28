---
name: ano-recommendation-engine
description: Use wenn aus Diagnosen konkrete Action-Items abgeleitet werden sollen. Wandelt Hypothesen aus `ano-funnel-diagnostics` plus Drift-Findings plus Cohort-Patterns in priorisierte Recommendations um. Hybrid Rule-Based (Templates pro Diagnose-Typ) plus LLM-Polish (Claude Opus, Voice-Adaption). Output strukturiertes JSON mit `action`, `confidence`, `expected_impact`, `effort`, `assignee_hint`, `dependencies`. Triggert immer als Folge-Step nach `ano-funnel-diagnostics` oder direkt aus `ano-snapshot-builder`.
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 3
---

# Ano · Recommendation Engine (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

Übersetzer-Schicht zwischen Diagnose und Handlung. Nimmt Hypothesen aus `ano-funnel-diagnostics` und macht daraus operative Tickets — kein "ihr solltet mal X tun", sondern "ändert Y in Z, erwartet Δ ROAS +0.4 in 7 Tagen".

## Recommendation-Schema

```json
{
  "id": "rec_001",
  "based_on_diagnose": "diag_xyz",
  "action": "Creative-Refresh: 3 neue Hooks gegen Frequency-Fatigue testen",
  "channel": "meta_ads",
  "confidence": 0.78,
  "expected_impact": {
    "metric": "roas",
    "delta": "+0.4",
    "horizon_days": 7,
    "basis": "historische Refresh-Effekte bei Frequency >3.5"
  },
  "effort": "M",
  "assignee_hint": "Visual (Ad-Creative-Skill) plus Writer (Hook-Variation)",
  "dependencies": ["Hook-Brief von Writer", "Frame-Briefing für Visual"],
  "rollback_plan": "Falls neue Creatives nach 3 Tagen schlechter performen als alte, zurück auf Top-3"
}
```

## Hybrid-Logik

| Layer | Aufgabe |
|---|---|
| Rule-Templates | Pro Diagnose-Typ (lp_mismatch, creative_fatigue, etc.) ein Action-Template mit Slot-Werten |
| LLM-Polish | Claude Opus füllt Slots projekt-spezifisch, adaptet Voice (the COO → the Owner) |
| Effort-Estimator | Mapped Action auf S/M/L basierend auf historischer Build-Zeit |

## Priorisierung

Recommendations werden sortiert nach **Impact ÷ Effort**. Top 3 werden als "Quick-Wins" markiert. Rest als "Optional".

## Anti-Garbage-Filter

- Keine Action ohne Expected-Impact-Range
- Keine Action ohne Confidence > 0.5
- Keine Action ohne Rollback-Plan bei Confidence < 0.75
- Bei LLM-Output: Stake-Test im Prompt ("Wenn die Daten zu dünn sind, sag das, statt zu raten")

## Was wir NICHT machen

- Auto-Execution von Recommendations (the COO plus the Owner entscheiden)
- Bullshit-Action-Items wie "Marke schärfen" oder "Content strategischer denken"
- Recommendations ohne Bezug zur aktuellen Datenlage

## Stub-Output

```json
{"skill": "ano-recommendation-engine", "status": "stub", "message": "Recommendation-Engine noch nicht gebaut. Phase-1, 3 Tage. Voraussetzung: ano-funnel-diagnostics liefert strukturierte Hypothesen."}
```
