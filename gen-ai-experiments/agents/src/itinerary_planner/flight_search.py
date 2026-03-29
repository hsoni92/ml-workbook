"""Flight search via fast_flights (Google Flights). Uses FlightQuery and search_flights."""

from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass
from typing import Any, List, Literal

from fast_flights import (
    FlightData,
    Passengers,
    get_flights_from_filter,
    TFSData,
)
from loguru import logger

# Re-export for the user's API
__all__ = ["FlightQuery", "Passengers", "search_flights", "FlightResult"]


@dataclass
class FlightResult:
    """One flight result with .price, .airline, .departure, .duration (and .arrival, .stops, .origin, .destination)."""

    price: str
    airline: str
    departure: str
    duration: str
    arrival: str = ""
    stops: int = 0
    origin: str = ""
    destination: str = ""


@dataclass
class FlightQuery:
    """Query for flight search. Dates in YYYY-MM-DD. Airports as IATA codes (e.g. BLR, DXB)."""

    origin: str
    destination: str
    date: str
    return_date: str | None = None
    passengers: Passengers | None = None
    currency: str = "USD"

    def __post_init__(self) -> None:
        if self.passengers is None:
            self.passengers = Passengers(adults=1)
        o = self.origin.strip()
        self.origin = o.upper() if len(o) == 3 and o.isalpha() else o
        d = self.destination.strip()
        self.destination = d.upper() if len(d) == 3 and d.isalpha() else d


def _norm(s: str) -> str:
    """Collapse whitespace so scraper quirks don't produce odd spacing."""
    return " ".join((s or "").split()).strip()


def _flight_to_result(f: Any) -> FlightResult:
    """Map fast_flights.Flight to FlightResult. Normalizes string fields."""
    stops_raw = getattr(f, "stops", 0) or 0
    try:
        stops = int(stops_raw)
    except (TypeError, ValueError):
        stops = 0
    return FlightResult(
        price=_norm(getattr(f, "price", "") or ""),
        airline=_norm(getattr(f, "name", "") or ""),
        departure=_norm(getattr(f, "departure", "") or ""),
        duration=_norm(getattr(f, "duration", "") or ""),
        arrival=_norm(getattr(f, "arrival", "") or ""),
        stops=stops,
    )


def _is_result_complete(r: FlightResult) -> bool:
    """True if result has at least airline and (departure or duration) for display."""
    has_airline = bool((r.airline or "").strip())
    has_time = bool((r.departure or "").strip()) or bool((r.duration or "").strip())
    return has_airline and has_time


def _validate_flight_results(
    results: List[FlightResult],
    min_complete: int = 1,
    min_complete_ratio: float = 0.25,
) -> bool:
    """Return True if results are good enough (enough entries have airline + time details)."""
    if not results:
        return False
    complete = sum(1 for r in results if _is_result_complete(r))
    return complete >= min_complete and (complete / len(results)) >= min_complete_ratio


_FETCH_MODES: tuple[str, ...] = ("common", "fallback", "force-fallback", "local")
_DEFAULT_FETCH_MODE: Literal["common", "fallback", "force-fallback", "local"] = "common"
_MAX_RETRIES = 3
_RETRY_DELAY_SECONDS = 2.0


def search_flights(
    query: FlightQuery,
    max_workers: int = 3,
    *,
    seat: Literal["economy", "premium-economy", "business", "first"] = "economy",
    fetch_mode: Literal["common", "fallback", "force-fallback", "local"] | None = None,
) -> List[FlightResult]:
    """Search flights using fast_flights (Google Flights). Returns list of FlightResult.

    Retries up to _MAX_RETRIES when results are incomplete (e.g. missing airline/departure/duration).

    Args:
        query: FlightQuery with origin, destination, date, optional return_date, passengers, currency.
        max_workers: Reserved for parallel requests if needed (single search for now).
        seat: economy | premium-economy | business | first.
        fetch_mode: common (default) | fallback | force-fallback | local.
            Default is "common" (direct HTTP). Set FLIGHT_SEARCH_FETCH_MODE=local to use local Playwright.

    Returns:
        List of FlightResult with .price, .airline, .departure, .duration, .arrival, .stops.
    """
    if fetch_mode is None:
        env_mode = os.environ.get("FLIGHT_SEARCH_FETCH_MODE", "").strip().lower()
        fetch_mode = env_mode if env_mode in _FETCH_MODES else _DEFAULT_FETCH_MODE

    flight_data: List[FlightData] = [
        FlightData(date=query.date, from_airport=query.origin, to_airport=query.destination),
    ]
    if query.return_date:
        flight_data.append(
            FlightData(date=query.return_date, from_airport=query.destination, to_airport=query.origin),
        )
        trip = "round-trip"
    else:
        trip = "one-way"

    last_results: List[FlightResult] = []
    for attempt in range(_MAX_RETRIES):
        try:
            filter_tfs = TFSData.from_interface(
                flight_data=flight_data,
                trip=trip,
                passengers=query.passengers,
                seat=seat,
            )
            result = get_flights_from_filter(
                filter_tfs,
                currency=query.currency or "",
                mode=fetch_mode,
            )
        except RuntimeError as e:
            msg = str(e)
            if "No flights found" in msg or "Loading results" in msg:
                logger.debug(
                    "fast_flights: Google returned loading/empty page (try FLIGHT_SEARCH_FETCH_MODE=local for Playwright)"
                )
            else:
                logger.warning("fast_flights error: {}", msg)
            if attempt < _MAX_RETRIES - 1:
                logger.debug("Retrying in {}s (attempt {}/{})", _RETRY_DELAY_SECONDS, attempt + 1, _MAX_RETRIES)
                time.sleep(_RETRY_DELAY_SECONDS)
                continue
            return []
        except Exception as e:
            logger.warning("fast_flights error: {} {}", type(e).__name__, str(e))
            if attempt < _MAX_RETRIES - 1:
                time.sleep(_RETRY_DELAY_SECONDS)
                continue
            return []

        if not result or not getattr(result, "flights", None):
            if attempt < _MAX_RETRIES - 1:
                time.sleep(_RETRY_DELAY_SECONDS)
                continue
            return []

        last_results = [_flight_to_result(f) for f in result.flights]
        for r in last_results:
            r.origin = query.origin
            r.destination = query.destination
        if _validate_flight_results(last_results):
            return last_results
        logger.debug(
            "Flight results incomplete ({} complete of {}), retrying in {}s (attempt {}/{})",
            sum(1 for r in last_results if _is_result_complete(r)),
            len(last_results),
            _RETRY_DELAY_SECONDS,
            attempt + 1,
            _MAX_RETRIES,
        )
        if attempt < _MAX_RETRIES - 1:
            time.sleep(_RETRY_DELAY_SECONDS)

    return last_results


# ----- Backward compatibility: same API as before for research/tools/build_itinerary -----

_CITY_TO_IATA: dict[str, str] = {
    "bangalore": "BLR",
    "bengaluru": "BLR",
    "mumbai": "BOM",
    "delhi": "DEL",
    "new delhi": "DEL",
    "dubai": "DXB",
    "abu dhabi": "AUH",
    "sharjah": "SHJ",
    "chennai": "MAA",
    "kolkata": "CCU",
    "hyderabad": "HYD",
    "kochi": "COK",
    "goa": "GOI",
    "pune": "PNQ",
    "ahmedabad": "AMD",
    "singapore": "SIN",
    "bangkok": "BKK",
    "hong kong": "HKG",
    "london": "LON",
    "new york": "NYC",
    "nyc": "NYC",
    "los angeles": "LAX",
    "san francisco": "SFO",
    "paris": "PAR",
    "tokyo": "TYO",
    "manila": "MNL",
    "sydney": "SYD",
    "doha": "DOH",
    # Countries / regions -> main airport
    "vietnam": "SGN",
    "ho chi minh": "SGN",
    "hanoi": "HAN",
    "philippines": "MNL",
    "thailand": "BKK",
    "india": "DEL",
    "uae": "DXB",
}


def _place_to_iata(place: str) -> str:
    s = (place or "").strip()
    if not s:
        return s
    if len(s) == 3 and s.isalpha():
        return s.upper()
    return _CITY_TO_IATA.get(s.lower(), s)


def _dd_mm_yyyy_to_iso(date_str: str) -> str:
    """Convert DD-MM-YYYY to YYYY-MM-DD for FlightQuery."""
    if not date_str:
        return date_str
    parts = date_str.strip().split("-")
    if len(parts) == 3:
        d, m, y = parts[0], parts[1], parts[2]
        return f"{y}-{m.zfill(2)}-{d.zfill(2)}"
    return date_str


def _flights_to_response(flights: List[FlightResult], from_place: str, to_place: str) -> dict[str, Any]:
    """Convert list of FlightResult to { search_results, first_page } for build_itinerary."""
    if not flights:
        return {}

    from_place = _norm(from_place)
    to_place = _norm(to_place)
    search_results = []
    for f in flights:
        title = _norm(f"{from_place}→{to_place} {f.airline} {f.price}")
        body = _norm(
            f"Price: {f.price} | Airline: {f.airline} | Dep: {f.departure} | Arr: {f.arrival} | Duration: {f.duration} | Stops: {f.stops}"
        )
        search_results.append({"title": title, "href": "", "body": body})

    first = search_results[0]
    summary_parts = [first["body"]]
    for r in search_results[1:4]:
        summary_parts.append(r["title"] + " — " + r["body"])

    return {
        "search_results": search_results,
        "first_page": {
            "url": "https://www.google.com/travel/flights",
            "title": _norm(f"Flights {from_place} → {to_place}"),
            "content": _norm(" | ".join(summary_parts))[:500],
        },
    }


def search_flights_compat(
    from_place: str,
    to_place: str,
    departure_date: str,
    return_date: str,
    *,
    headless: bool = True,
    adults: int = 1,
    curr: str = "USD",
    limit: int = 7,
) -> dict[str, Any]:
    """Backward-compatible search: (from_place, to_place, dates) -> { search_results, first_page }.

    Date format: DD-MM-YYYY. Used by research node and tools.
    """
    origin = _place_to_iata(from_place)
    destination = _place_to_iata(to_place)
    date_iso = _dd_mm_yyyy_to_iso(departure_date)
    return_date_iso = _dd_mm_yyyy_to_iso(return_date) if return_date else None

    query = FlightQuery(
        origin=origin,
        destination=destination,
        date=date_iso,
        return_date=return_date_iso,
        passengers=Passengers(adults=adults),
        currency=curr,
    )
    flights = search_flights(query, max_workers=3)
    if limit and len(flights) > limit:
        flights = flights[:limit]
    if not flights:
        return {}
    logger.debug(">> Flight search {}→{} -> {} results", origin, destination, len(flights))
    return _flights_to_response(flights, from_place, to_place)


async def search_flights_async(
    from_place: str,
    to_place: str,
    departure_date: str,
    return_date: str,
    *,
    headless: bool = True,
    adults: int = 1,
    curr: str = "USD",
    limit: int = 7,
) -> dict[str, Any]:
    """Async wrapper for search_flights_compat (same return shape)."""
    return await asyncio.to_thread(
        search_flights_compat,
        from_place,
        to_place,
        departure_date,
        return_date,
        headless=headless,
        adults=adults,
        curr=curr,
        limit=limit,
    )


def _stops_display(stops: int) -> str:
    """Format stops for display: 0 -> Nonstop, 1 -> 1 stop, etc."""
    if stops <= 0:
        return "Nonstop"
    return "1 stop" if stops == 1 else f"{stops} stops"


def print_flight_results(flights: List[FlightResult]) -> None:
    """Pretty-print flight list (for CLI/__main__) with route, price, airline, departure, arrival, duration, stops."""
    if not flights:
        print("No results")
        return
    # Columns: Origin | Destination | Price | Airline | Departure | Arrival | Duration | Stops
    w_orig, w_dest, w_price, w_airline, w_dep, w_arr, w_dur, w_stops = 6, 6, 8, 28, 22, 22, 14, 10
    fmt = (
        f"{{:<{w_orig}}}  {{:<{w_dest}}}  {{:>{w_price}}}  {{:<{w_airline}}}  {{:<{w_dep}}}  {{:<{w_arr}}}  {{:<{w_dur}}}  {{:<{w_stops}}}"
    )
    header = fmt.format("Origin", "Dest", "Price", "Airline", "Departure", "Arrival", "Duration", "Stops")
    print(header)
    print("-" * len(header))
    for f in flights:
        orig = (f.origin or "")[:w_orig]
        dest = (f.destination or "")[:w_dest]
        dep = (f.departure or "")[:w_dep]
        arr = (f.arrival or "")[:w_arr]
        dur = (f.duration or "")[:w_dur]
        airline = (f.airline or "")[:w_airline]
        stops_str = _stops_display(f.stops)
        print(fmt.format(orig, dest, f.price or "", airline, dep, arr, dur, stops_str))


if __name__ == "__main__":
    # New API: FlightQuery + search_flights(query, max_workers)
    query = FlightQuery(
        origin="BLR",
        destination="DXB",
        date="2026-07-20",
        return_date=None,
        passengers=Passengers(adults=1),
        currency="INR",
    )
    flights = search_flights(query, max_workers=3)
    for f in flights:
        print(f.price, f.airline, f.departure, f.duration)
    print_flight_results(flights)

    # Compat API (same shape for itinerary planner)
    results = search_flights_compat(
        from_place="Bangalore",
        to_place="Dubai",
        departure_date="20-07-2026",
        return_date="27-07-2026",
        limit=5,
    )
    if results:
        print("\nFirst page:", results.get("first_page", {}).get("content", "")[:200])
