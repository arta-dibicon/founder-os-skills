#!/usr/bin/env python3
"""
Founder OS Telegram COO Bot
Empfängt Voice + Text, transkribiert via Whisper, antwortet via Claude.

Modi:
- chat (default): COO antwortet wie in Antigravity
- interview: 6-Block-Interview, schreibt in owner-profile.md
"""

import asyncio
import logging
import os
import sys
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

# Load env from script dir
load_dotenv(Path(__file__).parent / ".env")

from claude import ClaudeWrapper
from interview import InterviewState
from whisper import transcribe_voice

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
WORKSPACE = Path(os.environ.get("WORKSPACE_ROOT", str(Path.home() / "workspace")))
ALLOWED_USER_FILE = Path.home() / ".founderos-allowed-user"
MODE_FILE = Path.home() / ".founderos-bot-mode"
VOICE_REPLY_FILE = Path.home() / ".founderos-voice-reply"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("founderos-bot")

bot = Bot(token=TOKEN)
dp = Dispatcher()
claude = ClaudeWrapper(workspace=WORKSPACE)
interview = InterviewState(workspace=WORKSPACE)


def get_allowed_user_id() -> int | None:
    if ALLOWED_USER_FILE.exists():
        try:
            return int(ALLOWED_USER_FILE.read_text().strip())
        except ValueError:
            return None
    return None


def set_allowed_user_id(user_id: int):
    ALLOWED_USER_FILE.write_text(str(user_id))
    ALLOWED_USER_FILE.chmod(0o600)


def get_mode() -> str:
    if MODE_FILE.exists():
        return MODE_FILE.read_text().strip() or "chat"
    return "chat"


def set_mode(mode: str):
    MODE_FILE.write_text(mode)


def is_authorized(message: Message) -> bool:
    allowed = get_allowed_user_id()
    if allowed is None:
        return True  # Erst-Start, nimm den ersten der /start macht
    return message.from_user.id == allowed


@dp.message(Command("start"))
async def cmd_start(message: Message):
    allowed = get_allowed_user_id()
    if allowed is None:
        # Erst-Start
        set_allowed_user_id(message.from_user.id)
        await message.answer(
            "Hi. Ich bin dein neuer COO im Telegram.\n\n"
            "Sprich mit mir wie mit einem Kollegen. Sprachnachricht geht auch.\n\n"
            "Wenn du bereit fürs Interview bist, schreib /interview.\n"
            "Status checken mit /status. Modus wechseln mit /chat oder /interview."
        )
        log.info(f"Erst-Start. User {message.from_user.id} ist jetzt Owner.")
    elif allowed == message.from_user.id:
        await message.answer("Schon connected. Wir können loslegen.")
    else:
        await message.answer("Sorry, dieser Bot ist privat.")
        log.warning(f"Unauthorized /start from {message.from_user.id}")


@dp.message(Command("interview"))
async def cmd_interview(message: Message):
    if not is_authorized(message):
        return
    set_mode("interview")
    first_q = interview.start()
    await message.answer(
        "Interview-Modus an. Ich frage Block 1 von 6: Über dich.\n\n"
        f"Frage 1: {first_q}\n\n"
        "Antworte per Sprachnachricht oder Text."
    )


@dp.message(Command("chat"))
async def cmd_chat(message: Message):
    if not is_authorized(message):
        return
    set_mode("chat")
    await message.answer("Chat-Modus an. Sprich mit mir wie sonst auch.")


@dp.message(Command("status"))
async def cmd_status(message: Message):
    if not is_authorized(message):
        return
    mode = get_mode()
    progress = interview.progress() if mode == "interview" else None
    out = f"Modus: {mode}"
    if progress:
        out += f"\nInterview-Stand: Block {progress['block']}/6, Frage {progress['q_index']}"
    await message.answer(out)


@dp.message(Command("pause"))
async def cmd_pause(message: Message):
    if not is_authorized(message):
        return
    set_mode("chat")
    await message.answer("Interview pausiert. /resume um weiterzumachen.")


@dp.message(Command("resume"))
async def cmd_resume(message: Message):
    if not is_authorized(message):
        return
    set_mode("interview")
    next_q = interview.current_question()
    await message.answer(f"Weiter im Interview.\n\nFrage: {next_q}")


@dp.message(F.voice)
async def handle_voice(message: Message):
    if not is_authorized(message):
        return

    await message.answer("Hör ich mir an...")

    # Download voice
    voice_file = await bot.get_file(message.voice.file_id)
    tmp_dir = Path("/tmp/founderos-voice")
    tmp_dir.mkdir(exist_ok=True)
    local_path = tmp_dir / f"{message.voice.file_id}.ogg"
    await bot.download_file(voice_file.file_path, str(local_path))

    # Transcribe
    try:
        text = await transcribe_voice(local_path)
    except Exception as e:
        log.exception("Whisper-Fehler")
        await message.answer(f"Hat nicht geklappt mit der Transkription: {e}")
        return

    await message.answer(f"Verstanden: \"{text[:200]}{'...' if len(text) > 200 else ''}\"")
    await process_text(message, text)


@dp.message(F.text)
async def handle_text(message: Message):
    if not is_authorized(message):
        return
    if message.text.startswith("/"):
        return  # commands sind oben gehandhabt
    await process_text(message, message.text)


async def process_text(message: Message, text: str):
    mode = get_mode()

    if mode == "interview":
        result = interview.record_answer(text)
        if result.get("done"):
            set_mode("chat")
            await message.answer(
                "Interview ist durch. Ich verarbeite deine Antworten jetzt asynchron, "
                "das siehst du gleich in deinem Workspace unter "
                ".claude/rules/owner-profile.md.\n\n"
                "Ich melde mich wenn der Context-Harvest startet."
            )
            return
        next_q = result["next_question"]
        block = result["block"]
        block_num = result["block_num"]
        await message.answer(f"Block {block_num}/6 – {block}\n\nFrage: {next_q}")
    else:
        try:
            reply = await claude.respond(text)
            await message.answer(reply)
        except Exception as e:
            log.exception("Claude-Fehler")
            await message.answer(f"Claude hat geprustet: {e}")


async def main():
    log.info("Founder OS Telegram Bot startet...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Bot gestoppt.")
        sys.exit(0)
