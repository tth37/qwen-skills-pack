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
Qwen Audio Transcriber

Transcribe audio files to text using DashScope Qwen ASR API.

Usage:
    uv run scripts/transcribe.py <audio_path> [--language <lang>]

Examples:
    uv run transcribe.py recording.mp3
    uv run transcribe.py meeting.mp3 --language zh
    uv run transcribe.py podcast.mp3 --language en

Environment:
    DASHSCOPE_API_KEY - Required. Your DashScope API key.
    QWEN_ASR_MODEL - Optional. Model to use (default: qwen3-asr-flash)
"""

import sys
import os
import base64
import argparse
from pathlib import Path
import dashscope
from dashscope import MultiModalConversation
from http import HTTPStatus


def audio_to_base64(audio_path):
    """Convert local audio file to base64 string with proper MIME type detection."""
    path = Path(audio_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    # Detect MIME type from extension
    ext = path.suffix.lower()
    mime_types = {
        '.mp3': 'audio/mpeg',
        '.wav': 'audio/wav',
        '.m4a': 'audio/mp4',
        '.ogg': 'audio/ogg',
        '.opus': 'audio/opus',
        '.aac': 'audio/aac',
        '.flac': 'audio/flac',
        '.webm': 'audio/webm'
    }
    mime_type = mime_types.get(ext, 'audio/mpeg')
    
    with open(path, "rb") as audio_file:
        encoded = base64.b64encode(audio_file.read()).decode('utf-8')
    
    return f"data:{mime_type};base64,{encoded}"


def transcribe_audio(audio_path, language=None, model="qwen3-asr-flash"):
    """
    Transcribe audio file using Qwen ASR model.
    
    Args:
        audio_path: Path to local audio file
        language: Optional language hint (e.g., 'zh', 'en')
        model: Qwen ASR model to use
    
    Returns:
        Transcription text
    """
    # Convert audio to base64
    audio_base64 = audio_to_base64(audio_path)
    
    # Prepare messages
    messages = [{
        "role": "user",
        "content": [
            {"audio": audio_base64}
        ]
    }]
    
    # Prepare ASR options
    asr_options = {}
    if language:
        asr_options["language"] = language
    
    # Call API
    try:
        response = MultiModalConversation.call(
            model=model,
            messages=messages,
            api_key=os.getenv('DASHSCOPE_API_KEY'),
            result_format="message",
            asr_options=asr_options if asr_options else None
        )
        
        if response.status_code == HTTPStatus.OK:
            # Extract text from response
            content = response.output.choices[0].message.content
            if isinstance(content, list) and len(content) > 0:
                return content[0].get('text', str(content))
            return str(content)
        else:
            return f"API Error {response.code}: {response.message}"
            
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Transcribe audio files using Qwen ASR"
    )
    parser.add_argument("audio_path", help="Path to the audio file")
    parser.add_argument(
        "--language", "-l",
        help="Language hint (e.g., 'zh' for Chinese, 'en' for English)",
        default=None
    )
    
    args = parser.parse_args()
    
    # Check for API key
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        print("Error: DASHSCOPE_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set your DashScope API key:", file=sys.stderr)
        print("  export DASHSCOPE_API_KEY='your-api-key-here'", file=sys.stderr)
        sys.exit(1)
    
    # Get model from environment or use default
    model = os.environ.get("QWEN_ASR_MODEL", "qwen3-asr-flash")
    
    # Transcribe audio
    try:
        result = transcribe_audio(args.audio_path, args.language, model)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error transcribing audio: {e}", file=sys.stderr)
        sys.exit(1)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
