"""Hotel search via DuckDuckGo (web_search). Returns search results with names, cost, address from snippets."""

from __future__ import annotations

import asyncio
from typing import Any

from loguru import logger


def _hotel_search_query(location: str, budget: str = "", check_in: str = "", check_out: str = "") -> str:
    """Build a query that tends to return hotel listings with names, prices, address."""
    parts = [f"hotels in {location}"]
    if budget:
        parts.append(budget)
    parts.append("prices address")
    if check_in:
        parts.append(f"check-in {check_in}")
    if check_out:
        parts.append(f"check-out {check_out}")
    return " ".join(parts)


def search_hotels(
    location: str,
    budget: str = "",
    check_in: str = "",
    check_out: str = "",
    max_results: int = 8,
) -> dict[str, Any]:
    """Search hotels via DuckDuckGo. Returns search results only (no link clicking or scraping).

    Uses web_search from tools. Returns same shape as flight_search for consistency.

    Returns:
        Dict with keys: search_results (list of {title, href, body}), first_page (url, title, content=snippet).
        Empty dict on error or if dependencies unavailable.
    """
    from itinerary_planner.tools import web_search

    query = _hotel_search_query(location, budget=budget, check_in=check_in, check_out=check_out)
    try:
        search_results = web_search(query, max_results=max_results)
        if not search_results:
            return {}
        first = search_results[0]
        href = first.get("href") or ""
        title = first.get("title") or ""
        body = first.get("body") or ""
        logger.debug(">> Hotel search query: {} -> top: {}", query, title)
        return {
            "search_results": search_results,
            "first_page": {"url": href, "title": title, "content": body},
        }
    except Exception as e:
        logger.exception("hotel_search error: {}", e)
        return {}


async def search_hotels_async(
    location: str,
    budget: str = "",
    check_in: str = "",
    check_out: str = "",
    max_results: int = 8,
) -> dict[str, Any]:
    """Search hotels via DuckDuckGo (async). Returns search results only.

    Returns:
        Dict with keys: search_results, first_page (url, title, content=snippet). Empty dict on error.
    """
    # Run blocking web_search in a thread to avoid blocking the event loop (LangGraph)
    return await asyncio.to_thread(
        search_hotels,
        location,
        budget=budget,
        check_in=check_in,
        check_out=check_out,
        max_results=max_results,
    )
