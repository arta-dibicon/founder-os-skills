#!/usr/bin/env python3
"""Test the COO access to a Google Workspace.

Env vars required:
  WS_SA_KEY        — path to service account JSON key
  WS_IMPERSONATE   — admin email to impersonate (e.g. arta@example.com)
  WS_DOMAIN        — workspace domain (optional; defaults to impersonate domain)
"""
import os, ssl, certifi, sys
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

from google.oauth2 import service_account
from googleapiclient.discovery import build

KEY = os.environ["WS_SA_KEY"]
IMPERSONATE = os.environ["WS_IMPERSONATE"]
DOMAIN = os.environ.get("WS_DOMAIN", IMPERSONATE.split("@")[1])

tests = []

def check(name, fn):
    try:
        print(f"✅ {name}: {fn()}")
        tests.append((name, "✅"))
    except Exception as e:
        print(f"❌ {name}: {str(e)[:200]}")
        tests.append((name, "❌"))

def creds(scopes):
    return service_account.Credentials.from_service_account_file(KEY, scopes=scopes, subject=IMPERSONATE)

def test_drive():
    svc = build("drive", "v3", credentials=creds(["https://www.googleapis.com/auth/drive"]))
    return f"user={svc.about().get(fields='user').execute()['user']['emailAddress']}"

def test_gmail():
    svc = build("gmail", "v1", credentials=creds(["https://www.googleapis.com/auth/gmail.readonly"]))
    p = svc.users().getProfile(userId="me").execute()
    return f"{p['emailAddress']}, msgs={p.get('messagesTotal',0)}"

def test_calendar():
    svc = build("calendar", "v3", credentials=creds(["https://www.googleapis.com/auth/calendar"]))
    return f"{len(svc.calendarList().list(maxResults=5).execute().get('items',[]))} calendars"

def test_chat():
    svc = build("chat", "v1", credentials=creds(["https://www.googleapis.com/auth/chat.spaces"]))
    return f"{len(svc.spaces().list(pageSize=5).execute().get('spaces',[]))} spaces"

def test_youtube():
    svc = build("youtube", "v3", credentials=creds(["https://www.googleapis.com/auth/youtube"]))
    r = svc.search().list(part="snippet", q="test", maxResults=1, type="video").execute()
    return f"API reachable, {len(r.get('items',[]))} hits"

def test_sheets():
    svc = build("sheets", "v4", credentials=creds(["https://www.googleapis.com/auth/spreadsheets"]))
    sid = svc.spreadsheets().create(body={"properties":{"title":"ws-setup-test"}}).execute()["spreadsheetId"]
    build("drive", "v3", credentials=creds(["https://www.googleapis.com/auth/drive"])).files().delete(fileId=sid).execute()
    return "create+delete ok"

def test_docs():
    svc = build("docs", "v1", credentials=creds(["https://www.googleapis.com/auth/documents"]))
    did = svc.documents().create(body={"title":"ws-setup-test"}).execute()["documentId"]
    build("drive", "v3", credentials=creds(["https://www.googleapis.com/auth/drive"])).files().delete(fileId=did).execute()
    return "create+delete ok"

def test_admin():
    svc = build("admin", "directory_v1", credentials=creds(["https://www.googleapis.com/auth/admin.directory.user"]))
    return f"{len(svc.users().list(domain=DOMAIN, maxResults=10).execute().get('users',[]))} users in {DOMAIN}"

check("Drive",    test_drive)
check("Gmail",    test_gmail)
check("Calendar", test_calendar)
check("Chat",     test_chat)
check("YouTube",  test_youtube)
check("Sheets",   test_sheets)
check("Docs",     test_docs)
check("Admin",    test_admin)

failed = [t for t in tests if t[1] == "❌"]
print(f"\n{'='*50}\nResults: {len(tests)-len(failed)}/{len(tests)} passed")
sys.exit(1 if failed else 0)
