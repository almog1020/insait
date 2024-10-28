from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key: str):
        """
        A client that wraps OpenAI services in a simple and easy interface.

        :param api_key: An API key that will be used to identify the account which uses the client.
        """
        self._api_key = api_key
        self._client = OpenAI(api_key=api_key)

    def send_message(self, message: str) -> str:
        """
        Send a single message to OpenAI's chatbot and receive its generated answer.

        :param message: Free text content of the message to send.
        :return: The answer as being received by the chatbot.
        """
        chat = self._client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model="gpt-3.5-turbo-0125",
        )
        return chat.choices[0].message.content

    def close(self) -> None:
        """
        Close the underlying client, freeing any open connections.
        """
        self._client.close()
