from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

# Replace "YOUR_ACTUAL_API_KEY" with your Groq API key
API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key=API_KEY)

@app.route('/generate', methods=['POST'])
def generate():
    # Get the user input from the frontend
    data = request.json
    user_input = data.get("question", "Hi")

    # Call the Groq API
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="mixtral-8x7b-32768",
    )

    # Get the generated response
    response = chat_completion.choices[0].message.content
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
