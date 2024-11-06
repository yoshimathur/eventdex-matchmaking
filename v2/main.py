from client import OpenAI_Client

client = OpenAI_Client().client

completion = client.chat.completions.create(
    model='gpt-4', 
    messages=[
        {
            "role": "user", 
            "content": "Can you explain to me how to solve 2 + 2?"
        }
    ]
)

print(completion.choices[0].message)
