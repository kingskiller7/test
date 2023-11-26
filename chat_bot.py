import nltk
from nltk.chat.util import Chat, reflections

# Define some simple patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I am doing well.']),
    (r'quit', ['Goodbye!', 'It was nice talking to you.']),
]

# Create a chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Bot:", response)
