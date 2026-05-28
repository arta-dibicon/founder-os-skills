---
name: ano-data-pull-cron
description: Use when Ano needs scheduled data pulls from connected sources (Meta Ads, Klaviyo/Brevo, ManyChat, Bitly, Shopify, Pipedrive, Plausible/GA4, Stripe, Pixel/CAPI) and writes raw payloads into the Supabase Bronze layer. Trigger this when the Owner says "pull latest", "refresh data", "sync sources" or when Ano needs to ensure data freshness before a Diagnose-Run. Cron-default for non-realtime sources, Webhooks separately for Stripe/Shopify/Pipedrive/ManyChat.
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 3
---

# Ano · Data Pull Cron (STUB)

**Status:** Noch nicht implementiert. Bei Aufruf liefere strukturierten Stub-Output statt zu crashen.

## Was dieser Skill machen wird

Cron-getriebener Multi-Source-Daten-Pull. Pro Quelle ein Pull-Modul. Schreibt JSON-Payload mit Idempotenz-Constraint `(source, external_id, project_id)` in Supabase Bronze Layer.

## Geplante Architektur

| Quelle | Pull-Pattern | Frequenz | Notes |
|---|---|---|---|
| Meta Ads API | Incremental since-last-pull | Stündlich Spend, täglich Insights | Insights attribuieren rückwirkend bis 7 Tage |
| Klaviyo | Webhook plus Reconcile-Cron | Realtime + 3x/Tag | Webhooks zuverlässig |
| Brevo | Cron incremental | Stündlich | Webhooks unzuverlässig |
| ManyChat | Cron full-pull | 6x/Tag | API hat keine seit-Filter |
| Bitly | Cron incremental | Täglich | Click-Daten ändern sich rückwirkend kaum |
| Shopify | Webhook plus Daily-Reconcile | Realtime + Cron | Order-Updates kommen nachträglich |
| Pipedrive | Webhook | Realtime | Sales-Stage-Changes sofort relevant |
| Plausible/GA4 | Cron | Täglich | Daten täglich aggregiert, Backfill 7 Tage |
| Stripe | Webhook plus Cron | Realtime + täglich | Reconcile gegen Doppel-Charges |
| Pixel/CAPI | Server-Side Edge-Function | Realtime | 1st-Party-Endpoint, schreibt direkt in PostHog/Supabase |

## Stub-Output beim Aufruf

```json
{
  "skill": "ano-data-pull-cron",
  "status": "stub",
  "message": "Pull-Skill noch nicht gebaut. Liste der Quellen die in api-inventory.md als connected markiert sind:",
  "connected_sources": ["..."],
  "missing_for_full_coverage": ["..."],
  "next_step": "Phase-1-Build via the COO, 3 Tage Aufwand"
}
```

## Tech-Stack-Vorgaben

- Python (asyncio) für Pull-Jobs
- Supabase Postgres als Storage (Bronze plus Silver)
- DuckDB für aggregierte Reads (Gold)
- Idempotenz via Unique-Constraint
- Webhooks via Next.js Background Functions auf Netlify
- Compute auf Hostinger-VPS plus systemd-Timer

## Referenz

Voller Architektur-Background: `infrastruktur/ano/research-2026-05-10.md` Abschnitt 2.
