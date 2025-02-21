import os
import time

from openai import OpenAI
import httpx

ROLE_SYSTEM = "system"
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"
client = OpenAI(
    # This is the default and can be omitted
    base_url="https://api.xty.app/v1",
    # api_key=os.environ.get("OPENAI_API_KEY"),
    api_key='sk-srljt7dQbU9C8S6p8372A5Fd5aB2476b920837E43d84138c',
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)


def chat(messages: list[dict[str, str]]) -> str:
    while True:
        try:
            chat_completion = client.chat.completions.create(
                # model="gpt-3.5-turbo-0301",
                model="gpt-4o",
                messages=messages,
            )

            return chat_completion.choices[0].message.content
        except Exception as e:
            print(e, "sleep for 30 second...")
            time.sleep(30)


def append_messages(messages: list[dict[str, str]], role: str, content: str):
    messages.append(
        {"role": role, "content": content},
    )


def print_messages(messages: list[dict[str, str]]):
    for message in messages:
        role, content = message["role"], message["content"]
        if role == ROLE_USER:
            log = color_str("green", "user: ") + content
        elif role == ROLE_ASSISTANT:
            log = color_str("blue", "assistant: ") + content
        else:
            log = color_str("yellow", "system: ") + content
        print(log)


def store_messages(messages: list[dict[str, str]], filename):
    for message in messages:
        role, content = message["role"], message["content"]
        if role == ROLE_USER:
            log = color_str("green", "user: ") + content
        elif role == ROLE_ASSISTANT:
            log = color_str("blue", "assistant: ") + content
        else:
            log = color_str("yellow", "system: ") + content

        with open(filename, 'a') as f:
            f.write(log + '\n')

def color_str(color: str, s: str) -> str:
    if color == "red":
        return "\033[1;31m" + s + "\033[0m"
    if color == "green":
        return "\033[1;32m" + s + "\033[0m"
    if color == "yellow":
        return "\033[1;33m" + s + "\033[0m"
    if color == "blue":
        return "\033[1;34m" + s + "\033[0m"
    return s
