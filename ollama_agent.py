import ollama

query = input("Enter Query: ")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": query
        }
    ]
)

print("\nUser Query:")
print(query)

print("\nLLM Response:")
print(response["message"]["content"])