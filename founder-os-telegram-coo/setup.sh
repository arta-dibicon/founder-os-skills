#!/usr/bin/env bash
# founder-os-telegram-coo Setup-Script
# Wird vom COO ausgeführt in Phase C des Onboarding-Flows.
# Voraussetzung: TELEGRAM_BOT_TOKEN als ENV oder in ~/.env.founderos
#
# Was es macht:
# 1. Lädt Token + Keys aus ~/.env.founderos
# 2. Installiert Python-Deps falls fehlen (aiogram, anthropic, openai)
# 3. Schreibt .env.telegram (chmod 600)
# 4. Erzeugt systemd-Unit founderos-telegram-bot.service
# 5. Startet Service und prüft Health

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT_DIR="${SKILL_DIR}/bot"
HOME_ENV="${HOME}/.env.founderos"

echo "[telegram-coo] Setup gestartet..."

# Lade ENV
if [[ -f "${HOME_ENV}" ]]; then
  set -a
  source "${HOME_ENV}"
  set +a
fi

# Token-Check
if [[ -z "${TELEGRAM_BOT_TOKEN:-}" ]]; then
  echo "ERROR: TELEGRAM_BOT_TOKEN fehlt. Entweder als ENV setzen oder in ~/.env.founderos."
  exit 1
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
  echo "ERROR: ANTHROPIC_API_KEY fehlt in ~/.env.founderos."
  exit 1
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "WARN: OPENAI_API_KEY fehlt. Voice-Transkription geht nicht. Setup läuft trotzdem weiter."
fi

# Python-Deps
echo "[telegram-coo] Python-Deps prüfen..."
pip3 install --break-system-packages --quiet aiogram openai anthropic python-dotenv 2>&1 | tail -3

# Erstelle Bot-Verzeichnis im Home
INSTALL_DIR="${HOME}/founderos-telegram-bot"
mkdir -p "${INSTALL_DIR}"
cp -R "${BOT_DIR}"/* "${INSTALL_DIR}/"

# Schreibe .env.telegram
cat > "${INSTALL_DIR}/.env" <<EOF
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
OPENAI_API_KEY=${OPENAI_API_KEY:-}
WORKSPACE_ROOT=${HOME}/workspace
EOF
chmod 600 "${INSTALL_DIR}/.env"

# systemd-Unit
SERVICE_FILE="/etc/systemd/system/founderos-telegram-bot.service"
USER_NAME=$(whoami)

if [[ ! -f "${SERVICE_FILE}" ]]; then
  echo "[telegram-coo] systemd-Unit erstellen..."
  sudo tee "${SERVICE_FILE}" >/dev/null <<EOF
[Unit]
Description=Founder OS Telegram COO Bot
After=network.target

[Service]
Type=simple
User=${USER_NAME}
WorkingDirectory=${INSTALL_DIR}
EnvironmentFile=${INSTALL_DIR}/.env
ExecStart=/usr/bin/python3 ${INSTALL_DIR}/main.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
  sudo systemctl daemon-reload
  sudo systemctl enable founderos-telegram-bot.service
fi

echo "[telegram-coo] Service starten..."
sudo systemctl restart founderos-telegram-bot.service
sleep 3

# Health-Check
if sudo systemctl is-active --quiet founderos-telegram-bot.service; then
  echo "[telegram-coo] ✓ Bot läuft."

  # Bot-Username abfragen
  BOT_INFO=$(curl -s "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getMe" 2>/dev/null || echo "")
  BOT_USERNAME=$(echo "${BOT_INFO}" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('result', {}).get('username', '?'))" 2>/dev/null || echo "?")

  echo ""
  echo "=========================================="
  echo "  Bot deployed"
  echo "=========================================="
  echo "Bot-Username:  @${BOT_USERNAME}"
  echo "Telegram-URL:  https://t.me/${BOT_USERNAME}"
  echo "Service:       founderos-telegram-bot.service"
  echo "Logs:          journalctl -u founderos-telegram-bot.service -f"
  echo ""
  echo "Owner kann jetzt im Telegram nach @${BOT_USERNAME} suchen und /start drücken."
else
  echo "[telegram-coo] ✗ Bot konnte nicht gestartet werden."
  echo "Logs:"
  sudo journalctl -u founderos-telegram-bot.service -n 30 --no-pager
  exit 1
fi
