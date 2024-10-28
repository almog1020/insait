import os
from typing import Optional

from flask import Flask, request, current_app

from insait.logic import ask_logic
from insait.database import db
from insait.openai_client import OpenAIClient

app = Flask(__name__)
openai_clients: dict[Flask, OpenAIClient] = {}

@app.post("/ask")
def ask():
    """
    Ask a free text question

    :return: A question id which identifies the asked question. It can be used to fetch the relevant answer.
    """
    data = request.get_json()
    try:
        question = data["question"]
    except KeyError:
        return "Field `question` is missing.", 422

    question_id = ask_logic(get_openai_client(), question)
    return {"question_id": question_id}

def initialize_db() -> None:
    """
    Initialize the server's connection to the database. It will cause any future operations with
    the database to automatically work with an active connection and session which will be closed at the server's
    shutdown.
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_CONNECTION_STRING"]
    db.init_app(app)

@app.teardown_appcontext
def close_openai_client(exception: Optional[BaseException] = None) -> None:
    """
    Close the active connection to OpenAI's servers.

    :param exception: If given, the exception with which the server was shutdown.
    """
    if current_app not in openai_clients:
        return

    openai_clients[current_app].close()
    openai_clients.pop(current_app)


def get_openai_client() -> OpenAIClient:
    """
    Get the active openai client associated with the current flask application.
    """
    if current_app in openai_clients:
        return openai_clients[current_app]

    openai_clients[current_app] = OpenAIClient(os.environ["API_KEY"])
    return openai_clients[current_app]


def setup_app() -> None:
    """
    Initialize the server's connections to external sources.
    """
    initialize_db()
    with app.app_context():
        db.create_all()

def main():
    setup_app()
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
