# Imports
from groq import Groq   

# Read API keys
with open(r"E:\Lenovo Ideapad 330\company-material\digital-workforce-transformation\ai-upskill-6\key-vault\groq\api.key") as f:
    api_key = f.read().strip()

# Initialize Groq client
client = Groq(api_key=api_key)

# Select model (gpt-4.1-mini)
MODEL = "llama-3.1-8b-instant"

# Chat function
def chat():

    # Welcome message
    print("Welcome to the Groq chatbot! Type 'exit' to end the conversation.")
    print("Chatbot: Hello! How can I assist you today?")

    # Conversation history (list)
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Inifinite loop
    while True:

        # User input
        user_input = input("You: ")

        # Check for the exit condition (exit, quit, end)
        if user_input.lower() in ["exit", "quit", "end"]:
            print("Chatbot: Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Build a prompt using conversation history
        

        try:

            # Get the Groq response
            response = client.chat.completions.create(
                model=MODEL,
                messages=conversation_history,
                temperature=0.7,
                max_tokens=500
            )

            # extract the output text
            output_text = response.choices[0].message.content

            # print the output text
            print(f"Chatbot: {output_text}")

            # add the ai message into the conversation history
            conversation_history.append({"role": "assistant", "content": output_text})

        except:

            # Add an exception message
            print("Chatbot: Sorry, something went wrong. Please try again.")

# run the chatbot
if __name__ == "__main__":
    chat()
