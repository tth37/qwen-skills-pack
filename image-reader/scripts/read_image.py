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
Qwen Image Reader

Analyze images using DashScope Qwen multimodal API.
Supports extracting text, solving problems, describing scenes, etc.

Usage:
    uv run read_image.py <image_path> ["custom prompt"]
    ./read_image.py <image_path> ["custom prompt"]  (if executable)

Examples:
    uv run read_image.py math.jpg "Solve this math problem"
    uv run read_image.py document.png "Extract all text"
    uv run read_image.py photo.jpg

Environment:
    DASHSCOPE_API_KEY - Required. Your DashScope API key.
    QWEN_VL_MODEL - Optional. Model to use (default: qwen3-vl-plus)
"""

import sys
import os
import base64
from pathlib import Path
import dashscope
from dashscope import MultiModalConversation
from http import HTTPStatus


def image_to_base64(image_path):
    """Convert local image to base64 string with proper MIME type detection."""
    path = Path(image_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Detect MIME type from extension
    ext = path.suffix.lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.webp': 'image/webp',
        '.gif': 'image/gif',
        '.bmp': 'image/bmp'
    }
    mime_type = mime_types.get(ext, 'image/jpeg')
    
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
    
    return f"data:{mime_type};base64,{encoded}"


def analyze_image(image_path, prompt, model="qwen3-vl-plus"):
    """
    Analyze image with Qwen-VL model.
    
    Args:
        image_path: Path to local image file
        prompt: Text prompt/question about the image
        model: Qwen-VL model to use
    
    Returns:
        Model's response text
    """
    # Convert image to base64
    image_base64 = image_to_base64(image_path)
    
    # Prepare messages
    messages = [{
        "role": "user",
        "content": [
            {"image": image_base64},
            {"text": prompt}
        ]
    }]
    
    # Call API
    try:
        response = MultiModalConversation.call(
            model=model,
            messages=messages,
            api_key=os.getenv('DASHSCOPE_API_KEY')
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
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: uv run read_image.py <image_path> [\"custom prompt\"]", file=sys.stderr)
        print("\nExamples:", file=sys.stderr)
        print('  uv run read_image.py math.jpg "Solve this math problem"', file=sys.stderr)
        print('  uv run read_image.py document.png "Extract all text"', file=sys.stderr)
        print('  uv run read_image.py photo.jpg', file=sys.stderr)
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Get prompt from args or use default
    if len(sys.argv) >= 3:
        prompt = sys.argv[2]
    else:
        prompt = "Describe what you see in this image"
    
    # Check for API key
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        print("Error: DASHSCOPE_API_KEY environment variable not set.", file=sys.stderr)
        print("Please set your DashScope API key:", file=sys.stderr)
        print("  export DASHSCOPE_API_KEY='your-api-key-here'", file=sys.stderr)
        sys.exit(1)
    
    # Get model from environment or use default
    model = os.environ.get("QWEN_VL_MODEL", "qwen3-vl-plus")
    
    # Analyze image
    try:
        result = analyze_image(image_path, prompt, model)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing image: {e}", file=sys.stderr)
        sys.exit(1)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
