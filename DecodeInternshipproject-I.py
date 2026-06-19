while True:
    user = input("You: ").lower()
    if user == "hi" or user == "hello":
        print("Hello")

    elif user == "how are you":
        print("i am fine , Thanks for asking")

    elif user == "help":
        print("i am only the chatbot , i can only chat")

    elif user == "who are you?":
        print("i am the chatbot , i can chat")

    elif user == "bye":
        print("Goodbye!")
        break

    else:
        print("I don't understand")