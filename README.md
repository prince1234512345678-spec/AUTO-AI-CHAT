# 🤖 AI Auto Chat Reply Bot

An **AI-powered desktop automation bot** that reads messages from a browser-based chat application (like WhatsApp Web) and automatically replies using a **Groq-hosted LLM**. The bot detects new incoming messages from a specific person and responds intelligently, simulating human-like conversation.

---

## ✨ Features

- Automatically detects the **last message sender**
- Replies only to **new messages from the other person** to avoid loops
- Uses **Groq LLM** (free alternative to OpenAI)
- Fully automated mouse and keyboard actions via **PyAutoGUI**
- Clipboard-based chat extraction using **Pyperclip**
- Built-in **failsafe** for emergency stopping (move mouse to any screen corner)
- Easy to **customize screen coordinates** and sender name

---

## 🛠️ Tech Stack

- **Python 3** – main programming language  
- **PyAutoGUI** – simulates mouse and keyboard actions  
- **Pyperclip** – copies and pastes chat text from clipboard  
- **Groq Python SDK** – AI-powered chat responses  
- **LLama 3.x models** hosted on Groq  

---

## 📂 Project Structure

```text
aiautochat/
│
├── main.py        # Main bot loop: automates reading and replying
├── groq_ai.py     # Interacts with Groq API to get AI replies
├── utils.py       # Message parsing & reply logic
├── config.py      # Screen coordinates and delay settings
└── README.md      # This file
