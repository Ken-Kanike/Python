import os
import google.generativeai as genai

print("Welcome to google.generativeai ( Gemini AI )")

api_key = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

while True:
    propmt = input("Ask Gemini / Enter X for exit : ")
    if propmt == "X" or propmt == "x":
        exit()
    elif propmt == "":
        print("Please provide a question.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("" + propmt)
        print(response.text)