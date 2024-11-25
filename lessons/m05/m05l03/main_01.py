from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion)
print()
print()
print()
print(completion.choices[0].message)