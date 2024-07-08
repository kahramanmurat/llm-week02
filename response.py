from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

response = client.chat.completions.create(
    model="gemma2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the formula for energy?"}
    ],
    temperature=0.0
)

# Extract and print the number of completion tokens from the response
completion_tokens = response.usage.completion_tokens
print(completion_tokens)
