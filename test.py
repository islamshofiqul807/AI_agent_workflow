# test_ollama.py
import ollama

resp = ollama.chat(
    model="mistral",
    messages=[
        {"role": "system", "content": "You are a concise helpful assistant."},
        {"role": "user", "content": "how to run python ?"}
    ],
)
print(resp["message"]["content"])
