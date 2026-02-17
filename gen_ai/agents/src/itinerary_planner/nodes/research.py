"""Optional research: enrich destinations via web search or LLM/tools."""

from loguru import logger
from pydantic import BaseModel, Field

from itinerary_planner.llm import chat_structured
from itinerary_planner.prompt_garden import EXPAND_COUNTRY_PROMPT
from itinerary_planner.state import PlannerState
from itinerary_planner.tools import web_search

# Static map: country name (lowercase) -> list of representative regions/cities
COUNTRY_REGIONS: dict[str, list[str]] = {
    "philippines": ["Manila", "Palawan", "Boracay", "Cebu"],
    "japan": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
    "italy": ["Rome", "Florence", "Venice", "Milan"],
    "thailand": ["Bangkok", "Chiang Mai", "Phuket", "Krabi"],
    "india": ["Delhi", "Mumbai", "Rajasthan", "Kerala", "Goa"],
    "spain": ["Madrid", "Barcelona", "Seville", "Valencia"],
    "france": ["Paris", "Lyon", "Nice", "Provence"],
    "indonesia": ["Bali", "Jakarta", "Yogyakarta", "Lombok"],
    "vietnam": ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hoi An"],
    "australia": ["Sydney", "Melbourne", "Cairns", "Great Barrier Reef"],
    "usa": ["New York", "Los Angeles", "San Francisco", "Miami"],
    "united states": ["New York", "Los Angeles", "San Francisco", "Miami"],
    "uk": ["London", "Edinburgh", "Bath", "Manchester"],
    "united kingdom": ["London", "Edinburgh", "Bath", "Manchester"],
    "greece": ["Athens", "Santorini", "Mykonos", "Crete"],
    "portugal": ["Lisbon", "Porto", "Algarve"],
    "turkey": ["Istanbul", "Cappadocia", "Antalya", "Ephesus"],
    "malaysia": ["Kuala Lumpur", "Penang", "Langkawi", "Borneo"],
    "sri lanka": ["Colombo", "Kandy", "Galle", "Ella"],
    "new zealand": ["Auckland", "Queenstown", "Wellington", "Rotorua"],
}


class ExpandRegionsSchema(BaseModel):
    """LLM response for country -> regions expansion."""

    regions: list[str] = Field(description="List of region or city names")


def _expand_destination(dest: str) -> list[str]:
    """Expand a destination (country or city) to a list of regions. Uses static map first, then LLM."""
    key = dest.strip().lower()
    if key in COUNTRY_REGIONS:
        return list(COUNTRY_REGIONS[key])
    try:
        result = chat_structured(
            ExpandRegionsSchema,
            EXPAND_COUNTRY_PROMPT.format(country=dest),
            max_tokens=256,
        )
        regions = getattr(result, "regions", []) or []
        return [r.strip() for r in regions if r and r.strip()] if regions else [dest]
    except Exception as e:  # noqa: BLE001
        logger.warning("expand destination '{}' failed: {}, keeping as-is", dest, e)
        return [dest]


def _is_likely_country(dest: str) -> bool:
    """True if destination is in our country map (expand to regions)."""
    return dest.strip().lower() in COUNTRY_REGIONS


def research(state: PlannerState) -> dict:
    """Add optional research notes: expand countries to regions, web search tips, transport (including origin bookends)."""
    logger.debug("research started")
    parsed = state.get("parsed")
    if not parsed:
        return {"research": None}

    raw_destinations = [d.strip() for d in parsed.get("destinations", []) if d and d.strip()]
    # Expand countries to regions; leave cities/regions as single-item lists then flatten
    expanded_destinations: list[str] = []
    for d in raw_destinations:
        if _is_likely_country(d):
            expanded_destinations.extend(_expand_destination(d))
        else:
            expanded_destinations.append(d)

    # Use expanded list for downstream; fallback to raw if expansion produced nothing
    destinations = expanded_destinations if expanded_destinations else raw_destinations
    preferences = parsed.get("preferences", [])
    transport_preference = (parsed.get("transport_preference") or "").strip()
    origin = (parsed.get("origin") or "").strip() or None

    notes_by_destination: dict[str, str] = {}
    search_limit = 3

    for dest in destinations:
        query = f"{dest} things to do opening hours tips for visitors"
        if preferences:
            query += " " + " ".join(preferences[:3])
        results = web_search(query, max_results=search_limit)
        if results:
            snippets = [r.get("body", r.get("title", "")) for r in results if r.get("body") or r.get("title")]
            notes_by_destination[dest] = " | ".join(snippets[:3]) if snippets else "No web results."
        else:
            notes_by_destination[dest] = "No web results (search unavailable or rate limited)."

    # Transport: between consecutive destinations; and origin -> first, last -> origin when origin is set
    transport_by_leg: dict[str, str] = {}
    if not transport_preference:
        # Origin bookends
        if origin and destinations:
            first_dest = destinations[0]
            if first_dest.lower() != origin.lower():
                leg_key = f"{origin} to {first_dest}"
                query = f"best way to get from {origin} to {first_dest} flight transport"
                results = web_search(query, max_results=3)
                if results:
                    snippets = [r.get("body", r.get("title", "")) for r in results if r.get("body") or r.get("title")]
                    transport_by_leg[leg_key] = " | ".join(snippets[:3]) if snippets else "Flight (international/long distance)."
                else:
                    transport_by_leg[leg_key] = "Flight (international/long distance)."
            if len(destinations) > 1 or first_dest.lower() != origin.lower():
                last_dest = destinations[-1]
                if last_dest.lower() != origin.lower():
                    leg_key = f"{last_dest} to {origin}"
                    query = f"best way to get from {last_dest} to {origin} flight transport"
                    results = web_search(query, max_results=3)
                    if results:
                        snippets = [r.get("body", r.get("title", "")) for r in results if r.get("body") or r.get("title")]
                        transport_by_leg[leg_key] = " | ".join(snippets[:3]) if snippets else "Flight (international/long distance)."
                    else:
                        transport_by_leg[leg_key] = "Flight (international/long distance)."
        # Between consecutive destinations
        if len(destinations) >= 2:
            for i in range(len(destinations) - 1):
                orig, dest = destinations[i], destinations[i + 1]
                leg_key = f"{orig} to {dest}"
                if leg_key not in transport_by_leg:
                    query = f"best easiest way to get from {orig} to {dest} transport"
                    results = web_search(query, max_results=3)
                    if results:
                        snippets = [r.get("body", r.get("title", "")) for r in results if r.get("body") or r.get("title")]
                        transport_by_leg[leg_key] = " | ".join(snippets[:3]) if snippets else "No transport search results."
                    else:
                        transport_by_leg[leg_key] = "No transport search results (search unavailable or rate limited)."

    research_notes = {
        "destinations": destinations,
        "notes_by_destination": notes_by_destination,
        "transport_by_leg": transport_by_leg,
        "notes": "Web search used for destination tips and opening hours." if notes_by_destination else "No external research data.",
    }
    return {"research": research_notes}
