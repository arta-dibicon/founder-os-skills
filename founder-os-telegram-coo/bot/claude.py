"""Claude-API-Wrapper für den Bot. Lädt Identity + Context aus Workspace."""

import os
from pathlib import Path

from anthropic import AsyncAnthropic

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-7")
MAX_TOKENS = 2048


class ClaudeWrapper:
    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        self.history = []

    def _system_prompt(self) -> str:
        """Lädt die wichtigsten Rules aus dem Workspace."""
        parts = []
        rules_dir = self.workspace / ".claude" / "rules"

        # Priority files
        for name in ["coo-identity.md", "owner-profile.md", "business-context.md", "anti-ai-voice.md"]:
            f = rules_dir / name
            if f.exists():
                parts.append(f"# {name}\n\n{f.read_text()}")

        if not parts:
            parts.append("Du bist ein hilfsbereiter COO. Antworte direkt und konkret.")

        # Telegram-specific addendum
        parts.append(
            "\n# Telegram-Kontext\n\n"
            "Du sprichst hier via Telegram-Bot mit dem Owner. "
            "Antworten sollen kurz sein (max 3-4 Sätze normal, mehr nur wenn nötig). "
            "Kein Markdown-Formatting (Bold/Italic), Telegram zeigt das nicht sauber. "
            "Kein Em-Dash. Konkrete Antworten. Wenn du eine Datei im Workspace ändern willst, "
            "sag es dem Owner statt es selbst zu versuchen."
        )

        return "\n\n".join(parts)

    async def respond(self, user_text: str) -> str:
        self.history.append({"role": "user", "content": user_text})

        # Keep last 20 turns
        if len(self.history) > 20:
            self.history = self.history[-20:]

        response = await self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=self._system_prompt(),
            messages=self.history,
        )

        reply = response.content[0].text
        self.history.append({"role": "assistant", "content": reply})
        return reply
