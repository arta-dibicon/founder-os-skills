---
name: workspace-setup
description: Vollständiges Google Workspace Setup — von Zero zu "the COO hat Superadmin-Zugriff auf alles". Erstellt GCP-Projekt, aktiviert APIs, baut Service Account mit Domain-Wide Delegation, richtet Shared Drive + Ordner + Chat Spaces ein, testet 8 APIs.
allow_tools: Read, Write, Edit, Bash, Glob, Grep
---

# Workspace Setup — End-to-End

Du automatisierst jetzt das komplette Google Workspace Setup für ein neues Projekt. Ziel: the COO hat volle programmatische Kontrolle über Drive, Gmail, Calendar, Chat, Sheets, Docs, Admin SDK, YouTube.

## Voraussetzungen (vor Start prüfen)

Frag the Owner kurz ab (falls nicht im Prompt):
1. **Projektname** (z.B. "[brand]") → wird Slug: `[brand]`
2. **Domain** (z.B. `example.com`) — muss auf Google Workspace liegen (MX auf google)
3. **Super Admin E-Mail** (z.B. `arta@example.com`) — Account mit Super-Admin-Rolle, wird Impersonation-Subject
4. **Organization ID** (aus https://console.cloud.google.com/iam-admin/settings — "Resource ID") falls schon vorhanden, sonst beim ersten GCP-Project-Erstellen anzeigen lassen
5. **Projektordner** auf Disk (z.B. `~/workspace/[project]/`)

## Phasenplan

### Phase 1 — GCP Projekt + APIs (5 Min)

```bash
# Projekt erstellen (the Owner muss ggf. ToS in console.cloud.google.com akzeptieren falls erster Kauf)
PROJECT_ID="{slug}-prod"
ORG_ID="{org_id}"
gcloud projects create $PROJECT_ID --organization=$ORG_ID --name="{name}"
gcloud config set project $PROJECT_ID

# Billing verknüpfen (manuell — Billing Account muss existieren)
# → https://console.cloud.google.com/billing/linkedaccount?project=$PROJECT_ID

# APIs aktivieren (in 2 Batches à max 20, Limit ist 20)
gcloud services enable \
  drive.googleapis.com gmail.googleapis.com calendar-json.googleapis.com \
  chat.googleapis.com docs.googleapis.com sheets.googleapis.com \
  slides.googleapis.com forms.googleapis.com script.googleapis.com \
  admin.googleapis.com youtube.googleapis.com \
  youtubeanalytics.googleapis.com people.googleapis.com \
  tasks.googleapis.com webmasters.googleapis.com \
  analytics.googleapis.com analyticsreporting.googleapis.com \
  mybusinessbusinessinformation.googleapis.com iam.googleapis.com
gcloud services enable \
  iamcredentials.googleapis.com orgpolicy.googleapis.com \
  cloudresourcemanager.googleapis.com meet.googleapis.com
```

### Phase 2 — Org Policy Override (Service-Account-Key erlauben)

**Stolperfalle:** Viele Orgs haben `iam.disableServiceAccountKeyCreation` als enforced Policy. Muss auf Projektebene gekippt werden.

```bash
# the Owner braucht roles/orgpolicy.policyAdmin auf der Organisation
gcloud organizations add-iam-policy-binding $ORG_ID \
  --member="user:{admin_email}" \
  --role="roles/orgpolicy.policyAdmin"

# Policy-Override schreiben
cat > /tmp/disable-sa-key.yaml <<EOF
name: projects/$PROJECT_ID/policies/iam.disableServiceAccountKeyCreation
spec:
  inheritFromParent: false
  rules:
    - enforce: false
EOF

gcloud org-policies set-policy /tmp/disable-sa-key.yaml
```

### Phase 3 — Service Account + JSON Key

```bash
SA_NAME="charles-jarvis"
SA_EMAIL="$SA_NAME@$PROJECT_ID.iam.gserviceaccount.com"

gcloud iam service-accounts create $SA_NAME \
  --display-name="the COO — $PROJECT_ID COO Agent"

# Project Owner Rolle (damit the COO in GCP auch alles kann)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/owner"

# JSON Key erstellen
mkdir -p "{project_folder}/.keys"
chmod 700 "{project_folder}/.keys"
gcloud iam service-accounts keys create \
  "{project_folder}/.keys/charles-jarvis.json" \
  --iam-account=$SA_EMAIL
chmod 600 "{project_folder}/.keys/charles-jarvis.json"

# Client-ID (numerisch, brauchen wir für DWD)
gcloud iam service-accounts describe $SA_EMAIL --format="value(uniqueId)"
```

### Phase 4 — Domain-Wide Delegation (MANUELLER SCHRITT)

Das geht nicht per CLI. the Owner muss:

1. **Direktlink öffnen:** https://admin.google.com/ac/owl/domainwidedelegation
2. Klick **"API-Clients hinzufügen"**
3. **Client-ID** einfügen (aus Phase 3 `uniqueId`)
4. **OAuth Scopes:** Inhalt von `templates/dwd-scopes.txt` in Clipboard kopieren (`pbcopy < templates/dwd-scopes.txt`), dann in das Scope-Feld pasten
5. **Authorize** klicken

Die Scope-Liste enthält: drive, gmail (modify/send/readonly/settings), calendar, **chat (inkl. spaces.create!)**, docs, sheets, presentations, forms, script.projects, youtube (+upload/analytics), admin.directory (user/group/orgunit), webmasters, analytics, business.manage, contacts, tasks, meetings.space.

**Kritisch:** `chat.spaces.create` ist ein eigener Scope neben `chat.spaces` — beide nötig für `spaces().create()`. War bei [brand] ein Stolperstein.

### Phase 5 — Chat App Konfiguration (MANUELLER SCHRITT)

**Direktlink:** `https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat?project={PROJECT_ID}`
→ Tab **Configuration**

Werte:
| Feld | Wert |
|---|---|
| App-Name | `the COO` |
| Avatar-URL | `https://www.gstatic.com/images/branding/product/2x/chat_2020q4_48dp.png` (platzhalter) |
| Beschreibung | `{project_name} — virtueller COO für Automation, Reporting und Ops.` |
| Interaktive Features | ✅ AN |
| Funktionalität | ✅ 1:1-Nachrichten, ✅ Bereiche/Gruppen |
| Verbindung | HTTPS-Endpoint: `https://charles-jarvis.placeholder.{domain}/chat` (dummy — echter Handler später wenn Bot-Interaktivität gebraucht) |
| Sichtbarkeit | Bestimmte Personen: alle Workspace-Admin-User eintragen |

### Phase 6 — Automatisiertes Setup (Scripts)

Kopiere `scripts/` aus dem Skill in `{project_folder}/scripts/`:
- `test_access.py` — testet 8 APIs (Drive, Gmail, Calendar, Chat, YouTube, Sheets, Docs, Admin)
- `setup_drive.py` — Shared Drive + Ordnerstruktur + Berechtigungen
- `setup_chat_spaces.py` — Chat Spaces + Member

**Vor Ausführung:** in jedem Script Pfad `KEY` und `IMPERSONATE` auf Projekt anpassen (oder über env vars `{SLUG}_SA_KEY` / `{SLUG}_IMPERSONATE`).

Frag the Owner nach **Ordnerstruktur** (default aus `templates/folder-structure.txt` — im [brand]-Stil nummeriert 00-10) und **Chat-Space-Namen** (default aus `templates/chat-spaces.txt` — general/content/shop-ads/ebooks/community/ops mit Projekt-Präfix).

```bash
cd {project_folder}
python3 scripts/test_access.py       # 8/8 APIs müssen grün sein, sonst debuggen
python3 scripts/setup_drive.py       # Drive + 11 Ordner
python3 scripts/setup_chat_spaces.py # 6 Spaces + Member
```

### Phase 7 — Env Vars + Memory

Füge in `~/.zshrc` hinzu:
```bash
export {SLUG_UPPER}_SA_KEY="$HOME~/workspace/{project-folder}/.keys/charles-jarvis.json"
export {SLUG_UPPER}_IMPERSONATE="{admin_email}"
export {SLUG_UPPER}_GCP_PROJECT="{project_id}"
```

Erstelle Memory-Files:
1. `reference_{slug}_service_account.md` — SA-Email, Client-ID, GCP-Projekt-Nummer, Org-ID, JSON-Key-Pfad, Impersonate, Chat-App-Status, Space-IDs, bekannte Besonderheiten
2. Update `project_{slug}.md` (falls existiert) mit neuem Block "Infrastruktur ✅"
3. Update `MEMORY.md` Index
4. Update `.claude/rules/business-context.md` falls neues Projekt

### Phase 8 — Validierung + Handoff

Schicke Testnachricht in `{project}-general` via Chat API. Zeige the Owner:
- Drive-Link: `https://drive.google.com/drive/folders/{drive_id}`
- Alle Space-IDs
- Test-Suite-Ergebnis (8/8 grün)

## Bekannte Stolpersteine (aus [brand]-Lessons)

1. **GCP ToS nicht akzeptiert** → the Owner muss einmal https://console.cloud.google.com öffnen und durchklicken, bevor CLI-Commands greifen
2. **Org Policy inheritance** → `inheritFromParent: false` ist Pflicht, sonst greift die Org-Enforcement trotz Projekt-Override
3. **API Enable Batch-Limit** → max 20 APIs pro `gcloud services enable`, in 2 Batches splitten
4. **`chat.spaces.create` separat** → nicht mit `chat.spaces` verwechseln, beide nötig
5. **Chat Delete** → `chat.spaces.delete` ist nicht Standard-Scope — Test-Spaces manuell im UI löschen oder Scope nachträglich granten
6. **YouTube-Kanal muss existieren** → Test schlägt fehl bis arta@... oder impersonated User einen Kanal hat. Bei Migration von Alt-Accounts: prüfen ob YT-Channel schon unter Alt-Email liegt, ggf. auf Brand Account umhängen
7. **SSL Certs** → Scripts MÜSSEN `ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())` nutzen, sonst SSL-Fails auf macOS
8. **DWD-Autorisierung wirkt ~1 Min** — nach Save in Admin Console kurz warten vor Tests

## Templates

- `templates/dwd-scopes.txt` — komma-separierte Scope-Liste für Admin-Console-Paste
- `templates/folder-structure.txt` — Shared-Drive-Default-Ordner (editierbar)
- `templates/chat-spaces.txt` — Default Chat-Spaces mit Beschreibungen (editierbar)

## Output

Nach erfolgreichem Run zeigst du the Owner einen Handoff-Block:

```
✅ Workspace Setup {name} komplett
→ Drive: https://drive.google.com/drive/folders/{drive_id}
→ Spaces: 6 angelegt, Member drin
→ APIs: 8/8 grün
→ Service Account: charles-jarvis@{project_id}.iam.gserviceaccount.com
→ Memory aktualisiert, env vars in ~/.zshrc
→ Offen: [YT-Kanal-Setup / Chat-App-Avatar / ...]
```
