---
name: ano-cohort-analysis
description: Use für eCom-Projekte (Within, PLC, Wayro, künftige Shops) wenn RFM-Segmentation, Retention-Curves oder LTV-Buckets gebraucht werden. Berechnet `champions`, `at-risk`, `lost`, `new`, `loyal` Buckets wöchentlich. Triggert Flow-Empfehlungen für Klaviyo/Brevo (z.B. Win-Back-Campaign für `at-risk` mit 60-90 Days-Since-Last-Order). Nicht für Coaching/Lead-Gen-Projekte (zu kleine N, andere Buyer-Logik).
metadata:
  status: STUB
  phase: 2
  build_priority: medium
  estimated_effort_days: 2
---

# Ano · Cohort Analysis (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

RFM-Segmentation (Recency, Frequency, Monetary) plus Retention-Curves plus LTV-Buckets für eCom-Projekte. Wöchentlich.

## Buckets

| Segment | Definition | Action-Trigger |
|---|---|---|
| Champions | Top 10% R+F+M | VIP-Flow, Referral-Push |
| Loyal | High F+M, mittlere R | Cross-Sell, Bundle-Push |
| At-Risk | 60-90 Days-Since-Last-Order, früher hoch F+M | Win-Back-Email-Sequenz |
| Lost | >120 Days-Since-Last, ehemals aktiv | Reactivation-Offer oder Suppress |
| New | Erster Order in letzten 30 Tagen | Welcome-Flow, Second-Purchase-Push |

## Retention-Curve

Cohorten nach `acquisition_month`, plotten gegen Days-Since-Acquisition. Liefert Curve plus 30/60/90d Retention-Rate plus Median-Repeat-Cycle pro Cohort.

## LTV-Buckets

Pro Cohort: 30/60/90/180/360-Tage-LTV. Vergleich zwischen Acquisition-Quellen (Meta vs Email-Organic vs Affiliate).

## Eignung

✅ [brand], [brand] (wenn Shopify-Daten verbunden), künftige eCom-Projekte
❌ Coaching/Lead-Gen ([brand], [brand], ZZB) — zu kleine N, Buyer-Cycle anders strukturiert

## Stub-Output

```json
{"skill": "ano-cohort-analysis", "status": "stub", "message": "RFM/Retention/LTV noch nicht gebaut. Phase-2, 2 Tage."}
```
