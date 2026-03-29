"""Parse user message into structured intent."""

import re
from datetime import date
from typing import Literal, Optional

from langchain_core.messages import AIMessage, HumanMessage
from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import (
    OPENROUTER_401_MESSAGE,
    chat_structured,
    is_openrouter_auth_error,
)
from itinerary_planner.dates import compute_default_dates
from itinerary_planner.prompt_garden import (
    FOLLOW_UP_CLASSIFIER_PROMPT,
    PARSE_PROMPT,
    PARSE_WITH_CONTEXT_PROMPT,
)
from itinerary_planner.state import ParsedIntent, PlannerState


class FollowUpClassification(BaseModel):
    """Classifier result: follow_up or new_query."""

    result: Literal["follow_up", "new_query"] = Field(
        description="follow_up if user is refining the previous itinerary, new_query if starting a new request"
    )


class ParsedIntentSchema(BaseModel):
    """Structured intent for the LLM to fill."""

    origin: Optional[str] = Field(
        None,
        description="Departure/return city when user says 'from X', 'starting from X', or 'trip from X to Y'. Leave empty if not specified.",
    )
    destinations: list[str] = Field(description="List of cities or regions to visit (can include country names e.g. Philippines)")
    start_date: Optional[str] = Field(None, description="Trip start date, YYYY-MM-DD if possible")
    end_date: Optional[str] = Field(None, description="Trip end date, YYYY-MM-DD if possible")
    trip_duration_days: Optional[int] = Field(
        None,
        description="Number of days when user says 'N days' or 'N-day trip'. Leave null if not specified.",
    )
    budget: str = Field(
        description="Budget level: budget, mid-range, or luxury",
        default="mid-range",
    )
    preferences: list[str] = Field(
        description="Interests e.g. museums, food, outdoors, nature, places close to nature",
        default_factory=list,
    )
    transport_preference: Optional[str] = Field(
        None,
        description="Only set if user explicitly mentions how they want to travel (e.g. by train, flight, car). Leave empty if not specified.",
    )


def _last_human_content(messages: list) -> str:
    """Get content of the last human message for Chat UI / server input."""
    for msg in reversed(messages or []):
        if isinstance(msg, HumanMessage):
            content = getattr(msg, "content", None)
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                parts = [p.get("text", p) if isinstance(p, dict) else str(p) for p in content]
                return " ".join(str(p) for p in parts)
            return str(content) if content is not None else ""
    return ""


def _last_assistant_content(messages: list) -> str:
    """Get content of the last assistant message (previous itinerary or summary)."""
    for msg in reversed(messages or []):
        if isinstance(msg, AIMessage):
            content = getattr(msg, "content", None)
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                parts = [p.get("text", p) if isinstance(p, dict) else str(p) for p in content]
                return " ".join(str(p) for p in parts)
            return str(content) if content is not None else ""
    return ""


def _heuristic_follow_up(user_message: str) -> Optional[bool]:
    """Fast heuristic: return True if likely follow-up, False if likely new query, None if ambiguous."""
    msg = (user_message or "").strip().lower()
    if not msg:
        return None
    follow_up_starts = (
        r"^(also|and)\s+(add|include)",
        r"^can you (also\s+)?(add|include)",
        r"^(please\s+)?(add|include)\s+",
        r"^(actually|instead|one more thing)",
        r"^(could you|would you)\s+(also\s+)?(add|include|change)",
    )
    if any(re.search(p, msg) for p in follow_up_starts):
        return True
    new_query_starts = (
        r"^(plan|planning)\s+(a\s+)?(new\s+)?(trip|itinerary)",
        r"^i want (a\s+)?(new\s+)?(trip|itinerary)",
        r"^(new\s+)?(trip|itinerary)\s+(for|to|please)",
    )
    if any(re.search(p, msg) for p in new_query_starts):
        return False
    return None


def _classify_follow_up(
    user_message: str, last_assistant_content: str
) -> bool:
    """Classify whether the user message is a follow-up (True) or new query (False)."""
    heuristic = _heuristic_follow_up(user_message)
    if heuristic is not None:
        logger.debug("follow-up heuristic: {}", heuristic)
        return heuristic
    try:
        classification = chat_structured(
            FollowUpClassification,
            FOLLOW_UP_CLASSIFIER_PROMPT.format(
                previous_assistant_response=last_assistant_content[:8000],
                user_message=user_message,
            ),
            max_tokens=64,
        )
        is_follow_up = getattr(classification, "result", "new_query") == "follow_up"
        logger.debug("follow-up classifier: {}", is_follow_up)
        return is_follow_up
    except Exception as e:  # noqa: BLE001
        logger.warning("follow-up classifier failed, treating as new_query: {}", e)
        return False


def parse_input(state: PlannerState) -> dict:
    """Extract structured intent from userMessage or last human message; write to parsed or set error.
    When conversation history exists, classifies follow-up vs new query and parses with context if follow-up."""
    logger.debug("parse_input started")
    messages = state.get("messages") or []
    user_message = (state.get("user_message") or "").strip()
    if not user_message:
        user_message = _last_human_content(messages).strip()
    if not user_message:
        logger.warning("parse_input: user_message is empty")
        return {"error": "user_message is empty", "parsed": None}

    last_assistant_content = _last_assistant_content(messages)
    is_follow_up = False
    if last_assistant_content.strip():
        is_follow_up = _classify_follow_up(user_message, last_assistant_content)

    today_str = date.today().isoformat()
    try:
        if is_follow_up:
            prompt = PARSE_WITH_CONTEXT_PROMPT.format(
                today=today_str,
                previous_assistant_response=last_assistant_content[:8000],
                user_follow_up=user_message,
            )
        else:
            prompt = PARSE_PROMPT.format(today=today_str, user_message=user_message)

        result = chat_structured(ParsedIntentSchema, prompt)
        if not result:
            return {"error": "LLM returned no structured intent", "parsed": None}
        start_date = (getattr(result, "start_date", "") or "").strip()
        end_date = (getattr(result, "end_date", "") or "").strip()
        destinations = getattr(result, "destinations", []) or []
        num_destinations = len([d for d in destinations if d and str(d).strip()])
        trip_duration = getattr(result, "trip_duration_days", None)
        if trip_duration is not None and (not isinstance(trip_duration, int) or trip_duration < 1):
            trip_duration = None
        start_date, end_date = compute_default_dates(
            start_date,
            end_date,
            num_destinations,
            trip_duration_days=trip_duration,
        )
        origin_val = (getattr(result, "origin", None) or "").strip() or None
        parsed: ParsedIntent = {
            "origin": origin_val,
            "destinations": destinations,
            "start_date": start_date,
            "end_date": end_date,
            "trip_duration_days": trip_duration,
            "budget": getattr(result, "budget", "mid-range") or "mid-range",
            "preferences": getattr(result, "preferences", []) or [],
            "transport_preference": (getattr(result, "transport_preference", None) or "").strip() or None,
        }
        return {"parsed": parsed, "error": None, "is_follow_up": is_follow_up}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"error": OPENROUTER_401_MESSAGE, "parsed": None}
        logger.exception("parse_input failed: {}", e)
        return {"error": str(e), "parsed": None}
