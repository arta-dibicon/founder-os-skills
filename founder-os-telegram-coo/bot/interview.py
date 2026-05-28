"""Interview-Modus State-Machine. 6 Blöcke, schreibt in owner-profile.md."""

import json
from datetime import datetime
from pathlib import Path

STATE_FILE = Path.home() / ".founderos-interview-state.json"

BLOCKS = [
    {
        "name": "Über dich",
        "questions": [
            "Wie ist dein voller Name, dein Alter, wo du wohnst?",
            "Wer gehört zu deinem engsten Kreis? Partner, Kinder, beste Freunde, Mentor.",
            "Hast du einen operativen Partner im Business?",
        ],
    },
    {
        "name": "Wie du arbeitest",
        "questions": [
            "Wie viele Stunden arbeitest du realistisch pro Woche? Wie ist dein Tagesrhythmus?",
            "Was bringt dich in Flow? Was killt dich aus dem Flow raus?",
            "Wann ist deine produktivste Tageszeit? Wo flaut die Energie ab?",
            "Beschreib mir dein Setup. Hardware, Raum, Stille oder Musik.",
        ],
    },
    {
        "name": "Werte und 10-Jahres-Vision",
        "questions": [
            "An welche 3-5 Leitsätze glaubst du wirklich?",
            "Was ist deine Werte-Hierarchie? Was kommt zuerst, was am Ende?",
            "Was lehnst du klar ab? Was würdest du nie tun?",
            "In zwei Sätzen, wo willst du in 10 Jahren stehen?",
        ],
    },
    {
        "name": "Deine Geschäfte heute",
        "questions": [
            "Welche Ventures hast du aktiv? Bitte für jedes: Name, was es ist, wer beteiligt, Status.",
            "Welches Venture ist dein Hauptbaby? Wo geht der meiste Fokus hin?",
            "Gibt es ein Venture das du gerade abgeben oder pausieren willst?",
            "Was läuft finanziell? Wo bist du heute, wo willst du in 12 Monaten sein?",
        ],
    },
    {
        "name": "Tools im Detail",
        "questions": [
            "Welche Tools nutzt du täglich? Bitte alles was dir einfällt.",
            "Welche Tools sind kritisch? Wo würde dein Business stehenbleiben wenn das ausfällt?",
            "Gibt es Tools die du wechseln willst oder die dich nerven?",
            "Mit welchen VAs, Mitarbeitern oder externen Partnern arbeitest du regelmäßig?",
        ],
    },
    {
        "name": "Brennpunkte",
        "questions": [
            "Was klemmt gerade am meisten? Drei Sachen die dich wach halten.",
            "Wo verlierst du am meisten Zeit auf Sachen die du nicht magst?",
            "Was hast du schon mehrmals versucht zu lösen und es klappt nicht?",
            "Wenn ich dir morgen früh einen Schmerz wegnehmen könnte: welcher?",
        ],
    },
]


class InterviewState:
    def __init__(self, workspace: Path):
        self.workspace = workspace
        self.profile_file = workspace / ".claude" / "rules" / "owner-profile.md"
        self.profile_file.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> dict:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
        return {"block": 0, "q_index": 0, "answers": []}

    def _save(self, state: dict):
        STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))

    def start(self) -> str:
        state = {"block": 0, "q_index": 0, "answers": [], "started_at": datetime.now().isoformat()}
        self._save(state)
        return BLOCKS[0]["questions"][0]

    def current_question(self) -> str:
        state = self._load()
        if state["block"] >= len(BLOCKS):
            return "Interview ist durch."
        return BLOCKS[state["block"]]["questions"][state["q_index"]]

    def progress(self) -> dict:
        state = self._load()
        return {"block": state["block"] + 1, "q_index": state["q_index"] + 1}

    def record_answer(self, text: str) -> dict:
        state = self._load()
        block = BLOCKS[state["block"]]
        question = block["questions"][state["q_index"]]

        state["answers"].append({
            "block": block["name"],
            "question": question,
            "answer": text,
            "ts": datetime.now().isoformat(),
        })

        # Inkrementell speichern in owner-profile.md
        self._append_to_profile(block["name"], question, text)

        # Move to next question
        state["q_index"] += 1
        if state["q_index"] >= len(block["questions"]):
            state["block"] += 1
            state["q_index"] = 0

        # Done?
        if state["block"] >= len(BLOCKS):
            self._save(state)
            return {"done": True}

        self._save(state)
        next_block = BLOCKS[state["block"]]
        return {
            "done": False,
            "block": next_block["name"],
            "block_num": state["block"] + 1,
            "next_question": next_block["questions"][state["q_index"]],
        }

    def _append_to_profile(self, block: str, question: str, answer: str):
        """Inkrementell in owner-profile.md schreiben."""
        if not self.profile_file.exists():
            self.profile_file.write_text(
                "# Owner Profile (vom Telegram-Interview befüllt)\n\n"
            )

        with self.profile_file.open("a", encoding="utf-8") as f:
            f.write(f"\n## {block} — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Frage:** {question}\n\n")
            f.write(f"{answer}\n")
