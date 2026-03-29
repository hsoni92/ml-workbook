"""Research agent node: LLM with tool-calling (search_web, search_flights)."""

from __future__ import annotations

import os
from typing import Any

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_openai import ChatOpenAI
from loguru import logger

import json

from itinerary_planner.prompt_garden import RESEARCH_AGENT_SYSTEM, RESEARCH_AGENT_USER_TEMPLATE
from itinerary_planner.state import PlannerState
from itinerary_planner.tools import search_flights_tool, search_hotels_tool, search_web_tool


def _date_to_dd_mm_yyyy(iso_date: str) -> str:
    """Convert YYYY-MM-DD to DD-MM-YYYY for flight tool."""
    if not iso_date or len(iso_date) < 10:
        return iso_date
    try:
        parts = iso_date.strip()[:10].split("-")
        if len(parts) == 3:
            y, m, d = parts[0], parts[1], parts[2]
            return f"{d}-{m}-{y}"
    except Exception:
        pass
    return iso_date


def _build_messages(parsed: dict[str, Any]) -> list[BaseMessage]:
    origin = (parsed.get("origin") or "").strip() or "Not specified"
    destinations = parsed.get("destinations") or []
    start_date = (parsed.get("start_date") or "").strip() or "Not specified"
    end_date = (parsed.get("end_date") or "").strip() or "Not specified"
    prefs = parsed.get("preferences") or []
    preferences = ", ".join(prefs) if prefs else "None"

    user_content = RESEARCH_AGENT_USER_TEMPLATE.format(
        origin=origin,
        destinations=", ".join(destinations) if destinations else "Not specified",
        start_date=start_date,
        end_date=end_date,
        preferences=preferences,
    )
    if start_date != "Not specified" and end_date != "Not specified":
        user_content += f"\n\nWhen calling search_flights use dates in DD-MM-YYYY format (e.g. {_date_to_dd_mm_yyyy(start_date)} for departure, {_date_to_dd_mm_yyyy(end_date)} for return)."
    if (
        origin != "Not specified"
        and destinations
        and start_date != "Not specified"
        and end_date != "Not specified"
    ):
        first_dest = (destinations[0] or "").strip()
        if first_dest and first_dest.lower() != origin.lower():
            user_content += f"\n\nYou must call search_flights for round-trip from {origin} to {first_dest} with the given dates before summarizing."

    return [
        SystemMessage(content=RESEARCH_AGENT_SYSTEM),
        HumanMessage(content=user_content),
    ]


def _extract_hotels_by_location(messages: list[BaseMessage]) -> dict[str, list[dict[str, str]]]:
    """From agent messages, extract hotel search results keyed by location."""
    tool_call_id_to_name_args: dict[str, tuple[str, dict]] = {}
    for msg in messages:
        if isinstance(msg, AIMessage) and getattr(msg, "tool_calls", None):
            for tc in msg.tool_calls:
                tid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", "")
                name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", "")
                args = tc.get("args", {}) if isinstance(tc, dict) else getattr(tc, "args", {}) or {}
                if tid:
                    tool_call_id_to_name_args[tid] = (name, args)
    hotels_by_location: dict[str, list[dict[str, str]]] = {}
    for msg in messages:
        if not isinstance(msg, ToolMessage):
            continue
        tid = getattr(msg, "tool_call_id", "") or (msg.additional_kwargs.get("tool_call_id") if hasattr(msg, "additional_kwargs") else "")
        name, args = tool_call_id_to_name_args.get(tid, (None, {}))
        if name != "search_hotels_tool":
            continue
        location = (args.get("location") or "").strip() or "Unknown"
        try:
            data = json.loads(msg.content) if isinstance(msg.content, str) else {}
        except json.JSONDecodeError:
            continue
        results = data.get("search_results") or []
        if results:
            hotels_by_location[location] = [
                {"title": r.get("title", ""), "href": r.get("href", ""), "body": r.get("body", "")}
                for r in results
            ]
    return hotels_by_location


def _extract_flight_by_leg(messages: list[BaseMessage]) -> dict[str, dict]:
    """From agent messages, extract flight search results keyed by leg (from_place to to_place)."""
    tool_call_id_to_name_args: dict[str, tuple[str, dict]] = {}
    for msg in messages:
        if isinstance(msg, AIMessage) and getattr(msg, "tool_calls", None):
            for tc in msg.tool_calls:
                tid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", "")
                name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", "")
                args = tc.get("args", {}) if isinstance(tc, dict) else getattr(tc, "args", {}) or {}
                if tid:
                    tool_call_id_to_name_args[tid] = (name, args)
    flight_by_leg: dict[str, dict] = {}
    for msg in messages:
        if not isinstance(msg, ToolMessage):
            continue
        tid = getattr(msg, "tool_call_id", "") or (msg.additional_kwargs.get("tool_call_id") if hasattr(msg, "additional_kwargs") else "")
        name, args = tool_call_id_to_name_args.get(tid, (None, {}))
        if name != "search_flights_tool":
            continue
        from_place = (args.get("from_place") or "").strip() or ""
        to_place = (args.get("to_place") or "").strip() or ""
        if not from_place or not to_place:
            continue
        try:
            data = json.loads(msg.content) if isinstance(msg.content, str) else {}
        except json.JSONDecodeError:
            continue
        if not isinstance(data, dict) or not data.get("search_results"):
            continue
        leg_key = f"{from_place} to {to_place}"
        flight_by_leg[leg_key] = {
            "search_results": data.get("search_results", []),
            "first_page": data.get("first_page") or {},
        }
    return flight_by_leg


def _get_tools() -> list:
    tools = []
    if search_web_tool is not None:
        tools.append(search_web_tool)
    if search_flights_tool is not None:
        tools.append(search_flights_tool)
    if search_hotels_tool is not None:
        tools.append(search_hotels_tool)
    return tools


def _get_llm():
    api_key = (os.getenv("OPENROUTER_API_KEY") or "").strip().split(",")[0].strip()
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is not set (required for research agent).")
    model = (os.getenv("OPENROUTER_MODEL") or "openai/gpt-4o-mini").strip()
    headers = {}
    if os.getenv("OPENROUTER_HTTP_REFERER", "").strip():
        headers["HTTP-Referer"] = os.getenv("OPENROUTER_HTTP_REFERER", "").strip()
    if os.getenv("OPENROUTER_X_TITLE", "").strip():
        headers["X-Title"] = os.getenv("OPENROUTER_X_TITLE", "").strip()
    return ChatOpenAI(
        model=model,
        temperature=0.2,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        default_headers=headers or None,
    )


async def research_agent(state: PlannerState) -> dict:
    """Run tool-calling agent to gather travel research; store summary in state['research']['agent_summary']."""
    parsed = state.get("parsed")
    if not parsed:
        return {"research": {"agent_summary": ""}}

    tools = _get_tools()
    if not tools:
        logger.warning("No tools available for research agent; skipping tool-calling.")
        return {"research": {"agent_summary": "Tool-calling skipped (no tools available)."}}

    try:
        llm = _get_llm().bind_tools(tools)
        messages = _build_messages(parsed)
        max_turns = 8
        turn = 0

        while turn < max_turns:
            turn += 1
            response = await llm.ainvoke(messages)
            if not getattr(response, "tool_calls", None):
                break
            messages.append(
                AIMessage(content=response.content or "", tool_calls=response.tool_calls)
            )
            for tc in response.tool_calls:
                name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", "")
                args = tc.get("args", {}) if isinstance(tc, dict) else getattr(tc, "args", {}) or {}
                tid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", "")
                tool_map = {t.name: t for t in tools}
                if name not in tool_map:
                    messages.append(ToolMessage(content=f"Unknown tool: {name}", tool_call_id=tid))
                    continue
                try:
                    result = await tool_map[name].ainvoke(args)
                    content = result if isinstance(result, str) else str(result)
                except Exception as e:
                    content = f"Tool error: {e}"
                    logger.warning("Tool {} failed: {}", name, e)
                messages.append(ToolMessage(content=content, tool_call_id=tid))

        summary = (response.content or "").strip() if response else ""
        hotels_by_location = _extract_hotels_by_location(messages)
        flight_by_leg = _extract_flight_by_leg(messages)
        research_out: dict[str, Any] = {"agent_summary": summary}
        if hotels_by_location:
            research_out["hotels_by_location"] = hotels_by_location
        if flight_by_leg:
            research_out["flight_by_leg"] = flight_by_leg
        return {"research": research_out}
    except Exception as e:
        logger.exception("research_agent failed: {}", e)
        return {"research": {"agent_summary": f"Research agent failed: {e}"}}
