"""Logging setup and LangChain callback for request/response and errors."""

from __future__ import annotations

import sys
from typing import Any

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from loguru import logger

# Truncate long strings in logs so they stay readable
MAX_LOG_BODY = 2000


def _truncate(s: str, max_len: int = MAX_LOG_BODY) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len] + f"... [truncated, total {len(s)} chars]"


def configure_logging(
    *,
    level: str = "DEBUG",
    serialize: bool = False,
) -> None:
    """Configure loguru: one sink to stderr with level and format.

    Call once at app startup (e.g. in main).
    """
    logger.remove()
    fmt = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
    logger.add(
        sys.stderr,
        format=fmt,
        level=level,
        serialize=serialize,
        backtrace=True,
        diagnose=True,
    )


def get_logger(name: str) -> Any:
    """Return a logger bound to the given module/component name."""
    return logger.bind(component=name)


class LLMLoggingCallback(BaseCallbackHandler):
    """LangChain callback that logs every LLM request, response, and error."""

    def __init__(self, max_body_len: int = MAX_LOG_BODY) -> None:
        super().__init__()
        self._max = max_body_len

    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        **kwargs: Any,
    ) -> None:
        model = serialized.get("id", [""])[-1] if isinstance(serialized.get("id"), list) else serialized.get("id", "?")
        prompt_text = "\n".join(prompts) if prompts else "(no prompts)"
        logger.debug(
            "LLM request | model={} | prompt={}",
            model,
            _truncate(prompt_text, self._max),
        )

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        texts: list[str] = []
        for gen_list in response.generations:
            for g in gen_list:
                if getattr(g, "text", None):
                    texts.append(g.text)
        body = "\n".join(texts) if texts else "(empty)"
        logger.debug(
            "LLM response | {}",
            _truncate(body, self._max),
        )

    def on_llm_error(self, error: BaseException, **kwargs: Any) -> None:
        logger.exception("LLM error | {}", error)
