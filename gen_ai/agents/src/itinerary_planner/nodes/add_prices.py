"""Add price estimates to legs, stays, activities; compute totals."""

from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import (
    OPENROUTER_401_MESSAGE,
    chat_structured,
    is_openrouter_auth_error,
)
from itinerary_planner.constants import DEFAULT_CURRENCY
from itinerary_planner.prompt_garden import ADD_PRICES_PROMPT
from itinerary_planner.state import (
    AccommodationStay,
    DayPlan,
    PriceSummary,
    PlannerState,
    TransportLeg,
)


class PriceSummarySchema(BaseModel):
    transport: float = Field(description="Total estimated transport cost")
    accommodation: float = Field(description="Total estimated accommodation cost")
    activities: float = Field(description="Total estimated activities cost")
    total_estimated: float = Field(description="Total trip estimate")
    currency: str = Field(default="EUR", description="Currency code")


def add_prices(state: PlannerState) -> dict:
    """Attach estimated prices and compute price summary."""
    logger.debug("add_prices started")
    parsed = state.get("parsed") or {}
    budget = parsed.get("budget", "mid-range")
    currency = DEFAULT_CURRENCY

    transport_legs: list[TransportLeg] = state.get("transport_legs") or []
    accommodation: list[AccommodationStay] = state.get("accommodation") or []
    days: list[DayPlan] = state.get("days") or []

    transport_str = "\n".join(
        f"- {l.get('from_place', '')} to {l.get('to', '')} by {l.get('mode', '')}"
        for l in transport_legs
    )
    accom_str = "\n".join(
        f"- {a.get('place', '')} in {a.get('city', '')}"
        for a in accommodation
    )
    days_str = "\n".join(
        f"- {d.get('date', '')} {d.get('city', '')}: {[a.get('title') for a in d.get('activities', [])]}"
        for d in days
    )

    try:
        result = chat_structured(
            PriceSummarySchema,
            ADD_PRICES_PROMPT.format(
                budget=budget,
                currency=currency,
                transport=transport_str or "None",
                accommodation=accom_str or "None",
                days=days_str or "None",
            ),
        )
        if not result:
            return {"prices": None, "error": "No price summary from LLM"}

        summary: PriceSummary = {
            "transport": result.transport,
            "accommodation": result.accommodation,
            "activities": result.activities,
            "total_estimated": result.total_estimated,
            "currency": result.currency or currency,
        }
        # Optionally annotate legs/stays with estimatedCost (simplified: we don't re-call LLM per leg)
        return {"prices": summary, "error": None}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"prices": None, "error": OPENROUTER_401_MESSAGE}
        logger.exception("add_prices failed: {}", e)
        return {"prices": None, "error": str(e)}
