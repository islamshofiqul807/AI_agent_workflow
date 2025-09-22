# hello_ai_doc_openai.py
import os, openai
openai.api_key = os.getenv("")

FAQS = [
    {"q":"What is a fever?", "a":"Fever is a rise in body temperature above normal..."},
    {"q":"How to reduce fever at home?", "a":"Stay hydrated, rest, paracetamol (as directed), tepid sponging..."},
    {"q":"When to see a doctor for fever?", "a":"If fever > 3 days, >39°C, severe symptoms, difficulty breathing, rash, confusion..."},
]

def build_prompt(user_q):
    kb = "\n".join([f"Q: {f['q']}\nA: {f['a']}" for f in FAQS])
    system = "You are a medical assistant giving general, non-diagnostic information. At the end include: 'This is not medical advice.'"
    prompt = f"{system}\n\nKnowledge base:\n{kb}\n\nUser question: {user_q}\nAnswer:"
    return prompt

from openai import OpenAI

client = OpenAI()

def answer(question):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",   # or "gpt-3.5-turbo" if you want cheaper/faster
        messages=[
            {"role": "system", "content": "You are a helpful medical FAQ assistant."},
            {"role": "user", "content": question}
        ],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    q = input("Ask the medical bot: ")
    print("\nBot answer:\n", answer(q))
