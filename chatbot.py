import openai

# Add your API key here
openai.api_key = "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"

def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",  # You can use "gpt-4" if available and if your account has access
      messages=[{"role": "user", "content": user_input}]
    )
    return response['choices'][0]['message']['content']

# Chat loop to keep the conversation going
print("Chatbot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    bot_reply = chatbot_response(user_input)
    print("Chatbot:", bot_reply)
