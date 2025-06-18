#!/usr/bin/env python3
"""Run a browser-use agent for Codex."""

import asyncio
import sys

from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: browser_agent.py <model> <task>", file=sys.stderr)
        return 1
    model = sys.argv[1]
    task = " ".join(sys.argv[2:])

    agent = Agent(task=task, llm=ChatOpenAI(model=model))
    history = await agent.run()
    # Print the final result if available
    if history.final_result:
        print(history.final_result)
    return 0

if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
