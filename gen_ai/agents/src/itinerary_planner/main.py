"""Entry point: load .env, build graph, run with user message."""

import json
import sys

from dotenv import load_dotenv
from loguru import logger

from itinerary_planner.graph import build_planner_graph
from itinerary_planner.log import LLMLoggingCallback, configure_logging


def main() -> None:
    load_dotenv()
    configure_logging()
    logger.info("Starting itinerary planner")

    graph = build_planner_graph()

    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = (
            "5 days in Paris and Lyon, mid-range budget, "
            "I like museums and food."
        )
        print("Using example message (pass your own as args):")
        print(f"  {user_message}\n")

    initial_state: dict = {
        "user_message": user_message,
        "days": [],
        "transport_legs": [],
        "accommodation": [],
    }

    logger.debug("Invoking graph with user_message length={}", len(user_message))
    result = graph.invoke(
        initial_state,
        config={"callbacks": [LLMLoggingCallback()]},
    )

    if result.get("error"):
        logger.error("Planner error: {}", result["error"])
        print("Error:", result["error"])
        sys.exit(1)

    itinerary = result.get("itinerary")
    if itinerary:
        # API shape: use "from" in transport (design doc)
        out = dict(itinerary)
        if "transport" in out:
            out["transport"] = [
                {("from" if k == "from_place" else k): v for k, v in t.items()}
                for t in out["transport"]
            ]
        print("--- Itinerary (JSON) ---")
        print(json.dumps(out, indent=2, default=str))

    itinerary_text = result.get("itinerary_text")
    if itinerary_text:
        print("\n--- Itinerary (Markdown) ---")
        print(itinerary_text)

    logger.info("Itinerary planner finished successfully")


if __name__ == "__main__":
    main()
