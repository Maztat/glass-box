from commands import *

def main():
    print("Glass Box")
    print("Type a command, or type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip().lower()

        if user_input == "exit":
            "Exiting..."
            break

        if not user_input:
            continue

        if user_input == "prompt":
            prompt()
        elif user_input == "prompt-with-file":
            prompt_with_file()
        elif user_input == "prompt-with-files":
            prompt_with_files()
        elif user_input == "prompt-with-all-files":
            prompt_with_all_files()

if __name__ == "__main__":
    main()