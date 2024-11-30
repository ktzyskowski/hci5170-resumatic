from openai import OpenAI


def chat_completion(messages: list, api_key: str, model="gpt-4o-mini"):
    """

    :param messages:
    :param api_key:
    :param model:
    :return:
    """
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(model=model, messages=messages)
    msg = response.choices[0].message.content
    return msg
