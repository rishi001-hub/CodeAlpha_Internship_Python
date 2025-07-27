# -----------------------------------------------
# Basic Rule-Based Chatbot
# Description: A friendly chatbot that replies to simple user inputs.
# ------------------------------------------------

def print_welcome():
    print("=" * 60)
    print("🤖 Welcome to ChatBuddy - Your Friendly Rule-Based Chatbot!")
    print("Type something to start chatting or type 'bye' to exit.")
    print("=" * 60)


def get_response(user_input):
    """Return chatbot's response based on user input."""
    user_input = user_input.lower().strip()  # normalize input

    if user_input in ["hi", "hello", "hey"]:
        return "Hi there! 😊 How can I help you today?"

    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thanks for asking! What about you?"

    elif user_input in ["i'm fine", "i am fine", "doing good", "good"]:
        return "That's wonderful to hear! 🌟"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm ChatBuddy, your simple rule-based chatbot assistant 🤖."

    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! 👋 Have a great day ahead!"

    elif user_input in ["thanks", "thank you"]:
        return "You're welcome! 😊"

    elif user_input in ["help", "what can you do"]:
        return "I can respond to greetings, tell you how I'm doing, and wish you goodbye!"

    else:
        return "Hmm... I'm still learning. Can you ask something else?"


def start_chat():
    """Main function to start the chatbot loop."""
    print_welcome()

    while True:
        user_input = input("🧑 You: ")
        response = get_response(user_input)
        print(f"🤖 ChatBuddy: {response}")

        # Exit condition
        if user_input.lower().strip() in ["bye", "goodbye"]:
            break

    print("=" * 60)
    print("🔒 Chat session ended.")
    print("=" * 60)


# Entry point
if __name__ == "__main__":
    start_chat()
