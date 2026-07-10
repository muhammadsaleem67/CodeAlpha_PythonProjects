# function wrap our response logic inside a reusable function
def get_bot_reponse(user_input):
    # convert the user's input to lowercase and strip extra spaces
    # so "Hello", and "hello" all match correctly
    text = user_input.lower().strip()
    # if elif logic : check for specific keyword or phrases
    if text in ["hello","hi","hey"]:
        return "Hi there!"
    elif text in ["how are you","how are you?"]:
        return "I'm fine, thanks for asking!"
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye, Have a great day!"
    else :
        # if bot doesn't understand the input
        return "I don't understand that yet. Try asking 'hello'!"
# set up interface
print("🤖 Chatbot initialized! Type 'bye' to exit.")
print("-"*35)
# using while loop
while True:
    # get input
    user_message = input("You: ")
    # pass our input to function
    bot_reply = get_bot_reponse(user_message)
    print(f"Bot: {bot_reply}")
    # if user writes goodbye, break the loop
    if bot_reply == "Goodbye, Have a great day!":
        break
