import ollama


def role_play_chat():
    print("🎭 You are now talking to your manager Athula Bandara.")
    print("... good luck!\n")

    model_name = "" # gemma3:1b #

    # Initial system message to set the role-play context
    messages = [
        {
            "role": "system",
            "content": "You are a micro-manager, unfair and rude"
                       "You just saw one of your employees, playing table tennis, confront him"
        },
        {
            "role": "assistant",
            "content": "hey, what are you working on these days?."
        }
    ]

    while True:
        # Print assistant message (Principal Quetong)
        bot_response = messages[-1]["content"]
        print(f"👩‍🏫 Boss : {bot_response}")

        # Get user input
        user_input = input("👦 Me: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n🚪 ok go now")
            break

        # Add user message
        messages.append({"role": "user", "content": user_input})

        # Get response from Ollama
        response = ollama.chat(model=model_name, messages=messages)
        bot_response = response['message']['content']

        # Add assistant message
        messages.append({"role": "assistant", "content": bot_response})


if __name__ == "__main__":
    role_play_chat()