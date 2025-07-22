# Glass Box

My submission for the [Boot.Dev](https://www.boot.dev/) 2025 Hackathon.

## Description

Glass Box is a re-imagining of IDE-based AI coding assistants that's focused on privacy, security, and, most importantly, transparency.

## Problems

This project aims to solve three main problems:

1. **Privacy** – AI assistants typically don’t let you limit their access and permissions.  
2. **Security** – AI assistants often operate as black boxes, making it difficult to fully understand what data they access or how that data might be used. While mainstream providers have policies to protect user privacy, transparency around data access and usage remains limited.
3. **Transparency** – Most AI assistants (all that I’m aware of) provide little to no feedback on how or why they arrived at a solution, or what information (which files) they accessed to contribute to that solution.

## Solutions

My solutions to these problems are as follows:

1. Glass Box limits file access and permissions of the AI assistant via a dedicated config file. This file functions like an inverse of a `.gitignore` file, where you explicitly define directories and files the AI can access, along with read/write permissions on an individual basis.  
2. By explicitly limiting the AI assistant’s access and permissions through a dedicated file, Glass Box gives users control and peace of mind about what code the AI can interact with.
3. Glass Box logs metadata about every AI query, including the files accessed by the AI and relevant details about the LLM’s operation.

## Installation

*PLACEHOLDER*

## Configuration

*PLACEHOLDER*
