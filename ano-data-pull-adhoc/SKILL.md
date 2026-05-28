---
name: ano-data-pull-adhoc
description: Use when Ano needs manual or on-demand backfill of historical data, re-sync after API-Token-Wechsel, or one-shot pulls für eine spezifische Analyse-Frage. Trigger wenn the Owner sagt "zieh mal die letzten 90 Tage Meta-Daten", "sync nochmal Pipedrive vom letzten Quartal" oder wenn Ano im Diagnose-Mode bemerkt dass Daten lückenhaft sind. Unterschied zum Cron-Skill: nicht scheduled, sondern parameterisiert (source, project, date-range).
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 1
---

# Ano · Data Pull Adhoc (STUB)

**Status:** Noch nicht implementiert. Bei Aufruf liefere strukturierten Stub-Output statt zu crashen.

## Was dieser Skill machen wird

On-Demand Daten-Pull mit Parametern. CLI-Interface plus Programmatic-API. Schreibt ebenfalls in Supabase Bronze, aber mit `pull_source: adhoc` plus `triggered_by`-Metadata für Audit-Trail.

## Geplante Inputs

```yaml
project_id: [brand]
source: meta_ads | klaviyo | shopify | pipedrive | ...
date_range:
  from: 2026-02-01
  to: 2026-05-10
mode: backfill | re-sync | one-shot
overwrite: true | false  # bei re-sync: alte Rows ersetzen
```

## Stub-Output beim Aufruf

```json
{
  "skill": "ano-data-pull-adhoc",
  "status": "stub",
  "message": "Adhoc-Pull noch nicht gebaut. Würde folgendes ausführen:",
  "would_pull": {
    "project": "[brand]",
    "source": "meta_ads",
    "range": "2026-02-01 to 2026-05-10",
    "estimated_rows": "unknown until built"
  },
  "next_step": "Phase-1-Build via the COO, 1 Tag Aufwand"
}
```

## Use-Cases

- Backfill nach neuem API-Token-Setup
- Re-Sync wenn Schema in der Source sich geändert hat
- One-Shot-Pull für historische Analyse (z.B. "Wie war der Q1-Funnel im letzten Jahr?")
- Recovery wenn Cron-Job ausgefallen ist

## Referenz

Abhängig von `ano-data-pull-cron` (gleiche Pull-Module, anderer Trigger).
