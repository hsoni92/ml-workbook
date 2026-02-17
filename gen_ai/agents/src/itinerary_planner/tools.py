"""Optional tools: search, transport, price (mock or real APIs)."""

from __future__ import annotations

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
    def search_web(keywords: str, max_results: int = 5) -> str:
        """Search the web for current information. Use for opening hours, tips, events, or general facts about places."""
        results = web_search(keywords, max_results=max_results)
        if not results:
            return "No search results found."
        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"{i}. {r['title']}\n   {r.get('href', '')}\n   {r.get('body', '')}")
        return "\n\n".join(lines)

    return search_web


# Expose a single tool instance for binding to an LLM
search_web_tool = web_search_tool_for_agents() if tool else None


def mock_destination_info(destination: str) -> str:
    """Return mock destination info (e.g. opening hours, tips)."""
    return f"Mock info for {destination}: best visited in spring; main sights open 09:00–18:00."


def mock_transport_estimate(origin: str, destination: str) -> dict[str, Any]:
    """Return mock transport estimate between two places."""
    return {
        "from": origin,
        "to": destination,
        "mode": "train",
        "duration_minutes": 120,
        "estimated_cost": 50,
    }


def mock_night_price(city: str, budget: str) -> float:
    """Return mock price per night for city and budget level."""
    base = {"budget": 60, "mid-range": 120, "luxury": 280}.get(budget, 120)
    return base
