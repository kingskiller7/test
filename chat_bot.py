import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I am doing well.']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.']),
    (r'your age', ['I don\'t have an age. I\'m just a program.']),
    (r'who created you', ['I was created by a team of developers.']),
    (r'programming|code', ['I can help you with programming questions.']),
    (r'weather', ['I don\'t have real-time data, but you can check a weather website.']),
    (r'time', ['I don\'t have real-time clock access.']),
    (r'bye|goodbye', ['Goodbye!', 'It was nice talking to you.']),
    (r'your favorite color', ['I don\'t have preferences. I am just a program.']),
    (r'joke|funny', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'open Google', ['I can\'t open websites.']),
    (r'help', ['I can assist you with general questions. Try asking me something!']),
    # Add more patterns and responses here...
]

# Create a chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Bot:", response)
