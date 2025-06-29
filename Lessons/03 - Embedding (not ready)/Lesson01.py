import ollama

# Simple chat completion
response = ollama.chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])

# Generate text (for completion-style models)
response = ollama.generate(model='llama3.1', prompt='The capital of France is')
print(response['response'])

# Stream responses
stream = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Tell me a joke'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)