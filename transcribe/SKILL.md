---
name: transcribe
description: Transkribiere ein YouTube-Video oder Web-Video. TRIGGER wenn der User einen YouTube-Link sendet (youtube.com, youtu.be) oder explizit nach Transkription fragt. Auch bei "transkribier das", "was sagt er im Video", oder ähnlichen Anfragen mit Video-URL.
allow_tools: Read, Write, Edit, Bash, Glob, Grep
---

# Transcribe — Video zu Text in Sekunden

Du transkribierst jetzt ein Video. Der gesamte Prozess läuft automatisch ohne Rückfrage.

## Voraussetzungen (bereits installiert)
- `yt-dlp` — Video/Audio Download + Untertitel-Extraktion
- `openai-whisper` — Lokale KI-Transkription (LETZTER Fallback — LANGSAM!)
- `ffmpeg` — Audio-Konvertierung

## Arbeitsverzeichnis
Alle temporären Dateien kommen nach `/tmp/transcribe/`. Am Ende aufräumen.

```bash
mkdir -p /tmp/transcribe && cd /tmp/transcribe
```

## Ablauf

### Phase 1: URL erkennen
- Extrahiere die Video-URL aus der User-Nachricht
- Unterstützte Formate:
  - YouTube: `youtube.com/watch?v=`, `youtu.be/`, `youtube.com/shorts/`
  - Andere Video-URLs: Direkt zu Phase 3 (Whisper)

### Phase 2: Untertitel ziehen (IMMER ZUERST — dauert Sekunden!)

**KRITISCH: Dieser Schritt wird NIEMALS übersprungen bei YouTube-Videos!**
95%+ aller YouTube-Videos haben Auto-Untertitel. Das dauert 2-5 Sekunden statt 30+ Minuten mit Whisper.

```bash
cd /tmp/transcribe

# Schritt 1: Untertitel direkt ziehen (auto-sub + manual, de + en)
yt-dlp --write-sub --write-auto-sub --sub-lang de,en --sub-format vtt --skip-download --no-playlist -o "transcript" "URL" 2>&1
```

**Prüfe das Ergebnis:**
```bash
ls -la /tmp/transcribe/transcript*.vtt 2>/dev/null
```
- Wenn `.vtt` Datei existiert → **DIREKT zu Phase 4** (Cleanup + Ausgabe)
- Wenn KEINE Datei → und NUR DANN → Phase 3 (Whisper)

### Phase 3: Whisper Fallback (NUR wenn Phase 2 komplett fehlgeschlagen)

**ACHTUNG: Whisper ist LANGSAM (10-45 Min für lange Videos). Nur nutzen wenn wirklich KEINE Untertitel verfügbar sind!**

Audio runterladen und lokal transkribieren:

```bash
cd /tmp/transcribe
# Audio extrahieren (nur Audio, kein Video — spart Zeit + Speicher)
yt-dlp -x --audio-format mp3 --audio-quality 5 --no-playlist -o "audio.%(ext)s" "URL" 2>&1

# Mit Whisper transkribieren — IMMER tiny für Speed, Qualität reicht für Inhalt
whisper audio.mp3 --model tiny --output_dir /tmp/transcribe --output_format txt 2>&1
```

**Whisper Modell-Wahl (NUR relevant wenn Phase 2 fehlgeschlagen):**
- Default: `tiny` — schnellstes Modell, reicht für Inhaltsverständnis
- Nur wenn User explizit "perfekte Qualität" will: `small`
- NIEMALS `medium` oder `large` für automatische Transkription — zu langsam

### Phase 4: Cleanup + Ausgabe

**VTT/SRT Cleanup** (Untertitel haben Timestamps + Duplikate):
```bash
# VTT zu sauberem Text: Timestamps entfernen, Duplikat-Zeilen raus
cat transcript.*.vtt 2>/dev/null | grep -v "^WEBVTT" | grep -v "^Kind:" | grep -v "^Language:" | grep -v "^$" | grep -v "^[0-9]" | grep -v "\-\->" | sed 's/<[^>]*>//g' | awk '!seen[$0]++' > clean_transcript.txt
```

**Ausgabe:**
1. Zeige dem User das Transkript direkt in der Antwort (bei < 500 Zeilen)
2. Bei langen Transkripten: Speichere als Datei und frage wo es hin soll
3. Nenne Quelle: Video-Titel + URL + Methode (Subs/Whisper) + Sprache

### Phase 5: Aufräumen
```bash
rm -rf /tmp/transcribe/*
```

## Wichtige Regeln

1. **UNTERTITEL ZUERST — IMMER!** — Whisper ist der LETZTE Ausweg, nicht der Standard. 95% der YouTube-Videos haben Auto-Subs die in Sekunden heruntergeladen werden können.
2. **Keine Rückfragen** — Einfach machen. URL rein → Text raus.
3. **Sprache auto-detecten** — Nicht fragen welche Sprache, erkennt sich von selbst
4. **Video-Titel immer mit ausgeben** — `yt-dlp --get-title "URL"` für Kontext
5. **Bei Fehler: klar sagen was nicht funktioniert** — z.B. "Video ist privat" oder "Geo-blocked"
6. **Temporäre Dateien IMMER aufräumen** — Nichts in /tmp liegen lassen
7. **Speicherort für finales Transkript:** Frag nur wenn User es explizit speichern will. Default: nur in der Antwort anzeigen.
8. **Whisper = NOTFALL** — Wenn du Whisper startest und es länger als 5 Min läuft, erwähne das explizit. Lokales Whisper auf CPU ist extrem langsam bei langen Videos.

## Nicht-YouTube URLs
Für andere Video-URLs (Vimeo, Twitter/X, Instagram, TikTok etc.):
- `yt-dlp` unterstützt 1000+ Seiten — einfach versuchen
- Wenn yt-dlp scheitert: Sag dem User Bescheid, schlage Alternative vor (z.B. Apify Actor)

## Output-Format
```
**📹 [Video-Titel]**
🔗 URL
📝 Methode: YouTube-Untertitel (de) | Whisper (tiny)
---

[Transkript hier]

---
⏱️ Dauer: X Min | 🔤 Wörter: ~X
```
