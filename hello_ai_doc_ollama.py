# hello_ai_doc_ollama.py
import re
import ollama

# --- small FAQ knowledge base (expand as you like) ---


# --- simple normalizer ---
def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# --- naive retrieval by word overlap ---
def naive_retrieve(user_q: str, faqs: list, k: int = 2):
    u = set(normalize(user_q).split())
    scores = []
    for idx, f in enumerate(faqs):
        txt = normalize(f["q"] + " " + f["a"])
        s = len(u & set(txt.split()))
        scores.append((s, idx))
    scores.sort(reverse=True)
    chosen = [faqs[i] for _, i in scores[:k] if _ > 0]
    return chosen

# --- build prompt with retrieved KB ---
def build_messages(user_q: str, retrieved_faqs: list):
    kb = "\n".join([f"Q: {f['q']}\nA: {f['a']}" for f in retrieved_faqs]) or "No matching FAQ found."
    system = (
        "You are a helpful medical information assistant. Provide general information only, not medical diagnosis. "
        "If the user describes emergency symptoms (difficulty breathing, chest pain, loss of consciousness), "
        "advise them to seek immediate medical attention. Always end with: 'This is not medical advice; consult a healthcare professional.'"
    )
    user_content = f"Knowledge:\n{kb}\n\nUser question: {user_q}\nAnswer concisely:"
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user_content},
    ]
    return messages

# --- main answer function calling Ollama ---
def answer(user_q: str):
    retrieved = naive_retrieve(user_q, FAQS, k=2)
    messages = build_messages(user_q, retrieved)
    try:
        resp = ollama.chat(model="mistral", messages=messages)
        return resp["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# --- CLI loop ---
if __name__ == "__main__":
    print("=== Hello AI Doc (Ollama) ===")
    while True:
        q = input("\nAsk a medical question (or 'quit'): ").strip()
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            break
        ans = answer(q)
        print("\nBot answer:\n", ans)




