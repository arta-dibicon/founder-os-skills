# Meta Ads Deployer — Kampagnen automatisch live schalten

Nimmt fertige Ad Creatives (Bilder) + Ad Copy (JSON) und deployt eine komplette Kampagne in Meta Ads Manager. Campaign → Ad Set → Ad Creative → Ad — alles automatisch via Marketing API.

---

## WARUM DIESER SKILL EXISTIERT

Die Pipeline endet hier:
```
/ad-creative → Bilder (PNGs)
/ad-copy     → Copy + Struktur (ad-copy.json)
/meta-ads    → LIVE in Meta Ads Manager
```

Kein manuelles Hochladen. Kein Copy-Paste. Kein Ads Manager klicken. Alles über die API.

---

## SAFETY FIRST

### Grundregeln
1. **Ads werden IMMER als PAUSED erstellt** — nie automatisch ACTIVE
2. **Budget-Limit: $50/Tag** Default — höheres Budget nur mit expliziter Bestätigung
3. **Vor dem Deploy: Zusammenfassung zeigen** — the Owner bestätigt bevor API-Calls losgehen
4. **Kein Löschen** — bestehende Kampagnen werden NIE gelöscht oder überschrieben
5. **Dry-Run Modus** verfügbar — zeigt was passieren WÜRDE ohne API-Calls

### Was NIEMALS ohne Rückfrage passiert
- Kampagnen auf ACTIVE setzen
- Budget über $50/Tag
- Bestehende Ads/Kampagnen modifizieren
- Ad Account wechseln

---

## CREDENTIALS

Aus `.env` laden:
```
META_ACCESS_TOKEN     — System User Access Token (EAA...)
META_AD_ACCOUNT_ID    — Ad Account ID (act_XXXXXXXXX)
META_PAGE_ID          — Facebook Page ID
META_PAGE_ACCESS_TOKEN — Page-spezifischer Token
```

### API-Grundlagen
- **Base URL:** `https://graph.facebook.com/v22.0/`
- **Auth:** `?access_token=${META_ACCESS_TOKEN}` als Query-Parameter
- **Method:** POST für Create, GET für Read
- **Response:** JSON mit `id` bei Erfolg, `error` bei Fehler

---

## INPUT ERWARTEN

### Pflicht-Inputs
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **CREATIVES_PATH**: Pfad zu den Ad-Bildern (z.B. "ads/v4-listicle/")
- **AD_COPY_JSON**: Pfad zur ad-copy.json (z.B. "ads/v4-listicle/ad-copy.json")
- **FUNNEL_URL**: Ziel-URL der Landing Page

### Optionale Inputs
- **CAMPAIGN_NAME**: Name der Kampagne (Default: "[Produkt] — [Funnel] — [Datum]")
- **DAILY_BUDGET**: Tagesbudget in Account-Währung (Default: $20)
- **OBJECTIVE**: Campaign Objective (Default: OUTCOME_SALES)
- **OPTIMIZATION_GOAL**: Ad Set Optimization (Default: OFFSITE_CONVERSIONS → PURCHASE)
- **TARGETING**: Targeting-Config (Default: Broad/Advantage+)
- **PIXEL_ID**: Pixel für Conversion-Tracking
- **STATUS**: PAUSED (Default) oder ACTIVE
- **DRY_RUN**: true/false (Default: false)

Falls ad-copy.json nicht existiert → the Owner fragen ob /ad-copy zuerst laufen soll.

---

## DEPLOY-FLOW (Reihenfolge KRITISCH)

### Übersicht
```
1. Bilder hochladen → image_hashes
2. Campaign erstellen → campaign_id
3. Ad Set erstellen → adset_id
4. Ad Creatives erstellen (pro Bild) → creative_ids[]
5. Ads erstellen (verknüpft Creative + Ad Set) → ad_ids[]
6. Zusammenfassung + Links
```

### Step 1: Bilder hochladen

Jedes Bild muss als `image_hash` in Meta's Bildbibliothek liegen.

```bash
# Pro Bild:
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/adimages" \
  -F "filename=@[BILD_PFAD]" \
  -F "access_token=${META_ACCESS_TOKEN}"
```

**Response:**
```json
{
  "images": {
    "filename.png": {
      "hash": "abc123...",
      "url": "https://..."
    }
  }
}
```

→ `image_hash` speichern pro Bild. Wird für Ad Creative gebraucht.

### Step 2: Campaign erstellen

```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/campaigns" \
  -d "name=[CAMPAIGN_NAME]" \
  -d "objective=OUTCOME_SALES" \
  -d "status=PAUSED" \
  -d "special_ad_categories=[]" \
  -d "access_token=${META_ACCESS_TOKEN}"
```

**Objectives (ODAX — nur diese funktionieren):**
- `OUTCOME_AWARENESS` — Reichweite
- `OUTCOME_TRAFFIC` — Link-Klicks
- `OUTCOME_ENGAGEMENT` — Interaktion
- `OUTCOME_LEADS` — Lead-Generierung
- `OUTCOME_SALES` — Conversions/Käufe ← **Default für eCommerce**
- `OUTCOME_APP_PROMOTION` — App-Installs

**CBO (Campaign Budget Optimization):**
```
-d "daily_budget=[BETRAG_IN_CENTS]"    # z.B. 2000 = $20/Tag
-d "bid_strategy=LOWEST_COST_WITHOUT_CAP"
```

### Step 3: Ad Set erstellen

```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/adsets" \
  -d "name=[ADSET_NAME]" \
  -d "campaign_id=[CAMPAIGN_ID]" \
  -d "status=PAUSED" \
  -d "billing_event=IMPRESSIONS" \
  -d "optimization_goal=OFFSITE_CONVERSIONS" \
  -d "promoted_object={\"pixel_id\":\"[PIXEL_ID]\",\"custom_event_type\":\"PURCHASE\"}" \
  -d "targeting={\"geo_locations\":{\"countries\":[\"DE\"]},\"age_min\":18,\"age_max\":65}" \
  -d "access_token=${META_ACCESS_TOKEN}"
```

**Targeting-Templates:**

**Broad (Advantage+ / Empfohlen):**
```json
{
  "geo_locations": {"countries": ["DE"]},
  "age_min": 18,
  "age_max": 65
}
```
→ Meta Advantage+ findet die richtige Zielgruppe. Keine Interessen, keine Lookalikes. Broad ist Post-Andromeda der Standard.

**DACH:**
```json
{
  "geo_locations": {"countries": ["DE", "AT", "CH"]},
  "age_min": 25,
  "age_max": 55
}
```

**Attribution Settings:**
```
-d "attribution_spec=[{\"event_type\":\"CLICK_THROUGH\",\"window_days\":7},{\"event_type\":\"VIEW_THROUGH\",\"window_days\":1}]"
```

### Step 4: Ad Creatives erstellen

Pro Bild ein Creative:

```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/adcreatives" \
  -d "name=[CREATIVE_NAME]" \
  -d 'object_story_spec={
    "page_id": "[META_PAGE_ID]",
    "link_data": {
      "image_hash": "[IMAGE_HASH]",
      "link": "[FUNNEL_URL]",
      "message": "[PRIMARY_TEXT]",
      "name": "[HEADLINE]",
      "description": "[DESCRIPTION]",
      "call_to_action": {
        "type": "LEARN_MORE",
        "value": {"link": "[FUNNEL_URL]"}
      }
    }
  }' \
  -d "access_token=${META_ACCESS_TOKEN}"
```

**Für Flexible Ads (mehrere Text-Varianten):**
```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/adcreatives" \
  -d "name=[CREATIVE_NAME]" \
  -d 'asset_feed_spec={
    "images": [{"hash": "[IMAGE_HASH]"}],
    "bodies": [
      {"text": "[PRIMARY_TEXT_1]"},
      {"text": "[PRIMARY_TEXT_2]"},
      {"text": "[PRIMARY_TEXT_3]"},
      {"text": "[PRIMARY_TEXT_4]"},
      {"text": "[PRIMARY_TEXT_5]"}
    ],
    "titles": [
      {"text": "[HEADLINE_1]"},
      {"text": "[HEADLINE_2]"},
      {"text": "[HEADLINE_3]"},
      {"text": "[HEADLINE_4]"},
      {"text": "[HEADLINE_5]"}
    ],
    "descriptions": [
      {"text": "[DESCRIPTION_1]"},
      {"text": "[DESCRIPTION_2]"},
      {"text": "[DESCRIPTION_3]"},
      {"text": "[DESCRIPTION_4]"},
      {"text": "[DESCRIPTION_5]"}
    ],
    "call_to_action_types": ["LEARN_MORE"],
    "link_urls": [{"website_url": "[FUNNEL_URL]"}]
  }' \
  -d 'object_story_spec={"page_id": "[META_PAGE_ID]"}' \
  -d "access_token=${META_ACCESS_TOKEN}"
```

**Advantage+ Creative Enhancements (ALLE AUS):**
```
-d 'degrees_of_freedom_spec={
  "creative_features_spec": {
    "standard_enhancements": {"enroll_status": "OPT_OUT"},
    "image_uncrop": {"enroll_status": "OPT_OUT"},
    "image_touchups": {"enroll_status": "OPT_OUT"},
    "text_optimizations": {"enroll_status": "OPT_OUT"},
    "adapt_to_placement": {"enroll_status": "OPT_OUT"}
  }
}'
```

### Step 5: Ads erstellen

Pro Creative eine Ad (verknüpft Creative mit Ad Set):

```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/${META_AD_ACCOUNT_ID}/ads" \
  -d "name=[AD_NAME]" \
  -d "adset_id=[ADSET_ID]" \
  -d "creative={\"creative_id\":\"[CREATIVE_ID]\"}" \
  -d "status=PAUSED" \
  -d "access_token=${META_ACCESS_TOKEN}"
```

### Step 6: UTM-Parameter

Jede Ad bekommt eigene UTM-Parameter für Tracking:
```
?utm_source=facebook&utm_medium=paid&utm_campaign=[campaign_name]&utm_content=[ad_id]
```

Wird an die Funnel-URL angehängt.

---

## KAMPAGNEN-STRUKTUREN

### Struktur A: Single Ad Set (Einfach, für Test-Runs)
```
Campaign (CBO, $20-50/Tag)
└── Ad Set (Broad Targeting DE)
    ├── Ad 1 (Creative 1 + Copy)
    ├── Ad 2 (Creative 2 + Copy)
    ├── ...
    └── Ad 23 (Creative 23 + Copy)
```
- Alle Ads in einem Ad Set
- Meta verteilt Budget automatisch
- Gut für erste Tests

### Struktur B: Multi Ad Set (Post-Andromeda, empfohlen)
```
Campaign (CBO, $50-100/Tag)
├── Ad Set 1: "Foto Ads" (Broad DE)
│   ├── Ad 01-04 (Foto+Overlay)
│   └── Ad 11-16 (Foto+Overlay)
├── Ad Set 2: "Chat & Social" (Broad DE)
│   ├── Ad 05-07 (WhatsApp)
│   ├── Ad 08-09 (Notifications)
│   └── Ad 22 (Testimonial)
└── Ad Set 3: "Editorial & Humor" (Broad DE)
    ├── Ad 13-14 (Checklisten)
    ├── Ad 17 (Kosten-Vergleich)
    ├── Ad 18-19 (Memes)
    ├── Ad 20-21 (Breaking News)
    └── Ad 23 (Frage)
```
- Gruppiert nach Creative-Typ
- Meta optimiert innerhalb und zwischen Ad Sets
- Bessere Learnings welcher Format-Typ performt

### Struktur C: ABO (Ad Set Budget, für Kontrolle)
```
Campaign (kein CBO)
├── Ad Set 1: $15/Tag — Top Concepts
│   └── 5-8 beste Ads
├── Ad Set 2: $10/Tag — Test Concepts
│   └── 5-8 experimentelle Ads
└── Ad Set 3: $10/Tag — Wild Cards
    └── 5-8 ungewöhnliche Ads
```

**Default: Struktur A** für erste Tests. the Owner kann Struktur wählen.

---

## ABLAUF (Step by Step)

### Step 0: Inputs + Validierung
1. Credentials aus .env laden
2. ad-copy.json laden und validieren
3. Alle Bilder im Creatives-Ordner vorhanden?
4. Funnel-URL erreichbar? (Quick HTTP Check)
5. **the Owner die Deploy-Zusammenfassung zeigen:**

```
📋 DEPLOY-PLAN
━━━━━━━━━━━━━
Campaign:    [Name]
Objective:   OUTCOME_SALES
Budget:      $[X]/Tag (CBO)
Structure:   [A/B/C]
Ad Account:  [Name] ([ID])
Page:        [Name] ([ID])
Targeting:   Broad DE (18-65)
Ads:         [X] Creatives
Funnel URL:  [URL]
Status:      PAUSED
Pixel:       [Name] ([ID])

⚠️  Bestätige mit "Go" um zu deployen.
```

### Step 1: Bilder hochladen
- Alle PNGs aus dem Creatives-Ordner hochladen
- image_hash pro Bild speichern
- Progress: "Bild X/23 hochgeladen ✓"
- **Bei Fehler: stoppen, nicht weitermachen**

### Step 2: Campaign erstellen
- Name, Objective, Budget, Status=PAUSED
- Campaign ID speichern

### Step 3: Ad Set(s) erstellen
- Je nach gewählter Struktur (A/B/C)
- Targeting, Optimization, Attribution
- Ad Set ID(s) speichern

### Step 4: Ad Creatives erstellen
- Pro Bild ein Creative mit Copy aus ad-copy.json
- Flexible Ads: 5× Primary Text + 5× Headline + 5× Description
- Advantage+ Enhancements: ALLE AUS
- Creative IDs speichern

### Step 5: Ads erstellen
- Pro Creative eine Ad im richtigen Ad Set
- Status: PAUSED
- Ad IDs speichern

### Step 6: Verifizierung + Report
1. Alle erstellten Objekte per GET-Request prüfen
2. **Deploy-Report erstellen:**

```
✅ DEPLOY ERFOLGREICH
━━━━━━━━━━━━━━━━━━━
Campaign:   [Name] (ID: [X])
Ad Sets:    [X] erstellt
Creatives:  [X] erstellt
Ads:        [X] erstellt (PAUSED)
Budget:     $[X]/Tag

🔗 Ads Manager: https://www.facebook.com/adsmanager/manage/campaigns?act=[ACCOUNT_ID]

⚠️  Alle Ads sind PAUSED.
    Zum Aktivieren: "Aktiviere die Kampagne" sagen
    oder im Ads Manager manuell auf ACTIVE setzen.
```

3. **Deploy-Log speichern:**
```
[projekt]/ads/[creatives_path]/deploy-log.json
```

---

## DEPLOY-LOG FORMAT

```json
{
  "deployed_at": "2026-04-08T18:30:00Z",
  "ad_account": "act_1050201929851426",
  "page_id": "682221861652372",
  "campaign": {
    "id": "123456789",
    "name": "[Name]",
    "objective": "OUTCOME_SALES",
    "daily_budget": 2000,
    "status": "PAUSED"
  },
  "ad_sets": [
    {
      "id": "234567890",
      "name": "[Name]",
      "targeting": {"countries": ["DE"]},
      "optimization_goal": "OFFSITE_CONVERSIONS"
    }
  ],
  "ads": [
    {
      "id": "345678901",
      "name": "[Name]",
      "creative_id": "456789012",
      "image_hash": "abc123",
      "image_file": "ad-01-kerzenschein-vater.png",
      "status": "PAUSED"
    }
  ]
}
```

---

## POST-DEPLOY AKTIONEN

### Kampagne aktivieren
```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/[CAMPAIGN_ID]" \
  -d "status=ACTIVE" \
  -d "access_token=${META_ACCESS_TOKEN}"
```

### Einzelne Ads aktivieren/pausieren
```bash
curl -s -X POST \
  "https://graph.facebook.com/v22.0/[AD_ID]" \
  -d "status=ACTIVE" \
  -d "access_token=${META_ACCESS_TOKEN}"
```

### Performance lesen (nach 24-48h)
```bash
curl -s "https://graph.facebook.com/v22.0/[CAMPAIGN_ID]/insights?fields=impressions,clicks,spend,actions,cost_per_action_type,ctr,cpc&time_range={\"since\":\"2026-04-08\",\"until\":\"2026-04-09\"}&access_token=${META_ACCESS_TOKEN}"
```

### Ad-Level Performance
```bash
curl -s "https://graph.facebook.com/v22.0/[ADSET_ID]/insights?fields=ad_id,ad_name,impressions,clicks,spend,actions,ctr,cpc&level=ad&access_token=${META_ACCESS_TOKEN}"
```

---

## REGELN

1. **PAUSED als Default** — NIEMALS automatisch ACTIVE deployen
2. **Budget bestätigen** — über $50/Tag immer Rückfrage
3. **Deploy-Plan zeigen** — the Owner bestätigt vor jedem Deploy
4. **Advantage+ Enhancements AUS** — Meta soll unsere Creatives nicht verändern
5. **Broad Targeting** — Post-Andromeda: keine Interessen, keine Lookalikes
6. **UTM-Parameter** — Jede Ad bekommt eigene utm_content
7. **Deploy-Log** — Immer speichern, immer als JSON
8. **Fehlerbehandlung** — Bei API-Error stoppen, NICHT weitermachen
9. **Keine Löschungen** — bestehende Kampagnen werden NIE gelöscht
10. **Credentials NIE im Output** — Token/IDs nie in Markdown oder HTML zeigen
11. **Incremental** — Nach jedem erfolgreichen API-Call den Stand in deploy-log.json speichern
12. **Dry-Run** — Wenn the Owner "Dry Run" sagt, alle Schritte zeigen ohne API-Calls
