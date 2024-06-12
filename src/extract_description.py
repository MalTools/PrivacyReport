#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import copy
import time

from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages, store_messages


def read_description(file):
    with open(file, 'r') as f:
        des = f.read()
    return des


description_list = [('Jingdong', read_description('../data/Jingdong-description.txt')),
                    ('Weibo', read_description('../data/Weibo-description.txt'))]


def prompt_system() -> str:
    return "I need your help to summarize the main features of an app from its description."


def prompt_extract(app: str, description: str) -> str:
    return f'Here is a description about "{app}" app: {description}\n' \
           f'Your task is to briefly summarize (in a few sentences) the main functionalities and services of this app.'


if __name__ == '__main__':
    base_messages = []
    append_messages(base_messages, ROLE_SYSTEM, prompt_system())

    statements = description_list

    for sec in statements:
        messages = copy.deepcopy(base_messages)
        start = time.time()
        append_messages(messages, ROLE_USER, prompt_extract(sec[0], sec[1]))
        resp = chat(messages)
        append_messages(messages, ROLE_ASSISTANT, resp)

        print_messages(messages)
        store_messages(messages, '../result/functionality_log.txt')
        time.sleep(5)
