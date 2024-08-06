from dotenv import load_dotenv
from google.cloud import firestore
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from termcolor import colored

# load environment variables
load_dotenv()

# Setup Firebase Firestore
PROJECT_ID = "langchain-c3da7"
SESSION_ID = "langchain-chat-conversation"
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

print("Chat History Initialized.")

# Prompt the user to choose the model they want to chat with
while True:
    print(colored("Choose the model you want to chat with:", "blue"))
    print(colored("1. GPT (OpenAI)", "light_cyan"))
    print(colored("2. Claude (Antrophic)", "light_cyan"))
    print(colored("3. Gemini (Google)", "light_cyan"))
    model_choice = input(
        colored("Enter the number of the model you want to chat with: ", "blue")
    )

    # Create an instance of the selected model
    if model_choice == "1":
        model = ChatOpenAI(model_name="gpt-4o")
        break
    elif model_choice == "2":
        model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
        break
    elif model_choice == "3":
        model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-001")
        break
    else:
        print(colored("Invalid choice. Please enter a valid number.", "red"))
        continue

print(colored("Start chatting with the AI. Type 'exit' to quit.", "yellow"))
print()

while True:
    # Get user input and generate a response from the model
    human_input = input(colored("You: ", "green"))
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    # Display the model's response
    print(colored("Model: ", "magenta"), ai_response.content)

print(colored("\nChat ended. Goodbye!", "light_cyan"))
