"""Plan transport legs between cities/key points, including outbound and return from origin."""

from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import (
    OPENROUTER_401_MESSAGE,
    chat_structured,
    is_openrouter_auth_error,
)
from itinerary_planner.prompt_garden import PLAN_TRANSPORT_PROMPT
from itinerary_planner.state import DayPlan, PlannerState, TransportLeg


class TransportLegSchema(BaseModel):
    from_place: str = Field(description="Origin city or place")
    to: str = Field(description="Destination city or place")
    mode: str = Field(description="e.g. TGV, car, flight, walk")
    duration_minutes: int = Field(description="Approximate duration in minutes")
    departure: str = Field(description="ISO datetime or time e.g. 2025-03-12T09:00")
    arrival: str = Field(description="ISO datetime or time e.g. 2025-03-12T11:30")


class PlanTransportSchema(BaseModel):
    legs: list[TransportLegSchema] = Field(description="Transport legs between locations")


def _required_legs(days: list[DayPlan], origin: str | None) -> list[tuple[str, str]]:
    """Build list of (from_place, to) that must appear in transport (outbound, between cities, return)."""
    if not days:
        return []
    first_city = (days[0].get("city") or "").strip()
    last_city = (days[-1].get("city") or "").strip()
    origin = (origin or "").strip() or None

    legs: list[tuple[str, str]] = []
    if origin and first_city and first_city.lower() != origin.lower():
        legs.append((origin, first_city))
    for i in range(len(days) - 1):
        a = (days[i].get("city") or "").strip()
        b = (days[i + 1].get("city") or "").strip()
        if a and b and a.lower() != b.lower():
            legs.append((a, b))
    if origin and last_city and last_city.lower() != origin.lower():
        legs.append((last_city, origin))
    return legs


def _inject_bookend_legs(
    legs: list[TransportLeg],
    days: list[DayPlan],
    origin: str | None,
) -> list[TransportLeg]:
    """If origin is set but outbound or return leg is missing, inject synthetic legs."""
    origin = (origin or "").strip() or None
    if not origin or not days:
        return legs
    first_city = (days[0].get("city") or "").strip()
    last_city = (days[-1].get("city") or "").strip()
    first_date = days[0].get("date", "")
    last_date = days[-1].get("date", "")

    has_outbound = any(
        (l.get("from_place") or "").strip().lower() == origin.lower()
        for l in legs
    )
    has_return = any(
        (l.get("to") or "").strip().lower() == origin.lower()
        for l in legs
    )
    result = list(legs)
    if first_city and first_city.lower() != origin.lower() and not has_outbound:
        result.insert(
            0,
            {
                "from_place": origin,
                "to": first_city,
                "mode": "flight",
                "duration_minutes": 360,
                "departure": f"{first_date}T06:00",
                "arrival": f"{first_date}T12:00",
            },
        )
    if last_city and last_city.lower() != origin.lower() and not has_return:
        result.append({
            "from_place": last_city,
            "to": origin,
            "mode": "flight",
            "duration_minutes": 360,
            "departure": f"{last_date}T18:00",
            "arrival": f"{last_date}T23:59",
        })
    return result


def plan_transport(state: PlannerState) -> dict:
    """Produce transport legs (outbound, between cities, return), using user preference or web-researched options."""
    logger.debug("plan_transport started")
    days = state.get("days") or []
    if not days:
        logger.warning("plan_transport: no days to plan for")
        return {"transport_legs": [], "error": "No days to plan transport for"}

    days_str = "\n".join(
        f"- {d.get('date', '')} in {d.get('city', '')}" for d in days
    )
    parsed = state.get("parsed") or {}
    origin = parsed.get("origin")
    required = _required_legs(days, origin)
    required_legs_str = "\n".join(
        f"- {fr} -> {to}" for fr, to in required
    ) if required else "(same as city-to-city transitions from the days above)"

    transport_preference = (parsed.get("transport_preference") or "").strip()
    transport_preference_str = transport_preference if transport_preference else "(none – use research to pick best/easiest)"

    research_data = state.get("research") or {}
    transport_by_leg = research_data.get("transport_by_leg") or {}
    if transport_by_leg:
        transport_research = "\n".join(
            f"- {leg}: {text}" for leg, text in transport_by_leg.items()
        )
    else:
        transport_research = "(no web research available – choose sensible default e.g. train for city pairs, flight for long distance)"

    try:
        result = chat_structured(
            PlanTransportSchema,
            PLAN_TRANSPORT_PROMPT.format(
                days=days_str,
                required_legs=required_legs_str,
                transport_preference=transport_preference_str,
                transport_research=transport_research,
            ),
        )
        if not result or not getattr(result, "legs", None):
            legs = []
        else:
            legs = [
                {
                    "from_place": leg.from_place,
                    "to": leg.to,
                    "mode": leg.mode,
                    "duration_minutes": leg.duration_minutes,
                    "departure": leg.departure,
                    "arrival": leg.arrival,
                }
                for leg in result.legs
            ]
        legs = _inject_bookend_legs(legs, days, origin)
        return {"transport_legs": legs, "error": None}
    except Exception as e:  # noqa: BLE001
        if is_openrouter_auth_error(e):
            logger.error(OPENROUTER_401_MESSAGE)
            return {"transport_legs": [], "error": OPENROUTER_401_MESSAGE}
        logger.exception("plan_transport failed: {}", e)
        return {"transport_legs": [], "error": str(e)}
