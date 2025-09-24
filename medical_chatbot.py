from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# CPU-only model
MODEL_NAME = "TheBloke/vicuna-7B-1.1-HF"  # CPU compatible

print("Loading model... (this may take a few minutes)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",  # will use CPU automatically
    torch_dtype=torch.float32  # CPU-friendly
)

def ask_model(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def build_prompt(question, style):
    if style == "kids":
        return f"Explain '{question}' to a 10-year-old."
    elif style == "doctor":
        return f"Explain '{question}' professionally as a doctor."
    elif style == "summary":
        return f"Give bullet points for '{question}'."
    else:
        return question

def main():
    print("👨‍⚕️ Hugging Face Offline Medical Chatbot (CPU)")
    print("Choose style: kids / doctor / summary")
    print("Type 'exit' to quit.\n")

    while True:
        style = input("Choose style: ").strip().lower()
        if style == "exit":
            break

        question = input("Ask your medical question: ").strip()
        if question.lower() == "exit":
            break

        prompt = build_prompt(question, style)
        answer = ask_model(prompt)
        print("\n🤖 AI Answer:\n", answer, "\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
