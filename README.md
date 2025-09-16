# Sira Guide Generator

This is a simple Python API that generates Notion-ready help guides using Sira LLM.

## How it works

1. Receives a prompt from Zapier or another tool.
2. Sends the prompt to Sira LLM.
3. Returns a guide in JSON format for Notion or other tools.

## Requirements

- Python 3.10 or higher
- Flask / FastAPI
- gunicorn / uvicorn
- requests

## Usage

Send a POST request to `/generate` with a JSON payload like:

{
  "prompt": "Generate a Notion-ready guide for the topic: Setting Up Work Types in Performance Margin."
}
