"""OpenRouter-backed chat via official OpenAI SDK (load from .env)."""

import os
import re
import threading
from typing import TypeVar

from dotenv import load_dotenv
from loguru import logger
from openai import AuthenticationError, OpenAI
from pydantic import BaseModel

# Load .env at module import so keys are available
load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "z-ai/glm-4.5-air:free"

OPENROUTER_401_MESSAGE = (
    "OpenRouter returned 401 (invalid API key). "
    "Check OPENROUTER_API_KEY in .env and ensure your key is valid at https://openrouter.ai/keys"
)


def is_openrouter_auth_error(exc: BaseException) -> bool:
    """True if the exception is an OpenRouter/API 401 auth error (invalid key, user not found)."""
    if isinstance(exc, AuthenticationError):
        return True
    msg = str(exc).lower()
    return "401" in msg or "user not found" in msg


# Comma-separated keys, rotated cyclically for rate-limit handling
_API_KEYS: list[str] = []
_KEY_INDEX = 0
_KEY_LOCK = threading.Lock()


def _load_api_keys() -> list[str]:
    raw = os.getenv("OPENROUTER_API_KEY") or ""
    logger.debug(">> Loading API keys from environment variable: {}", raw[:20] + "..." if len(raw) > 20 else raw)
    keys = [k.strip() for k in raw.split(",") if k.strip()]
    logger.debug(">> Loaded {} API keys", len(keys))
    return keys


def _get_next_key() -> str:
    """Return next API key in round-robin rotation (thread-safe)."""
    global _API_KEYS, _KEY_INDEX
    with _KEY_LOCK:
        if not _API_KEYS:
            _API_KEYS = _load_api_keys()
        if not _API_KEYS:
            raise ValueError(
                "OPENROUTER_API_KEY is not set. Add one or more keys to .env (see .env.example)."
            )
        key = _API_KEYS[_KEY_INDEX % len(_API_KEYS)]
        _KEY_INDEX += 1
        return key


def _default_headers() -> dict[str, str]:
    """Optional OpenRouter ranking headers from env."""
    headers: dict[str, str] = {}
    referer = os.getenv("OPENROUTER_HTTP_REFERER", "").strip()
    if referer:
        headers["HTTP-Referer"] = referer
    title = os.getenv("OPENROUTER_X_TITLE", "").strip()
    if title:
        headers["X-Title"] = title
    return headers


def get_openai_client() -> OpenAI:
    """Return an OpenAI client configured for OpenRouter (rotated API key per call)."""
    logger.debug("get_openai_client called")
    try:
        api_key = _get_next_key()
        model = os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
        logger.info(
            "Creating OpenRouter client | model={} base_url={} keys_in_rotation={}",
            model,
            OPENROUTER_BASE_URL,
            len(_API_KEYS) if _API_KEYS else 0,
        )
        headers = _default_headers()
        return OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=api_key,
            default_headers=headers if headers else None,
        )
    except ValueError as e:
        logger.error(
            "OpenRouter config error: {} | Check OPENROUTER_API_KEY in .env (see .env.example)",
            e,
        )
        raise
    except Exception as e:
        logger.exception("Failed to create OpenRouter client: {}", e)
        raise


def _strip_markdown_json(content: str) -> str:
    """Extract raw JSON from content that may be markdown-wrapped or have trailing text."""
    if not content or not content.strip():
        return content
    text = content.strip()

    # 1. Fenced block: find first ```json or ```, then next ``` (trailing text allowed)
    fence_start = re.search(r"```(?:json)?\s*\n", text)
    if fence_start:
        after_open = text[fence_start.end() :]
        fence_end = re.search(r"\n?```", after_open)
        if fence_end:
            return after_open[: fence_end.start()].strip()

    # 2. Fallback: extract first JSON object by brace-matching
    start = text.find("{")
    if start >= 0:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    return text[start : i + 1]
    return text


T = TypeVar("T", bound=BaseModel)


def chat_structured(
    response_format: type[T],
    prompt: str,
    *,
    temperature: float = 0,
    max_tokens: int = 4096,
) -> T:
    """Call OpenRouter chat with structured output; returns parsed Pydantic model.
    Handles models that wrap JSON in markdown code blocks (e.g. ```json ... ```).
    """
    client = get_openai_client()
    model = os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    logger.debug(f">> Model: {model}")
    logger.debug(f">> Prompt: {prompt}")
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": response_format.model_json_schema().get("title", "response"),
                "strict": True,
                "schema": response_format.model_json_schema(),
            },
        },
        temperature=temperature,
        max_tokens=max_tokens,
    )
    raw = completion.choices[0].message.content
    logger.debug(f">> Model Raw response: {raw}")
    if not raw:
        raise ValueError("OpenRouter returned no structured output")
    json_str = _strip_markdown_json(raw)
    return response_format.model_validate_json(json_str)
