# Itinerary Planner — Design Document

## 1. Overview

An **itinerary planner** that accepts a user’s travel intent as a single natural-language message and produces a **detailed day-by-day itinerary**, including:

- **Destinations & activities** — what to do each day
- **Inter-place travel** — how to move between locations (modes, routes, durations)
- **Accommodation** — when to check in and check out, and where
- **Prices** — estimated costs for transport, hotels, and activities (where available)

The system is **agentic**: multiple steps (parsing, research, transport, accommodation, pricing, synthesis) are orchestrated with **LangGraph**, and the LLM is provided by **OpenRouter** (keys and model from `.env`).

---

## 2. User Flow

1. **Input**: User sends one message, e.g.  
   *“5 days in Paris and Lyon, mid-range budget, I like museums and food.”*
2. **Processing**: The graph runs nodes to parse intent, (optionally) gather data, plan days, transport, hotels, and prices.
3. **Output**: A structured itinerary (e.g. JSON + optional markdown) with:
   - Per-day breakdown
   - Transport legs (from → to, mode, duration, approximate cost)
   - Hotel stays (name, check-in/check-out date and time)
   - Activity suggestions with rough prices
   - Total or per-category budget estimates

---

## 3. Technology Stack

| Component        | Choice                                      |
|-----------------|---------------------------------------------|
| Orchestration   | **LangGraph** (graph of nodes + state)      |
| LLM             | **OpenRouter** (any model via one API)      |
| Config          | **`.env`** for API keys and model           |
| Language        | **JavaScript/TypeScript** (Node)            |

### 3.1 Environment Variables (`.env`)

Read all OpenRouter and app config from `.env` (do not commit `.env`; use `.env.example` as template).

```bash
# Required: OpenRouter API key (https://openrouter.ai/keys)
OPENROUTER_API_KEY=sk-or-v1-...

# Optional: model override (default e.g. openai/gpt-4o-mini or anthropic/claude-3-haiku)
OPENROUTER_MODEL=openai/gpt-4o-mini

# Optional: base URL if using LangChain's OpenAI-compatible client
# OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Usage in code:

- Load with `dotenv` (or similar) at startup.
- Create the LangChain chat model with:
  - `openai`-compatible client,
  - `baseURL`: `https://openrouter.ai/api/v1`,
  - `apiKey`: `process.env.OPENROUTER_API_KEY`,
  - `model`: `process.env.OPENROUTER_MODEL` or a default.

---

## 4. LangGraph Architecture

### 4.1 High-Level Graph

The workflow is a **StateGraph** with one shared state. Flow is linear with optional branches (e.g. “need more info” vs “continue”).

```
                    ┌─────────────────┐
                    │  parse_input     │  Extract destinations, dates, budget, preferences
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  research       │  Optional: enrich destinations, get constraints
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
│ plan_days       │ │ plan_transport  │ │ plan_accommodation│  (can be parallel or ordered)
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                    ┌────────▼────────┐
                    │  add_prices     │  Attach estimates to each item
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  build_itinerary│  Single structured output (JSON + text)
                    └────────┬────────┘
                             │
                            END
```

### 4.2 State Schema

All nodes read and write the same state. Use a **StateSchema** (or TypedDict-like structure) with clear fields and, where needed, reducers (e.g. append for lists).

Suggested state shape:

| Field               | Type     | Description |
|---------------------|----------|-------------|
| `userMessage`       | `string` | Raw user input. |
| `parsed`            | `object` | Parsed intent: `{ destinations, startDate, endDate, budget, preferences }`. |
| `research`          | `object` | Optional research notes (opening hours, tips, constraints). |
| `days`              | `array`  | Day plans: `{ date, city, activities[], notes }`. |
| `transportLegs`     | `array`  | Legs: `{ from, to, mode, durationMinutes, departure, arrival }`. |
| `accommodation`     | `array`  | Stays: `{ place, checkIn, checkOut, city }`. |
| `prices`            | `object` | Per-leg, per-stay, per-activity estimates and totals. |
| `itinerary`         | `object` | Final output: `{ summary, days[], transport[], accommodation[], priceSummary }`. |
| `messages`          | `list`   | Optional: conversation messages (if using chat + reducer). |
| `error`             | `string` | Optional: last error message. |

Reducers:

- **Override** for single-value fields (`parsed`, `research`, `days`, `transportLegs`, `accommodation`, `prices`, `itinerary`, `error`).
- **Append** (e.g. `add_messages`) for `messages` if you keep chat history in state.

### 4.3 Nodes (Agents / Steps)

1. **`parse_input`**
   - **Input**: `userMessage`.
   - **Action**: Call LLM (OpenRouter) to extract structured intent: destinations, date range, budget level (e.g. budget/mid-range/luxury), preferences (e.g. museums, food, outdoors).
   - **Output**: Update `parsed` in state. On failure, set `error` and optionally route to END or retry.

2. **`research`** (optional)
   - **Input**: `parsed`, optionally `userMessage`.
   - **Action**: Use tools (e.g. web search, mock “destination info” API) or LLM to add constraints (weather, events, opening hours). Can be no-op if no tools.
   - **Output**: Update `research`.

3. **`plan_days`**
   - **Input**: `parsed`, `research`.
   - **Action**: LLM produces a day-by-day plan: which city each day, main activities, rough timing.
   - **Output**: Update `days`.

4. **`plan_transport`**
   - **Input**: `parsed`, `days`.
   - **Action**: For each transition between cities (or key points), LLM (or a tool) decides mode (train, car, flight, etc.), duration, and suggested departure/arrival. Can use tools for real routes or mock data.
   - **Output**: Update `transportLegs`.

5. **`plan_accommodation`**
   - **Input**: `parsed`, `days`, `transportLegs`.
   - **Action**: Decide where the user stays each night; for each stay set check-in and check-out (date + time).
   - **Output**: Update `accommodation`.

6. **`add_prices`**
   - **Input**: `transportLegs`, `accommodation`, `days`, `parsed.budget`.
   - **Action**: Attach estimated prices (per transport leg, per night, per activity or day). Use LLM to estimate or call mock/real APIs. Compute totals.
   - **Output**: Update `prices` (and optionally annotate legs/stays with `estimatedCost`).

7. **`build_itinerary`**
   - **Input**: `days`, `transportLegs`, `accommodation`, `prices`.
   - **Action**: LLM (or pure code) formats everything into the final structure: summary, daily breakdown, “how to get from A to B”, check-in/check-out table, price summary.
   - **Output**: Update `itinerary` and optionally a human-readable `itinerary.text` (markdown).

### 4.4 Edges

- **START → `parse_input`**
- **`parse_input` → `research`** (or conditional: skip if no tools)
- **`research` → `plan_days`**
- **`plan_days` → `plan_transport`**
- **`plan_transport` → `plan_accommodation`**
- **`plan_accommodation` → `add_prices`**
- **`add_prices` → `build_itinerary`**
- **`build_itinerary` → END**

Conditional edges (optional):

- After `parse_input`: if parsing fails or required fields missing → END or a “clarify” node that asks the user for more info (if you add a second turn).
- After `research`: always to `plan_days` (or skip research with a “no research” branch).

### 4.5 Tools (Optional)

- **Search / destination info**: e.g. DuckDuckGo or a mock function returning opening hours or “best time to visit”.
- **Transport**: mock or real API returning modes and durations between two places.
- **Prices**: mock or real API returning estimated cost for a leg or a night in a city.

Tools are invoked from within a node (e.g. in `research`, `plan_transport`, or `add_prices`) and results are written into state. All tool calls use the same OpenRouter-backed LLM when the node is LLM-driven.

---

## 5. OpenRouter Integration

- **Config**: Use only `.env` for `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`. No keys in code.
- **Client**: Use an OpenAI-compatible client (e.g. `@langchain/openai` or `openai` package) with:
  - `baseURL`: `https://openrouter.ai/api/v1`
  - `apiKey`: from `process.env.OPENROUTER_API_KEY`
  - `model`: from `process.env.OPENROUTER_MODEL` or a safe default
- **LangGraph**: Every node that calls an LLM uses this same chat model instance so the whole agentic system runs on OpenRouter.

---

## 6. Output Shape (Itinerary)

The `itinerary` state field (and API response) should look like:

```json
{
  "summary": "5-day trip to Paris and Lyon, mid-range budget.",
  "days": [
    {
      "date": "2025-03-10",
      "city": "Paris",
      "activities": [
        { "title": "Louvre", "time": "09:00–12:00", "estimatedCost": 17 }
      ],
      "notes": "..."
    }
  ],
  "transport": [
    {
      "from": "Paris",
      "to": "Lyon",
      "mode": "TGV",
      "departure": "2025-03-12T09:00",
      "arrival": "2025-03-12T11:30",
      "durationMinutes": 150,
      "estimatedCost": 45
    }
  ],
  "accommodation": [
    {
      "place": "Hotel X, Paris",
      "checkIn": "2025-03-10T15:00",
      "checkOut": "2025-03-12T11:00",
      "nights": 2,
      "estimatedCostPerNight": 120
    }
  ],
  "priceSummary": {
    "transport": 90,
    "accommodation": 480,
    "activities": 150,
    "totalEstimated": 720,
    "currency": "EUR"
  }
}
```

Plus an optional `itinerary.text` (markdown) for display.

---

## 7. Implementation Notes

- **LangGraph (JS)**: Use `@langchain/langgraph` (and `@langchain/core`). Define state with `StateSchema`, add nodes as functions `(state) => partialUpdate`, connect with `addEdge` / `addConditionalEdges`, then `compile()`.
- **Idempotency**: Nodes should depend only on state; avoid non-deterministic side effects where possible so replay/debugging is easier.
- **Errors**: On LLM or tool failure, set `state.error` and optionally route to END or a recovery node.
- **Streaming**: If the product needs incremental output, stream from the node that produces the final text (e.g. `build_itinerary`) or use LangGraph’s stream API and expose `itinerary` updates as they’re written.
- **.env**: Keep `.env` in `.gitignore`; document all variables in `.env.example` (OpenRouter key, model, and any optional search/delay keys if you add them later).

---

## 8. File Structure (Suggested)

```
gen_ai/agents/
├── .env                 # Not committed; keys and OPENROUTER_MODEL
├── .env.example         # Template (OPENROUTER_API_KEY, OPENROUTER_MODEL)
├── DESIGN.md            # This document
├── package.json
├── src/
│   ├── index.js         # Entry: load .env, build graph, run or serve
│   ├── graph.js         # LangGraph: state schema, nodes, edges, compile
│   ├── nodes/
│   │   ├── parseInput.js
│   │   ├── research.js
│   │   ├── planDays.js
│   │   ├── planTransport.js
│   │   ├── planAccommodation.js
│   │   ├── addPrices.js
│   │   └── buildItinerary.js
│   ├── llm.js           # Create OpenRouter-backed chat model from .env
│   ├── tools.js         # Optional: search, transport, price tools
│   └── state.js         # State schema and reducers
└── README.md            # How to run, env vars, example input/output
```

---

## 9. Summary

- **Product**: Single-message → detailed itinerary (days, transport, check-in/check-out, prices).
- **Stack**: LangGraph (orchestration) + OpenRouter (LLM), config from `.env`.
- **Graph**: Linear pipeline of nodes (parse → research → plan days → plan transport → plan accommodation → add prices → build itinerary) with one shared state.
- **State**: Holds raw message, parsed intent, research, days, transport legs, accommodation, prices, and final itinerary object.
- **Output**: Structured JSON plus optional markdown, suitable for API or UI.

This design is ready to implement in JavaScript/TypeScript with `@langchain/langgraph` and an OpenRouter-configured chat model.
