import copy
import time

from lib import ROLE_SYSTEM, ROLE_USER, ROLE_ASSISTANT, chat, append_messages, print_messages

data_inputs = []

def prompt_system() -> str:
    return "You are an expert on mobile app development. I need your help in analyzing API call stack traces."


def prompt_input(functionality: str, statements: str, stack_trace: str, data_type: str) -> str:
    return f'Here is the app: : "{functionality}"\n' \
           f'While running this app, we noticed it accessed {data_type} data through system API. ' \
           f'The API call stack trace is as follows: \n{stack_trace}\n' \
           f'Its privacy policy states the use of this data as follows: "{statements}"\n' \
           f'Please use chain-of-thought reasoning to infer what the app uses this data for based on these contexts.\n' \
           f'Example of chain-of-thought reasoning:\n' \
           f'According to the stack trace, the call is from the updateViewWithForecastCardVM method, suggesting that the location data may be used to update forecast card views. Given that the app supports the functionality of tracking the weather at the current location, and states that it needs location information to provide weather alert pushes, we can infer that the location data is used to get weather and update weather forecast views.\n' \
           f'You don not need to output the reasoning process, just output a brief summary of the purpose.' \
           f'Example Output: The location data is used to update the local weather forecast views.'


if __name__ == '__main__':
    base_messages = []
    append_messages(base_messages, ROLE_SYSTEM, prompt_system())

    inputs = data_inputs
    for items in data_inputs:
        messages = copy.deepcopy(base_messages)
        start = time.time()
        append_messages(messages, ROLE_USER, prompt_input(items[0], items[1], items[2], items[3]))
        resp = chat(messages)
        end = time.time()
        print("time:", end - start)
        append_messages(messages, ROLE_ASSISTANT, resp)

        # print_messages(messages)
        time.sleep(5)