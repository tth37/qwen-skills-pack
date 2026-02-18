---
name: qwen-web-researcher
description: Perform agentic web research using Qwen model and web search. Use when the user asks questions requiring up-to-date information from the web, complex research tasks, or when Tavily/Brave search results need synthesis by a reasoning model. Not for simple questions answerable from training data alone.
metadata:
  { "openclaw": { "emoji": "🔍", "requires": { "env": ["DASHSCOPE_API_KEY"], "bins": ["python3"] }, "install": [{ "id": "pip", "kind": "pip", "package": "dashscope", "label": "Install dashscope library" }] } }
---

# Qwen Web Researcher

Perform agentic web research by combining web search with Qwen model reasoning.

## Quick Start

Run the research script with your query:

```bash
python3 scripts/research.py "Your research question here"
```

## How It Works

1. Takes a user prompt/question
2. Calls DashScope Qwen API with `enable_search=True` (built-in web search)
3. Streams the response, separating reasoning from answer
4. Returns only the final answer (reasoning is processed but not returned)

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
  - Usage: `python3 scripts/research.py "<query>"`
  - Returns: Synthesized answer with citations

## Example Usage

```bash
python3 scripts/research.py "What are the latest developments in quantum computing 2025?"
python3 scripts/research.py "Compare the features of iPhone 16 vs Samsung S25"
```

## Notes

- Uses DashScope Qwen model with built-in web search (`enable_search=True`)
- Model: `qwen3-max-2026-01-23`
- Search strategy: `agent_max` (high-performance mode)
- Streaming is used internally but only the final answer is returned
- Reasoning/thinking process is collected but not returned

### 🎯 Usage Tips

**This is NOT a classic web search tool** — it's an **agentic research assistant** with advanced web search capabilities.

For best results, **don't just feed it keywords**. Instead, ask it to generate structured outputs like:
- Reports or summaries
- Comparisons or analysis
- Timelines or event recaps
- Explanations with context

**❌ Less effective:** `"quantum computing 2025"`

**✅ More effective:** `"Generate a report on the latest developments in quantum computing in 2025, including key breakthroughs and major players"`
