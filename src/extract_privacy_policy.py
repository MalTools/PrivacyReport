#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import copy
import time
from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages, store_messages
from input_privacy_policy import read_paragraphs_from_file


file_path = "/Users/liuwang/Desktop/bupt/毕设/PrivacyReport/privacypolicies/pp_slicing/NetEase Youdao Dictionary.txt"
privacy_policy_statements = read_paragraphs_from_file(file_path)


def prompt_system() -> str:
    return "You are an expert on mobile app analysis. I need your help in analyzing a privacy policy."


def prompt_identify(statements: str) -> str:
    return f'This is part of the app’s privacy policy:\n--- {statements}\n---\n' \
           f'Please identify whether it includes descriptions of app accessing user data, including location, camera, microphone, contacts, photo library, media library, and screen recording. ' \
           f'Just answer Yes or No.'


def prompt_extract() -> str:
    return '''Please identify each related statement and organize them in three items: <"subject", "object", "scenario">.
            subject indicates the data controller (first-party (we, app, developer) or third-party), object indicates the data type (including location, camera, microphone, contacts, photo library, media library, and screen recording), and scenario describes the specific activities or purposes using the data. 
            For example: 
            Statement in privacy policy: “To save photos, the developer will request your permission to access your photo library”.
            Output Extracted items: <"first-party", "photo library", "save photo">.  
        '''
# If you can't extract any item, use "-". For example if you are not sure about the subject, output <"-", "photo library", "save photo">


if __name__ == '__main__':
    base_messages = []
    append_messages(base_messages, ROLE_SYSTEM, prompt_system())
    # messages = copy.deepcopy(base_messages)

    statements = privacy_policy_statements

    # i = 0
    for sec in statements:
        # i += 1
        # if i % 10 == 0:
        messages = copy.deepcopy(base_messages)
        append_messages(messages, ROLE_USER, prompt_identify(sec))
        resp = chat(messages)
        append_messages(messages, ROLE_ASSISTANT, resp)

        if 'Yes' in resp:
            append_messages(messages, ROLE_USER, prompt_extract())
            resp2 = chat(messages)
            append_messages(messages, ROLE_ASSISTANT, resp2)

        # if (i+1) % 10 == 0:
        print_messages(messages)
        store_messages(messages, '/Users/liuwang/Desktop/bupt/毕设/PrivacyReport/privacypolicies/pp_slicing/NetEase Youdao Dictionary_log.txt')

        time.sleep(2)
