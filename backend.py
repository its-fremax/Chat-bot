import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response_ = chatbot.get_response("Write a story about birds.")
    print(response_)


