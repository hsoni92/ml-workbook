"""State schema for the itinerary planner graph."""

from typing import Annotated, Any, Optional

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


# --- Parsed intent (from parse_input) ---
class ParsedIntent(TypedDict, total=False):
    """Structured intent extracted from user message."""

    origin: Optional[str]  # departure/return city e.g. Bangalore when user says "from X" or "trip from X to Y"
    destinations: list[str]
    start_date: str
    end_date: str
    trip_duration_days: Optional[int]  # explicit N when user says "N days" or "N-day trip"; overrides date span
    budget: str  # e.g. budget, mid-range, luxury
    preferences: list[str]  # e.g. museums, food, outdoors
    transport_preference: Optional[str]  # e.g. train, flight, car; empty if not specified


# --- Day plan ---
class Activity(TypedDict, total=False):
    title: str
    time: str
    estimated_cost: Optional[float]
    notes: Optional[str]


class DayPlan(TypedDict, total=False):
    date: str
    city: str
    activities: list[Activity]
    notes: Optional[str]


# --- Transport ---
class TransportLeg(TypedDict, total=False):
    from_place: str
    to: str
    mode: str
    duration_minutes: Optional[int]
    departure: Optional[str]
    arrival: Optional[str]
    estimated_cost: Optional[float]


# --- Accommodation ---
class AccommodationStay(TypedDict, total=False):
    place: str
    check_in: str
    check_out: str
    city: str
    nights: Optional[int]
    estimated_cost_per_night: Optional[float]


# --- Prices summary ---
class PriceSummary(TypedDict, total=False):
    transport: float
    accommodation: float
    activities: float
    total_estimated: float
    currency: str


# --- Final itinerary output ---
class ItineraryDay(TypedDict, total=False):
    date: str
    city: str
    activities: list[dict[str, Any]]
    notes: Optional[str]


class ItineraryTransport(TypedDict, total=False):
    from_place: str
    to: str
    mode: str
    departure: str
    arrival: str
    duration_minutes: int
    estimated_cost: Optional[float]


class ItineraryAccommodation(TypedDict, total=False):
    place: str
    check_in: str
    check_out: str
    nights: int
    estimated_cost_per_night: Optional[float]


class ItineraryOutput(TypedDict, total=False):
    summary: str
    days: list[ItineraryDay]
    transport: list[ItineraryTransport]
    accommodation: list[ItineraryAccommodation]
    price_summary: PriceSummary


# --- Graph state (single shared state) ---
class PlannerState(TypedDict, total=False):
    """Shared state for the itinerary planner graph."""

    user_message: str
    is_follow_up: Optional[bool]  # True when current turn was classified as follow-up (for observability)
    parsed: Optional[ParsedIntent]
    research: Optional[dict[str, Any]]
    days: list[DayPlan]
    transport_legs: list[TransportLeg]
    accommodation: list[AccommodationStay]
    prices: Optional[PriceSummary]
    itinerary: Optional[ItineraryOutput]
    itinerary_text: Optional[str]  # markdown
    messages: Annotated[list[BaseMessage], add_messages]
    error: Optional[str]
