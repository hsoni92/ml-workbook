# Itinerary Planner

Agentic itinerary planner: one natural-language message → detailed day-by-day itinerary (destinations, transport, accommodation, prices). Built with **LangGraph** and **OpenRouter**, config from `.env`.

## Setup

- **Python**: 3.11–3.13 (required for `langgraph dev`; 3.14 is not yet supported by `langgraph-cli`’s native deps)
- **Package manager**: [uv](https://docs.astral.sh/uv/)

```bash
cd gen_ai/agents
uv sync
```

Copy env template and set your OpenRouter key:

```bash
cp .env.example .env
# Edit .env: set OPENROUTER_API_KEY=sk-or-v1-...
```

Get a key at [OpenRouter](https://openrouter.ai/keys). Optional: set `OPENROUTER_MODEL` (default `openai/gpt-4o-mini`). Optional ranking headers: `OPENROUTER_HTTP_REFERER`, `OPENROUTER_X_TITLE`.

## Run

```bash
uv run itinerary-planner
# Example message: "5 days in Paris and Lyon, mid-range budget, I like museums and food."

# Or pass your own message:
uv run itinerary-planner 7 days in Rome and Florence, luxury, art and wine
```

Or run as module:

```bash
uv run python -m itinerary_planner "3 days in Berlin, budget, street food"
```

## Run as server

Run the planner as a LangGraph API server and connect the [Agent Chat UI](https://agentchat.vercel.app/) (or a local create-agent-chat-app):

```bash
cd gen_ai/agents
uv sync
uv run langgraph dev --no-browser
```

Server runs at **http://127.0.0.1:2024** by default. In the Chat UI set:

- **Deployment URL**: `http://127.0.0.1:2024`
- **Graph ID** (or Assistant / Graph): **`itinerary`** — use this exact value. If you leave the default `agent`, you’ll get *Invalid assistant: 'agent'* (422).

Ensure `.env` has `OPENROUTER_API_KEY` (and optional `OPENROUTER_MODEL`); the server loads them via `langgraph.json`. Use Python 3.11–3.13 for `langgraph dev` (or `langgraph up` with Docker; see [LangGraph CLI docs](https://docs.langchain.com/langgraph-platform/cli)). If you only have Python 3.14, install 3.13 with `uv python install 3.13` and run `uv sync` again.

### Troubleshooting the server

- **"3 changes detected" every ~10 seconds**
  The dev server watches files for hot reload. To stop the repeated messages (and disable auto-reload), run:
  ```bash
  uv run langgraph dev --no-reload
  ```

- **422 "Invalid assistant: 'agent'"**
  The UI is sending graph/assistant id `agent` (its default). This server only has the graph **`itinerary`**. In the Chat UI, change **Graph ID** (or “Assistant” / “Graph”) from `agent` to **`itinerary`** and save/reconnect.

- **422 on `POST .../runs/stream` (other)**
  If 422 persists after setting Graph ID to `itinerary`, the run **input** may not match the graph’s state. This graph accepts:
  - **`messages`**: a list of LangChain-style messages, e.g. `[{ "type": "human", "content": "5 days in Paris, mid-range" }]`
  - **`user_message`**: a string, e.g. `"5 days in Paris, mid-range"`
  Use the server’s `/docs` (e.g. http://127.0.0.1:2024/docs) to see the run request schema or try a stateless run with curl:
  ```bash
  curl -X POST http://127.0.0.1:2024/runs/stream \
    -H "Content-Type: application/json" \
    -d '{"assistant_id": "itinerary", "input": {"messages": [{"type": "human", "content": "3 days in Berlin"}]}, "stream_mode": "updates"}'
  ```

### Conversation history and follow-ups

The planner supports **follow-up messages** (e.g. *"also add Bangalore as last location since I live there"*). It classifies each turn as a follow-up (refining the previous itinerary) or a new query, and when it’s a follow-up it merges your feedback into the full intent and re-plans.

For this to work in the Chat UI, conversation history must be available in state. Either:

- **Use a checkpointer with a stable `thread_id`** when invoking the graph (e.g. via the LangGraph server). The server typically sends a `thread_id` in the run config so that state (including `messages`) is restored and accumulated across turns. Ensure your client uses the same thread for a conversation so that the planner sees the previous assistant reply and can detect follow-ups.
- Or have the **client send the full `messages` array** on each request (all prior human and assistant messages). Then the planner can read the last assistant message from that list without a checkpointer.

Without either, only the latest user message is visible and the planner will treat every turn as a new query.

## Output

- **JSON**: `summary`, `days` (date, city, activities), `transport` (from → to, mode, times, cost), `accommodation` (place, check-in/out), `priceSummary`.
- **Markdown**: Human-readable itinerary printed after the JSON.

## Web search tool

The planner uses [ddgs](https://pypi.org/project/ddgs/) (DuckDuckGo search) for destination research (opening hours, tips). The **research** node runs a web search per destination and passes snippets into the day-planning prompt.

For agent use (e.g. an LLM with `bind_tools`), a LangChain tool is available:

```python
from itinerary_planner.tools import search_web_tool, web_search

# Plain function (used by the research node)
results = web_search("Paris museums opening hours", max_results=5)

# LangChain tool for agents
if search_web_tool:
    llm_with_tools = llm.bind_tools([search_web_tool])
```

`search_web_tool` is `None` if `langchain_core.tools` is not available.

## Design

See [DESIGN.md](DESIGN.md) for architecture (graph nodes, state schema, OpenRouter integration).

## File layout

```
gen_ai/agents/
├── .env                 # Not committed; OPENROUTER_API_KEY, OPENROUTER_MODEL
├── .env.example
├── DESIGN.md
├── langgraph.json       # LangGraph CLI: graph id "itinerary", env .env
├── README.md
├── pyproject.toml       # uv / hatch
└── src/itinerary_planner/
    ├── __init__.py
    ├── main.py          # Entry: load .env, build graph, run
    ├── graph.py         # LangGraph: state, nodes, edges, compile
    ├── state.py         # State schema (TypedDict)
    ├── llm.py           # OpenRouter via OpenAI SDK (from .env)
    ├── tools.py         # Web search (DuckDuckGo), LangChain tool for agents, mocks
    └── nodes/
        ├── parse_input.py
        ├── research.py
        ├── plan_days.py
        ├── plan_transport.py
        ├── plan_accommodation.py
        ├── add_prices.py
        ├── build_itinerary.py
        └── chat_response.py  # Appends AIMessage for Chat UI
```
