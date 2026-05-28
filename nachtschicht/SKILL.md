---
name: nachtschicht
description: Starte die Nachtschicht — sammle Aufgaben von the Owner, bereite Task-Files vor, starte parallele Claude-Agenten über Nacht, präsentiere morgens einen sauberen Report.
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebFetch, WebSearch
---

# Nachtschicht — the COO arbeitet, the Owner schläft

Du startest jetzt den Nachtschicht-Modus. the Owner gibt dir Aufgaben die über Nacht von parallelen Claude-Agenten autonom abgearbeitet werden. Am Morgen liegt ein sauberer Report bereit.

## Ablauf

### Phase 1: Tasks sammeln

Frage the Owner: **"Was soll ich heute Nacht erledigen?"**

Für jeden Task den the Owner nennt:
1. **Kontext sammeln** — Lies relevante Projektdateien, Memory, Google Chat, Referenzen. Nutze Explore-Agents parallel für mehrere Projekte.
2. **Task-Datei schreiben** — Erstelle eine `.md` Datei in `~/nachtschicht-tasks/` mit:
   - Klarer Rollenbeschreibung (the COO, COO, Nachtschicht)
   - Arbeitsverzeichnis
   - Alle relevanten Dateipfade + API-Credentials die der Agent braucht
   - Schritt-für-Schritt Anleitung (Phasen mit klaren Deliverables)
   - Qualitätskriterien
3. **Bestätigung** — Zeige the Owner kurz was der Task beinhaltet

Alte Task-Dateien aus `~/nachtschicht-tasks/` vorher löschen:
```bash
rm -f ~/nachtschicht-tasks/*.md
```

Nummeriere Tasks: `01-name.md`, `02-name.md`, etc.

### Phase 2: Task-Dateien vorbereiten

Jede Task-Datei MUSS enthalten:
- **Absolute Pfade** (kein `~` oder `$HOME` — der Agent läuft in tmux)
- **API-Credentials** mit Code-Snippets (Service Account Pfade, Scopes)
- **Referenzdokumente** die der Agent zuerst lesen soll
- **Output-Verzeichnis** wo Ergebnisse gespeichert werden
- **Phasen** mit klaren Schritten (nicht nur "mach X", sondern "1. Lies Y, 2. Analysiere Z, 3. Baue W")

### Phase 3: Pre-Flight Check

Prüfe ALLE Voraussetzungen:

```bash
# 1. Strom angeschlossen?
system_profiler SPPowerDataType 2>/dev/null | grep -E "Connected|Charging"

# 2. Disk Space
df -h / | tail -1

# 3. Claude CLI funktioniert
claude -p "Antworte NUR mit FUNKTIONIERT" --dangerously-skip-permissions 2>&1 | head -3

# 4. Netzwerk
ping -c 1 -t 5 api.anthropic.com 2>&1 | head -2

# 5. Task-Dateien vorhanden
ls ~/nachtschicht-tasks/*.md

# 6. Google APIs (falls benötigt)
python3 -c "from google.oauth2 import service_account; print('OK')"
```

**BLOCKER wenn:**
- Strom NICHT angeschlossen → the Owner auffordern
- Claude `-p` Mode funktioniert nicht → Debuggen
- Kein Netzwerk → Abbrechen

### Phase 4: Nachtschicht starten

```bash
# 1. Sleep deaktivieren (braucht sudo — the Owner muss Passwort eingeben)
# NUR wenn nicht bereits deaktiviert
pmset -g | grep "disablesleep"
# Falls nicht 1: the Owner auffordern: sudo pmset disablesleep 1 && sudo pmset -a sleep 0 && sudo pmset -a hibernatemode 0 && sudo pmset -a standby 0

# 2. Nachtschicht starten (OHNE sudo!)
bash ~/nachtschicht-start.sh

# 3. Verifizieren
tmux list-sessions
sleep 10 && ps aux | grep "claude -p" | grep -v grep | wc -l
```

### Phase 5: Verifizierung

Bestätige dass:
- [ ] tmux Session "nachtschicht" läuft
- [ ] Alle N Claude-Prozesse aktiv sind (N = Anzahl Tasks)
- [ ] Sleep deaktiviert
- [ ] Strom angeschlossen

Dann sage the Owner: **"Nachtschicht läuft. X Agenten aktiv. Strom dran lassen, Lid zu, gute Nacht."**

### Phase 6: Morning Report (nächste Konversation)

Wenn the Owner morgens fragt was passiert ist:

1. **Report lesen:**
```bash
cat ~/nachtschicht-results/latest/summary.md
```

2. **HTML Report starten:**
```bash
python3 -m http.server 9999 -d ~/nachtschicht-results/latest/
# → http://localhost:9999/report.html
```

3. **Detaillierte Übersicht** pro Task:
   - Was wurde erstellt (Dateien + Pfade)
   - Status (Erfolgreich/Fehler)
   - Key Findings / Highlights
   - Nächste Schritte
   - Was the Owner entscheiden muss

4. Wenn Tasks Fehler hatten → analysiere warum und schlage Fix vor.

---

## Infrastruktur-Dateien

| Datei | Zweck |
|---|---|
| `~/nachtschicht.sh` | Hauptscript: Startet Claude-Agenten parallel, generiert HTML Report |
| `~/nachtschicht-start.sh` | Starter: tmux + caffeinate (OHNE sudo laufen!) |
| `~/nachtschicht-tasks/*.md` | Task-Dateien (eine pro Agent) |
| `~/nachtschicht-results/latest/` | Symlink zum letzten Run |
| `~/nachtschicht-results/latest/report.html` | Morning Report HTML |

## Wichtige Regeln

1. **NIEMALS `sudo` für nachtschicht-start.sh** — `--dangerously-skip-permissions` blockiert unter root
2. **Sleep-Settings separat** — the Owner gibt einmal `sudo pmset disablesleep 1` ein, danach alles als User
3. **Absolute Pfade in Task-Files** — kein `~`, kein `$HOME`, immer `~/...`
4. **Kontext ist King** — Je mehr Kontext in der Task-Datei, desto besser das Ergebnis. Lieber zu viel als zu wenig.
5. **Parallel recherchieren** — Nutze Explore-Agents parallel beim Task-Sammeln um Zeit zu sparen

## Wöchentlicher System-Upgrade Task

**Jeden Sonntag (oder wenn >7 Tage seit letztem Check):** Automatisch einen `/system-upgrade` Task in die Nachtschicht einplanen.

Prüfe beim Task-Sammeln:
```bash
# Wann war der letzte Upgrade-Check?
cat ~/.claude/projects/[workspace]/memory/project_system_upgrade_log.md | grep "Letzter Check"
```

Wenn >7 Tage her → füge als Task hinzu:
- **Task-Name:** `00-system-upgrade.md` (läuft immer als erstes)
- **Inhalt:** Vollständiger `/system-upgrade` Ablauf (siehe Skill)
- **Output:** Report in `infrastruktur/system-upgrades/YYYY-MM-DD-upgrade-report.md`

Wenn the Owner die Nachtschicht startet und der letzte Check >7 Tage her ist, **proaktiv vorschlagen:**
"Letzter System-Upgrade ist X Tage her — soll ich den heute Nacht mitlaufen lassen?"
