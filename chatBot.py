import os
from groq import Groq

user_input = input("Enter your question : ")
if( user_input == ""):
    user_input = "hii"


# Replace "YOUR_ACTUAL_API_KEY" with your Groq API key
api_key = "YOUR_GROQ_API_KEY"  # groq api key
api_key2 = "YOUR_GROQ_API_KEY"  # groq api key


client = Groq(
    api_key=api_key2,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":user_input,
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)