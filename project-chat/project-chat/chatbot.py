import random
import json

# List of agent names to randomly choose from
agent_names = ["Alex", "Jordan", "Taylor", "Chris", "Morgan"]

# Load responses from the JSON file
def load_responses(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["responses"], data["random_responses"]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)

# Function to log the conversation
def log_conversation(user_input, agent_response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nAgent: {agent_response}\n\n")

# Function to choose a random agent name
def get_random_agent_name():
    return random.choice(agent_names)

# Function to generate a response based on the user's input
def get_response(user_input, responses, random_responses):
    # Check for key words in the input
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    # If no keyword is found, return a random response
    return random.choice(random_responses)

def chatbot():
    print("Welcome to the University of Poppleton chatbot!")
    
    # Specify the absolute path to the JSON file
    json_file_path = r"C:\Users\gaura\Desktop\New folder (2)\project-chat\responses.json"
    
    # Load responses from JSON file
    responses, random_responses = load_responses(json_file_path)
    
    # Ask for user's name
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! I'm your chatbot assistant.")

    # Randomly select the agent's name
    agent_name = get_random_agent_name()
    print(f"My name is {agent_name}, and I'm here to help you!")

    # Start the conversation
    while True:
        user_input = input(f"{user_name}: ")
        
        if user_input.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            break
        
        # Get the agent's response
        response = get_response(user_input, responses, random_responses)
        
        # Print agent's response
        print(f"{agent_name}: {response}")

        # Log the conversation
        log_conversation(user_input, response)

        # Randomly disconnect the chat
        if random.random() < 0.05:  # 5% chance of disconnect
            print(f"{agent_name}: Oops, looks like I got disconnected! Try again later.")
            break

if __name__ == "__main__":
    chatbot()
