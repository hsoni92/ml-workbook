"""Build final itinerary structure (JSON + optional markdown)."""

from loguru import logger

from itinerary_planner.state import (
    AccommodationStay,
    DayPlan,
    ItineraryAccommodation,
    ItineraryDay,
    ItineraryOutput,
    ItineraryTransport,
    PlannerState,
    PriceSummary,
    TransportLeg,
)


def build_itinerary(state: PlannerState) -> dict:
    """Format days, transport, accommodation, prices into final itinerary."""
    logger.debug("build_itinerary started")
    days: list[DayPlan] = state.get("days") or []
    transport_legs: list[TransportLeg] = state.get("transport_legs") or []
    accommodation: list[AccommodationStay] = state.get("accommodation") or []
    prices: PriceSummary | None = state.get("prices")

    # Build itinerary days (add estimatedCost to activities if we had per-activity prices)
    itinerary_days: list[ItineraryDay] = []
    for d in days:
        itinerary_days.append({
            "date": d.get("date", ""),
            "city": d.get("city", ""),
            "activities": d.get("activities", []),
            "notes": d.get("notes"),
        })

    # Transport with "from" key for API output (design doc uses "from" in JSON)
    itinerary_transport: list[ItineraryTransport] = []
    for leg in transport_legs:
        itinerary_transport.append({
            "from_place": leg.get("from_place", ""),
            "to": leg.get("to", ""),
            "mode": leg.get("mode", ""),
            "departure": leg.get("departure", ""),
            "arrival": leg.get("arrival", ""),
            "duration_minutes": leg.get("duration_minutes") or 0,
            "estimated_cost": leg.get("estimated_cost"),
        })

    # Accommodation
    itinerary_accommodation: list[ItineraryAccommodation] = []
    for a in accommodation:
        itinerary_accommodation.append({
            "place": a.get("place", ""),
            "check_in": a.get("check_in", ""),
            "check_out": a.get("check_out", ""),
            "nights": a.get("nights"),
            "estimated_cost_per_night": a.get("estimated_cost_per_night"),
        })

    parsed = state.get("parsed") or {}
    origin = (parsed.get("origin") or "").strip() or None
    summary = "Trip itinerary"
    if days:
        summary = f"{len(days)}-day trip"
        cities = list({d.get("city", "") for d in days if d.get("city")})
        if origin:
            summary += f" from {origin}"
        if cities:
            summary += f" to {', '.join(cities)}"
        if origin:
            summary += " and back"
        summary += "."

    itinerary: ItineraryOutput = {
        "summary": summary,
        "days": itinerary_days,
        "transport": itinerary_transport,
        "accommodation": itinerary_accommodation,
        "price_summary": prices or {},
    }

    # Optional markdown text
    lines = [f"# {summary}", ""]
    lines.append("## Days")
    for d in itinerary_days:
        lines.append(f"### {d.get('date', '')} — {d.get('city', '')}")
        for a in d.get("activities", []):
            title = a.get("title", "")
            time_slot = a.get("time", "")
            lines.append(f"- **{title}** {time_slot}")
        if d.get("notes"):
            lines.append(f"  _{d['notes']}_")
        lines.append("")
    lines.append("## Transport")
    for t in itinerary_transport:
        lines.append(
            f"- {t.get('from_place', '')} → {t.get('to', '')} by {t.get('mode', '')} "
            f"({t.get('departure', '')}–{t.get('arrival', '')})"
        )
    lines.append("")
    lines.append("## Accommodation")
    for a in itinerary_accommodation:
        lines.append(f"- **{a.get('place', '')}** — Check-in: {a.get('check_in', '')}, Check-out: {a.get('check_out', '')}")
    if prices:
        lines.append("")
        lines.append("## Price summary")
        lines.append(f"- Transport: {prices.get('currency', 'EUR')} {prices.get('transport', 0)}")
        lines.append(f"- Accommodation: {prices.get('currency', 'EUR')} {prices.get('accommodation', 0)}")
        lines.append(f"- Activities: {prices.get('currency', 'EUR')} {prices.get('activities', 0)}")
        lines.append(f"- **Total (estimated): {prices.get('currency', 'EUR')} {prices.get('total_estimated', 0)}**")

    itinerary_text = "\n".join(lines)

    return {
        "itinerary": itinerary,
        "itinerary_text": itinerary_text,
        "error": None,
    }
