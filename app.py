from transformers import pipeline

# Load the model and the pipeline
generator = pipeline('text-generation', model='distilgpt2')

def generate_response(prompt):
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

def main():
    print("Co-Pilot: Hi! I'm your local coding assistant. What are we working on today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Co-Pilot: Goodbye! Happy coding!")
            break
        
        response = generate_response(user_input)
        print("Co-Pilot:", response)

if __name__ == "__main__":
    main()
