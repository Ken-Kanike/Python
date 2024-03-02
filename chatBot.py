import os
from groq import Groq

# Replace "YOUR_ACTUAL_API_KEY" with your Groq API key
api_key = "YOUR_GROQ_API_KEY"

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is php",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)