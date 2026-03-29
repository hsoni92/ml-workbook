"""
Tool-calling demo using OpenRouter (OpenAI-compatible API).
Based on the user prompt, calls either web_search or search_flights.
Uses OPENROUTER_API_KEY (comma-separated for rotation) and optional OPENROUTER_MODEL from .env.
"""
import sys

from llm_client import _client, model
from tools.llm_tools import run_tool_call, tools


SYSTEM_PROMPT = (
    "You have access to web_search and search_flights. "
    "When the user asks about flights, prices, or travel between two places with dates, you MUST call search_flights with from_place, to_place, departure_date and return_date (DD-MM-YYYY) before answering. "
    "When they ask about facts, opening hours, or tips, use web_search. "
    "Prefer calling the relevant tool instead of answering without it."
)


def run_llm(prompt: str) -> str:
    """Run the LLM with tool calls; returns final assistant text."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    response = _client().chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    choice = response.choices[0]
    message = choice.message
    messages.append(message)

    while getattr(message, "tool_calls", None):
        for tc in message.tool_calls:
            result = run_tool_call(tc.function.name, tc.function.arguments)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                }
            )

        response = _client().chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        choice = response.choices[0]
        message = choice.message
        messages.append(message)

    return message.content or ""


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Your prompt: ").strip()
    if not prompt:
        print("Usage: uv run python llm.py <prompt>   or run and type prompt when asked.")
        sys.exit(1)
    final_text = run_llm(prompt)
    print(final_text)
