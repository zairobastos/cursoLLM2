from openai import OpenAI


client = OpenAI(base_url="http://localhost:49999/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="model-identifier",
    messages=[
        {
            "role": "user",
            "content": "Qual é a importância da educação para a sociedade?"
        },
    ],
    temperature=0.7,
)

print(completion.choices[0].message.content)
