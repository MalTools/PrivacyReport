#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import copy
import time

from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages


privacy_policy_statements = []


def prompt_system() -> str:
    return "You are an expert on mobile app analysis. I need your help in analyzing a privacy policy."


def prompt_identify(statements: str) -> str:
    return f'This is part of the app’s privacy policy:\n--- {statements}\n---\n' \
           f'Please identify whether it includes descriptions of data access, including location, camera, microphone, contacts, photo library, media library, and screen recording. ' \
           f'Just answer Yes or No.'


def prompt_extract() -> str:
    return '''Please extract each related statement and organize them in three items: <“subject”, “object”, “scenario”>.
            For example: 
            Statement in privacy policy: “To save photos, the developer will request your permission to access your photo library”.
            Extracted items: <“developer”, “photo library”, “save photo”>.    
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
        time.sleep(5)
