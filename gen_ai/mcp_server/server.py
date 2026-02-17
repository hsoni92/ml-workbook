import asyncio
import json

from fastmcp import FastMCP

from tools.flights import search_flights_async
from tools.web_search import web_search as web_search_impl

mcp = FastMCP("Itenary MCP Server")


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool
async def web_search(keywords: str, max_results: int = 5) -> str:
    """Search the web for current information. Use for opening hours, tips, events, or general facts about places.
    Returns formatted results with title, link, and snippet for each result."""
    results = await asyncio.to_thread(web_search_impl, keywords, max_results)
    if not results:
        return "No search results found."
    lines = []
    for i, r in enumerate(results, 1):
        lines.append(f"{i}. {r['title']}\n   {r.get('href', '')}\n   {r.get('body', '')}")
    return "\n\n".join(lines)


@mcp.tool
async def search_flights(
    from_place: str,
    to_place: str,
    departure_date: str,
    return_date: str,
    adults: int = 1,
    limit: int = 7,
) -> str:
    """Search for flights between two places. Use for round-trip options and prices.
    Dates must be in DD-MM-YYYY format (e.g. 14-06-2024)."""
    result = await search_flights_async(
        from_place,
        to_place,
        departure_date,
        return_date,
        adults=adults,
        limit=limit,
    )
    if not result:
        return "No flight results found (or flight search unavailable)."
    return json.dumps(result, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)