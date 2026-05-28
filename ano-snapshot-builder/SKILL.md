---
name: ano-snapshot-builder
description: Use für 60-Sekunden-Health-Check eines Projekts. Liefert kompakten Status-Output (Spend/ROAS/CAC/Conv/Drift-Flags/Top-3-Recommendations) in plain Markdown mit Unicode-Sparklines. Für Telegram-Bot oder the COO-Briefing geeignet. Per-Vertical-KPI-Sets (eCom anders als Coaching anders als Lead-Gen). Triggert intern `ano-data-quality-checker` plus `ano-funnel-diagnostics` plus `ano-recommendation-engine`. Output: kurz, scannbar, mobile-tauglich.
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 1
---

# Ano · Snapshot Builder (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

Komprimierter Health-Snapshot. Nicht für Deep-Dive, sondern für "wie steht's gerade um Projekt X in 60 Sekunden". Telegram-kompatibel, scannbar, plain Markdown.

## Output-Format

```markdown
**[brand] · Snapshot 2026-05-10 14:30**

Spend 7d: €2.847 ▂▃▅▇▆▄▃ (-12% WoW)
ROAS 7d: 2.1 ▅▆▇▆▅▄▃ (-0.3 vs target 2.4)
CAC: €38.50 (+4€ WoW)
Conv 7d: 74

**🟡 Drift-Flags (1)**
- ROAS sinkt 4. Tag in Folge → Frequency 4.2 (Fatigue?)

**Top-3 Quick-Wins**
1. Creative-Refresh (Confidence 78%, ΔROAS +0.4 erwartet)
2. LP-LCP unter 2.5s bringen (Mobile 3.8s aktuell)
3. Email-Reactivation für 60-90d-Cohorte starten

DQ-Check: ✓ pass | Volldiagnose: `/ano funnel within`
```

## Per-Vertical-KPI-Sets

| Vertical | Default-KPIs |
|---|---|
| eCom (Within, PLC) | Spend, ROAS, AOV, CAC, Conv, Drift-Flags |
| Coaching ([brand]) | Spend, CAC, Booked-Calls, Show-Rate, Close-Rate |
| Lead-Gen ([brand], ZZB) | Spend, CPL, Lead-Quality-Score, MQL-Rate |
| Email-Heavy (alle) | Open-Rate, Click-Rate, Unsub-Rate, Revenue-pro-Email |

## Sparkline-Logik

Unicode-Blocks `▁▂▃▄▅▆▇█` für 7- oder 14-Tage-Trends. Min-Max-skaliert pro Metric. Keine echten Charts, nur Inline-Hinweis auf Richtung.

## Mode-Varianten

| Mode | Inhalt | Zielmedium |
|---|---|---|
| `compact` | Snapshot wie oben | Telegram, Slack |
| `briefing` | Snapshot plus 1 Absatz Kontext | the COO → the Owner |
| `dashboard-card` | Snapshot als HTML-Card | Web-Dashboard |

## Dependencies

Snapshot ruft intern auf:
1. `ano-data-quality-checker` (PRE-FLIGHT)
2. `ano-funnel-diagnostics` (Top-3 Issues identifizieren)
3. `ano-recommendation-engine` (Top-3 Quick-Wins ableiten)
4. `ano-drift-detection` (Flags setzen)

Wenn DQ-Check `block` returnt: Snapshot wird abgebrochen, Hinweis "Daten nicht frisch, repull triggern".

## Stub-Output

```json
{"skill": "ano-snapshot-builder", "status": "stub", "message": "Snapshot-Builder noch nicht gebaut. Phase-1, 1 Tag. Voraussetzung: ano-data-quality-checker plus ano-funnel-diagnostics laufen real, nicht als Stub."}
```
