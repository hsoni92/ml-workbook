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
    address: str | None = Field(default=None, description="Address when available from hotel search")
    estimated_cost_per_night: float | None = Field(default=None, description="Estimated cost per night when available")


class PlanAccommodationSchema(BaseModel):
    stays: list[AccommodationStaySchema] = Field(description="Accommodation stays")


def _format_hotel_search_by_city(hotels_by_location: dict) -> str:
    """Format hotel search results per city for the accommodation prompt."""
    if not hotels_by_location:
        return "(No hotel search results available – suggest plausible hotel names and cities only.)"
    lines = []
    for city, results in hotels_by_location.items():
        lines.append(f"{city}:")
        for i, r in enumerate((results or [])[:6], 1):
            title = r.get("title", "")
            body = r.get("body", "")
            lines.append(f"  {i}. {title}" + (f" — {body}" if body else ""))
    return "\n".join(lines) if lines else "(No hotel search results available.)"


def plan_accommodation(state: PlannerState) -> dict:
    """Produce accommodation stays from days and transport."""
    logger.debug("plan_accommodation started")
    days: list[DayPlan] = state.get("days") or []
    transport_legs: list[TransportLeg] = state.get("transport_legs") or []
    research = state.get("research") or {}
    hotels_by_location = research.get("hotels_by_location") or {}

    days_str = "\n".join(
        f"- {d.get('date', '')} in {d.get('city', '')}" for d in days
    )
    transport_str = "\n".join(
        f"- {l.get('from_place', '')} -> {l.get('to', '')} depart {l.get('departure', '')}"
        for l in transport_legs
    )
    hotel_search_by_city = _format_hotel_search_by_city(hotels_by_location)

    try:
        result = chat_structured(
            PlanAccommodationSchema,
            PLAN_ACCOMMODATION_PROMPT.format(
                days=days_str,
                transport=transport_str,
                hotel_search_by_city=hotel_search_by_city,
            ),
        )
        if not result or not getattr(result, "stays", None):
            return {"accommodation": [], "error": None}

        accommodation: list[AccommodationStay] = []
        for s in result.stays:
            stay: AccommodationStay = {
                "place": s.place,
                "check_in": s.check_in,
                "check_out": s.check_out,
                "city": s.city,
            }
            if getattr(s, "address", None):
                stay["address"] = s.address
            if getattr(s, "estimated_cost_per_night", None) is not None:
                stay["estimated_cost_per_night"] = s.estimated_cost_per_night
            accommodation.append(stay)
        return {"accommodation": accommodation, "error": None}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"accommodation": [], "error": OPENROUTER_401_MESSAGE}
        logger.exception("plan_accommodation failed: {}", e)
        return {"accommodation": [], "error": str(e)}
