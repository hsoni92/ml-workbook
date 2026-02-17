"""Optional tools: search, transport, price (mock or real APIs)."""

from __future__ import annotations

import asyncio
import json
from typing import Any

from loguru import logger

try:
    from ddgs import DDGS
    from ddgs.exceptions import DDGSException, RatelimitException, TimeoutException
except ImportError:
    DDGS = None  # type: ignore[misc, assignment]
    DDGSException = BaseException  # type: ignore[misc, assignment]
    RatelimitException = BaseException  # type: ignore[misc, assignment]
    TimeoutException = BaseException  # type: ignore[misc, assignment]

try:
    from itinerary_planner.flight_search import (
        search_flights_compat as _search_flights,
        search_flights_async as _search_flights_async,
    )
except ImportError:
    _search_flights = None  # type: ignore[misc, assignment]
    _search_flights_async = None  # type: ignore[misc, assignment]

try:
    from itinerary_planner.hotel_search import (
        search_hotels as _search_hotels,
        search_hotels_async as _search_hotels_async,
    )
except ImportError:
    _search_hotels = None  # type: ignore[misc, assignment]
    _search_hotels_async = None  # type: ignore[misc, assignment]

# LangChain tool for agent use (bind_tools, etc.)
try:
    from langchain_core.tools import tool
except ImportError:
    tool = None  # type: ignore[misc, assignment]


def web_search(keywords: str, max_results: int = 5) -> list[dict[str, str]]:
    """Run a DuckDuckGo text search and return results as list of {title, href, body}.

    Args:
        keywords: Search query string.
        max_results: Maximum number of results (default 5).

    Returns:
        List of dicts with keys title, href, body. Empty list on error or if package unavailable.
    """
    if DDGS is None:
        logger.warning("ddgs not installed; web_search is a no-op")
        return []
    try:
        with DDGS(timeout=10) as ddgs:
            results = list(ddgs.text(keywords, max_results=max_results))
            logger.debug(f">> Web search results: {results}")
        return [{"title": r.get("title", ""), "href": r.get("href", ""), "body": r.get("body", "")} for r in results]
    except (RatelimitException, TimeoutException, DDGSException) as e:
        logger.warning("DuckDuckGo search failed: {}", e)
        return []
    except Exception as e:
        logger.exception("web_search error: {}", e)
        return []


def web_search_tool_for_agents():
    """Return a LangChain tool that agents can use for web search (e.g. with bind_tools)."""
    if tool is None:
        raise ImportError("langchain_core.tools is required for web_search_tool_for_agents")

    @tool
    async def search_web(keywords: str, max_results: int = 5) -> str:
        """Search the web for current information. Use for opening hours, tips, events, or general facts about places."""
        # Run blocking DDGS/fake_useragent in a thread to avoid blocking the event loop (LangGraph)
        results = await asyncio.to_thread(web_search, keywords, max_results=max_results)
        if not results:
            return "No search results found."
        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"{i}. {r['title']}\n   {r.get('href', '')}\n   {r.get('body', '')}")
        return "\n\n".join(lines)

    return search_web


def search_flights(from_place: str, to_place: str, departure_date: str, return_date: str, *, headless: bool = True) -> dict[str, Any]:
    """Search flights via fast_flights (Google Flights). Dates in DD-MM-YYYY. Returns search_results and first_page (url, title, content)."""
    if _search_flights is None:
        logger.warning("flight_search module unavailable; search_flights is a no-op")
        return {}
    return _search_flights(from_place, to_place, departure_date, return_date, headless=headless)


def flight_search_tool_for_agents():
    """Return a LangChain tool for flight search (for bind_tools)."""
    if tool is None:
        raise ImportError("langchain_core.tools is required for flight_search_tool_for_agents")

    @tool
    async def search_flights_tool(
        from_place: str,
        to_place: str,
        departure_date: str,
        return_date: str,
    ) -> str:
        """Search for round-trip flight options and prices between two places. Call whenever the user has an origin and trip dates: search round-trip from origin to destination with departure_date = trip start, return_date = trip end. Returns real options with airline, price, departure time, and duration. Dates must be DD-MM-YYYY (e.g. 14-06-2024)."""
        logger.debug(f">> Flight search tool: {from_place}, {to_place}, {departure_date}, {return_date}")
        results = await _search_flights_async(from_place, to_place, departure_date, return_date)
        logger.debug(f">> Flight search results: {results}")
        if not results:
            return "No flight results found (or flight search unavailable)."
        return json.dumps(results, indent=2, ensure_ascii=False)

    return search_flights_tool


def search_hotels(
    location: str,
    budget: str = "",
    check_in: str = "",
    check_out: str = "",
    max_results: int = 8,
) -> dict[str, Any]:
    """Search hotels via DuckDuckGo. Returns search_results and first_page (url, title, content=snippet)."""
    if _search_hotels is None:
        logger.warning("hotel_search module unavailable; search_hotels is a no-op")
        return {}
    return _search_hotels(location, budget=budget, check_in=check_in, check_out=check_out, max_results=max_results)


def hotel_search_tool_for_agents():
    """Return a LangChain tool for hotel search (for bind_tools)."""
    if tool is None:
        raise ImportError("langchain_core.tools is required for hotel_search_tool_for_agents")

    @tool
    async def search_hotels_tool(
        location: str,
        budget: str = "",
        check_in: str = "",
        check_out: str = "",
    ) -> str:
        """Search for hotels in a location. Use to find hotel names, cost, and address from search results.
        Call once per destination/location. Budget can be e.g. budget, mid-range, luxury."""
        logger.debug(">> Hotel search tool: %s, budget=%s", location, budget)
        results = await _search_hotels_async(
            location, budget=budget, check_in=check_in, check_out=check_out
        )
        if not results:
            return "No hotel results found (or hotel search unavailable)."
        return json.dumps(results, indent=2, ensure_ascii=False)

    return search_hotels_tool


# Expose a single tool instance for binding to an LLM
search_web_tool = web_search_tool_for_agents() if tool else None
search_flights_tool = flight_search_tool_for_agents() if tool and _search_flights else None
search_hotels_tool = hotel_search_tool_for_agents() if tool and _search_hotels else None
