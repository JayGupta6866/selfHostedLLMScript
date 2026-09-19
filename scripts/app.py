import ollama

MODEL_NAME = "gemma4:e4b"   # Change this to your installed model

prompt = """
Explain what Retrieval-Augmented Generation (RAG) is
in simple terms.
"""

response = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])