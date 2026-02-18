---
name: qwen-image-reader
description: Analyze and extract content from images using Qwen multimodal model via DashScope API. Useful for reading text from images, solving math problems, describing scenes, and understanding visual content.
metadata:
  { "openclaw": { "emoji": "👁️", "requires": { "env": ["DASHSCOPE_API_KEY"], "bins": ["python3"] }, "install": [{ "id": "pip", "kind": "pip", "package": "dashscope", "label": "Install dashscope library" }] } }
---

# Qwen Image Reader

Analyze images using Qwen's multimodal capabilities via DashScope API. Extract text, solve problems, describe scenes, or get detailed analysis of any image.

## Quick Start

Read an image with a custom prompt:

```bash
python3 scripts/read_image.py /path/to/image.jpg "Extract and solve the math problem in this image"
```

Or use the default prompt for general analysis:

```bash
python3 scripts/read_image.py /path/to/image.jpg
```

## How It Works

1. Takes an image file path and optional text prompt
2. Converts the image to base64 encoding
3. Sends to DashScope Qwen-VL API with your prompt
4. Returns the model's analysis/response

## Configuration

Requires `DASHSCOPE_API_KEY` environment variable. Set it in your shell or OpenClaw config:

```json
{
  "skills": {
    "entries": {
      "qwen-image-reader": {
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

- `scripts/read_image.py` - Main image analysis script
  - Usage: `python3 scripts/read_image.py <image_path> ["custom prompt"]`
  - Returns: Model's analysis of the image

## Example Usage

### Extract and solve math problems
```bash
python3 scripts/read_image.py math_homework.jpg "user want to solve the math problem in the picture, please extract the math problem"
```

### Extract text from an image
```bash
python3 scripts/read_image.py document.png "Extract all text from this image"
```

### Describe a scene
```bash
python3 scripts/read_image.py photo.jpg "Describe what you see in this image in detail"
```

### General analysis (no prompt)
```bash
python3 scripts/read_image.py image.jpg
```

## Notes

- Uses DashScope Qwen-VL model (`qwen3-vl-plus` by default)
- Supports JPG, PNG, WEBP formats (max 20MB)
- Images are base64-encoded before sending to API
- Default prompt if none provided: "Describe what you see in this image"

### 🎯 Usage Tips

**Be specific with your prompts** for best results:

**❌ Less effective:** `"What's this?"`

**✅ More effective:** `"Extract the math problem and show the step-by-step solution"`

**✅ More effective:** `"List all the objects visible in this image and their approximate positions"`

**✅ More effective:** `"Read the text in this image and format it as markdown"`

## Supported Models

| Model | Best For |
|-------|----------|
| `qwen3-vl-plus` | General vision tasks, good balance (default) |
| `qwen-vl-max` | Complex visual reasoning, higher accuracy |
| `qwen-vl-plus` | Cost-effective image analysis |

To use a different model, edit the script or set `QWEN_VL_MODEL` environment variable.
