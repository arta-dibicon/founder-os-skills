#!/usr/bin/env bash
# Bootstrap GCP project + APIs + Service Account + DWD-ready JSON Key.
# Required env vars:
#   WS_PROJECT_ID     — GCP project ID (e.g. [brand]-prod)
#   WS_PROJECT_NAME   — human-readable name (e.g. "[brand]")
#   WS_ORG_ID         — organization ID (numeric)
#   WS_ADMIN_EMAIL    — super admin email (for org policy role)
#   WS_PROJECT_FOLDER — local project folder (for .keys/ destination)
#   WS_BILLING_ACCOUNT — billing account ID (optional, format: 0X0X0X-0X0X0X-0X0X0X)
set -euo pipefail
: "${WS_PROJECT_ID:?}" "${WS_PROJECT_NAME:?}" "${WS_ORG_ID:?}" "${WS_ADMIN_EMAIL:?}" "${WS_PROJECT_FOLDER:?}"

SA_NAME="charles-jarvis"
SA_EMAIL="${SA_NAME}@${WS_PROJECT_ID}.iam.gserviceaccount.com"
KEY_DIR="${WS_PROJECT_FOLDER}/.keys"
KEY_PATH="${KEY_DIR}/charles-jarvis.json"

echo "━━━ Phase 1: GCP Project ━━━"
if gcloud projects describe "$WS_PROJECT_ID" >/dev/null 2>&1; then
  echo "⏭  Projekt existiert: $WS_PROJECT_ID"
else
  gcloud projects create "$WS_PROJECT_ID" --organization="$WS_ORG_ID" --name="$WS_PROJECT_NAME"
  echo "✅ Projekt angelegt"
fi
gcloud config set project "$WS_PROJECT_ID"

if [[ -n "${WS_BILLING_ACCOUNT:-}" ]]; then
  gcloud billing projects link "$WS_PROJECT_ID" --billing-account="$WS_BILLING_ACCOUNT" || echo "⚠️  Billing bereits verlinkt oder Permission fehlt"
fi

echo "━━━ Phase 2: APIs aktivieren ━━━"
gcloud services enable \
  drive.googleapis.com gmail.googleapis.com calendar-json.googleapis.com \
  chat.googleapis.com docs.googleapis.com sheets.googleapis.com \
  slides.googleapis.com forms.googleapis.com script.googleapis.com \
  admin.googleapis.com youtube.googleapis.com youtubeanalytics.googleapis.com \
  people.googleapis.com tasks.googleapis.com webmasters.googleapis.com \
  analytics.googleapis.com analyticsreporting.googleapis.com \
  mybusinessbusinessinformation.googleapis.com iam.googleapis.com \
  iamcredentials.googleapis.com

gcloud services enable \
  orgpolicy.googleapis.com cloudresourcemanager.googleapis.com \
  meet.googleapis.com

echo "━━━ Phase 3: Org Policy Override (SA Key erlauben) ━━━"
gcloud organizations add-iam-policy-binding "$WS_ORG_ID" \
  --member="user:${WS_ADMIN_EMAIL}" \
  --role="roles/orgpolicy.policyAdmin" --condition=None >/dev/null || true

cat > /tmp/ws-disable-sa-key.yaml <<EOF
name: projects/${WS_PROJECT_ID}/policies/iam.disableServiceAccountKeyCreation
spec:
  inheritFromParent: false
  rules:
    - enforce: false
EOF
gcloud org-policies set-policy /tmp/ws-disable-sa-key.yaml || echo "⚠️  Org-Policy-Override failed — vermutlich fehlen Rechte"

echo "━━━ Phase 4: Service Account ━━━"
if gcloud iam service-accounts describe "$SA_EMAIL" >/dev/null 2>&1; then
  echo "⏭  SA existiert: $SA_EMAIL"
else
  gcloud iam service-accounts create "$SA_NAME" \
    --display-name="the COO — ${WS_PROJECT_NAME} COO Agent"
fi

gcloud projects add-iam-policy-binding "$WS_PROJECT_ID" \
  --member="serviceAccount:${SA_EMAIL}" --role="roles/owner" --condition=None >/dev/null

mkdir -p "$KEY_DIR" && chmod 700 "$KEY_DIR"
if [[ -f "$KEY_PATH" ]]; then
  echo "⏭  Key existiert: $KEY_PATH"
else
  gcloud iam service-accounts keys create "$KEY_PATH" --iam-account="$SA_EMAIL"
  chmod 600 "$KEY_PATH"
  echo "✅ Key: $KEY_PATH"
fi

CLIENT_ID=$(gcloud iam service-accounts describe "$SA_EMAIL" --format="value(uniqueId)")

echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ GCP Bootstrap fertig."
echo "SA Email:  $SA_EMAIL"
echo "Client-ID: $CLIENT_ID"
echo "Key:       $KEY_PATH"
echo
echo "▶ Nächster Schritt: DWD autorisieren"
echo "  1. Open: https://admin.google.com/ac/owl/domainwidedelegation"
echo "  2. Add API client → Client-ID: $CLIENT_ID"
echo "  3. Scopes: pbcopy < \$SKILL_DIR/templates/dwd-scopes.txt && paste into scope field"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
