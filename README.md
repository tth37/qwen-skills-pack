# Qwen Skills Pack

A collection of OpenClaw skills powered by Qwen models via DashScope API.

## Skills Included

| Skill | Emoji | Description | Default Model |
|-------|-------|-------------|---------------|
| **web-researcher** | 🔍 | Agentic web research with reasoning synthesis | `qwen3-max-2026-01-23` |
| **image-reader** | 👁️ | Extract text, solve problems, describe images | `qwen3-vl-plus` |
| **audio-transcriber** | 🎤 | Speech-to-text transcription | `qwen3-asr-flash` |

## Prerequisites

### 1. Install `uv`

`uv` is a fast Python package manager that handles dependencies automatically.

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via Homebrew
brew install uv
```

### 2. Set up DashScope API Key

Get your API key from [DashScope Console](https://dashscope.console.aliyun.com/):

```bash
export DASHSCOPE_API_KEY='your-api-key-here'
```

Add to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.) to persist across sessions.

## Quick Start

Each script uses PEP 723 inline metadata — `uv` automatically creates ephemeral environments and installs dependencies. No manual `pip install` needed!

### Web Research

```bash
uv run web-researcher/scripts/research.py "Latest AI developments 2025"
```

### Image Analysis

```bash
uv run image-reader/scripts/read_image.py photo.jpg "Describe this image"
```

### Audio Transcription

```bash
uv run audio-transcriber/scripts/transcribe.py recording.mp3 --language zh
```

### Make Scripts Executable (Optional)

```bash
chmod +x web-researcher/scripts/research.py
chmod +x image-reader/scripts/read_image.py
chmod +x audio-transcriber/scripts/transcribe.py

# Then run directly
./web-researcher/scripts/research.py "Your query"
```

## How It Works

These scripts use **PEP 723 inline script metadata** — a modern Python standard that embeds dependency declarations directly in the script:

```python
# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "dashscope",
# ]
# [tool.uv]
# exclude-newer = "2025-02-18T00:00:00Z"
# ///
```

When you run `uv run script.py`:
1. `uv` reads the metadata block
2. Creates an ephemeral virtual environment (cached for reuse)
3. Installs the exact dependencies from the lock file
4. Runs the script

**Benefits:**
- ✅ No global Python environment pollution
- ✅ Reproducible builds with lock files
- ✅ Fast cold starts via aggressive caching
- ✅ Self-contained scripts — dependencies travel with the code

## OpenClaw Integration

Add to your OpenClaw configuration:

```json
{
  "skills": {
    "entries": {
      "qwen-web-researcher": {
        "enabled": true,
        "env": { "DASHSCOPE_API_KEY": "your-key" }
      },
      "qwen-image-reader": {
        "enabled": true,
        "env": { "DASHSCOPE_API_KEY": "your-key" }
      },
      "qwen-audio-transcriber": {
        "enabled": true,
        "env": { "DASHSCOPE_API_KEY": "your-key" }
      }
    }
  }
}
```

## Skill Details

### 🔍 Web Researcher

Performs agentic web research with built-in search and reasoning.

```bash
uv run web-researcher/scripts/research.py "Your research question"
```

**Features:**
- Built-in web search with source citations
- Structured output generation
- Reasoning synthesis

### 👁️ Image Reader

Analyzes images using multimodal capabilities.

```bash
uv run image-reader/scripts/read_image.py <image_path> ["custom prompt"]
```

**Features:**
- OCR text extraction
- Math problem solving
- Scene description
- Custom prompt support

### 🎤 Audio Transcriber

Converts speech to text.

```bash
uv run audio-transcriber/scripts/transcribe.py <audio_path> [--language <lang>]
```

**Features:**
- Multiple format support (MP3, WAV, OGG, OPUS)
- Language hints for better accuracy
- Up to 5 minutes per file

## Reproducibility & Lock Files

Each script has a companion `.lock` file (e.g., `research.py.lock`) that pins exact dependency versions. These are committed to ensure:

- Same behavior across different machines
- Protection from upstream breaking changes
- Audit trail of dependencies

To update dependencies:

```bash
cd web-researcher/scripts
uv lock --script research.py  # Updates research.py.lock
```

## Tips for Best Results

### Web Researcher

**❌ Less effective:** `"quantum computing 2025"`

**✅ More effective:** 
- `"Generate a report on quantum computing developments in 2025"`
- `"Compare features of X vs Y with pros and cons"`

### Image Reader

**❌ Less effective:** `"What's this?"`

**✅ More effective:** 
- `"Extract the math problem and show step-by-step solution"`
- `"Read the text and format as markdown"`

### Audio Transcriber

**❌ Less effective:** Auto-detection on noisy/mixed-language audio

**✅ More effective:** 
- Use `--language zh` for Chinese
- Use `--language en` for English

## Troubleshooting

### `uv: command not found`

Install `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### `DASHSCOPE_API_KEY not set`

Set your API key:
```bash
export DASHSCOPE_API_KEY='sk-xxxxxx'
```

### Lock file out of sync

If you see warnings about lock files:
```bash
uv lock --script script.py
```

## License

MIT
