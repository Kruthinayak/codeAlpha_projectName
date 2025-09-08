# Start of the chatbot
print("Chatbot: Hello! Type something (e.g., 'hello', 'how are you', 'bye')")

# Get user input
user_input = input("You: ").lower()

# Respond based on the input
if user_input == "hello":
    print("Chatbot: Hi!")
elif user_input == "how are you":
    print("Chatbot: I'm fine, thanks!")
elif user_input == "bye":
    print("Chatbot: Goodbye!")
else:
    print("Chatbot: I don't understand that.")