from ollama import
response=chat(
    model="llama3.2"
    messages=[
        {
            "role":"user",
            "context":"what is SQL?Expalin"
        }
    ]
)
print(response.message.context)