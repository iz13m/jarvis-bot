from responses import get_response

print("=== Jarvis Bot ===")
print("Type something to Jarvis (or type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Jarvis: Goodbye!")
        break

    response = get_response(user_input)
    print(f"Jarvis: {response}")