"""OpenAI-format tool schemas and run_tool_call for OpenRouter/LLM demo."""

import json

from tools.flights import search_flights_compat
from tools.web_search import web_search

# OpenAI chat-completion tool format (OpenRouter compatible)
tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for current information. Use for opening hours, tips, events, or general facts about places.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keywords": {
                        "type": "string",
                        "description": "Search query string",
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results (default 5)",
                        "default": 5,
                    },
                },
                "required": ["keywords"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_flights",
            "description": "Search for round-trip flight options and prices between two places. Call this whenever the user asks about flights, trip from A to B with dates, or travel costs between cities with given dates. Returns real options with airline, price, departure time, and duration. Dates must be DD-MM-YYYY.",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_place": {
                        "type": "string",
                        "description": "Origin city or IATA code (e.g. Bangalore, BLR)",
                    },
                    "to_place": {
                        "type": "string",
                        "description": "Destination city or IATA code (e.g. Dubai, DXB)",
                    },
                    "departure_date": {
                        "type": "string",
                        "description": "Departure date in DD-MM-YYYY format (e.g. 01-03-2026)",
                    },
                    "return_date": {
                        "type": "string",
                        "description": "Return date in DD-MM-YYYY format (e.g. 05-03-2026)",
                    },
                    "adults": {
                        "type": "integer",
                        "description": "Number of adult passengers (default 1)",
                        "default": 1,
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Max number of results to return (default 7)",
                        "default": 7,
                    },
                },
                "required": ["from_place", "to_place", "departure_date", "return_date"],
            },
        },
    },
]


def run_tool_call(name: str, arguments: str) -> str:
    args = json.loads(arguments)
    if name == "web_search":
        print(f"Running web_search tool with arguments: {args}")
        keywords = args.get("keywords", "")
        max_results = args.get("max_results", 5)
        results = web_search(keywords, max_results=max_results)
        if not results:
            return "No search results found."
        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"{i}. {r.get('title', '')}\n   {r.get('href', '')}\n   {r.get('body', '')}")
        return "\n\n".join(lines)
    if name == "search_flights":
        print(f"Running search_flights tool with arguments: {args}")
        from_place = args.get("from_place", "")
        to_place = args.get("to_place", "")
        departure_date = args.get("departure_date", "")
        return_date = args.get("return_date", "")
        adults = args.get("adults", 1)
        limit = args.get("limit", 7)
        result = search_flights_compat(
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
    raise ValueError(f"Unknown tool: {name}")
