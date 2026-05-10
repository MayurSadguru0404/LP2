# Simple Customer Interaction Chatbot
print("----- CHATBOT -----")
print("Type 'bye' to exit\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "price":
        print("Bot: Product price starts from Rs. 500")

    elif user == "location":
        print("Bot: We are located in Pune")

    elif user == "timing":
        print("Bot: Shop timing is 9 AM to 9 PM")

    elif user == "contact":
        print("Bot: Contact number is 9876543210")

    elif user == "bye":
        print("Bot: Thank you!")
        break

    else:
        print("Bot: Sorry, I don't understand")