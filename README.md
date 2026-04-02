# 🤖 AI Auto Chat Reply Bot

An AI-powered desktop automation bot that reads chat messages from a browser-based chat app and automatically replies using a Groq-hosted LLM.

The bot detects whether the **last message is from the other person** and replies only once, preventing infinite loops. It uses PyAutoGUI to simulate mouse and keyboard actions and the Groq API for free AI responses (no OpenAI key required).

## Features
- Auto-detects new incoming messages
- Replies only when the sender is not the bot
- Uses Groq LLM (free tier)
- Screen-coordinate based automation
- Built-in PyAutoGUI fail-safe

## Tech Stack
Python, PyAutoGUI, Pyperclip, Groq API

## Usage
Update screen coordinates in `config.py`, add your Groq API key, and run `main.py`.

⚠️ For educational and personal automation purposes only.
