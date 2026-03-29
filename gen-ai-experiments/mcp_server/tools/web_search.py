"""Web search via DuckDuckGo (ddgs)."""

from __future__ import annotations

try:
    from ddgs import DDGS
    from ddgs.exceptions import DDGSException, RatelimitException, TimeoutException
except ImportError:
    DDGS = None  # type: ignore[misc, assignment]
    DDGSException = BaseException  # type: ignore[misc, assignment]
    RatelimitException = BaseException  # type: ignore[misc, assignment]
    TimeoutException = BaseException  # type: ignore[misc, assignment]

try:
    from loguru import logger
except ImportError:
    logger = None  # type: ignore[misc, assignment]


def web_search(keywords: str, max_results: int = 5) -> list[dict[str, str]]:
    """Run a DuckDuckGo text search and return results as list of {title, href, body}.

    Args:
        keywords: Search query string.
        max_results: Maximum number of results (default 5).

    Returns:
        List of dicts with keys title, href, body. Empty list on error or if package unavailable.
    """
    if DDGS is None:
        if logger:
            logger.warning("ddgs not installed; web_search is a no-op")
        return []
    try:
        with DDGS(timeout=10) as ddgs:
            results = list(ddgs.text(keywords, max_results=max_results))
            if logger:
                logger.debug(f">> Web search results: {results}")
        return [{"title": r.get("title", ""), "href": r.get("href", ""), "body": r.get("body", "")} for r in results]
    except (RatelimitException, TimeoutException, DDGSException) as e:
        if logger:
            logger.warning("DuckDuckGo search failed: {}", e)
        return []
    except Exception as e:
        if logger:
            logger.exception("web_search error: {}", e)
        return []
