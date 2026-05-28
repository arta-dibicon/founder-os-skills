---
name: ano-funnel-diagnostics
description: Core-Diagnose-Engine von Ano. Use wenn Symptom-Pattern (Metric-Kombinationen) interpretiert werden sollen. Beispiele "Hohe CTR + niedrige CVR → LP-Mismatch?", "Hohe Add-to-Cart + niedrige Purchase → Checkout-Friction?", "ROAS sinkt 30% in 7 Tagen → Creative Fatigue?". Lädt `infrastruktur/ano/heuristics.yaml` (30-50 Regeln) und führt Rule-Cascade aus. LLM-Fallback (Claude Opus) nur wenn keine Regel matcht. Triggert vorher automatisch `ano-data-quality-checker` und `ano-benchmark-library`. Output strukturiertes JSON plus Plain-Markdown.
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 2
---

# Ano · Funnel Diagnostics (STUB)

**Status:** Noch nicht implementiert. Das ist das Herzstück von Ano.

## Was dieser Skill machen wird

Rule-Cascade-Engine auf aggregierten Daten-Slices. Lädt `heuristics.yaml`, prüft jede Regel gegen aktuelle Metrics, gibt priorisierte Hypothesen-Liste plus Confidence plus Folge-Query plus Recommendation-Template.

## Initial-Heuristics (30-50 Regeln geplant, Beispiele)

| Symptom-Pattern | Hypothesen (priorisiert) | Folge-Query |
|---|---|---|
| CTR > 2% UND CVR < 1% | (1) LP-Mismatch (2) Targeting breit (3) LP-LCP lahm | LP-Bounce, LP-LCP, Audience-Saving-Score |
| CTR < 0.8% UND CPM steigend WoW | Creative Fatigue, Audience saturated | Frequency >2.5? Days-Active-Creative |
| Add-to-Cart > 8% UND Purchase < 1% | Checkout-Friction, Payment-Methods, Versandkosten-Schock | Stripe-Cart-Abandon-Logs |
| Email Open > 35% UND Click < 2% | Subject stark, Body schwach, CTA-Position | Heatmap/Bitly-Position |
| Lead > 50/Tag UND Booking < 5% | Lead-Qualität, Booking-Friction | Self-Report-Source, Booking-Page-LCP |
| ROAS sinkt 30%+ in 7d | (1) Creative Fatigue (2) Saisonale Drift (3) Konkurrenz-Bid-Inflation | CUSUM CPM, Frequency, Benchmark |
| LP-Time-on-Page > 90s UND CVR < 1% | Information-Overload oder Trust-Issue | Scroll-Depth-Heatmap |

## Output-Schema

```json
{
  "diagnose_id": "diag_xyz",
  "project_id": "...",
  "timestamp": "...",
  "data_window": "2026-04-25 to 2026-05-09",
  "matched_rules": [
    {"id": "lp_mismatch", "confidence": 0.78, "hypothesis": "...", "follow_up_query": "...", "recommendation": "..."}
  ],
  "llm_fallback_triggered": false,
  "anti_garbage_filters_passed": true
}
```

## Hybrid Rule + LLM

- 80% der Diagnosen: pure Rule-Cascade
- 20%: LLM-Fallback (Claude Opus, structured prompt) für Edge-Cases ohne Regel-Match
- LLM-Output bekommt Caveat "experimentelle Hypothese, niedrige Konfidenz"

## Anti-Garbage-Filter

Bevor Diagnose rausgeht: Min-Volume-Filter (Spend >200€/d UND Conv >100), Confidence-Threshold (>0.6), Stake-Test im LLM-Prompt ("Wenn ambivalent, sag das").

## Stub-Output beim Aufruf

```json
{
  "skill": "ano-funnel-diagnostics",
  "status": "stub",
  "message": "Diagnose-Engine noch nicht gebaut. Würde heuristics.yaml laden, Rule-Cascade ausführen, LLM-Fallback bei Edge-Case.",
  "next_step": "Phase-1-Build via the COO, 2 Tage Aufwand, davor: heuristics.yaml mit 30 Initialregeln definieren"
}
```
