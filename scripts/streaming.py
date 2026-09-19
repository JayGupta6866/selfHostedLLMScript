import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma4:e4b"   # Change to your pulled model


def chat_with_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }

    with requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True
    ) as response:

        response.raise_for_status()

        for line in response.iter_lines():
            if line:
                data = json.loads(line)

                if "message" in data:
                    content = data["message"].get("content", "")
                    print(content, end="", flush=True)

                if data.get("done", False):
                    break

        print()


if __name__ == "__main__":
    prompt = input("You: ")

    print("\nAI: ", end="")

    chat_with_ollama(prompt)