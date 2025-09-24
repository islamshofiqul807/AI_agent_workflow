from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load tokenizer & model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def business_chat():
    print("💼 Welcome to the Business Mentor Chatbot!")
    print("Ask me anything about startups, business ideas, or strategy.")
    
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye! Wishing you success in your business journey!")
            break

        # Encode user input
        inputs = tokenizer([user_input], return_tensors="pt")

        # Generate reply
        reply_ids = model.generate(**inputs, max_new_tokens=100)
        reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    business_chat()
