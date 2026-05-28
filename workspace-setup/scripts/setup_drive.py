#!/usr/bin/env python3
"""Create Shared Drive + folder structure + grant organizer access.

Env vars:
  WS_SA_KEY         — service account JSON key path
  WS_IMPERSONATE    — admin to impersonate
  WS_DRIVE_NAME     — Shared Drive name (e.g. "[brand]")
  WS_ORGANIZERS     — comma-separated emails to grant organizer role
  WS_FOLDERS_FILE   — path to folder-structure.txt (one folder per line)
"""
import os, ssl, certifi, uuid, pathlib
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY = os.environ["WS_SA_KEY"]
IMPERSONATE = os.environ["WS_IMPERSONATE"]
DRIVE_NAME = os.environ["WS_DRIVE_NAME"]
ORGANIZERS = [e.strip() for e in os.environ.get("WS_ORGANIZERS","").split(",") if e.strip()]
FOLDERS_FILE = os.environ["WS_FOLDERS_FILE"]

creds = service_account.Credentials.from_service_account_file(
    KEY, scopes=["https://www.googleapis.com/auth/drive"], subject=IMPERSONATE
)
drive = build("drive", "v3", credentials=creds)

# 1. Find or create Shared Drive
existing = drive.drives().list(q=f"name='{DRIVE_NAME}'").execute()
if existing.get("drives"):
    drive_id = existing["drives"][0]["id"]
    print(f"⏭  Drive existiert: {drive_id}")
else:
    sd = drive.drives().create(body={"name": DRIVE_NAME}, requestId=str(uuid.uuid4())).execute()
    drive_id = sd["id"]
    print(f"✅ Drive angelegt: {drive_id}")

# 2. Permissions
existing_perms = drive.permissions().list(
    fileId=drive_id, supportsAllDrives=True, fields="permissions(emailAddress,role)"
).execute()
existing_emails = {p.get("emailAddress") for p in existing_perms.get("permissions", [])}
for email in ORGANIZERS:
    if email in existing_emails:
        print(f"⏭  {email}: bereits berechtigt")
        continue
    try:
        drive.permissions().create(
            fileId=drive_id, supportsAllDrives=True, sendNotificationEmail=False,
            body={"type": "user", "role": "organizer", "emailAddress": email}
        ).execute()
        print(f"✅ {email} → organizer")
    except Exception as e:
        print(f"❌ {email}: {str(e)[:150]}")

# 3. Folders
folders = [l.strip() for l in pathlib.Path(FOLDERS_FILE).read_text().splitlines() if l.strip()]
existing_folders = drive.files().list(
    q=f"'{drive_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
    corpora="drive", driveId=drive_id, includeItemsFromAllDrives=True, supportsAllDrives=True,
    fields="files(id,name)"
).execute()
existing_names = {f["name"] for f in existing_folders.get("files", [])}

print(f"\n📁 Ordner in {DRIVE_NAME}:")
for name in folders:
    if name in existing_names:
        print(f"⏭  {name}")
        continue
    drive.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [drive_id]},
        supportsAllDrives=True, fields="id"
    ).execute()
    print(f"✅ {name}")

print(f"\n🎉 Link: https://drive.google.com/drive/folders/{drive_id}")
print(f"   Drive ID: {drive_id}")
