---
name: dream
description: Memory consolidation — bereinigt, komprimiert und dedupliziert alle Memory-Files. Entfernt Duplikate, löst Widersprüche auf, konvertiert relative Daten in absolute und baut den Memory-Index neu auf.
allow_tools: Read, Write, Edit, Glob, Grep, Bash
---

Du führst jetzt einen **Dream-Durchlauf** durch — eine vollständige Memory-Konsolidierung für dieses Projekt.

## Ziel
Das Memory-System soll nach dem Durchlauf:
- Keine Duplikate oder widersprüchlichen Einträge enthalten
- Keine relativen Daten ("nächste Woche", "gestern") — nur absolute Daten
- Keine veralteten oder irrelevanten Einträge
- Einen kompakten Index (MEMORY.md, max 80 Zeilen)
- Jede Memory-File präzise und auf dem neuesten Stand

## Phase 1: Orientierung

1. Lies `MEMORY.md` aus dem Memory-Ordner: `~/.claude/projects/[workspace-id]/memory/MEMORY.md`
2. Lies alle Memory-Files in diesem Ordner
3. Lies die letzten **5 Session-Transcripts** aus: `~/.claude/projects/[workspace-id]/` (JSONL-Files, nach Änderungszeit sortiert, neueste zuerst)
   - Extrahiere daraus: neue wichtige Infos, Korrekturen, Muster, Präferenzen

## Phase 2: Analyse

Identifiziere für jede Memory-File:
- **Duplikate**: Zwei Files die dasselbe sagen
- **Widersprüche**: Zwei Files die sich widersprechen — welche ist aktueller/korrekter?
- **Veraltete Einträge**: Abgeschlossene Projekte, gelöste Probleme, alte Status
- **Relative Daten**: "nächsten Freitag", "letzte Woche" → absolutes Datum ermitteln oder streichen
- **Neue Infos aus Transcripts**: Was sollte in eine bestehende oder neue File?

Erstelle eine Liste der gefundenen Probleme mit Aktionsvorschlag bevor du Änderungen machst.

## Phase 3: Konsolidierung

Führe die Änderungen durch:
- **Zusammenführen**: Zwei Files zu einer mergen wenn sie dasselbe Thema haben
- **Aktualisieren**: Files mit neuen Infos updaten
- **Bereinigen**: Veraltete/irrelevante Files löschen (mit `rm` via Bash)
- **Relative Daten fixieren**: Ersetzen oder streichen
- **Neue Files erstellen**: Nur wenn wirklich nötig und kein passendes File existiert

### Memory-File Format
```markdown
---
name: [name]
description: [einzeilige Beschreibung — wird für Relevanz-Entscheidung genutzt]
type: [user | feedback | project | reference]
---

[Inhalt — bei feedback/project: Regel/Fakt, dann **Why:** und **How to apply:** Zeilen]
```

## Phase 4: Index rebuilden

Schreibe `MEMORY.md` neu:
- Nur Pointer zu bestehenden Files — kein direkter Inhalt
- Format: `- [filename.md](filename.md) — kurze Beschreibung`
- Gruppiert nach Typ: Feedback, Project, Reference, User
- **Max 80 Zeilen** (inkl. Überschriften)
- Endet mit `# currentDate\nToday's date is YYYY-MM-DD.`

## Abschlussbericht

Nach dem Durchlauf: kurze Zusammenfassung was gemacht wurde:
- Anzahl Files vorher/nachher
- Was gemergt/gelöscht/aktualisiert/neu erstellt wurde
- Größte Verbesserungen
