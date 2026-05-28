---
name: ano-drift-detection
description: Use wenn Metriken auf Anomalien oder Trends geprüft werden sollen (Spend, ROAS, CPM, Open-Rate, AOV, CAC). Methoden Z-Score (Rolling 14d) plus EWMA (für langsame Drifts). Triggert Alert NUR wenn 3 aufeinanderfolgende Tage über Schwellwert (Single-Day-Spikes werden geloggt aber nicht alarmiert). Output enthält immer Erwartung plus Realität plus Z-Score plus mögliche Ursache. Kein Prophet/Isolation Forest (Daten zu dünn pro Projekt).
metadata:
  status: STUB
  phase: 2
  build_priority: medium
  estimated_effort_days: 1
---

# Ano · Drift Detection (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

Statistische Anomalie-Detection auf Time-Series-Metriken. Lightweight, weil Daten oft <100 Tage Historie pro Kampagne haben.

## Methoden

| Methode | Sample-Bedarf | Eignung |
|---|---|---|
| Z-Score (Rolling 14d) | 14 Tage | Default für 80% der Metriken |
| EWMA (Exp. Weighted Moving Avg) | 30 Tage | Spend, ROAS (langsame Drifts) |
| CUSUM | 30 Tage | Phase 2, Creative-Fatigue |

## Confidence-Logik

Drift gilt als "real" wenn 3 aufeinanderfolgende Tage über Schwellwert. Sonst: Log-only, kein Alert.

## Output-Format

```
Metric: ROAS
Erwartung: 2.4 (90% CI: 2.1-2.7) [basis: rolling 14d]
Realität: 1.6 (-33%)
Z-Score: -3.1
Drift-Status: real, seit 4 Tagen
Mögliche Ursache: Frequency 4.2 (war 2.1) → Creative Fatigue
Severity: high
```

## Was wir NICHT machen

- Isolation Forest (Daten zu dünn)
- Prophet/NeuralProphet (Saisonale Modelle würden Garbage liefern)

## Stub-Output

```json
{"skill": "ano-drift-detection", "status": "stub", "message": "Drift-Engine noch nicht gebaut. Phase-2-Build, 1 Tag."}
```
