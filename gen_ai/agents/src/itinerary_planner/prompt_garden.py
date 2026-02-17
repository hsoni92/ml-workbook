"""Centralized prompts for structured LLM calls. All include a common JSON-only instruction."""

STRUCTURED_JSON_INSTRUCTION = (
    "Respond with only valid JSON. Do not wrap in markdown code blocks (no ```json). "
    "Do not add any explanation, commentary, or text before or after the JSON."
)


def structured_prompt(body: str) -> str:
    """Prepend the common JSON-only instruction to a task prompt."""
    return f"{STRUCTURED_JSON_INSTRUCTION}\n\n{body}"


# --- Follow-up vs new query ---
FOLLOW_UP_CLASSIFIER_PROMPT = structured_prompt("""You are classifying the user's current message in a travel itinerary chat.

Previous assistant reply (itinerary or summary):
{previous_assistant_response}

User's current message:
{user_message}

Is the user asking to modify or refine the previous itinerary (e.g. add a city, change dates, adjust something) or starting a completely new trip request? Return JSON with a single key "result" and value either "follow_up" or "new_query".""")

# --- Parse intent ---
PARSE_PROMPT = structured_prompt("""Extract travel intent from this message. Infer dates and budget level if not explicit.
Today's date (for reference): {today}
Return only the structured fields. Use today's date context if they say "next week" or similar.
- origin: Set when the user says "from X", "starting from X", or "trip from X to Y" (X is the origin city). Otherwise leave empty.
- trip_duration_days: Set to the number N when the user says "N days", "N-day trip", "for 15 days", etc. Otherwise leave null.
- If the user does not specify travel dates, leave start_date and end_date empty; they will be set automatically (using trip_duration_days if provided).
- Only set transport_preference if the user explicitly says how they want to travel (e.g. "by train", "flying", "drive"). Otherwise leave it empty.
- destinations: List cities or regions to visit; if the user names a country (e.g. Philippines, Japan), you may return that country as a single destination; it will be expanded later.

User message:
{user_message}
""")

# --- Parse intent with conversation context (follow-up) ---
PARSE_WITH_CONTEXT_PROMPT = structured_prompt("""The user is giving feedback on a previous itinerary. Extract the FULL updated travel intent after applying their feedback.
Today's date (for reference): {today}

Previous assistant response (itinerary or summary):
{previous_assistant_response}

User's follow-up:
{user_follow_up}

Merge the user's feedback into a single complete intent: e.g. add or remove a city, change order (e.g. "add X as last location"), change dates, budget, or preferences. Return the complete list of destinations (in order if specified), dates, budget, preferences. Include origin if the user mentioned where they start/return from, and trip_duration_days if they specified a number of days. Use today's date context if needed. If dates are not specified, leave start_date and end_date empty. Only set transport_preference if the user explicitly mentions how they want to travel. Otherwise leave it empty.

Return only the structured fields.""")


# --- Expand country to regions (research node) ---
EXPAND_COUNTRY_PROMPT = structured_prompt("""The user's trip destination is "{country}".
If "{country}" is a country (e.g. Philippines, Japan, Thailand), return 3-5 representative regions or cities that tourists typically visit, in a sensible order (e.g. Manila, Palawan, Boracay, Cebu for Philippines).
If "{country}" is already a city or region, return a list containing only that one place: ["{country}"].

Return JSON with a single key "regions" containing a list of strings (e.g. ["Manila", "Palawan", "Boracay"]).
""")


# --- Plan days ---
PLAN_DAYS_PROMPT = structured_prompt("""Create a day-by-day itinerary.
Today's date (reference): {today}

Parsed intent:
- Origin (trip starts and ends here): {origin}
- Destinations to cover: {destinations}
- Start date: {start_date}
- End date: {end_date}
- Budget: {budget}
- Preferences: {preferences}

Research/constraints (if any): {research}

You MUST output exactly one day object for every calendar day from start_date to end_date (inclusive). The number of day objects MUST equal the number of days in the date range. No fewer, no more.
When the user names a country (e.g. Philippines, Japan), you MUST spread the itinerary across multiple regions (e.g. Manila, Palawan, Boracay), not just one city. Each region should get at least one full day.
Respect preferences strongly: e.g. if the user wants "nature", "outdoors", or "places close to nature", prioritize beaches, islands, national parks, wildlife, and natural scenery; avoid an urban-only itinerary unless the user also asks for cities.
Each destination must get at least one full day. Distribute destinations across the days in the order given. Do not put multiple cities on the same day unless the date range is shorter than the number of destinations.
For each day specify city, 2-4 activities with rough times, and optional notes.
Return JSON with a single key "days" containing a list of day objects with: date (YYYY-MM-DD), city, activities (list of {{title, time, notes}}), notes.
""")


# --- Plan transport ---
PLAN_TRANSPORT_PROMPT = structured_prompt("""Given the day-by-day itinerary, list every transport leg needed to move between cities/locations.
Only include legs where the user actually travels (e.g. Paris -> Lyon), not same-day local movement.

Days (each has date and city):
{days}

Required legs (you MUST include each of these in order):
{required_legs}

User transport preference (only use if non-empty): {transport_preference}

Web research on best/easiest transport for each leg (use this to choose mode when user did not specify):
{transport_research}

For each required leg provide: from_place, to, mode (e.g. TGV, train, flight, car), duration_minutes, departure, arrival (use dates from the itinerary).
For legs that connect the trip origin (where the traveller starts and ends) to the first or last destination: use "flight" when cities are in different countries or far apart (e.g. Bangalore to Manila). Otherwise use train/car as appropriate.
If the user specified a transport preference, use it for all legs where it makes sense. Otherwise pick the best option based on the web research above.
Return JSON with key "legs" containing a list of legs in the same order as the required legs.
""")


# --- Plan accommodation ---
PLAN_ACCOMMODATION_PROMPT = structured_prompt("""From the day plan and transport legs, determine where the user stays each night.
Assign one accommodation stay per location (e.g. 2 nights in Paris, then 2 in Lyon). Include check-in and check-out date/time aligned with transport.

Days:
{days}

Transport legs (departure/arrival times):
{transport}

For each stay provide: place (e.g. "Hotel X, Paris"), check_in, check_out (use ISO or readable datetime), city.
Return JSON with key "stays" containing the list.
""")


# --- Add prices ---
ADD_PRICES_PROMPT = structured_prompt("""Estimate costs for this trip. Budget level: {budget}. Use {currency}.

Transport legs (estimate per leg in {currency}):
{transport}

Include realistic estimates for flight legs (e.g. international or long-distance): do not use 0 for flights. Use typical economy/mid-range fares for the given budget level.

Accommodation stays (estimate per night):
{accommodation}

Days with activities (estimate per activity or per day):
{days}

Return a single JSON object with: transport (total), accommodation (total), activities (total), total_estimated, currency.
Use realistic estimates for the given budget level and region.
""")
