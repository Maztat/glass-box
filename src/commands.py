from ai_client import *
from history import *
from parser import *

sys_ask_msg = "\nEnter your prompt, or type 'back' to go back.\n"
sys_ask_file = "\nEnter the path to your file, or type back to go back.\n"
sys_msg_gen = "\nGenerating response, this could take some time...\n"

def prompt() -> None:
    message = get_user_message()
    if not message:
        return

    print(sys_msg_gen)
    results = query_ai(message)
    print("\nAI Response:")
    print(results)

def prompt_with_file() -> None:
    message = get_user_message()
    if not message:
        return

    input_files = []

    print(sys_ask_file)
    while True:
        input_file = input(">> ")

        if input_file == "back":
            return
        if not input_file:
            continue
        input_files.append(input_file)
        break

    file = get_valid_files(input_files)
    if not file:
        print("At least one valid file is required.")
        return
    print(sys_msg_gen)
    results = query_ai(message, file)
    print("\nAI Response:")
    print(results)

def prompt_with_files() -> None:
    message = get_user_message()
    if not message:
        return
    files = {}
    input_files = []

    print(sys_ask_file)
    print("Enter file paths one at a time, type 'submit' when done.")
    while True:
        file = input(">> ")

        if file == "back":
            return
        if not file:
            continue
        if file == "submit":
            break

        input_files.append(file)

    files = get_valid_files(input_files)
    if not files:
        print("At least one valid file is required.")
        return
    print(sys_msg_gen)
    results = query_ai(message, files)
    print("\nAI Response:")
    for path, response in results.items():
        print(f"\n{path}\n{response}\n")

def prompt_with_all_files() -> None:
    files = get_files()
    if not files:
        print("\nNo files found in config.")
        return
    
    message = get_user_message()
    if not message:
        return

    print(sys_msg_gen)
    results = query_ai(message, files)
    print("\nAI Response:")
    for path, response in results.items():
        print(f"\n{path}\n{response}\n")

def get_user_message():
    print(sys_ask_msg)
    while True:
        message = input(">> ")
        if message == "back":
            return None
        if message:
            return message.lower()