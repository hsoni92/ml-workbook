"""Plan accommodation: where to stay each night, check-in/check-out."""

from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import (
    OPENROUTER_401_MESSAGE,
    chat_structured,
    is_openrouter_auth_error,
)
from itinerary_planner.prompt_garden import PLAN_ACCOMMODATION_PROMPT
from itinerary_planner.state import AccommodationStay, DayPlan, PlannerState, TransportLeg


class AccommodationStaySchema(BaseModel):
    place: str = Field(description="Hotel or accommodation name and city")
    check_in: str = Field(description="Check-in datetime ISO or date")
    check_out: str = Field(description="Check-out datetime ISO or date")
    city: str = Field(description="City of stay")


class PlanAccommodationSchema(BaseModel):
    stays: list[AccommodationStaySchema] = Field(description="Accommodation stays")


def plan_accommodation(state: PlannerState) -> dict:
    """Produce accommodation stays from days and transport."""
    logger.debug("plan_accommodation started")
    days: list[DayPlan] = state.get("days") or []
    transport_legs: list[TransportLeg] = state.get("transport_legs") or []

    days_str = "\n".join(
        f"- {d.get('date', '')} in {d.get('city', '')}" for d in days
    )
    transport_str = "\n".join(
        f"- {l.get('from_place', '')} -> {l.get('to', '')} depart {l.get('departure', '')}"
        for l in transport_legs
    )

    try:
        result = chat_structured(
            PlanAccommodationSchema,
            PLAN_ACCOMMODATION_PROMPT.format(days=days_str, transport=transport_str),
        )
        if not result or not getattr(result, "stays", None):
            return {"accommodation": [], "error": None}

        accommodation: list[AccommodationStay] = [
            {
                "place": s.place,
                "check_in": s.check_in,
                "check_out": s.check_out,
                "city": s.city,
            }
            for s in result.stays
        ]
        return {"accommodation": accommodation, "error": None}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"accommodation": [], "error": OPENROUTER_401_MESSAGE}
        logger.exception("plan_accommodation failed: {}", e)
        return {"accommodation": [], "error": str(e)}
