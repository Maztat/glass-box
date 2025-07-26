from ollama import Client
from history import *

client = Client()
history = get_history()

# builds the prompts (one for each file in .glassbox) and returns replies
# more details of the replies are logged into history.json to be viewed
def query_ai(message: str, files: dict[str, str]={}):
    results = {}
    file_num = 1
    total = len(files)

    for filepath, content in files.items():
        context = {"role": "system", "content": f"{filepath}:\n{content}"}

        # Prompt provides context and should improve accuracy in the AI responses
        system_prompt = (
            f"You are a helpful and careful code reviewer. "
            f"You will be shown one file at a time for every file paired with the user prompt. "
            f"You will not retain memory or context of any previous files. "
            f"Do not make assumptions about the existence or behavior of other files, functions, or modules unless they are defined within the current file. "
            f"Including file {file_num} of {total}..."
        )

        response = client.chat(model="codellama", messages=[
            {"role": "system", "content": system_prompt},
            context,
            {"role": "user", "content": message},
        ])

        result = response["message"]["content"]
        results[filepath] = result

        write_history({
            "file": filepath,
            "user_message": message,
            "response": result,
            "model": "codellama"
        })

        file_num += 1
    return results