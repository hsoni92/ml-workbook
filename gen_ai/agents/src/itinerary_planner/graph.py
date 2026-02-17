"""LangGraph: state schema, nodes, edges, compile."""

from langgraph.graph import END, START, StateGraph

from itinerary_planner.state import PlannerState
from itinerary_planner.nodes import (
    parse_input,
    research,
    plan_days,
    plan_transport,
    plan_accommodation,
    add_prices,
    build_itinerary,
    chat_response,
)


def build_planner_graph():
    """Build and compile the itinerary planner StateGraph."""
    builder = StateGraph(PlannerState)

    builder.add_node("parse_input", parse_input)
    builder.add_node("research", research)
    builder.add_node("plan_days", plan_days)
    builder.add_node("plan_transport", plan_transport)
    builder.add_node("plan_accommodation", plan_accommodation)
    builder.add_node("add_prices", add_prices)
    builder.add_node("build_itinerary", build_itinerary)
    builder.add_node("chat_response", chat_response)

    builder.add_edge(START, "parse_input")
    builder.add_edge("parse_input", "research")
    builder.add_edge("research", "plan_days")
    builder.add_edge("plan_days", "plan_transport")
    builder.add_edge("plan_transport", "plan_accommodation")
    builder.add_edge("plan_accommodation", "add_prices")
    builder.add_edge("add_prices", "build_itinerary")
    builder.add_edge("build_itinerary", "chat_response")
    builder.add_edge("chat_response", END)

    return builder.compile()


# Module-level compiled graph for LangGraph CLI (langgraph.json).
graph = build_planner_graph()
