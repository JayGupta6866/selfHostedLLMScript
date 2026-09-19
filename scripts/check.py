import requests

MODEL_NAME = "gemma4:e4b"

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