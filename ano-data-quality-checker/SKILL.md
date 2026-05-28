---
name: ano-data-quality-checker
description: Use als Pre-Flight vor jeder Diagnose oder Snapshot. Prüft ob Daten frisch sind (Bronze-Layer-Aktualität <24h), ob Pulls erfolgreich liefen (kein Error-State im Pull-Log), ob Schema-Drift aufgetreten ist (neue/fehlende Felder in API-Responses) und ob Row-Counts plausibel sind (Outlier-Detection auf Daily-Volumes). Trigger automatisch zu Beginn jeder Ano-Operation. Output: Pass/Fail plus Liste der Probleme plus Empfehlung (proceed/block/repull).
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 1
---

# Ano · Data Quality Checker (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

Pre-Flight-Check vor jeder Diagnose. Verhindert "Garbage-In-Garbage-Out". Drei Layer:

1. **Freshness:** Letzter erfolgreicher Pull pro Quelle <24h alt?
2. **Schema-Integrity:** Erwartete Felder vorhanden? Neue Felder aufgetaucht (potentielle API-Änderung)?
3. **Volume-Sanity:** Daily-Row-Counts innerhalb 2-SD vom 30d-Mean? Nullen/Crashes erkennen.

## Output-Schema

```json
{
  "status": "pass | warn | block",
  "checks": [
    {"name": "freshness_meta_ads", "status": "pass", "last_pull": "2026-05-10T22:15:00Z"},
    {"name": "schema_klaviyo", "status": "warn", "issue": "New field 'predictive_clv' detected"},
    {"name": "volume_shopify_orders", "status": "block", "issue": "0 orders in last 24h (norm 12-40)"}
  ],
  "recommendation": "block | proceed | repull"
}
```

## Wann triggert dieser Skill

Automatisch vor `ano-funnel-diagnostics`, `ano-drift-detection`, `ano-snapshot-builder`. Auch manuell aufrufbar zur Wartung.

## Stub-Output beim Aufruf

```json
{
  "skill": "ano-data-quality-checker",
  "status": "stub",
  "message": "Pre-Flight-Check noch nicht implementiert. Würde 3 Layer prüfen: freshness, schema, volume.",
  "next_step": "Phase-1-Build via the COO, 1 Tag Aufwand"
}
```
