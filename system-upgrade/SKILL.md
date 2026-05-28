---
name: system-upgrade
description: "Wöchentlicher Self-Upgrade — prüft Neuigkeiten, reviewed Setup, macht konkrete Verbesserungsvorschläge"
---

# System Upgrade — the COO hält sich selbst aktuell

Du führst ein systematisches Self-Upgrade durch. Das Ziel: Unser Claude Code Setup bleibt immer auf dem neuesten Stand und wird kontinuierlich besser.

## Phase 1: News-Check (Was gibt es Neues?)

Recherchiere parallel mit Agents:

### 1a. Claude Code Changelog
- Fetch: https://docs.anthropic.com/en/docs/claude-code/changelog
- Identifiziere neue Features, Bugfixes, Breaking Changes seit dem letzten Upgrade
- Fokus: Neue Tools, neue Flags, neue Konfigurationsoptionen, Performance-Verbesserungen

### 1b. Anthropic API & Modelle
- Fetch: https://docs.anthropic.com/en/docs/about-claude/models
- Neue Modelle? Neue Capabilities? Preisänderungen?
- Fetch: https://docs.anthropic.com/en/docs/build-with-claude/tool-use
- Neue Tool-Use-Features?

### 1c. Claude Code Docs — Best Practices
- Fetch: https://docs.anthropic.com/en/docs/claude-code/overview
- Gibt es neue empfohlene Patterns für Hooks, Skills, Agents, MCP?
- Neue MCP-Server die für uns relevant sind?

### 1d. AI Space Highlights (optional, wenn relevant)
- WebSearch: "Claude Code new features" + aktueller Monat
- WebSearch: "Anthropic announcement" + aktuelle Woche
- Nur wirklich relevante Neuigkeiten, kein Noise

## Phase 2: Setup-Audit (Wo stehen wir?)

Analysiere unser aktuelles Setup:

### 2a. Rules Review
- Lies alle Dateien in `.claude/rules/` — sind sie noch aktuell?
- Widersprechen sich Rules? Sind welche redundant?
- Gibt es neue Claude Code Features die eine Rule obsolet machen?

### 2b. Skills & Commands Review
- Lies alle Skills in `.claude/skills/` und Commands in `.claude/commands/`
- Werden alle noch genutzt? Gibt es veraltete?
- Können bestehende Skills von neuen Features profitieren?

### 2c. Memory Health-Check
- MEMORY.md Index prüfen: Alle Files gelistet? Beschreibungen aktuell?
- Veraltete Memories identifizieren
- Duplikate oder Überschneidungen?
- Index unter 120 Zeilen?

### 2d. Agents & MCP Review
- `.claude/agents/` — Agents noch relevant? Richtige Modelle zugewiesen?
- `.claude/.mcp.json` + `settings.json` MCP-Config — neue Server verfügbar?
- Hooks aktuell?

### 2e. Projekt-Aktivität
- `git log --oneline -30` in jedem Projektordner (oder ls -lt für letzte Änderungen)
- Welche Projekte waren diese Woche aktiv?
- Welche Projekte sind eingeschlafen?

## Phase 3: Upgrade-Vorschläge generieren

Basierend auf Phase 1 + 2, erstelle eine priorisierte Liste:

### Format pro Vorschlag:
```
### [Priorität: HOCH/MITTEL/NIEDRIG] Titel

**Was:** Konkrete Änderung (1-2 Sätze)
**Warum:** Was bringt es uns? (Speed, Qualität, neue Capability)
**Quelle:** Welche News/Erkenntnis hat das getriggert?
**Aufwand:** Minuten-Schätzung
**Risiko:** Gibt es Seiteneffekte?
```

### Kategorien:
- **Neue Features nutzen** — Claude Code hat was Neues, wir sollten es einbauen
- **Setup-Optimierung** — Bestehende Config verbessern
- **Memory-Hygiene** — Aufräumen, konsolidieren, aktualisieren
- **Skill-Upgrades** — Bestehende Skills verbessern oder neue bauen
- **Deprecation-Warnungen** — Etwas wird bald nicht mehr funktionieren

## Phase 4: Upgrade-Report

Erstelle den Report als Datei:
- Speichere in: `infrastruktur/system-upgrades/YYYY-MM-DD-upgrade-report.md`
- Formatierung: Markdown, klar strukturiert, max 2 Seiten

### Report-Struktur:
```markdown
# System Upgrade Report — [Datum]

## Letzer Upgrade: [Datum aus Memory]
## Neue Features seit letztem Check
[Bullet Points der relevanten News]

## Aktive Projekte diese Woche
[Aus Phase 2e]

## Upgrade-Vorschläge (priorisiert)
[Aus Phase 3]

## Memory-Hygiene
[Status + durchgeführte Bereinigungen]

## Nächster Check: [Datum + 7 Tage]
```

## Phase 5: Memory updaten

- Update `project_system_upgrade_log.md` mit:
  - Datum des Checks
  - Welche News gefunden
  - Welche Vorschläge gemacht
  - Was davon umgesetzt wurde (nach Artas Feedback)
- Damit der nächste Upgrade-Lauf weiß wo er anfangen muss

## Wichtig
- KEINE Änderungen automatisch umsetzen — nur vorschlagen
- the Owner entscheidet was gemacht wird
- Bei HOCH-Priorität Vorschlägen: klar begründen warum sofort
- Bei neuen Modellen: Benchmarks/Preise vergleichen, nicht blind upgraden
- Report soll in 2 Minuten lesbar sein — kein Roman
