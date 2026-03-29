"""Run flight search for every transport leg with mode=flight; merge into research.flight_by_leg.

Flight search is guaranteed for: (1) bookend legs (origin<->first/last destination) when
origin and dates are present, via the research node; (2) all legs with mode=flight here.
Do not rely solely on the research agent for flight data; research node + this node
are the source of truth for flight_by_leg."""

from loguru import logger

from itinerary_planner.state import PlannerState, TransportLeg
from itinerary_planner.tools import search_flights

# Normalize transport mode so LLM wording (plane, air, fly) still triggers flight search
_FLIGHT_MODES = frozenset({"flight", "plane", "air", "fly", "flying"})


def _is_flight_leg(mode: str) -> bool:
    """True if the leg mode indicates flight (flight, plane, air, fly, etc.)."""
    return (mode or "").strip().lower() in _FLIGHT_MODES


def _departure_to_dd_mm_yyyy(departure: str) -> str:
    """Convert leg departure (e.g. 2026-02-20T18:00 or 2026-02-20) to DD-MM-YYYY."""
    if not departure or len(departure) < 10:
        return ""
    date_part = departure.strip()[:10]
    parts = date_part.split("-")
    if len(parts) != 3:
        return ""
    y, m, d = parts[0], parts[1], parts[2]
    return f"{d}-{m}-{y}"


def flight_search_legs(state: PlannerState) -> dict:
    """For each transport leg with mode=flight (or plane/air/fly), run flight search and merge into research.flight_by_leg."""
    transport_legs: list[TransportLeg] = state.get("transport_legs") or []
    existing_research = state.get("research") or {}
    flight_by_leg = dict(existing_research.get("flight_by_leg") or {})

    for leg in transport_legs:
        if not _is_flight_leg(leg.get("mode") or ""):
            continue
        from_place = (leg.get("from_place") or "").strip()
        to_place = (leg.get("to") or "").strip()
        if not from_place or not to_place:
            continue
        leg_key = f"{from_place} to {to_place}"
        if leg_key in flight_by_leg:
            continue
        dep = leg.get("departure") or ""
        dep_dd = _departure_to_dd_mm_yyyy(dep)
        if not dep_dd:
            logger.warning("flight_search_legs: no date for leg {} -> {}, skipping", from_place, to_place)
            continue
        result = search_flights(from_place, to_place, dep_dd, dep_dd)
        if result:
            flight_by_leg[leg_key] = result
            logger.debug("flight_search_legs: {} -> {} ({} results)", from_place, to_place, len(result.get("search_results") or []))

    if not flight_by_leg:
        return {}
    return {"research": {**existing_research, "flight_by_leg": flight_by_leg}}
