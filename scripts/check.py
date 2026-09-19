import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import requests
from config import MODEL_NAME

url = "http://localhost:11434/api/chat"

payload = {
    "model": MODEL_NAME,
    "messages": [
        {
            "role": "user",
            "content": "Explain RAG in simple terms."
        }
    ],
    "stream": True
}

response = requests.post(url, json=payload)

response.raise_for_status()

result = response.json()

print(result["message"]["content"])