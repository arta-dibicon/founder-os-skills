---
name: ano-benchmark-library
description: Use wenn Ano Benchmark-Werte für ein Projekt braucht (CTR/CPM/CPC/CVR/AOV/Open-Rate/Click-Rate-Ranges, Channel-Mix-Patterns, Pricing-Anker, Creative-Patterns, Red-Flags). Liest primär aus `[projekt]/_research/benchmark_anchors.md` (von Rechit gepflegt). Fallback auf globale Industry-Defaults wenn Anker fehlt. Injiziert Werte als dynamische Schwellen in `heuristics.yaml`. Wird von `ano-funnel-diagnostics` und `ano-drift-detection` als Pre-Step aufgerufen.
metadata:
  status: STUB
  phase: 1
  build_priority: high
  estimated_effort_days: 0.5
---

# Ano · Benchmark Library (STUB)

**Status:** Noch nicht implementiert.

## Was dieser Skill machen wird

Lädt Benchmark-Werte aus zwei Quellen, mit klarer Hierarchie:

1. **Primary:** `[projekt]/_research/benchmark_anchors.md` (Rechit-Output, Konkurrenz-Deep-Dive-Daten)
2. **Fallback:** `infrastruktur/ano/benchmarks-global.yaml` (Industry-Defaults pro Vertical)

Wenn beide fehlen: explizites Caveat im Diagnose-Output "Benchmark-Anker fehlt, Werte generisch."

## Schema (Rechit-Output)

```yaml
project: [brand]
vertical: supplements-dach
researched_at: 2026-05-08
source_competitors:
  - { name: "...", sample_size: "..." }
benchmarks:
  meta_ads: { ctr_range: [1.4, 3.2], cpm_range: [12, 28], frequency_threshold: 3.5 }
  landing_page: { cvr_lead_range: [3, 8], cvr_purchase_range: [1, 4] }
  email: { open_range: [28, 42], click_range: [2, 6] }
  pricing: { entry_offer_range: [29, 79], main_offer_range: [99, 299] }
channel_mix_typical: { meta_ads: 55, organic_ig: 25, email: 15, affiliate: 5 }
creative_patterns: ["...", "..."]
red_flags: ["..."]
```

## API für andere Ano-Skills

```python
benchmark.get("meta_ads.ctr_range", project="[brand]")
# → [1.4, 3.2] oder global-default mit Caveat
```

## Stub-Output beim Aufruf

```json
{
  "skill": "ano-benchmark-library",
  "status": "stub",
  "message": "Lookup-Logik noch nicht gebaut. Würde lesen aus _research/benchmark_anchors.md oder fallback global.",
  "next_step": "Phase-1-Build via the COO, 0.5 Tage Aufwand"
}
```
