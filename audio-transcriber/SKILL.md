---
name: qwen-audio-transcriber
description: Transcribe audio files to text using Qwen ASR model via DashScope API. Supports various audio formats for speech-to-text conversion.
metadata:
  { "openclaw": { "emoji": "🎤", "requires": { "env": ["DASHSCOPE_API_KEY"], "bins": ["python3"] }, "install": [{ "id": "pip", "kind": "pip", "package": "dashscope", "label": "Install dashscope library" }] } }
---

# Qwen Audio Transcriber

Transcribe audio files to text using Qwen's speech recognition capabilities via DashScope API.

## Quick Start

Transcribe an audio file:

```bash
python3 scripts/transcribe.py /path/to/audio.mp3
```

With custom language hint:

```bash
python3 scripts/transcribe.py /path/to/audio.mp3 --language zh
```

## How It Works

1. Takes an audio file path
2. Reads and base64-encodes the audio
3. Sends to DashScope Qwen ASR API
4. Returns the transcription text

## Configuration

Requires `DASHSCOPE_API_KEY` environment variable. Set it in your shell or OpenClaw config:

```json
{
  "skills": {
    "entries": {
      "qwen-audio-transcriber": {
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

- `scripts/transcribe.py` - Main transcription script
  - Usage: `python3 scripts/transcribe.py <audio_path> [--language <lang>]`
  - Returns: Transcribed text

## Example Usage

### Transcribe Chinese audio
```bash
python3 scripts/transcribe.py meeting.mp3 --language zh
```

### Transcribe English audio
```bash
python3 scripts/transcribe.py podcast.mp3 --language en
```

### Auto-detect language
```bash
python3 scripts/transcribe.py recording.mp3
```

## Notes

- Uses DashScope Qwen ASR model (`qwen3-asr-flash` by default)
- Supports MP3, WAV, M4A, OGG, OPUS formats
- Maximum audio duration: 5 minutes
- For longer audio, use async model (`qwen3-asr-flash-filetrans`)

### 🎯 Usage Tips

**Specify language for better accuracy:**

**❌ Less effective:** Auto-detection on noisy audio

**✅ More effective:** `--language zh` for Chinese, `--language en` for English

## Supported Models

| Model | Max Duration | Best For |
|-------|--------------|----------|
| `qwen3-asr-flash` | 5 minutes | Quick transcription (default) |
| `qwen3-asr-flash-filetrans` | 12 hours | Long meetings, podcasts (async) |

To use a different model, edit the script or set `QWEN_ASR_MODEL` environment variable.

## Audio Format Support

- MP3
- WAV
- M4A
- OGG
- OPUS
- AAC
