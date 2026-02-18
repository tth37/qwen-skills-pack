# Qwen Skills Pack

A collection of OpenClaw skills powered by Qwen models via DashScope API.

## Skills Included

| Skill | Emoji | Description | Default Model |
|-------|-------|-------------|---------------|
| **web-researcher** | 🔍 | Agentic web research with reasoning synthesis | `qwen3-max-2026-01-23` |
| **image-reader** | 👁️ | Extract text, solve problems, describe images | `qwen3-vl-plus` |
| **audio-transcriber** | 🎤 | Speech-to-text transcription | `qwen3-asr-flash` |

## Quick Start

### 1. Set up DashScope API Key

```bash
export DASHSCOPE_API_KEY='your-api-key-here'
```

Get your API key from [DashScope Console](https://dashscope.console.aliyun.com/).

### 2. Install Dependencies

```bash
pip install dashscope
```

### 3. Use a Skill

```bash
# Web research
python3 web-researcher/scripts/research.py "Latest AI developments"

# Image analysis
python3 image-reader/scripts/read_image.py photo.jpg "Describe this image"

# Audio transcription
python3 audio-transcriber/scripts/transcribe.py recording.mp3 --language zh
```

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
python3 web-researcher/scripts/research.py "Your research question"
```

**Features:**
- Built-in web search with source citations
- Structured output generation
- Reasoning synthesis

### 👁️ Image Reader

Analyzes images using multimodal capabilities.

```bash
python3 image-reader/scripts/read_image.py <image_path> ["custom prompt"]
```

**Features:**
- OCR text extraction
- Math problem solving
- Scene description
- Custom prompt support

### 🎤 Audio Transcriber

Converts speech to text.

```bash
python3 audio-transcriber/scripts/transcribe.py <audio_path> [--language <lang>]
```

**Features:**
- Multiple format support (MP3, WAV, OGG, OPUS)
- Language hints for better accuracy
- Up to 5 minutes per file

## Requirements

- Python 3.8+
- DashScope API key
- `dashscope` Python library

## License

MIT
