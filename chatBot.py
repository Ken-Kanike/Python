import os
from groq import Groq

user_input = input("Enter your question : ")
if user_input == "":
    user_input = "hii"

# Set your Groq API key in your environment variables or replace placeholder below
api_key = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)