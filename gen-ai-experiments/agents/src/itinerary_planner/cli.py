"""Small CLI to test flight_search and hotel_search."""

from __future__ import annotations

import argparse
import sys

from itinerary_planner.flight_search import (
    FlightQuery,
    Passengers,
    print_flight_results,
    search_flights,
    search_flights_compat,
)
from itinerary_planner.hotel_search import search_hotels


def _parse_date(s: str) -> str:
    """Accept YYYY-MM-DD or DD-MM-YYYY; return YYYY-MM-DD for FlightQuery."""
    s = (s or "").strip()
    if not s:
        return s
    parts = s.replace("/", "-").split("-")
    if len(parts) != 3:
        return s
    a, b, c = parts[0], parts[1], parts[2]
    if len(a) == 4 and a.isdigit():  # YYYY-MM-DD
        return f"{a}-{b.zfill(2)}-{c.zfill(2)}"
    # DD-MM-YYYY
    return f"{c}-{b.zfill(2)}-{a.zfill(2)}"


def _to_dd_mm_yyyy(iso: str) -> str:
    """Convert YYYY-MM-DD to DD-MM-YYYY for compat API."""
    if not iso or len(iso) < 10:
        return iso
    return f"{iso[8:10]}-{iso[5:7]}-{iso[0:4]}"


def cmd_flights(args: argparse.Namespace) -> int:
    """Run flight search and print results."""
    date_iso = _parse_date(args.date)
    return_iso = _parse_date(args.return_date) if args.return_date else None

    query = FlightQuery(
        origin=args.origin.strip(),
        destination=args.destination.strip(),
        date=date_iso,
        return_date=return_iso,
        passengers=Passengers(adults=args.adults),
        currency=args.currency or "USD",
    )

    print(f"Searching flights: {query.origin} → {query.destination} on {date_iso}", end="")
    if return_iso:
        print(f" return {return_iso}")
    else:
        print()

    flights = search_flights(query, max_workers=3)
    if args.limit and len(flights) > args.limit:
        flights = flights[: args.limit]

    print_flight_results(flights)
    if flights:
        print(f"\n({len(flights)} result(s))")
    return 0


def cmd_flights_compat(args: argparse.Namespace) -> int:
    """Run backward-compatible flight search (from_place, to_place, DD-MM-YYYY dates)."""
    date_iso = _parse_date(args.date)
    return_iso = _parse_date(args.return_date) if args.return_date else None
    dep = _to_dd_mm_yyyy(date_iso)
    ret = _to_dd_mm_yyyy(return_iso) if return_iso else "01-01-2020"

    print(f"Searching flights (compat): {args.origin} → {args.destination} ({dep} return {ret})")
    results = search_flights_compat(
        from_place=args.origin,
        to_place=args.destination,
        departure_date=dep,
        return_date=ret,
        adults=args.adults,
        curr=args.currency or "USD",
        limit=args.limit or 7,
    )
    if not results:
        print("No results")
        return 0
    for r in results.get("search_results", [])[: args.limit or 7]:
        print(f"  {r.get('title', '')}")
        print(f"    {r.get('body', '')}")
    fp = results.get("first_page", {})
    if fp:
        print(f"\nFirst page: {fp.get('title', '')}")
        print(f"  {fp.get('content', '')[:300]}...")
    return 0


def cmd_hotels(args: argparse.Namespace) -> int:
    """Run hotel search and print results."""
    print(f"Searching hotels: {args.location}" + (f" (budget: {args.budget})" if args.budget else ""))
    results = search_hotels(
        location=args.location,
        budget=args.budget or "",
        check_in=args.check_in or "",
        check_out=args.check_out or "",
        max_results=args.max_results,
    )
    if not results:
        print("No results")
        return 0
    for r in results.get("search_results", [])[: args.max_results]:
        print(f"  {r.get('title', '')}")
        print(f"    {r.get('body', '')[:200]}")
    fp = results.get("first_page", {})
    if fp:
        print(f"\nFirst page: {fp.get('title', '')}")
        print(f"  {fp.get('content', '')[:300]}...")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Test flight_search and hotel_search")
    sub = parser.add_subparsers(dest="command", required=True)

    # flights
    p_flights = sub.add_parser("flights", help="Search flights (FlightQuery API)")
    p_flights.add_argument("origin", help="Origin city or IATA (e.g. BLR, Bangalore)")
    p_flights.add_argument("destination", help="Destination city or IATA (e.g. DXB, Dubai)")
    p_flights.add_argument("date", help="Departure date (YYYY-MM-DD or DD-MM-YYYY)")
    p_flights.add_argument("--return-date", "-r", default=None, help="Return date (optional)")
    p_flights.add_argument("--adults", "-n", type=int, default=1)
    p_flights.add_argument("--currency", "-c", default="USD")
    p_flights.add_argument("--limit", "-l", type=int, default=10)
    p_flights.set_defaults(run=cmd_flights)

    # flights-compat
    p_compat = sub.add_parser("flights-compat", help="Search flights (compat API, DD-MM-YYYY)")
    p_compat.add_argument("origin", help="From place (e.g. Bangalore)")
    p_compat.add_argument("destination", help="To place (e.g. Dubai)")
    p_compat.add_argument("date", help="Departure date (DD-MM-YYYY)")
    p_compat.add_argument("--return-date", "-r", default="", help="Return date DD-MM-YYYY")
    p_compat.add_argument("--adults", "-n", type=int, default=1)
    p_compat.add_argument("--currency", "-c", default="USD")
    p_compat.add_argument("--limit", "-l", type=int, default=7)
    p_compat.set_defaults(run=cmd_flights_compat)

    # hotels
    p_hotels = sub.add_parser("hotels", help="Search hotels")
    p_hotels.add_argument("location", help="City or area (e.g. Paris, Dubai)")
    p_hotels.add_argument("--budget", "-b", default="", help="Budget hint (e.g. mid-range)")
    p_hotels.add_argument("--check-in", default="", help="Check-in date")
    p_hotels.add_argument("--check-out", default="", help="Check-out date")
    p_hotels.add_argument("--max-results", "-n", type=int, default=8)
    p_hotels.set_defaults(run=cmd_hotels)

    args = parser.parse_args()
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())


# Flights (new API)
# uv run python -m itinerary_planner.cli flights BLR DXB 2026-07-20
# uv run python -m itinerary_planner.cli flights Bangalore Dubai 20-07-2026 --return-date 27-07-2026 -l 5

# Flights (compat API)
# uv run python -m itinerary_planner.cli flights-compat Bangalore Dubai 20-07-2026 -r 27-07-2026

# Hotels
# uv run python -m itinerary_planner.cli hotels Paris
# uv run python -m itinerary_planner.cli hotels Dubai --budget mid-range -n 5
