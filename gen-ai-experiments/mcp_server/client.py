import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        if name == "search_flights":
            result = await client.call_tool("search_flights", {"from_place": "BLR", "to_place": "DXB", "departure_date": "2026-03-01", "return_date": "2026-03-05"})
            print(result)
        elif name == "web_search":
            result = await client.call_tool("web_search", {"keywords": "New York"})
            print(result)
        else:
            print("Invalid tool name")

asyncio.run(call_tool("web_search"))
