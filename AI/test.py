
# from langchain_cohere.llms import Cohere
# llm = Cohere(cohere_api_key = 'BDYh8zVIL549NfSIjtGVKrlTG8HBZmhSQhgkWJ0M')

# print(llm.invoke("What are the seven wonders of the world"))

from langchain_cohere import ChatCohere

# Initialize the ChatCohere instance with your API key
chat = ChatCohere(cohere_api_key= 'BDYh8zVIL549NfSIjtGVKrlTG8HBZmhSQhgkWJ0M')

# Define your messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
]

# Invoke the chat model with the messages
response = chat.invoke(messages)

# Handle the response
try:
    token_count = response.token_count
except AttributeError:
    token_count = None

print(f"Response: {response.content}")