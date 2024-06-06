#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import copy
import time

from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages, store_messages


domain_list = []
with open('data/domain_list.txt', 'r') as f:
    for line in f:
        domain = line.rstrip('\n')
        domain_list.append(domain)

def prompt_system() -> str:
    return "You are an expert in the field of network and I need your help in identifying a domain name."


def prompt_identify(statements: str) -> str:
    return f'Do you know this domain name: "{statements}"\n' \
           f'Please just answer Yes or No'


def prompt_extract() -> str:
    return "Please give a brief description (one or two sentences) of the owner of this domain and its main services."


if __name__ == '__main__':
    base_messages = []
    append_messages(base_messages, ROLE_SYSTEM, prompt_system())

    statements = domain_list
    for sec in statements:
        messages = copy.deepcopy(base_messages)

        append_messages(messages, ROLE_USER, prompt_identify(sec))
        resp = chat(messages)
        append_messages(messages, ROLE_ASSISTANT, resp)

        if 'Yes' in resp:
            append_messages(messages, ROLE_USER, prompt_extract())
            append_messages(messages, ROLE_ASSISTANT, chat(messages))
        # else:
        print_messages(messages)
<<<<<<< HEAD
        store_messages(messages, 'result/domain_desc_log.txt')
=======
        store_messages(messages, 'data/domain_log.txt')
>>>>>>> 5663ddca6fc347aa4a0aa26b47908ac6096ced6e
        time.sleep(5)
