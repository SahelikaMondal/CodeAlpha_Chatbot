def chatbot():
    print("\n" + "=" * 40)
    print("              BASIC CHATBOT")
    print("=" * 40)
    print("Hello! I'm your simple Python chatbot.")
    print("You can chat with me using simple commands.")
    print("\nTry saying:")
    print("  • hello")
    print("  • how are you")
    print("  • what is your name")
    print("  • what can you do")
    print("  • thank you")
    print("  • bye")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking. 😊")

        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm CodeBot, a simple rule-based chatbot built with Python.")

        elif user_input in ["what can you do", "help"]:
            print("Bot: I can respond to simple messages and have a basic conversation with you.")

        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're very welcome!")

        elif user_input in ["good morning", "good afternoon", "good evening"]:
            print("Bot: Hello! I hope you're having a wonderful day.")

        elif user_input == "bye":
            print("Bot: Goodbye! It was nice chatting with you. 👋")
            break

        elif user_input == "":
            print("Bot: Please type something so I can respond!")

        else:
            print("Bot: Hmm... I don't understand that yet.")
            print("Bot: Try saying 'help' to see what I can do.")


if __name__ == "__main__":
    chatbot()