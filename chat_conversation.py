from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from termcolor import colored

# load environment variables
load_dotenv()

# Prompt the user to choose the model they want to chat with
while True:
    print(colored("Choose the model you want to chat with:", "blue"))
    print(colored("1. ChatOpenAI", "light_cyan"))
    print(colored("2. ChatAnthropic", "light_cyan"))
    model_choice = input(
        colored("Enter the number of the model you want to chat with: ", "blue")
    )

    # Create an instance of the selected model
    if model_choice == "1":
        model = ChatOpenAI(model_name="gpt-4o")
    elif model_choice == "2":
        model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    else:
        print(colored("Invalid choice. Please enter a valid number.", "red"))
        continue

    print()

    # Get user input and generate a response from the model
    message = input(colored("You: ", "green"))
    response = model.invoke(message)

    # Display the model's response
    print(colored("Model: ", "magenta"), response.content)
    print()

    # Ask the user if they want to continue chatting
    continue_chat = input(colored("Do you want to continue chatting? (y/n): ", "blue"))
    if continue_chat == "n":
        break

print(colored("Chat ended. Goodbye!", "light_cyan"))
