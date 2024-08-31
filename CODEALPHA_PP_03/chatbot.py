import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data (if not already downloaded)
nltk.download('punkt')

# Define pairs of input and output
pairs = [
    (r"Hi|Hello|Hey", ["Hello! How can I assist you today?"]),
    (r"What is your name?", ["I'm a chatbot created for your assistance."]),
    (r"How are you?", ["I'm just a program, but I'm doing great! How can I help you?"]),
    (r"(.*) your (.*)", ["Why do you want to know about my %2?"]),
    (r"Quit", ["Bye! Have a great day!"]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle conversation
def chat():
    print("Hello! I'm a chatbot. Type 'Quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
