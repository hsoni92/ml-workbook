"""OpenRouter client and config for LLM tool-calling demo."""

import itertools
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_raw = os.getenv("OPENROUTER_API_KEY") or ""
api_keys = [k.strip() for k in _raw.split(",") if k.strip()]
if not api_keys:
    raise ValueError("OPENROUTER_API_KEY must be set in .env (comma-separated keys for rotation)")

# Round-robin over keys to spread rate limits
_key_cycle = itertools.cycle(api_keys)

model = os.getenv("OPENROUTER_MODEL", "arcee-ai/trinity-large-preview:free")


def _client() -> OpenAI:
    """OpenRouter client using the next key in rotation."""
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=next(_key_cycle),
    )
