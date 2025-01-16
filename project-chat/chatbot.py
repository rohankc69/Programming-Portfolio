import random
import json


agent_names = ["Ram", "hari", "Gaurav", "Rohan", "Rejina"]


def load_responses(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["responses"], data["random_responses"]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)

def log_conversation(user_input, agent_response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nAgent: {agent_response}\n\n")


def get_random_agent_name():
    return random.choice(agent_names)


def get_response(user_input, responses, random_responses):
    
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    
    return random.choice(random_responses)

def chatbot():
    print("Welcome to the University of Poppleton chatbot!")
    
   
    json_file_path = r"C:\Users\PcModNepal\Desktop\Python Code\project-chat\responses.json"
    
    
    responses, random_responses = load_responses(json_file_path)    
    
  
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! I'm your chatbot assistant.")

  
    agent_name = get_random_agent_name()
    print(f"My name is {agent_name}, and I'm here to help you!")


    while True:
        user_input = input(f"{user_name}: ")
        
        if user_input.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            break
        
       
        response = get_response(user_input, responses, random_responses)
        
       
        print(f"{agent_name}: {response}")

      
        log_conversation(user_input, response)

       
        if random.random() < 0.05:  
            print(f"{agent_name}: Oops, looks like I got disconnected! Try again later.")
            break

if __name__ == "__main__":
    chatbot()
