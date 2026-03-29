"""Append itinerary as an AI message for Chat UI / LangGraph Server."""

from langchain_core.messages import AIMessage

from itinerary_planner.state import PlannerState


def chat_response(state: PlannerState) -> dict:
    """Append an AIMessage with itinerary_text or summary so the Chat UI shows the reply."""
    itinerary_text = state.get("itinerary_text") or ""
    itinerary = state.get("itinerary")
    if not itinerary_text and itinerary:
        summary = (itinerary.get("summary") or "Itinerary ready.").strip()
        itinerary_text = f"{summary}\n\nSee full itinerary in state."
    if not itinerary_text:
        itinerary_text = "No itinerary was produced. Check for errors in state."
    return {"messages": [AIMessage(content=itinerary_text)]}
