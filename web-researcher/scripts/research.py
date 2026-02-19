#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "dashscope",
#   "urllib3<2",
# ]
# [tool.uv]
# exclude-newer = "2025-02-18T00:00:00Z"
# ///
"""
Qwen Web Researcher

Performs agentic web research using DashScope Qwen model with built-in search.
Uses streaming but returns only the final answer (not the reasoning process).

Usage:
    uv run research.py "Your research question"
    ./research.py "Your research question"  (if executable)

Environment:
    DASHSCOPE_API_KEY - Required. Your DashScope API key.
"""

import sys
import os
import dashscope


def main():
    # Get query from command line arguments
    if len(sys.argv) < 2:
        print("Usage: uv run research.py '<your research question>'", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print('  uv run research.py "Latest AI developments 2025"', file=sys.stderr)
        sys.exit(1)
    
    query = sys.argv[1]
    
    # Check for API key
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        print("Error: DASHSCOPE_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set your DashScope API key:", file=sys.stderr)
        print("  export DASHSCOPE_API_KEY='your-api-key-here'", file=sys.stderr)
        sys.exit(1)
    
    # Call DashScope API with streaming
    try:
        completion = dashscope.Generation.call(
            api_key=api_key,
            model="qwen3-max-2026-01-23",
            messages=[{"role": "user", "content": query}],
            enable_search=True,
            search_options={
                "search_strategy": "agent_max",
                "enable_source": True
            },
            enable_thinking=True,
            result_format="message",
            stream=True
        )
    except Exception as e:
        print(f"Error calling DashScope API: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Collect answer content (skip reasoning)
    answer_content = ""
    is_answering = False
    
    for chunk in completion:
        # Skip empty chunks
        if (
            chunk.output.choices[0].message.content == ""
            and chunk.output.choices[0].message.reasoning_content == ""
        ):
            continue
        
        # Skip reasoning content, collect only answer
        if chunk.output.choices[0].message.content != "":
            if not is_answering:
                is_answering = True
            answer_content += chunk.output.choices[0].message.content
    
    # Print only the final answer (non-streaming)
    if answer_content:
        print(answer_content)
    else:
        print("No answer generated.", file=sys.stderr)
        sys.exit(1)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
