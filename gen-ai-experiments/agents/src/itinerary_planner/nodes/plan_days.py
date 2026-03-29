"""Plan day-by-day: which city each day, activities, timing."""

from datetime import date, timedelta
from typing import Optional

from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import (
    OPENROUTER_401_MESSAGE,
    chat_structured,
    is_openrouter_auth_error,
)
from itinerary_planner.prompt_garden import PLAN_DAYS_PROMPT
from itinerary_planner.state import DayPlan, PlannerState


class ActivitySchema(BaseModel):
    title: str = Field(description="Activity name")
    time: str = Field(description="Rough time e.g. 09:00–12:00")
    notes: Optional[str] = None


class DayPlanSchema(BaseModel):
    date: str = Field(description="Date YYYY-MM-DD")
    city: str = Field(description="City or area for this day")
    activities: list[ActivitySchema] = Field(default_factory=list)
    notes: Optional[str] = None


class PlanDaysSchema(BaseModel):
    days: list[DayPlanSchema] = Field(description="Day-by-day plan")


def _calendar_days_count(start: str, end: str) -> int:
    """Number of calendar days from start to end (inclusive). Returns 0 if parse fails."""
    try:
        start_d = date.fromisoformat(start.strip())
        end_d = date.fromisoformat(end.strip())
        if start_d > end_d:
            return 0
        return (end_d - start_d).days + 1
    except ValueError:
        return 0


def _enforce_days_count(days: list[DayPlan], start_date: str, end_date: str) -> list[DayPlan]:
    """Trim or pad days so length matches calendar days between start_date and end_date (in order)."""
    want = _calendar_days_count(start_date, end_date)
    if want <= 0:
        return days
    try:
        start_d = date.fromisoformat(start_date.strip())
        end_d = date.fromisoformat(end_date.strip())
    except ValueError:
        return days
    by_date = {d.get("date", ""): d for d in days}
    ordered: list[DayPlan] = []
    last = days[-1] if days else {}
    current = start_d
    while current <= end_d and len(ordered) < want:
        d_str = current.isoformat()
        if d_str in by_date:
            ordered.append(by_date[d_str])
        else:
            ordered.append({
                "date": d_str,
                "city": last.get("city", ""),
                "activities": last.get("activities", []),
                "notes": last.get("notes"),
            })
        current += timedelta(days=1)
    return ordered[:want]


def plan_days(state: PlannerState) -> dict:
    """Produce day-by-day plan from parsed intent and research."""
    logger.debug("plan_days started")
    parsed = state.get("parsed")
    if not parsed:
        logger.warning("plan_days: no parsed intent")
        return {"days": [], "error": "No parsed intent"}

    research = state.get("research") or {}
    # Use expanded destinations from research when present; otherwise parsed destinations
    effective_destinations = research.get("destinations") or parsed.get("destinations") or []
    research_str = str(research) if research else "None"
    origin = parsed.get("origin") or "not specified"

    try:
        result = chat_structured(
            PlanDaysSchema,
            PLAN_DAYS_PROMPT.format(
                today=date.today().isoformat(),
                origin=origin,
                destinations=effective_destinations,
                start_date=parsed.get("start_date", ""),
                end_date=parsed.get("end_date", ""),
                budget=parsed.get("budget", "mid-range"),
                preferences=parsed.get("preferences", []),
                research=research_str,
            ),
        )
        if not result or not getattr(result, "days", None):
            return {"days": [], "error": "No day plan from LLM"}

        days: list[DayPlan] = []
        for d in result.days:
            activities = [
                {
                    "title": a.title,
                    "time": a.time,
                    "notes": getattr(a, "notes", None),
                }
                for a in d.activities
            ]
            days.append({
                "date": d.date,
                "city": d.city,
                "activities": activities,
                "notes": getattr(d, "notes", None),
            })
        start_date = parsed.get("start_date", "")
        end_date = parsed.get("end_date", "")
        days = _enforce_days_count(days, start_date, end_date)
        return {"days": days, "error": None}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"days": [], "error": OPENROUTER_401_MESSAGE}
        logger.exception("plan_days failed: {}", e)
        return {"days": [], "error": str(e)}
