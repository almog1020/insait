import os

from flask import Flask, request, make_response, jsonify
from openai import OpenAI

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)

@app.post("/ask")
def ask():
    data = request.get_json()
    question = data["question"]
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user","content": question}],
        model="gpt-3.5-turbo-0125",
    )
    return chat_completion.choices[0].message.content

def main():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    main()
