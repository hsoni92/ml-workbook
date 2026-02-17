"""MCP tools: flight search and web search."""

from tools.flights import (
    FlightQuery,
    FlightResult,
    Passengers,
    search_flights,
    search_flights_async,
    search_flights_compat,
)
from tools.web_search import web_search

__all__ = [
    "FlightQuery",
    "FlightResult",
    "Passengers",
    "search_flights",
    "search_flights_async",
    "search_flights_compat",
    "web_search",
]
