# Glass Box
*A transparent and permission-aware AI code assistant*

My submission for the [Boot.Dev](https://www.boot.dev/) 2025 Hackathon.

## Description

Glass Box is a re-imagining of AI coding assistants and is focused on user control and transparency.

## Problems

This project aims to solve three main problems:

1. AI assistants typically don’t let you limit their access and permissions. This means that in some cases the AI has access to sensitive files.
2. AI assistants often operate as black boxes, making it difficult to fully understand what data they access or how that data might be used. Mainstream providers have policies to protect users, but transparency around data access and usage remains limited.
3. Most AI assistants provide little to no feedback on how or why they arrived at a solution, like which files they accessed to contribute to that solution.

## Solutions

My solutions to these problems are as follows:

1. Glass Box limits file access and permissions of the AI assistant via a dedicated config file (`.glassbox` by default). This file functions like an inverse of a `.gitignore` file, where you explicitly define directories and files the AI *can* access.  
2. By explicitly limiting the AI assistant’s access and permissions through a dedicated file, Glass Box gives users control over what code the AI can see.
3. Glass Box logs metadata about every AI query, including the files accessed by the AI and a few details about the LLM’s operation.

## Installation

> Requires python 3.10 or higher. Check with: `python3 --version`.
> Requires [Ollama](https://ollama.com/download/). Follow their install instructions.

1. Download or clone this repository.
2. Copy the `glassbox/` folder and `.glassbox` config file into your project directory (ideally at the root).
3. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
4. Install the requirements:
    ```bash
    pip install -r glassbox/requirements.txt
5. Pull Codellama:
    ```bash
    ollama pull codellama

## Usage

There are four commands you can use to prompt the AI. They all require a user message, and some require path(s) to files as well. No matter what, the AI will not read files that aren't in the config file (`.glassbox` by default) even if you manually input them when prompted.

To get started, make sure your virtual environment is active and run `python glassbox/src/main.py` from your project root (or wherever you put the glassbox folder).

From here you can run any of four commands or exit the program. The four commands and their intended use cases are as follows:

- `prompt`
    Send the AI a message and no files.

- `prompt-with-file`
    Send the AI a message and one file.

- `prompt-with-files`
    Send the AI a message and more than one file.

- `prompt-with-all-files`
    Send the AI a message and it will automatically look at every file listed in your config file (`.glassbox` by default)

You can see if you're able to enter a command by the amount of brackets. Single brackets `> ` means you can enter a command or exit (you can only exit here). Double brackets `>> ` means you can enter whatever you are being prompted to enter, or type back to go back to the command select. Once you enter a command you will be prompted to enter your message and file(s) if applicable.

*Note: Files are passed to the AI ***one at a time*** — there is no shared context between them.*

## Limitations and Issues

- Codellama has a low token limit. Large prompts (especially when multiple large files are involved) may cause Ollama to fail silently or return an error.
- To prevent this, Glass Box sends each file in a separate message without including history or references to other files.
- As a result, the AI cannot "cross-reference" files — it sees only one file at a time.