"""OpenAI Whisper Wrapper für Voice-Transkription."""

import os
from pathlib import Path

from openai import AsyncOpenAI

_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))


async def transcribe_voice(audio_path: Path, language: str = "de") -> str:
    """Transkribiert eine Voice-Datei via OpenAI Whisper-1 API."""
    with audio_path.open("rb") as f:
        result = await _client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language,
        )
    return result.text.strip()
