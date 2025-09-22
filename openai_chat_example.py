# openai_chat_example.py
import os, openai
openai.api_key = os.getenv("sk-...")

messages = [
    {"role":"system", "content":"You are a helpful medical assistant. Give general info only, not medical diagnoses; include a brief disclaimer."},
    {"role":"user", "content":"What are common causes of fever and what home-care steps help?"}
]

resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",   # use a model available to you; replace if needed
    messages=messages,
    max_tokens=300,
    temperature=0.2
)
print(resp["choices"][0]["message"]["content"].strip())
