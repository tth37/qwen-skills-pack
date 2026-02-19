---
name: qwen-web-researcher
description: Perform agentic web research using Qwen model and web search. Use when the user asks questions requiring up-to-date information from the web, complex research tasks, or when Tavily/Brave search results need synthesis by a reasoning model. Not for simple questions answerable from training data alone.
metadata:
  { "openclaw": { "emoji": "🔍", "requires": { "env": ["DASHSCOPE_API_KEY"], "bins": ["uv"] } }
---

# Qwen Web Researcher

Perform agentic web research by combining web search with Qwen model reasoning.

## Quick Start

Run the research script with your query:

```bash
./scripts/research "Your research question here"
```

Or use uv directly:

```bash
uv run scripts/research.py "Your research question here"
```

## Prerequisites

1. Install `uv` (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Or via Homebrew: brew install uv
   ```

2. Set your DashScope API key:
   ```bash
   export DASHSCOPE_API_KEY='your-api-key-here'
   ```

## How It Works

1. Takes a user prompt/question
2. Calls DashScope Qwen API with `enable_search=True` (built-in web search)
3. Streams the response, separating reasoning from answer
4. Returns only the final answer (reasoning is processed but not returned)

Uses PEP 723 inline script metadata — `uv` automatically manages the virtual environment and dependencies.

## Configuration

Requires `DASHSCOPE_API_KEY` environment variable. Set it in your shell or OpenClaw config:

```json
{
  "skills": {
    "entries": {
      "qwen-web-researcher": {
        "enabled": true,
        "env": {
          "DASHSCOPE_API_KEY": "your-api-key-here"
        }
      }
    }
  }
}
```

## Script Reference

- `scripts/research.py` - Main research script
  - Usage: `uv run scripts/research.py "<query>"` or `./scripts/research.py "<query>"`
  - Returns: Synthesized answer with citations
  - Lock file: `scripts/research.py.lock` (committed for reproducibility)

## Example Usage

```bash
uv run scripts/research.py "What are the latest developments in quantum computing 2025?"
uv run scripts/research.py "Compare the features of iPhone 16 vs Samsung S25"
```

## Notes

- Uses DashScope Qwen model with built-in web search (`enable_search=True`)
- Model: `qwen3-max-2026-01-23`
- Search strategy: `agent_max` (high-performance mode)
- Streaming is used internally but only the final answer is returned
- Reasoning/thinking process is collected but not returned
- Dependencies are managed automatically by `uv` via PEP 723 inline metadata

### 🎯 Usage Tips

**This is NOT a classic web search tool** — it's an **agentic research assistant** with advanced web search capabilities.

For best results, **don't just feed it keywords**. Instead, ask it to generate structured outputs like:
- Reports or summaries
- Comparisons or analysis
- Timelines or event recaps
- Explanations with context

**❌ Less effective:** `"quantum computing 2025"`

**✅ More effective:** `"Generate a report on the latest developments in quantum computing in 2025, including key breakthroughs and major players"`
