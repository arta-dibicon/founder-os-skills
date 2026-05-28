#!/usr/bin/env python3
"""Create Chat Spaces + add members.

Env vars:
  WS_SA_KEY         — service account JSON key
  WS_IMPERSONATE    — admin to impersonate (= space creator)
  WS_SPACES_FILE    — path to chat-spaces.txt (format: name|description per line)
  WS_MEMBERS        — comma-separated member emails (creator auto-skipped)
"""
import os, ssl, certifi, pathlib
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY = os.environ["WS_SA_KEY"]
IMPERSONATE = os.environ["WS_IMPERSONATE"]
SPACES_FILE = os.environ["WS_SPACES_FILE"]
MEMBERS = [e.strip() for e in os.environ.get("WS_MEMBERS","").split(",") if e.strip()]

creds = service_account.Credentials.from_service_account_file(
    KEY,
    scopes=["https://www.googleapis.com/auth/chat.spaces",
            "https://www.googleapis.com/auth/chat.spaces.create",
            "https://www.googleapis.com/auth/chat.memberships"],
    subject=IMPERSONATE
)
chat = build("chat", "v1", credentials=creds)

SPACES = []
for line in pathlib.Path(SPACES_FILE).read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"): continue
    parts = line.split("|", 1)
    SPACES.append((parts[0].strip(), parts[1].strip() if len(parts) > 1 else ""))

existing = {}
try:
    page = None
    while True:
        res = chat.spaces().list(pageSize=1000, pageToken=page).execute()
        for s in res.get("spaces", []):
            existing[s.get("displayName","")] = s["name"]
        page = res.get("nextPageToken")
        if not page: break
except Exception as e:
    print(f"⚠️  List: {str(e)[:200]}")

for name, desc in SPACES:
    if name in existing:
        print(f"⏭  {name}: {existing[name]}")
        space_name = existing[name]
    else:
        try:
            s = chat.spaces().create(body={
                "spaceType": "SPACE", "displayName": name,
                "spaceDetails": {"description": desc},
                "externalUserAllowed": False,
            }).execute()
            space_name = s["name"]
            print(f"✅ {name} → {space_name}")
        except Exception as e:
            print(f"❌ {name}: {str(e)[:200]}")
            continue

    for email in MEMBERS:
        if email == IMPERSONATE: continue
        try:
            chat.spaces().members().create(
                parent=space_name,
                body={"member": {"name": f"users/{email}", "type": "HUMAN"}}
            ).execute()
            print(f"   ➕ {email}")
        except Exception as e:
            msg = str(e)[:200]
            if "ALREADY_EXISTS" in msg or "already" in msg.lower():
                print(f"   ⏭  {email}")
            else:
                print(f"   ❌ {email}: {msg}")

print("\n🎉 Chat Spaces fertig.")
