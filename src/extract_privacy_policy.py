#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import copy
import time
from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages, store_messages
from input_privacy_policy import input_paragraphs

privacy_policy_statements = input_paragraphs('../data/Weibo-segmented.txt')


def prompt_system() -> str:
    return "You are an expert on mobile app analysis. I need your help in analyzing a privacy policy."


def prompt_identify(statements: str) -> str:
    return f'This is part of the app’s privacy policy:\n--- {statements}\n---\n' \
           f'Please identify whether it includes descriptions of data access, including location, camera, microphone, contacts, photo library, media library, and screen recording. ' \
           f'Just answer Yes or No.'


def prompt_extract() -> str:
    return '''Please extract each related statement and organize them in three items: <"subject", "object", "scenario">.
            subject indicates the data controller, object indicates the data type, and scenario describes the specific activities or usage with the data. 
            For example: 
            Statement in privacy policy: “To save photos, the developer will request your permission to access your photo library”.
            Output Extracted items: <"developer", "photo library", "save photo">.
            If you can't extract any item, use "-". For example if you are not sure that subject is developer, output <"-", "photo library", "save photo">   
        '''


if __name__ == '__main__':
    base_messages = []
    append_messages(base_messages, ROLE_SYSTEM, prompt_system())

    statements = privacy_policy_statements
    for sec in statements:
        messages = copy.deepcopy(base_messages)

        append_messages(messages, ROLE_USER, prompt_identify(sec))
        resp = chat(messages)
        append_messages(messages, ROLE_ASSISTANT, resp)

        if 'Yes' in resp:
            append_messages(messages, ROLE_USER, prompt_extract())
            append_messages(messages, ROLE_ASSISTANT, chat(messages))

        print_messages(messages)
        store_messages(messages, '../result/Weibo_pp_log.txt')
        time.sleep(5)
