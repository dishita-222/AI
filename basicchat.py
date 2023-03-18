import random

# Define a list of keywords and their corresponding responses
keywords = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["My name is Chatbot.", "I'm Chatbot.", "You can call me Chatbot."],
    "work":["My work is to help you."]
}

# Initialize the chatbot
def chatbot():
    print("Hello, I'm Chatbot. How can I help you?")
    
    # Loop to keep the chatbot running
    while True:
        # Get user input
        user_input = input("> ").lower()
        
        # Check for keywords and respond with a random message
        if "hello" in user_input:
            response = random.choice(keywords["hello"])
        elif "goodbye" in user_input:
            response = random.choice(keywords["goodbye"])
        elif "thanks" in user_input or "thank you" in user_input:
            response = random.choice(keywords["thanks"])
        elif "name" in user_input:
            response = random.choice(keywords["name"])
        elif "work" in user_input:
            response = random.choice(keywords["work"])   
        else:
            response = "I'm sorry, I don't understand."
        
        # Print the response
        print(response)

# Run the chatbot
chatbot()
