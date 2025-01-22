import ollama

## Ollama python api doesnot require you to run the ollama serve at the backend

response = ollama.list()

# print(response)

res = ollama.chat(
    model = 'tinyllama',
    messages = [
        {
            "role": "user",
            "content": "what is the capital of Uzbekistan?"
        }
    ],
    stream=True
)

for chunk in res:
    print(chunk['message']['content'], end='', flush=True)

print()
print("-"*100)



