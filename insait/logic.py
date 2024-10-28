from insait.database import Question, insert_question
from insait.openai_client import OpenAIClient

def ask_logic(openai_client: OpenAIClient, question: str) -> int:
    """
    Ask a question and insert the answer to a database.

    :param openai_client: The client to use in order to ask the question.
    :param question: The content of the question to ask. This is a free text.
    :return: A question id that can be used to identify the submitted question (along with its corresponding answer).
    """
    answer = openai_client.send_message(question)
    record = Question(question=question, answer=answer)

    return insert_question(record)
